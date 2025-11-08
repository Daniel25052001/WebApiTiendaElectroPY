import { useEffect, useState } from "react";

function ListaCiudades() {
  const [ciudades, setCiudades] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:7000/ciudadget")
      .then(res => res.json())
      .then(data => setCiudades(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Ciudades</h2>
      <ul>
        {ciudades.map(ciudad => (
          <li key={ciudad.IdCiudad}>
            {ciudad.Nombre} (ID: {ciudad.IdCiudad}, Departamento ID: {ciudad.IdDepartamento})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaCiudades;
