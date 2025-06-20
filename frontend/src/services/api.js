import axios from 'axios';

// Creating an Axios instance with base configs
const api = axios.create({
    baseURL: 'http://localhost:8000', // Our Django backend URL
    timeout: 10000, // Timeout after 10 seconds
    headers: {
        "Content-Type": 'application/json'
    }
})