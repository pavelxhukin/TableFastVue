export class ApiService {
    #axios;

    constructor (axios) {
        this.#axios = axios.create({});
    }

    get(...args) {
        return this.#axios.get(...args)
    }

    put(...args) {
        // --//--
    }
}
