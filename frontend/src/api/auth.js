import axios from "axios";

const API = "http://127.0.0.1:8000/api/auth";

export const register = (email, password) =>
  axios.post(`${API}/register`, { email, password });

export const login = (email, password) =>
  axios.post(`${API}/login`, { email, password });