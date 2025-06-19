<script setup>
import { ref } from 'vue'
import { useCounterStore } from './stores/counter'
const counterStore = useCounterStore();

const count = ref(0)
function increment() {
    count.value++
}

</script>

<template>
<h1>Hello World!</h1>
<h2> {{ count }}</h2>
<button @click="increment">Add +1</button>

<h2>New counter store thing:</h2>
<h2>Count: {{ counterStore.count  }}</h2>
<h2>Double of count: {{ counterStore.doubleCount }}</h2>
<h2>Is count even?: {{ counterStore.isCountEven }}</h2>
<button @click="counterStore.increment">Add +1</button>

</template>

<style scoped>

</style>
