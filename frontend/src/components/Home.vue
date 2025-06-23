<script setup>
    import useAuthStore from '@/stores/auth'
    import Posts from './Posts.vue'
    import Profile from './Profile.vue'
    const authStore = useAuthStore()

    // Just using our Pinia authStore with Axios similar to how we logged in
    function handleLogout() {
        authStore.logout()
    }
</script>

<template>
    <div class="content">
        <h1>Welcome to the home. You are logged in.</h1>
        <button class="sign-out" @click="handleLogout">Sign Out</button>
        <Posts></Posts>
        <Profile></Profile>
    </div>
</template>

<style scoped>
    .content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    h1 {
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        text-align: center;
        margin: 0px;
        padding: 20px 0px;
    }

    .sign-out {
        margin: 0px 0px 20px 0px;
        width: 300px;
        height: 40px;
        font-size: 1.2rem;
        background-color: #1f7f6a;
        color: #FFFFFF;
        transition: background-color, 0.4s ease;
        transition: color, 0.4s ease;
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        border-radius: 15px;
        border: none;
    }

    .sign-out:hover {
        background-color: #02C39A;
        color: #000000;
        cursor: pointer;
    }
</style>