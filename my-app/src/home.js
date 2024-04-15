import React from 'react';
import { Link } from 'react-router-dom';


function Home() {
  return (
    <div style={{ backgroundColor: '#b3e0ff', minHeight: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center' }}>
      <h1>Bienvenido </h1>
      <p>Selecciona una opción:</p>
      <div>
        <Link to="/clientes">
          <button style={{ backgroundColor: '#007bff', color: '#ffffff', fontSize: '20px', padding: '10px 20px', margin: '10px', borderRadius: '5px' }}>
            Clientes
          </button>
        </Link>
        <Link to="/peliculas">
          <button style={{ backgroundColor: '#007bff', color: '#ffffff', fontSize: '20px', padding: '10px 20px', margin: '10px', borderRadius: '5px' }}>
            Películas
          </button>
        </Link>
        <Link to="/rentas">
          <button style={{ backgroundColor: '#007bff', color: '#ffffff', fontSize: '20px', padding: '10px 20px', margin: '10px', borderRadius: '5px' }}>
            Rentas
          </button>
        </Link>
      </div>
    </div>
  );
}


export default Home;
