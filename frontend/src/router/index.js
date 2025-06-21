import { createWebHistory, createRouter } from 'vue-router'
import useAuthStore from '@/stores/auth'
import Home from '@/components/Home.vue'
import Login from '@/components/Login.vue'
import Contact from '@/components/Contact.vue'
import SignUp from '@/components/SignUp.vue'

const routes = [
    { path: '/', redirect: '/home'}, // Default route that redirects to home (if logged in)
    { path: '/login', name: 'Login', component: Login },
    { path: '/home', name: 'Home', component: Home, meta: { requiresAuth: true }}, // Meta field marks the route as protected
    { path: '/contact', name: 'Contact', component: Contact }, // Accessible to anyone who needs help
    { path: '/sign-up', name: 'Sign Up', component: SignUp }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// Nagivation guard (before any navigation happens)
router.beforeEach((to, from, next) => {
    const authStore = useAuthStore();
    // If route requiresAuth and user is not authenticated, go to /login
    if (to.matched.some(record => record.meta.requiresAuth) && !authStore.isAuthenticated) {
        next('/login')
    // If page is not protected or user is logged in, good to navigate
    } else {
        next()
    }
})

export default router