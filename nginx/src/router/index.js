import { createWebHistory, createRouter } from 'vue-router';
import UserRegister from '../components/UserRegister.vue';
import UserLogin from '../components/UserLogin.vue';
import TableList from '../components/TableList.vue';
import Gate from '../components/Gate.vue';


const routes = [
  {
    path: '/',
    name: 'Gate',
    component: Gate 
  },
  {
    path: '/register',
    name: 'UserRegister',
    component: UserRegister
  },
  {
    path: '/login',
    name: 'UserLogin',
    component: UserLogin
  },
  {
    path: '/table',
    name: 'TableList',
    component: TableList
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
