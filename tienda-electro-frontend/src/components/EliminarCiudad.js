
import { useState } from "react";

function EliminarCiudad() {
  const [id, setId] = useState("");

  const eliminar = () => {
    fetch(`http://127.0.0.1:7000/ciudaddelete?idciudad=${id}`, {
      method: "DELETE"
    })
      .then(res => res.json())
      .then(data => {
        alert(data.mensaje || JSON.stringify(data));
        setId("");
      })
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>Eliminar Ciudad</h2>
      <input
        type="text"
        placeholder="Ingrese ID de ciudad"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
      <button onClick={eliminar}>Eliminar</button>
    </div>
  );
}

export default EliminarCiudad;
