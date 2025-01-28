export default class AuthService {
    #api;
    #prefix = '/auth';

    constructor(api) {
        this.#api = api;
    }

    login(body) {
        return this.#api.put(this.#prefix, { body });
    }
}