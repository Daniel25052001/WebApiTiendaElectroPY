// src/components/ModificarProducto.js
import React, { useState } from "react";

function ModificarProducto() {
  const [idProducto, setIdProducto] = useState("");
  const [nombre, setNombre] = useState("");
  const [descripcion, setDescripcion] = useState("");
  const [precio, setPrecio] = useState(0);
  const [stock, setStock] = useState(0);
  const [activo, setActivo] = useState(true);
  const [mensaje, setMensaje] = useState("");

  const handleModificar = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:7000/productoput?idproducto=${idProducto}`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            idproducto: idProducto,
            nombre,
            descripcion,
            precio: Number(precio),
            stock: Number(stock),
            activo,
          }),
        }
      );
      const data = await response.json();
      setMensaje(data.mensaje || "Producto modificado correctamente");
    } catch (error) {
      console.error(error);
      setMensaje("Error al modificar el producto");
    }
  };

  return (
    <div>
      <h3>Modificar Producto</h3>
      <input
        type="text"
        placeholder="ID Producto"
        value={idProducto}
        onChange={(e) => setIdProducto(e.target.value)}
      />
      <input
        type="text"
        placeholder="Nombre"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
      />
      <input
        type="text"
        placeholder="Descripción"
        value={descripcion}
        onChange={(e) => setDescripcion(e.target.value)}
      />
      <input
        type="number"
        placeholder="Precio"
        value={precio}
        onChange={(e) => setPrecio(e.target.value)}
      />
      <input
        type="number"
        placeholder="Stock"
        value={stock}
        onChange={(e) => setStock(e.target.value)}
      />
      <label>
        Activo:
        <input
          type="checkbox"
          checked={activo}
          onChange={(e) => setActivo(e.target.checked)}
        />
      </label>
      <button onClick={handleModificar}>Modificar</button>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
}

export default ModificarProducto;


