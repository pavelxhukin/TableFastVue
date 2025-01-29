export class ApiService {
    #axios;
    constructor (axios) {
        this.#axios = axios.create({
            baseURL: 'http://localhost:8089/api',
        });

    }

    async get(url, data = {
        headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
        }}){
            return await this.#axios.get(url, data);
        } 

    async post(url, data={}){
        return await this.#axios.post(url, data);
    }    
}


// {
//     headers: {
//     'Authorization': `Bearer ${localStorage.getItem('token')}`,
//     }
// }