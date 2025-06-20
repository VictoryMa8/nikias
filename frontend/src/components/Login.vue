<script setup>
    import { ref } from 'vue'
    import axios from 'axios'
    import { useRouter } from 'vue-router'

    const router = useRouter()

    const data = ref({
        username: '',
        password: '',
    })

    // Simple function using Axios to hit /api/token/ endpoint
    async function login() {
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/token/', {
                username: data.value.username,
                password: data.value.password
            })
            // Setting tokens in local storage
            localStorage.setItem('access_token', response.data.access)
            localStorage.setItem('refresh_token', response.data.refresh)
            // Redirect to homepage after successful login
            router.push('/home')
        } catch (error) {
            console.log('Error occurred: ', error)
        }
    }

</script>

<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="login">
            <div>
                <label for="username">Username: </label>
                <input type="text" id="username" v-model="data.username" />
            </div>
            <div>
                <label for="password">Password: </label>
                <input type="text" id="password" v-model="data.password" />
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</template>