<template>
    <div class="container">
      <h2>Register</h2>
      <form @submit.prevent="register">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" class="form-control">
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" class="form-control">
        </div>
        <div class="form-group">
          <label for="username">Group:</label>
          <input type="number" id="group_id" v-model="group_id" class="form-control">
        </div>
        <button type="submit" class="btn btn-primary">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import authService from '../services/auth';

  export default {
    name: 'UserRegister',
    data() {
      return {
        username: '',
        password: '',
        group_id: ''
      };
    },
    methods: {
      async register() {
        try {
          const response = await authService.post('/register', {
            username: this.username,
            userpassword: this.password,
            group_id: this.group_id
          }, {
            headers: {
              'Content-Type': 'application/json'
            }
          });
          print(response.body)
          localStorage.setItem('token', response.data.access_token);
          this.$router.push('/');
        } catch (error) {
          console.error(error);
        }
      }
    }
  };
  </script>