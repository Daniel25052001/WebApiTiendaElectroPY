// components/AgregarProducto.js
import React, { useState } from "react";

const AgregarProducto = () => {
  const [nombre, setNombre] = useState("");
  const [descripcion, setDescripcion] = useState("");
  const [precio, setPrecio] = useState("");
  const [stock, setStock] = useState("");
  const [activo, setActivo] = useState(false);//se modifico el true para que no aparezca como activo por defecto
  const [mensaje, setMensaje] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const producto = {
      idproducto: "", // El backend puede generar el ID si es automático
      nombre,
      descripcion,
      precio: parseFloat(precio),
      stock: parseInt(stock),
      activo,
    };

    try {
      const response = await fetch("http://127.0.0.1:7000/productopost", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(producto),
      });

      const data = await response.json();
      setMensaje(data.mensaje);
      // Limpiar formulario
      setNombre("");
      setDescripcion("");
      setPrecio("");
      setStock("");
      setActivo(true);
    } catch (error) {
      setMensaje("Error al agregar el producto: " + error);
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Agregar Producto</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Nombre:</label>
          <input
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Descripción:</label>
          <input
            type="text"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Precio:</label>
          <input
            type="number"
            value={precio}
            onChange={(e) => setPrecio(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Stock:</label>
          <input
            type="number"
            value={stock}
            onChange={(e) => setStock(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Activo:</label>
          <input
            type="checkbox"
            checked={activo}
            onChange={(e) => setActivo(e.target.checked)}
          />
        </div>
        <button type="submit">Agregar</button>
      </form>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
};

export default AgregarProducto;
