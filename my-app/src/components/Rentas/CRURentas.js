import React, { useState } from 'react';
import './CRURentas.css';

function CRURentas() {
  const [rentas, setRentas] = useState([]);

  const [editandoId, setEditandoId] = useState(null);
  const [nuevoCliente, setNuevoCliente] = useState('');
  const [nuevaPelicula, setNuevaPelicula] = useState('');
  const [nuevaFecha, setNuevaFecha] = useState('');
  const [nuevosDiasRenta, setNuevosDiasRenta] = useState('');
  const [proximoId, setProximoId] = useState(4);

  const editarRenta = (id, cliente, pelicula, fecha, diasRenta) => {
    setEditandoId(id);
    setNuevoCliente(cliente);
    setNuevaPelicula(pelicula);
    setNuevaFecha(fecha);
    setNuevosDiasRenta(diasRenta);
  };

  const guardarCambios = () => {
    const nuevasRentas = rentas.map(renta => {
      if (renta.id === editandoId) {
        return {
          ...renta,
          cliente: nuevoCliente,
          pelicula: nuevaPelicula,
          fecha: nuevaFecha,
          diasRenta: nuevosDiasRenta
        };
      }
      return renta;
    });
    setRentas(nuevasRentas);
    setEditandoId(null);
    setNuevoCliente('');
    setNuevaPelicula('');
    setNuevaFecha('');
    setNuevosDiasRenta('');
  };

  const actualizarEstatus = (id) => {
    const nuevasRentas = rentas.map(renta => {
      if (renta.id === id) {
        return {
          ...renta,
          estatus: !renta.estatus
        };
      }
      return renta;
    });
    setRentas(nuevasRentas);
  };
  const validarEntrada = () => {
    return nuevoCliente.trim() !== '' && nuevaPelicula.trim() !== '' && nuevaFecha.trim() !== '' && nuevosDiasRenta.trim() !== '';
  };

  const agregarRenta = () => {
    if (validarEntrada()) {
      const nuevaRenta = {
        id: proximoId,
        cliente: nuevoCliente,
        pelicula: nuevaPelicula,
        fecha: nuevaFecha,
        diasRenta: nuevosDiasRenta,
        estatus: true
      };
      setRentas([...rentas, nuevaRenta]);
      setProximoId(proximoId + 1);
      setNuevoCliente('');
      setNuevaPelicula('');
      setNuevaFecha('');
      setNuevosDiasRenta('');
    } else {
      alert('Por favor, complete todos los campos.');
    }
  };

  return (
    <div className="cru-rentas">
      <h2>Rentas</h2>
      <div>
        <div className="input-container">
          <input
            type="text"
            placeholder="idCliente"
            value={nuevoCliente}
            onChange={e => setNuevoCliente(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="text"
            placeholder="idPelícula"
            value={nuevaPelicula}
            onChange={e => setNuevaPelicula(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="date"
            placeholder="Fecha (YYYY-MM-DD)"
            value={nuevaFecha}
            onChange={e => setNuevaFecha(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="number"
            placeholder="Días de renta"
            value={nuevosDiasRenta}
            onChange={e => setNuevosDiasRenta(e.target.value)}
          />
        </div>
        <div style={{ marginTop: '20px' }}>
          <button onClick={agregarRenta}>Agregar Renta</button>
        </div>
      </div>
      <ul>
        {rentas.map(renta => (
          <li key={renta.id}>
            {editandoId === renta.id ? (
              <div>
                <input
                  type="text"
                  value={nuevoCliente}
                  onChange={e => setNuevoCliente(e.target.value)}
                />
                <input
                  type="text"
                  value={nuevaPelicula}
                  onChange={e => setNuevaPelicula(e.target.value)}
                />
                <input
                  type="text"
                  value={nuevaFecha}
                  onChange={e => setNuevaFecha(e.target.value)}
                />
                <input
                  type="text"
                  value={nuevosDiasRenta}
                  onChange={e => setNuevosDiasRenta(e.target.value)}
                />
                <button onClick={guardarCambios}>Guardar</button>
              </div>
            ) : (
              <div>
                Cliente: {renta.cliente}, Película: {renta.pelicula}, Fecha: {renta.fecha}, Días de renta: {renta.diasRenta}, Estatus: {renta.estatus ? 'Activa' : 'Inactiva'}
                <button onClick={() => editarRenta(renta.id, renta.cliente, renta.pelicula, renta.fecha, renta.diasRenta)}>Editar</button>
                <button onClick={() => actualizarEstatus(renta.id)}>{renta.estatus ? 'Desactivar' : 'Activar'}</button>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
  
}

export default CRURentas;
