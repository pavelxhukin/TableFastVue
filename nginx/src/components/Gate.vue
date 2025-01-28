<template>
    <h1>Loading...</h1>
</template>

<script setup>
import axios from "axios";
import {ref, onMounted} from 'vue'

import { useRouter } from 'vue-router';
const router = useRouter()

import { useUserStore } from '../stores/UserStore'
const UserStore = useUserStore()

async function getUser() {
        try {
            const { data } = await axios.get('http://localhost:4000/user/', {
        headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
        }
        });
        localStorage.setItem('username', data.username);
        UserStore.setUserName(data.username)
        router.push({path:'/table'});
        }catch(error){
        console.error(error);
        localStorage.setItem('username', 'student');
        router.push({path:'/login'});
        }
        
    };

onMounted(() => {
  getUser()
});

</script>


