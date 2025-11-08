import { useState } from "react";

function ConsultarCiudadPorId() {
  const [id, setId] = useState("");
  const [ciudad, setCiudad] = useState(null);
  const [error, setError] = useState("");

  const handleBuscar = async () => {
    if (!id) return;

    try {
      const response = await fetch(`http://127.0.0.1:7000/ciudadgetID?idciudad=${id}`);
      const data = await response.json();
      setCiudad(data);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Error al consultar la ciudad");
      setCiudad(null);
    }
  };

  return (
    <div>
      <h2>Consultar Ciudad por ID</h2>
      <input
        type="text"
        placeholder="Ingresa el ID de la ciudad"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
      <button onClick={handleBuscar}>Buscar</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {ciudad && ciudad.IdCiudad ? (
        <div>
          <p><strong>ID:</strong> {ciudad.IdCiudad}</p>
          <p><strong>Nombre:</strong> {ciudad.Nombre}</p>
          <p><strong>Departamento ID:</strong> {ciudad.IdDepartamento}</p>
          <p><strong>Activo:</strong> {ciudad.Activo}</p>
        </div>
      ) : ciudad && ciudad.mensaje ? (
        <p>{ciudad.mensaje}</p>
      ) : null}
    </div>
  );
}

export default ConsultarCiudadPorId;