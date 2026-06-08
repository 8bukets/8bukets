import axios from "axios";
import { API_URL } from "../lib/config";

const API = axios.create({
  baseURL: API_URL,
});

export default API;
