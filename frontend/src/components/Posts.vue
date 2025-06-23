<script setup>
    import { onMounted } from 'vue'
    import usePostsStore from '@/stores/posts'

    const postsStore = usePostsStore()

    // When component mounts, fetch posts
    onMounted(() => {
        postsStore.fetchPosts()
        console.log('Posts: ', postsStore.posts)
    })

    function formatDate(date) {
        const dateObject = new Date(date);
        return dateObject.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: 'numeric',
            minute: 'numeric'
        });
    }

</script>

<template>
    <h1>Posts</h1>
    <!-- Looping through all posts -->
    <div class="list-of-posts" v-if="postsStore.posts.length > 0">
        <div class="post" v-for="post in postsStore.posts" :key="post.created_at">
            <h2>{{ post.title }}</h2>
            <p>{{ post.description }}</p>
            <p>{{ post.author_username }}</p>
            <p>{{ formatDate(post.created_at) }}</p>
        </div>
    </div>
    <!-- There are no posts found -->
    <div v-else>No posts found. Be the first to create one!</div>
</template>

<style scoped>
    .list-of-posts {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        background-color: #186352;
        color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        gap: 10px;
    }
    .post {
        border: 1px #ffffff solid;
        border-radius: 15px;
        padding: 20px;
    }
</style>