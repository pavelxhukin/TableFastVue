<template>
    <nav>
        <h4>Wellcome back, {{ username.name? username.name : "student"}}!</h4>
        <li>
          <button class="btn" @click="onButtonClick()">
            <span v-if="username.name">logOut</span>
            <span v-else>login</span>
          </button>
        </li>
        <li><a href="/table">Schedule</a></li>
    </nav>
</template>
  


<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
import axios from "axios";
import apiService from '../services/api';
import {ref, onMounted} from 'vue'
const name = ref('')

onMounted(() => {
  name.value = localStorage.getItem('username') || 'student'
})

import { useUserStore } from '../stores/UserStore'
import { storeToRefs } from 'pinia'
const UserStore = useUserStore()
const { userData : username } = storeToRefs(UserStore)

function onButtonClick(){
  if (UserStore.userData.name){
    try{ 
      const { data } = apiService.get("/exit/");
    }catch(error){
      console.error(error)
    }
    UserStore.setUserName(null);
    localStorage.removeItem('token');
  }
  router.push({path:'/'});
}

</script>

<style scoped>
button {
    border-radius: 0px;
    padding: 0.6em 1.2em;
    font-size: 1em;
    font-weight: 500;
    font-family: inherit;
    color: #ffffff;
    cursor: pointer;
    transition: border-color 0.25s;
    margin-bottom: 0px;
  }
button:hover {
    background-color: #ffffff;
    color: #000000;
  }
nav {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
}

nav h4 {
  float: left;
  display: block;
  color: white;
  text-align: center;
  padding: 14px 26px;
  text-decoration: none;
  margin: 0;
}

li {
  float: right;
  margin-right: 15px;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 26px;
  text-decoration: none;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  background-color: #111;
}
</style>
