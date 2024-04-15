import React, { useState } from 'react';
import './CRUDPeliculas.css';

function CRUDPeliculas() {
  const [peliculas, setPeliculas] = useState([]);

  const [editandoId, setEditandoId] = useState(null);
  const [nuevoTitulo, setNuevoTitulo] = useState('');
  const [nuevoGenero, setNuevoGenero] = useState('');
  const [nuevoInventario, setNuevoInventario] = useState('');
  const [nuevaDuracion, setNuevaDuracion] = useState('');
  const [proximoId, setProximoId] = useState(4);

  const editarPelicula = (id, titulo, genero, inventario, duracion) => {
    setEditandoId(id);
    setNuevoTitulo(titulo);
    setNuevoGenero(genero);
    setNuevoInventario(inventario);
    setNuevaDuracion(duracion);
  };

  const guardarCambios = () => {
    if (nuevoTitulo.trim() === '' || nuevoGenero.trim() === '' || nuevoInventario.toString().trim() === '' || nuevaDuracion.trim() === '') {
        // Mostrar un mensaje de error o realizar alguna acción adecuada
        alert('Por favor, completa todos los campos antes de guardar.');
        return;
    }
    const nuevasPeliculas = peliculas.map(pelicula => {
      if (pelicula.id === editandoId) {
        return {
          ...pelicula,
          titulo: nuevoTitulo,
          genero: nuevoGenero,
          inventario: nuevoInventario,
          duracion: nuevaDuracion
        };
      }
      return pelicula;
    });
    setPeliculas(nuevasPeliculas);
    setEditandoId(null);
    setNuevoTitulo('');
    setNuevoGenero('');
    setNuevoInventario(0);
    setNuevaDuracion('');
  };

  const eliminarPelicula = (id) => {
    const nuevasPeliculas = peliculas.filter(pelicula => pelicula.id !== id);
    setPeliculas(nuevasPeliculas);
  };

  const validarEntrada = () => {
    return nuevoTitulo.trim() !== '' && nuevoGenero.trim() !== '' && nuevoInventario.trim() !== '' && nuevaDuracion.trim() !== '';
  };
  

  const agregarPelicula = () => {
    if (validarEntrada()) {
      const nuevaPelicula = {
        id: proximoId,
        titulo: nuevoTitulo,
        genero: nuevoGenero,
        inventario: nuevoInventario,
        duracion: nuevaDuracion
      };
      setPeliculas([...peliculas, nuevaPelicula]);
      setProximoId(proximoId + 1);
      setNuevoTitulo('');
      setNuevoGenero('');
      setNuevoInventario('');
      setNuevaDuracion('');
    } else {
      alert('Por favor, complete todos los campos.');
    }
  };

  return (
    <div className="crud-peliculas">
      <h2>Películas</h2>
      <div>
        <div className="input-container">
          <input
            type="text"
            placeholder="Título"
            value={nuevoTitulo}
            onChange={e => setNuevoTitulo(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="text"
            placeholder="Género"
            value={nuevoGenero}
            onChange={e => setNuevoGenero(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="number"
            placeholder="Inventario"
            value={nuevoInventario}
            onChange={e => setNuevoInventario(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="number"
            placeholder="Duración"
            value={nuevaDuracion}
            onChange={e => setNuevaDuracion(e.target.value)}
          />
        </div>
        <div style={{ marginTop: '20px' }}>
          <button onClick={agregarPelicula}>Agregar Película</button>
        </div>
      </div>
      <ul>
        {peliculas.map(pelicula => (
          <li key={pelicula.id}>
            {editandoId === pelicula.id ? (
              <div>
                <input
                  type="text"
                  value={nuevoTitulo}
                  onChange={e => setNuevoTitulo(e.target.value)}
                />
                <input
                  type="text"
                  value={nuevoGenero}
                  onChange={e => setNuevoGenero(e.target.value)}
                />
                <input
                  type="number"
                  value={nuevoInventario}
                  onChange={e => setNuevoInventario(e.target.value)}
                />
                <input
                  type="number"
                  value={nuevaDuracion}
                  onChange={e => setNuevaDuracion(e.target.value)}
                />
                <button onClick={guardarCambios}>Guardar</button>
              </div>
            ) : (
              <div>
                {pelicula.titulo} - {pelicula.genero}
                <button onClick={() => editarPelicula(pelicula.id, pelicula.titulo, pelicula.genero, pelicula.inventario, pelicula.duracion)}>Editar</button>
                <button onClick={() => eliminarPelicula(pelicula.id)}>Eliminar</button>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CRUDPeliculas;
