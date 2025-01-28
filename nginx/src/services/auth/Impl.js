import AuthService from "./Service";
import apiService from "../api";

const authService = new AuthService(apiService);

export default authService;
