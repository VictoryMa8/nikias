import { createWebHistory, createRouter } from 'vue-router'

import Home from '../components/Home.vue'
import Login from '../components/Login.vue'

const routes = [
    { path: '/', redirect: '/home'}, // Default route that redirects to home (if logged in)
    { path: '/login', name: 'Login', component: Login },
    { path: '/home', name: 'Home', component: Home, meta: { requiresAuth: true }}, // Meta field marks the route as protected
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// Nagivation guard (before any navigation happens)
router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem('access_token')
    // Check if the route has meta: { requiresAuth: true }
    // Also checks if user is logged in (has access token in localStorage)
    if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
        next('/login')
    // If page is not protected or user is logged in, good to navigate
    } else {
        next()
    }
})

export default router