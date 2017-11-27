import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

// customer define
import Login from '../components/login.vue'
import UserInfo from '../components/UserInfo.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/login', omponent: Login },
    { path: '/user_info', component: UserInfo }
  ]
})
