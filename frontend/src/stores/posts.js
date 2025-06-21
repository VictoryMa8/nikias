import { ref } from 'vue'
import { defineStore } from 'pinia'
import api from '@/services/api'
import useAuthStore from '@/stores/auth'

const usePostsStore = defineStore('posts', () => {
    const posts = ref([])

    async function fetchPosts() {
        try {
            const authStore = useAuthStore()
            const response = await api.get('/posts/', {
                headers: {
                    'Authorization': `Bearer ${authStore.accessToken}`
                }
            })
            posts.value = response.data
        } catch (error) {
            console.log('Error fetching posts: ', error)
        }
    }

    return {
        posts,
        fetchPosts
    }
})

export default usePostsStore