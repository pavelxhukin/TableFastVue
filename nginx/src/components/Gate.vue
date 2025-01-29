<template>
    <h1>Loading...</h1>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import apiService from "../services/api";
import axios from "axios";

import { useRouter } from 'vue-router';
const router = useRouter()

import { useUserStore } from '../stores/UserStore'
import { storeToRefs } from 'pinia'
const UserStore = useUserStore()
const { User } = storeToRefs(UserStore)

async function getUser() {
        try {
            const { data: response } = await apiService.get("/user");
            console.log("username must be here: "+response.username);
            UserStore.setUserName(response.username);
            router.push({path:'/table'});
        }catch(error){
            console.error(error.body);
            router.push({path:'/login'});
        }
        
    };

onMounted(() => {
  getUser()
});

</script>


