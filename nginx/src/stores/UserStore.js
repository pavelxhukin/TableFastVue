import {defineStore} from 'pinia'

export const useUserStore = defineStore('userStore', {
    state: () => ({
        userData: {
            name: null,
        }
    }),
    actions: {
        setUserName(name) {
            this.userData.name = name;
        },
    }
});