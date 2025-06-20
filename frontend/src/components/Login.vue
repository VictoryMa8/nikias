<script setup>
    import { ref } from 'vue'
    import useAuthStore from '@/stores/auth'

    const authStore = useAuthStore()

    const data = ref({
        username: '',
        password: '',
    })

    // Simple function using our Pinia authStore with Axios to login with credentials
    async function handleLogin() {
        // Pass in our username and password into our authStore method
        const result = await authStore.login(data.value.username, data.value.password)
        console.log(data.value.username, data.value.password)
        if (!result) {
            console.log('Login failed...')
        }
    }

</script>

<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="handleLogin">
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