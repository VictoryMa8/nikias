<script setup>
    import { onMounted } from 'vue'
    import useAuthStore from '@/stores/auth'
    import usePostsStore from '@/stores/posts'

    const authStore = useAuthStore()
    const postsStore = usePostsStore()

    // When component mounts, fetch posts
    onMounted(() => {
        postsStore.fetchPosts()
        console.log('Posts: ', postsStore.posts)
    })

    // Just using our Pinia authStore with Axios similar to how we logged in
    function handleLogout() {
        authStore.logout()
    }
</script>

<template>
    <div class="content">
        <h1>Welcome to the home. You are logged in.</h1>
        <button class="sign-out" @click="handleLogout">Sign Out</button>
        <!-- Looping through all posts -->
        <div v-if="postsStore.posts.length > 0">
            <div v-for="post in postsStore.posts" :key="post.created_at">
                <h2>{{ post.title }}</h2>
                <p>{{ post.description }}</p>
                <p>{{ post.author_username }}</p>
                <p>{{ post.created_at }}</p>
            </div>
        </div>
        <!-- There are no posts found -->
        <div v-else>No posts found. Be the first to create one!</div>
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
        transition: background-color, 0.2s linear;
        transition: color, 0.2s linear;
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        border-radius: 15px;
    }

    .sign-out:hover {
        background-color: #02C39A;
        color: #000000;
        cursor: pointer;
    }
</style>