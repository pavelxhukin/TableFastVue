<template>
    <div class="container">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" class="form-control">
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" class="form-control">
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
      <div>
        <a href="/register">Dont have an account?</a>
      </div>
      </form> 
    </div>
</template>
  
  <script>
  import axios from 'axios';
  import authService from '../services/auth';

  export default {
    name: 'UserLogin',
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      async login() {
        try {
          const params = new URLSearchParams();
          params.append('username', this.username);
          params.append('password', this.password);
  
          const response = await authService.post('/token', params);
          localStorage.setItem('token', response.data.access_token);
          this.$router.push('/');
        } catch (error) {
          console.error(error);
        }
      }
    }
  };
  </script>

<style>
a {
  color: black;
}
a:hover{
  color:rgb(110, 4, 159);
}

</style>