import './App.css';
import React from 'react';
import { Home } from './Pages/Home';
import { Main } from './Pages/Main';
import { HowItWorks } from './Pages/HowItWorks';
import { PagesLayout } from './Pages/PagesLayout';
import Navbar from './Components/Navbar/Navbar';
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import Footer from './Components/Footer/Footer';

export default function App() {
  return (
    <React.Fragment>
      <div className="App container m-4">
        <BrowserRouter>
          <Navbar />
          <Routes>
            <Route element={<PagesLayout />}>
              <Route path='/' element={< Home />} />
              <Route path='/how-it-works' element={< HowItWorks />} />
              <Route path='/main' element={< Main />} />
            </Route>
          </Routes>
          <Footer />
        </BrowserRouter>
      </div>
    </React.Fragment>
  );
}
