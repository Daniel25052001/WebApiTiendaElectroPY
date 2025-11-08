
import { useState } from "react";

function CiudadPorId() {
  const [id, setId] = useState("");
  const [ciudad, setCiudad] = useState(null);

  const buscarCiudad = () => {
    fetch(`http://127.0.0.1:7000/ciudadgetID?idciudad=${id}`)
      .then(res => res.json())
      .then(data => setCiudad(data))
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>Consultar Ciudad por ID</h2>
      <input
        type="text"
        placeholder="Ingrese ID de la ciudad"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
      <button onClick={buscarCiudad}>Buscar</button>

      {ciudad && (
        <div>
          <p>ID: {ciudad.IdCiudad}</p>
          <p>Nombre: {ciudad.Nombre}</p>
          <p>Departamento ID: {ciudad.IdDepartamento}</p>
          <p>Activo: {ciudad.Activo}</p>
        </div>
      )}
    </div>
  );
}

export default CiudadPorId;
