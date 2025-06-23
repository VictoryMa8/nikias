<script setup>
    import { onMounted, ref } from 'vue'
    import usePostsStore from '@/stores/posts'

    const postsStore = usePostsStore()

    const newPost = ref({
        title: '',
        description: '',
        image: null,
    })

    async function handleCreatePost() {
        try {
            await postsStore.createPost(newPost.value)
            // Clearing fields
            newPost.value.title = '',
            newPost.value.description = ''
            newPost.value.image == ''
        } catch (error) {
            alert('Error creating a new post...')
        }
    }

</script>

<template>
    <h1>New Post</h1>
    <!-- Looping through all posts -->
    <div class="new-post">
        <form @submit.prevent="handleCreatePost">
            <div>
                <label for="title">Title: </label>
                <input type="text" id="title" v-model="newPost.title" />
            </div>
            <div>
                <label for="description">Description: </label>
                <input type="text" v-model="newPost.description" />
            </div>
            <div>
                <label for="image">Image (optional): </label>
                <input type="text" v-model="newPost.image" />
            </div>
            <button type="submit">Post</button>
        </form>
    </div>
</template>

<style scoped>
    .new-post {
        width: 70%;
        display: flex;
        flex-direction: column;
        background-color: #186352;
        color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        gap: 10px;
    }
    .new-post form {
        font-size: 1.2rem;
    }
    .new-post div {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        font-size: 1.2rem;
    }
    .new-post input {
        font-family: 'EB Garamond', 'Times New Roman', Times, serif;
        width: 40%;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }
    .new-post button {
        margin: 0px 0px 20px 0px;
        width: 200px;
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

    .new-post button:hover {
        background-color: #02C39A;
        color: #000000;
        cursor: pointer;
    }
</style>