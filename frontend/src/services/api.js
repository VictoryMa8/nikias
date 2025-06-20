import axios from 'axios';
import router from '@/router';

// Creating an Axios instance with base configs
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api', // Our Django backend URL
    timeout: 10000, // Timeout after 10 seconds
})

// Request interceptor that adds the access token to all requests
api.interceptors.request.use(config => {
    const token = localStorage.getItem('access_token')
    if (token) {
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
})

// Response interceptor that handles token refreshes/logout
api.interceptors.response.use(response => response,
    async error => {
        // If token is expired or invalid
        if (error.response.status === 401) {
            localStorage.removeItem('access_token')
            localStorage.removeItem('refresh_token')
            router.push('/login')
        }
        return Promise.reject(error)
    }
)

export default api