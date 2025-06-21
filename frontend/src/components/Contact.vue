<script setup>
    import useAuthStore from '@/stores/auth'
    const authStore = useAuthStore()
</script>

<template>
    <div class="content">
        <h1>Contact Us</h1>
        <h2>Need help with your account or have feedback?</h2>
        <h2>Contact us at: <b>victoryma23@gmail.com</b></h2>
        <RouterLink class="home" to="/home">Back To Home</RouterLink>
    </div>
</template>

<style scoped>
    .content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    h1, h2 {
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        text-align: center;
        margin: 0px;
        padding: 10px 0px;
    }

    .home {
        width: 200px;
        height: 30px;
        margin-top: 5px;
        padding: 5px 10px;
        font-size: 1.2rem;
        background-color: #1f7f6a;
        text-align: center;
        text-decoration: none;
        color: #FFFFFF;
        transition: background-color, 0.2s linear;
        transition: color, 0.2s linear;
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        border: none;
        border-radius: 15px;
    }

    .home:hover {
        background-color: #02C39A;
        color: #000000;
        cursor: pointer;
    }
</style>