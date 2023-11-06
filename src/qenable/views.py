"""
Flask App Module
Hosts all methods to be accessed by Webclients and serves the frontend.
"""
import os
import io
import json
import logging
import importlib.resources

import urllib3
from flask import request, jsonify, Response
from qaclient import ApiException, Configuration, ApiClient
from qaclient.apis import DatasetControllerKgApi
from qaclient.models import IndexConfig
from qenable.crawler import run_crawler
from qaclient.models import DatasetConfigRequest
from qaclient.models import UIMappings

import qenable.label_definitions
from qenable import app

if os.environ['FLASK_ENV'] == 'dev':
    from flask_cors import CORS

    CORS().init_app(app)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.NOTSET
)

client_config = Configuration(api_key_prefix={'JWT': 'Bearer'}, host="https://app.qanswer.ai")

# set a global variable to store the result from scarpy
scrapy_result = {'res': '0'}


@app.route("/")
def home() -> Response:
    """
    Returns the homepage.
    :return: The Homepage (index.html)
    """
    client_config.api_key = {'JWT': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNDY2IiwiaWF0IjoxNjc1MTk1MzE2LCJleHAiOjE2NzU4MDAxMTZ9.VleX-X1qdBrzvcH2801zNvdeBa7vUXN3PNtnmC2fbTJpQVNtyxdoXZzCE40U3fKsXguETSYbEatcsVMUa_pPJg'}
    return app.send_static_file('index.html')


@app.route('/api/process_run', methods=['POST'])
def process_run() -> Response:
    """
    Initiates a crawl with the given parameters.
    :return: Dummy-Response. Esit status of crawl unknown since it is done asynchronously through scrapyd
    """
    res = request.get_json()
    urls = res['url'].replace(' ', '').split(',')
    dataset_name = res['filename']
    run_crawler(dataset_name=dataset_name, start_urls=urls)
    return jsonify({})


@app.route('/api/upload_triples', methods=['POST'])
def upload_triples() -> Response:
    """
    Uploads crawled .nt file to QAnswer.
    This endpoint is supposed to be accessed by the crawler (scrapyd service), not by the end user directly.
    :return: Empty dummy-response.
    """
    global scrapy_result
    dataset_name = request.get_json()['dataset_name']
    triples = request.get_json()['rdf_data']

    triples = qa_slicer(triples)
    triples += get_label_definition()

    file = io.StringIO(triples)
    file.name = f"{dataset_name}.nt"  # Hack to set name attribute needed by qaclient
    with ApiClient(client_config) as api_client:
        api_instance = DatasetControllerKgApi(api_client)
        try:
            api_instance.upload_using_post(dataset_name, file)
            logging.info(api_instance.index_using_post(IndexConfig(dataset=dataset_name)))
            logging.info(api_instance.set_config_using_post(get_config(dataset_name)))
            logging.info(f'Dataset {dataset_name} was successfully uploaded')
            scrapy_result = {'res': '1', 'name': dataset_name, 'triples': triples}
        except ApiException as e:
            logging.warning(f'Dataset {dataset_name} could not be uploaded: {e}\n')
            scrapy_result = {'res': '2', 'name': dataset_name, 'triples': triples}  # To tell that an ApiException has occurred
    return jsonify({})


@app.route('/api/crawler_result', methods=['GET'])
def crawler_result() -> Response:
    """
    React sends several requests to know whether the crawling of Doamin is complete or not.
    This function works like a get method for updating a frontend component.
    :return: Scrapy Doamin Crawling Result.
    """
    global scrapy_result
    return jsonify(scrapy_result)


def get_label_definition() -> str:
    """
    Returns a string containing all default ontologies found in qenable.label_definitions
    :return: all default ontologies
    """
    labels = ""
    for file in importlib.resources.files(qenable.label_definitions).iterdir():
        labels += file.read_text() + "\n"
    return labels


def qa_slicer(triples: str) -> Response:
    """
    Returns the mapped triple, in front standing Blanc Nodes are adjusted with http
    :param triples:
    :return: qa_ready_edited_triples (mapped triples) in String Format
    """
    qa_ready_edited_triples = ""

    for line in triples.splitlines():
        logging.debug(f"array:{line}")
        if line[:2] == "_:":
            replace_beginning_start_of_blancnode = line.replace("_:", "<http://", 1)
            replace_beginning_end_of_blancnode = line.replace(" ", "> ", 1)

            edited_blancnode = replace_beginning_start_of_blancnode[:41] + replace_beginning_end_of_blancnode[35:]
            if "<http://schema.org/name>" in edited_blancnode:
                edited_blancnode = adding_label_tag(edited_blancnode)

            if line[-37: -35] == "_:":
                edited_blancnode = replace_ending_blancnode(edited_blancnode, line)
                qa_ready_edited_triples += edited_blancnode

            else:
                edited_blancnode = edited_blancnode + "\n"
                qa_ready_edited_triples += edited_blancnode

        elif line[-37: -35] == "_:":
            replaced_ending_blancnode = replace_ending_blancnode(line, line)
            qa_ready_edited_triples += replaced_ending_blancnode

        else:
            qa_ready_edited_triples += line + "\n"
    return qa_ready_edited_triples


def adding_label_tag(edited_blancnode: str) -> Response:
    """
    Add line with http://www.w3.org/2000/01/rdf-schema#label Tag
    :param edited_blancnode:
    :retun: triple lines, one with http://www.w3.org/2000/01/rdf-schema#label tag, the other with http://schema.org/name
    """
    triple_for_name_tag = edited_blancnode
    edited_blancnode = edited_blancnode.replace("<http://schema.org/name>",
                                                "<http://www.w3.org/2000/01/rdf-schema#label>")
    edited_blancnode += "\n" + triple_for_name_tag
    return edited_blancnode


def replace_ending_blancnode(edited_blancnode: str, line: str) -> Response:
    """
    Replaces object blancnodes to readable nodes | http is added to the behind standing blanc nodesgit st
    :param edited_blancnode, line
    :return: edited_blancnode + "\n" , hands over readable node
    """
    range_line = len(edited_blancnode)
    ending_blancnote_position = line[-37:]
    end_of_blancnote = ending_blancnote_position.replace(" .", "> .")
    start_of_blancnote = ending_blancnote_position.replace("_:", " <http://")
    edited_blancnode = edited_blancnode[:range_line - 37] + start_of_blancnote[:42] + end_of_blancnote[-3:]
    return edited_blancnode + "\n"


def get_config(dataset_name: str) -> DatasetConfigRequest:
    """
    Returns the default dataset configuration to be uploaded to qanswer.
    :param dataset_name: name of the dataset
    :return: DatasetConfigRequest object which defines the default label mappings
    """
    return DatasetConfigRequest(
        dataset=dataset_name,
        ui_mappings=UIMappings(
            label=[
                "http://www.w3.org/2000/01/rdf-schema#label",
                "http://www.w3.org/2004/02/skos/core#prefLabel",
                "https://www.w3.org/2004/02/skos/core#prefLabel",
                "http://www.w3.org/2004/02/skos/core#prefLabel",
                "http://www.w3.org/2004/02/skos/core#altLabel",
                "https://www.w3.org/2004/02/skos/core#altLabel",
                "http://www.w3.org/2000/01/rdf-schema#label",
                "https://www.w3.org/2000/01/rdf-schema#label",
                "http://purl.org/dc/terms/title",
                "http://xmlns.com/foaf/0.1/givenName",
                "http://purl.org/dc/elements/1.1/title",
                "http://schema.org/name"
            ],
            description=[
                "http://www.w3.org/2000/01/rdf-schema#description",
                "http://www.w3.org/2004/02/skos/core#definition"
            ],
            image=[
                "http://www.wikidata.org/prop/direct/P18",
                "http://schema.org/image",
                "http://schema.org/logo",
                "http://vocabulary.semantic-web.at/cocktail-ontology/image"
            ],
            coordinate=[
                "http://www.wikidata.org/prop/direct/P625"
            ],
            osmRelation=[
                "http://www.wikidata.org/prop/direct/P402"
            ],
            youtube=[
                "http://www.wikidata.org/prop/direct/P165"
            ],
            github=[
                "http://www.wikidata.org/prop/direct/P2037"
            ],
            twitter=[
                "http://www.wikidata.org/prop/direct/P2002"
            ],
            facebook=[
                "http://www.wikidata.org/prop/direct/P2013"
            ],
            instagram=[
                "http://www.wikidata.org/prop/direct/P2003"
            ],
            homepage=[
                "http://www.wikidata.org/prop/direct/P856"
            ],
            orcid=[
                "http://www.wikidata.org/prop/direct/P496"
            ],
            doi=[
                "http://www.wikidata.org/prop/direct/P356"
            ],
            geometry=[
                "http://www.opengis.net/ont/geosparql#hasGeometry"
            ],
            dbpedia=[
                "http://www.w3.org/2004/02/skos/core#exactMatch"
            ],
            ignore=[
                "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
            ]
        )
    )


def remove_unnecessary_characters(text):
    """This method remove unnecessary characters at the beginning and ending
    :param text:
    :return: json-ld format textfile
    """
    json_object = json.dumps(text, indent=4)
    json_object = json_object[19:]  # 19 -> removes start text
    json_object = json_object[:-8]  # -8 -> removes ending text
    return json_object
