import { useState } from "react";

function ConsultarProductoPorId() {
  const [idProducto, setIdProducto] = useState("");
  const [producto, setProducto] = useState(null);

  const handleBuscar = async () => {
    if (!idProducto) return;
    try {
      const response = await fetch(
        `http://127.0.0.1:7000/productogetID?idproducto=${idProducto}`
      );
      const data = await response.json();
      setProducto(data);
    } catch (error) {
      console.error("Error al consultar producto:", error);
      setProducto(null);
    }
  };

  return (
    <div>
      <h3>Consultar Producto por ID</h3>
      <input
        type="text"
        placeholder="Ingrese ID del producto"
        value={idProducto}
        onChange={(e) => setIdProducto(e.target.value)}
      />
      <button onClick={handleBuscar}>Buscar</button>

      {producto && (
        <div style={{ marginTop: "10px" }}>
          <p><strong>Nombre:</strong> {producto.Nombre}</p>
          <p><strong>Descripción:</strong> {producto.Descripcion}</p>
          <p><strong>Precio:</strong> {producto.Precio}</p>
          <p><strong>Stock:</strong> {producto.Stock}</p>
          <p><strong>Activo:</strong> {producto.Activo === "1" ? "Sí" : "No"}</p>
        </div>
      )}
    </div>
  );
}

export default ConsultarProductoPorId;
