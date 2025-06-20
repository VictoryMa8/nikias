import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import api from '@/services/api'
import router from '@/router'

const useAuthStore = defineStore('auth', () => {
    // State of tokens and user
    const accessToken = ref(localStorage.getItem('access_token'))
    const refreshToken = ref(localStorage.getItem('refresh_token'))
    const user = ref(null)
    // Getters, is the user authenticated?
    const isAuthenticated = computed(() => accessToken.value)
    // Actions (login and logout)
    async function login(username, password) {
        try {
            const response = await api.post('/token/', { username, password })
            accessToken.value = response.data.access
            refreshToken.value = response.data.refresh
            // Sync with localStorage
            localStorage.setItem('access_token', response.data.access)
            localStorage.setItem('refresh_token', response.data.refresh)
            // Redirect to homepage
            router.push('/home')
            return true
        } catch (error) {
            return false
        }
    }
    // Setting the tokens to null and removing them from localStorage, setting user to null
    function logout() {
        accessToken.value = null
        refreshToken.value = null

        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')

        router.push('/login')
    }

    return {
        accessToken,
        refreshToken,
        user,
        isAuthenticated,
        login,
        logout
    }
})

export default useAuthStore