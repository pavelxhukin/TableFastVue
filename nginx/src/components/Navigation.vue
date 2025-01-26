<template>
    <nav>
        <h4>Wellcome back, {{ name }}!</h4>
        <li><a href="/login">Login</a></li>
        <li></li>
        <li><a href="/table">Schedule</a></li>
    </nav>
</template>
  


<script setup>
import {ref, onMounted} from 'vue'
const name = ref('')

onMounted(() => {
  name.value = localStorage.getItem('username') || 'student'
})
</script>

<style>
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
