
import { useEffect, useState } from "react";

function ListaDepartamentos() {
  const [departamentos, setDepartamentos] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:7000/departamentoget")
      .then(res => res.json())
      .then(data => setDepartamentos(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Departamentos</h2>
      <ul>
        {departamentos.map(dep => (
          <li key={dep.iddepartamento}>
            {dep.nombre} (Pais ID: {dep.idpais})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaDepartamentos;
