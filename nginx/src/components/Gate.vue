<template>
    <h1>Loading...</h1>
</template>
  
<script>
import axios from "axios";

export default {
  name: "Gate",

  methods: {
    async getUser() {
        try {
            const { data } = await axios.get('http://localhost:4000/user/', {
        headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
        }
        });
        localStorage.setItem('username', data.username);
        this.$router.push('/table')
        }catch(error){
        console.error(error);
        localStorage.setItem('username', 'student');
        this.$router.push('/login')
        }
        
    },
  
  },
  beforeMount() {
    this.getUser();
  },
};
</script>


