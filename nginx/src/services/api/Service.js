export class ApiService {
    #axios;
    #base_url; 
    constructor (axios) {
        this.#axios = axios.create({});
        this.#base_url = "http://localhost/api";
    }

    JWTget(url, token) {
        return this.#axios.get(this.#base_url+url, {
            headers: {
                Authorization: `Bearer ${token}`
            }
            });
        
    }

    get(url) {
        return this.#axios.get(this.#base_url+url);
    }
}
