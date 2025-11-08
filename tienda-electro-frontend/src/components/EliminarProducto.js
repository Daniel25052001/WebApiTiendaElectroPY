import { useState } from "react";

function EliminarProducto({ onProductoEliminado }) {
  const [idProducto, setIdProducto] = useState("");
  const [mensaje, setMensaje] = useState("");

  const handleEliminar = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:7000/productodelete?idproducto=${idProducto}`,
        { method: "DELETE" }
      );
      const data = await response.json();
      setMensaje(data.mensaje);
      setIdProducto("");
      if (onProductoEliminado) onProductoEliminado(); // Actualiza la lista de productos
    } catch (error) {
      setMensaje("Error al eliminar producto");
    }
  };

  return (
    <div>
      <h3>Eliminar Producto</h3>
      <input
        type="text"
        placeholder="Ingrese ID del producto"
        value={idProducto}
        onChange={(e) => setIdProducto(e.target.value)}
      />
      <button onClick={handleEliminar}>Eliminar</button>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
}

export default EliminarProducto;
