import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import api from '@/services/api'
import router from '@/router'

const useAuthStore = defineStore('auth', () => {
    // State of tokens and user
    const accessToken = ref(localStorage.getItem('access_token'))
    const refreshToken = ref(localStorage.getItem('refresh_token'))
    const user = ref(localStorage.getItem('username'))
    const profiles = ref([])

    // Getters, is the user authenticated?
    const isAuthenticated = computed(() => accessToken.value)

    // Actions (login and logout)
    async function login(username, password) {
        try {
            const response = await api.post('/token/', { username, password })
            accessToken.value = response.data.access
            refreshToken.value = response.data.refresh
            user.value = username

            // Sync with localStorage
            localStorage.setItem('access_token', response.data.access)
            localStorage.setItem('refresh_token', response.data.refresh)
            localStorage.setItem('username', username)
            
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
        user.value = null
        profiles.value = []

        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('username')

        router.push('/login')
    }

    // Fetch profile of the current user
    async function fetchProfiles() {
        try {
            const authStore = useAuthStore()
            const response = await api.get('/profiles/', {
                headers: {
                    'Authorization': `Bearer ${authStore.accessToken}`
                }
            })
            profiles.value = response.data
        } catch (error) {
            console.log('Error fetching user profiles: ', error)
        }
    }

    return {
        accessToken,
        refreshToken,
        user,
        profiles,
        isAuthenticated,
        login,
        logout,
        fetchProfiles
    }
})

export default useAuthStore