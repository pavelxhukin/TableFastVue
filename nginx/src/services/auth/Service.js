export default class AuthService {
    #api;
    #prefix = '/auth';

    constructor(api) {
        this.#api = api;
    }

    async post(url, body={}) {
        return await this.#api.post(this.#prefix+url,body);
    }
}