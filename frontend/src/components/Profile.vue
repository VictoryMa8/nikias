<script setup>
    import { onMounted } from 'vue'
    import useAuthStore from '@/stores/auth'

    const authStore = useAuthStore()

    // When component mounts, fetch profile
    onMounted(() => {
        authStore.fetchProfiles()
        console.log('Profile: ', authStore.profiles)
    })
    
</script>

<template>
    <h1>Profiles</h1>
    <div class="list-of-profiles" v-if="authStore.profiles.length > 0">
        <div class="profile" v-for="profile in authStore.profiles" :key="profile.created_at">
            <h2>{{ profile.user.username }}</h2>
            <p>{{ profile.bio }}</p>
            <p>{{ profile.created_at }}</p>
        </div>
    </div>
    <!-- There are user profiles found -->
    <div v-else>Couldn't load user profiles, sorry!</div>
</template>

<style scoped>
    .list-of-profiles {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        background-color: #186352;
        color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        gap: 10px;
        margin-top: 10px;
    }
    .profile {
        border: 1px #ffffff solid;
        border-radius: 15px;
        padding: 20px;
    }
</style>