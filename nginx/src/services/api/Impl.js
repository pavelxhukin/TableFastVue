import axios from "axios";
import { ApiService } from "./Service";

const apiService = new ApiService(axios);

export default apiService;
