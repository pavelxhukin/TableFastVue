<template>
    <h1>Loading...</h1>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import apiService from "../services/api";

import { useRouter } from 'vue-router';
const router = useRouter()

import { useUserStore } from '../stores/UserStore'
import { storeToRefs } from 'pinia'
const UserStore = useUserStore()
const { User } = storeToRefs(UserStore)

async function getUser() {
        try {
            const { data } = await apiService.JWTget("/user/",localStorage.getItem('token'));
            console.log(data)
            UserStore.setUserName(data.username)
            router.push({path:'/table'});
            }catch(error){
            console.error(error);
            router.push({path:'/login'});
        }
        
    };

onMounted(() => {
  getUser()
});

</script>


