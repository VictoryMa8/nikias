<script setup>
    import useAuthStore from '@/stores/auth'
    const authStore = useAuthStore()

    // Just using our Pinia authStore with Axios similar to how we logged in
    function handleLogout() {
        authStore.logout()
    }
</script>

<template>
    <h1>Welcome to the home. You are logged in.</h1>
    <button @click="handleLogout">Sign Out</button>
</template>