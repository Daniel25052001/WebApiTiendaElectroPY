import { useEffect, useState } from "react";

function ListaPaises() {
  const [paises, setPaises] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:7000/paisget")
      .then(res => res.json())
      .then(data => setPaises(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <ul>
      {paises.map(pais => (
        <li key={pais.idpais}>{pais.nombre}</li>
      ))}
    </ul>
  );
}

export default ListaPaises;
