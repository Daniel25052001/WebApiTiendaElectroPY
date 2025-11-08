import { useEffect, useState } from "react";

function ListaSedes() {
  const [sedes, setSedes] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:7000/sedget")
      .then(res => res.json())
      .then(data => setSedes(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Sedes</h2>
      <ul>
        {sedes.map(sede => (
          <li key={sede.IdSede}>
            {sede.Nombre} - {sede.Direccion} - {sede.Telefono} - Ciudad: {sede.IdCiudad} - Activo: {sede.Activo === "1" ? "Sí" : "No"}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaSedes;
