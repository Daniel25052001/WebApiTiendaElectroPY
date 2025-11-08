import { useState } from "react";

function ModificarCiudad() {
  const [id, setId] = useState("");
  const [nombre, setNombre] = useState("");
  const [iddepartamento, setIdDepartamento] = useState("");

  const modificar = () => {
    fetch(`http://127.0.0.1:7000/ciudadput?idciudad=${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nombre, iddepartamento, activo: true })
    })
      .then(res => res.json())
      .then(data => {
        alert(data.mensaje || JSON.stringify(data));
        setId("");
        setNombre("");
        setIdDepartamento("");
      })
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>Modificar Ciudad</h2>
      <input
        type="text"
        placeholder="ID Ciudad"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
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
      <button onClick={modificar}>Modificar</button>
    </div>
  );
}

export default ModificarCiudad;

