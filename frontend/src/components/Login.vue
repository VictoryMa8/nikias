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
    <div class="content">
        <h1 class="title">Welcome to Nikias, the social media platform for peace of mind 🌿</h1>
        <img src="../assets/images/logo.png">
        <div class="login-items">
            <h2>Login to start connecting with your friends 🫂</h2>
            <form @submit.prevent="handleLogin">
                <div>
                    <label for="username">Username: </label>
                    <input type="text" id="username" v-model="data.username" />
                </div>
                <div>
                    <label for="password">Password: </label>
                    <input type="password" v-model="data.password" />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
        <button>Sign Up</button>
    </div>
</template>

<style scoped>
    template {
        margin: 0px;
        padding: 0px;
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .content img {
        width: 250px;
    }

    .title {
        background-color: #02644F;
        color: #FFFFFF;
        width: 100%;
        margin: 0;
    }

    h1 {
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        text-align: center;
        margin: 0px;
        padding: 20px 0px;
    }

    h2 {
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        text-align: center;
        margin: 10px 20px;
        color: #FFFFFF;
    }

    .login-items {
        display: flex;
        flex-direction: column;
        background-color: #02644F;
        margin: 20px;
        padding: 10px;
        border: 1px solid #02251e;
        border-radius: 15px;
    }

    .login-items h1 {
        margin: 0;
    }

    .login-items form {
        margin: 0px;
        padding: 0px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .login-items form div {
        display: flex;
        flex-direction: column;
        margin: 0px;
        padding: 0px;
    }

    .login-items form input {
        width: 200px;
        height: 40px;
        font-size: 1.2rem;
        margin: 5px 0px 20px 0px;
        font-family: 'Times New Roman', Times, serif;
        border: 1px solid #02251e;
        border-radius: 15px;
        padding: 5px;
    }

    .login-items form input:focus {
        outline: 2px solid #02C39A;
        outline-offset: 1px; 
    }

    .login-items form label {
        font-size: 1.2rem;
        color: #FFFFFF;
    }

    .login-items form button {
        width: 200px;
        height: 40px;
        font-size: 1.2rem;
        background-color: #034033;
        color: #FFFFFF;
        transition: background-color, 0.2s linear;
        transition: color, 0.2s linear;
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        border: 1px solid #02251e;
        border-radius: 15px;
    }

    .content button {
        margin: 0px 0px 20px 0px;
        width: 300px;
        height: 40px;
        font-size: 1.2rem;
        background-color: #1f7f6a;
        color: #FFFFFF;
        transition: background-color, 0.2s linear;
        transition: color, 0.2s linear;
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        border: 1px solid #02251e;
        border-radius: 15px;
    }

    .login-items form button:hover, .content button:hover {
        background-color: #02C39A;
        color: #000000;
        cursor: pointer;
    }
</style>