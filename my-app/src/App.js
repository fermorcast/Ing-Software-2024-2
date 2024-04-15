import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CRUDClientes from './components/Clientes/CRUDClientes';
import CRUDPeliculas from './components/Peliculas/CRUDPeliculas';
import CRURentas from './components/Rentas/CRURentas';
import Home from './home';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/clientes" element={<CRUDClientes />} />
        <Route path="/peliculas" element={<CRUDPeliculas />} />
        <Route path="/rentas" element={<CRURentas />} />
      </Routes>
    </Router>
  );
}

export default App;