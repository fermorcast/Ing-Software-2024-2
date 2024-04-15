import React, { useState } from 'react';
import './CRUDClientes.css';

function CRUDClientes() {
  const [clientes, setClientes] = useState([]);
  const [editandoId, setEditandoId] = useState(null);
  const [nuevoNombre, setNuevoNombre] = useState('');
  const [nuevoApellido, setNuevoApellido] = useState('');
  const [apellidoMaterno, setApellidoMaterno] = useState('');
  const [email, setEmail] = useState('');
  const [contrasena, setContrasena] = useState('');
  const [fotoPerfil, setFotoPerfil] = useState('');
  const [esSuperusuario, setEsSuperusuario] = useState(false);
  const [proximoId, setProximoId] = useState(4);

  const validarEntrada = () => {
    if (
      nuevoNombre.trim() === '' ||
      nuevoApellido.trim() === '' ||
      apellidoMaterno.trim() === '' ||
      email.trim() === '' ||
      contrasena.trim() === ''
    ) {
      alert('Todos los campos son obligatorios');
      return false;
    }
    // Verificar el formato de correo electrónico
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert('El formato de correo electrónico no es válido');
      return false;
    }
    return true;
  };

  const editarCliente = (id, nombre, apellido, apellidoMaterno, email, contrasena, fotoPerfil, esSuperusuario) => {
    setEditandoId(id);
    setNuevoNombre(nombre);
    setNuevoApellido(apellido);
    setApellidoMaterno(apellidoMaterno);
    setEmail(email);
    setContrasena(contrasena);
    setFotoPerfil(fotoPerfil);
    setEsSuperusuario(esSuperusuario);
  };

  const guardarCambios = () => {
    if (!validarEntrada()) {
        return;
      }
  
    const nuevosClientes = clientes.map(cliente => {
      if (cliente.id === editandoId) {
        return {
          ...cliente,
          nombre: nuevoNombre,
          apellido: nuevoApellido,
          apellidoMaterno: apellidoMaterno,
          email: email,
          contrasena: contrasena,
          fotoPerfil: fotoPerfil,
          esSuperusuario: esSuperusuario
        };
      }
      return cliente;
    });
    setClientes(nuevosClientes);
    setEditandoId(null);
    setNuevoNombre('');
    setNuevoApellido('');
    setApellidoMaterno('');
    setEmail('');
    setContrasena('');
    setFotoPerfil('');
    setEsSuperusuario(false);
  };

  const eliminarCliente = (id) => {
    const nuevosClientes = clientes.filter(cliente => cliente.id !== id);
    setClientes(nuevosClientes);
  };

  const agregarCliente = () => {
    if (!validarEntrada()) {
        return;
      }
    const nuevoCliente = {
      id: proximoId,
      nombre: nuevoNombre,
      apellido: nuevoApellido,
      apellidoMaterno: apellidoMaterno,
      email: email,
      contrasena: contrasena,
      fotoPerfil: fotoPerfil,
      esSuperusuario: esSuperusuario
    };
    setClientes([...clientes, nuevoCliente]);
    setProximoId(proximoId + 1);
    setNuevoNombre('');
    setNuevoApellido('');
    setApellidoMaterno('');
    setEmail('');
    setContrasena('');
    setFotoPerfil('');
    setEsSuperusuario(false);
  };
 
  return (
    <div className="crud-clientes">
      <h2>Clientes</h2>
      <div>
        <div className="input-container">
          <input
            type="text"
            placeholder="Nombre"
            value={nuevoNombre}
            onChange={e => setNuevoNombre(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="text"
            placeholder="Apellido Paterno"
            value={nuevoApellido}
            onChange={e => setNuevoApellido(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="text"
            placeholder="Apellido Materno"
            value={apellidoMaterno}
            onChange={e => setApellidoMaterno(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={e => setEmail(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="password"
            placeholder="Contraseña"
            value={contrasena}
            onChange={e => setContrasena(e.target.value)}
          />
        </div>
        <div className="input-container">
          <input
            type="file"
            accept="image/*"
            onChange={e => setFotoPerfil(e.target.files[0])}
          />
        </div>
        <div>
          <label>
            Superusuario:
            <input
              type="checkbox"
              checked={esSuperusuario}
              onChange={e => setEsSuperusuario(e.target.checked)}
            />
          </label>
        </div>
        <div style={{ marginTop: '20px' }}> {/* Aumenté el margen superior */}
          <button onClick={agregarCliente}>Agregar Cliente</button>
        </div>
      </div>
      <ul>
        {clientes.map(cliente => (
          <li key={cliente.id}>
            {editandoId === cliente.id ? (
              <div>
                <input
                  type="text"
                  value={nuevoNombre}
                  onChange={e => setNuevoNombre(e.target.value)}
                />
                <input
                  type="text"
                  value={nuevoApellido}
                  onChange={e => setNuevoApellido(e.target.value)}
                />
                <button onClick={guardarCambios}>Guardar</button>
              </div>
            ) : (
              <div>
                {cliente.nombre} {cliente.apellido}
                <button onClick={() => editarCliente(cliente.id, cliente.nombre, cliente.apellido, cliente.apellidoMaterno, cliente.email, cliente.contrasena, cliente.fotoPerfil, cliente.esSuperusuario)}>Editar</button>
                <button onClick={() => eliminarCliente(cliente.id)}>Eliminar</button>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
  
}

export default CRUDClientes;
