import { defineStore } from "pinia";

export const useCounterStore = defineStore('counter', {
    // state is our data we want to track
    state: () => ({
        count: 0
    }),

    // getters are computed properties based on our state
    getters: {
        doubleCount: (state) => state.count * 2,
        isCountEven: (state) => state.count % 2 === 0
    },

    // actions are functions that can modify our state
    actions: {
        increment() {
            this.count++
        },
        decrement() {
            this.count--
        },
        setCount(newCount) {
            this.count = newCount
        }
    }
})