const prod = {
  prod_url: 'http://localhost:80/api/',
  isDev:    false
};
const dev = {
  dev_url: 'http://localhost:5000/api/',
  isDev:   true
};

export const config = process.env.NODE_ENV === 'development' ? dev : prod;
