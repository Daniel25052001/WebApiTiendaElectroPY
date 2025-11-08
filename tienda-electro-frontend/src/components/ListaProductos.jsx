
import { useEffect, useState } from "react";

function ListaProductos() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:7000/productoget")
      .then(res => res.json())
      .then(data => setProductos(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Productos</h2>
      <ul>
        {productos.map(prod => (
          <li key={prod.IdProducto}>
            <strong>{prod.Nombre}</strong> - {prod.Descripcion} - Precio: {prod.Precio} - Stock: {prod.Stock}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaProductos;
