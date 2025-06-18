<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
    count.value++
}

</script>

<template>
<h1>Hello World!</h1>
<button @click="increment">Count: {{ count }}</button>
</template>

<style scoped>

</style>
