// App.js
import React from "react";

// ----------------- Sección Países -----------------
import ListaPaises from "./components/ListaPaises";

// ----------------- Sección Departamentos -----------------
import ListaDepartamentos from "./components/ListaDepartamentos";

// ----------------- Sección Ciudades -----------------
import ListaCiudades from "./components/ListaCiudades";
import ConsultarCiudadPorId from "./components/ConsultarCiudadPorId";
import AgregarCiudad from "./components/AgregarCiudad";
import ModificarCiudad from "./components/ModificarCiudad";
import EliminarCiudad from "./components/EliminarCiudad";

// ----------------- Sección Sedes -----------------
import ListaSedes from "./components/ListaSedes";

// ----------------- Sección Productos -----------------
import ListaProductos from "./components/ListaProductos";
import ConsultarProductoPorId from "./components/ConsultarProductoPorId";
import AgregarProducto from "./components/AgregarProducto";
import ModificarProducto from "./components/ModificarProducto";
import EliminarProducto from "./components/EliminarProducto";

function App() {
  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Tienda Electro - Gestión de la API</h1>

      {/* ----------------- Países ----------------- */}
      <section>
        <h2>Países</h2>
        <ListaPaises />
      </section>

      {/* ----------------- Departamentos ----------------- */}
      <section>
        <h2>Departamentos</h2>
        <ListaDepartamentos />
      </section>

      {/* ----------------- Gestión de Ciudades ----------------- */}
      <section>
        <h2>Ciudades</h2>
        <ListaCiudades />
        <ConsultarCiudadPorId />
        <AgregarCiudad />
        <ModificarCiudad />
        <EliminarCiudad />
      </section>

      {/* ----------------- Sedes ----------------- */}
      <section>
        <h2>Sedes</h2>
        <ListaSedes />
      </section>

      {/* ----------------- Gestión de Productos ----------------- */}
      <section>
        <h2>Productos</h2>
        <ListaProductos />
        <ConsultarProductoPorId />
        <AgregarProducto />
        <ModificarProducto />
        <EliminarProducto />
      </section>
    </div>
  );
}

export default App;
