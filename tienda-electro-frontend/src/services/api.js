
import axios from "axios";

// Cambia esta URL si tu backend corre en otro puerto
const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // URL de tu backend FastAPI
});

export default api;
