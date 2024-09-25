<template>
    <img :src="imageUrl" alt="" />
</template>

<script setup>
import {config} from '../Constants.js';
import { ref, onMounted } from 'vue'

const props = defineProps({
    id: Number,

})
const imageUrl = ref('')
console.log(props.id)
onMounted(async () => {
    const response2 = await fetch(`${config.url}/api/get_poster_img`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            id: props.id,
        })
    })
    const blob = await response2.blob()
    const objectUrl = URL.createObjectURL(blob)
    imageUrl.value = objectUrl
})

</script>