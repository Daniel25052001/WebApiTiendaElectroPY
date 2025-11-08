
import { useState } from "react";

function AgregarCiudad() {
  const [nombre, setNombre] = useState("");
  const [iddepartamento, setIdDepartamento] = useState("");

  const agregar = () => {
    fetch("http://127.0.0.1:7000/ciudadpost", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nombre, iddepartamento })
    })
      .then(res => res.json())
      .then(data => {
        alert(data.mensaje || JSON.stringify(data));
        setNombre("");
        setIdDepartamento("");
      })
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>Agregar Ciudad</h2>
      <input
        type="text"
        placeholder="Nombre"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
      />
      <input
        type="text"
        placeholder="ID Departamento"
        value={iddepartamento}
        onChange={(e) => setIdDepartamento(e.target.value)}
      />
      <button onClick={agregar}>Agregar</button>
    </div>
  );
}

export default AgregarCiudad;
