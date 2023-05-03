import Header from './components/staticos/header';
import Footer from './components/staticos/footer';
import Carousel from './components/staticos/contenido';
import Card from './components/staticos/card';

import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import {Home} from './pages/home';
import {Profile} from './pages/profile';
import {Found} from './pages/found';
import {Lost} from './pages/lost';
import {Adopt} from './pages/adopt';
import {GiveUpForAdoption} from './pages/giveupforadoption';



function App(){
  return(
    <BrowserRouter>
      <Header/>
      {location.pathname === '/home' && <Carousel/>}
      {location.pathname === '/home' && <Card/>}
      <Footer/>


        <Routes>
          <Route path='/' element={<Navigate to="/home"/>}/>
          <Route path='/index' element={<Home/>}/>
          <Route path='/profile' element={<Profile/>}/>
          <Route path='/found' element={<Found/>}/>
          <Route path='/lost' element={<Lost/>}/>
          <Route path='/adopt' element={<Adopt/>}/>
          <Route path='/giveupforadoption' element={<GiveUpForAdoption/>}/>
        </Routes>
    </BrowserRouter>
  );
}
export default App