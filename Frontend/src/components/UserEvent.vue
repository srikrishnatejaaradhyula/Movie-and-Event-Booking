<template>
    <UserNavBar class="sticky-top z-1" />
    <!-- <div class="overflow-y-hidden" >
        <div class="d-grid gap-2 d-md-flex justify-content-md-end d-grid gap-2 w-auto" >
            <button class=" primary-button m-2" @click="$router.push('/create_event')">Add Event</button>
        </div>
    </div> -->
    <div class="container ">
            <div class="row" >
                <div class="col-md-6" v-for="e in event.events" :key="e.id">

                    <div class="booking-card card  my-3 z-0">
                        <div class="card-body">
                                <div class="row col-md-12">
                                    <div class="col-6">
                                        <h3 class="md-4">
                                            {{ e.name }} 
                                            <a :href="e.location" class="m-2 h-auto" target="_blank" data-bs-toggle="tooltip" data-bs-placement="top" title="Tooltip on top">
                                                <i class="bi bi-geo-alt"></i>
                                            </a>
                                        </h3>
                                        <DownloadFile class="btn btn-outline-info mt-2" :id="e.id" />

                                    </div>
                                    <div class="col-6">
                                        <button type="button"   @click="IsModalEvent.ids[e.id] = true" class="mb-3 btn btn-warning" style="height: min-content;">
                                        View Details <i class="bi bi-box-arrow-up-right"></i></button>
                                        <br>
                                        <button type="button"   @click="$router.push('/event_booking/'+ e.id)"  class=" btn btn-success" style="height: min-content;">
                                        Book <i class="bi bi-ticket-perforated"></i></button>
                                        
                                    </div>
                                </div>
                                <Teleport to="#modal">
                                    <div class="modal-bg z-2" v-if="IsModalEvent.ids[e.id]">
                                        <div class="position-relative container h-auto w-auto modal_box p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                            <div class=" position-absolute top-0 end-0 "> 
                                                <button @click="IsModalEvent.ids[e.id] = false" class="m-2 border-0 rounded-5 ">
                                                    <i class="bi bi-x-lg" style="color:brown"></i>
                                                </button>
                                            </div>
                                                
                                            <h4> Event details </h4>
                                            <div class="row">
                                                <div class="col-md-10">
                                                    <table class="table table-striped-columns " >
                                                        <tbody >
                                                            <tr>
                                                                <th>Name</th>
                                                                <td>{{ e.name }}</td>
                                                            </tr>
                                                            <tr>
                                                                <th>Description</th>
                                                                <td>{{ e.description}}</td>
                                                            </tr>
                                                            <tr>
                                                                <th>Address</th>
                                                                <td>{{ e.address }}</td>
                                                            </tr>
                                                            <tr>
                                                                <th>Date</th>
                                                                <td>{{ e.date }}</td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                                
                                            </div>
                                        </div>

                                    </div>
                                </Teleport>
                        </div>
                    </div>
                    
                    
                </div>
            </div>
        </div>
</template>

<script setup>
import {config} from '../Constants.js';
import { ref, onMounted, reactive,defineProps } from "vue";
import VueJwtDecode from 'vue-jwt-decode'
import { toast } from 'vue3-toastify';
import DownloadFile from './DownloadFile.vue';



const token = localStorage.getItem('token')
const user = VueJwtDecode.decode(token)

const event = reactive({
        events: []
})

const IsModalEvent = reactive({
    ids: []
});

const fetchEvents = async () => {
    const response = await fetch(`${config.url}/api/get_event_all`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
        })
    });
    const data = await response.json();
    event.events = data;
    for (let i = 0; i < event.events.length; i++) {
        IsModalEvent.ids[event.events[i].id] = false
    }
}

onMounted(() => {
    fetchEvents();
})



</script>

<style  scoped>
.booking-card{
    background: rgba(182, 249, 254, 0.226);
    /* backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px); */
    border-radius: 10px;
    width: auto;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border: 1px solid rgba(255, 255, 255, 0.08);
}
</style>