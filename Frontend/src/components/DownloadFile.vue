<template>
    <!-- <img :src="imageUrl" alt="" /> -->
    <a :href="fileUrl" download>Download<i class="bi bi-cloud-download"></i></a>
</template>

<script setup>
import {config} from '../Constants.js';
import { ref, onMounted } from 'vue'

const props = defineProps({
    id: Number,
})

const fileUrl = ref('')
console.log(props.id)
onMounted(async () => {
    const response2 = await fetch(`${config.url}/api/get_brochure`, {
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
    fileUrl.value = objectUrl
})

</script>