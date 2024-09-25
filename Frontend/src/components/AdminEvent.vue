<template>
    <AdminNavBar class="sticky-top z-1" />
    <div class="overflow-y-hidden" >
        <div class="d-grid gap-2 d-md-flex justify-content-md-end d-grid gap-2 w-auto" >
            <button class=" primary-button m-2" @click="$router.push('/create_event')">Add Event</button>
        </div>
    </div>
    <div class="container ">
            <div class="row" >
                <div class="col-md-6" v-for="e in event.events" :key="e.id">

                    <div class="booking-card card  my-3 z-0">
                        <div class="card-body">
                                <div class="row col-md-12">
                                    <div class="col-6">
                                        <h3>
                                            {{ e.name }} 
                                            <a :href="e.location" class="m-2 h-auto" target="_blank" data-bs-toggle="tooltip" data-bs-placement="top" title="Tooltip on top">
                                                <i class="bi bi-geo-alt"></i>
                                            </a>
                                        </h3>
                                        <DownloadFile class="btn btn-outline-info" :id="e.id" />

                                    </div>
                                    <div class="col-6">
                                        <button type="button"   @click="IsModalEvent.ids[e.id] = true" class="mb-3 btn btn-warning" style="height: min-content;">
                                        View Details <i class="bi bi-box-arrow-up-right"></i></button>
                                        <button type="button"  @click="export_csv(e.id)"  class=" btn btn-success" style="height: min-content;">
                                        import booking <i class="bi bi-box-arrow-down"></i></button>
                                        
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
                                                <div class="col-md-2 ">
                                                    <div class="col-md-12 m-2">
                                                        <button @click="$router.push('/update_event/'+ e.id)" class=" rounded-2 border-0" style="color:aliceblue; background-color: rgb(88, 88, 255); font-size: xx-large;">
                                                            <i class="bi bi-pencil-square"></i>
                                                        </button>
                                                    </div>
                                                    <div class="col-md-12 m-2">
                                                        <button @click="IsModalEventDelete.ids[e.id] = true" class=" rounded-2 border-0" style="color:aliceblue; background-color: rgb(255, 87, 87); font-size: xx-large;">
                                                            <i class="bi bi-trash-fill"></i>
                                                        </button>
                                                    </div>
                                                </div>
                                                
                                            </div>
                                        </div>

                                    </div>
                                </Teleport>

                                <Teleport to="#modal1">
                                    <div class="modal-bg z-3" v-if="IsModalEventDelete.ids[e.id]">
                                        <div class=" position-relative container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                            <div class=" position-absolute top-0 end-0 "> 
                                                <button @click="IsModalEventDelete.ids[e.id] = false" class="m-2 border-0 rounded-5 ">
                                                    <i class="bi bi-x-lg" style="color:brown"></i>
                                                </button>
                                            </div>
                                            <h5 class="text-center">Are you sure you want to Delete Event?</h5>
                                            
                                            <div class="container d-flex justify-content-center align-center">
                                                <div class="row d-flex justify-content-evenly" >
                                                    <div class="col text-center " >
                                                        <button type="button" @click="DeleteEvent(e.id)"  class="btn btn-success " >
                                                            conform!
                                                        </button>
                                                    </div>
                                                    <div class="col text-center ">
                                                        <button type="button" @click="IsModalEventDelete.ids[e.id] = false"  class="btn btn-danger">Cancel</button>
                                                    </div>
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
import {csvParser} from '../csv-parser.js'
import {config} from '../Constants.js';
import { ref, onMounted, reactive,defineProps } from "vue";
import VueJwtDecode from 'vue-jwt-decode'
import { toast } from 'vue3-toastify';
import DownloadFile from './DownloadFile.vue';



const token = localStorage.getItem('isAdmin')
const user = VueJwtDecode.decode(token)

const event = reactive({
        events: []
})

const eventBooking = reactive({
    booking :[]
})

const IsModalEvent = reactive({
    ids: []
});
const IsModalEventDelete = reactive({
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
        IsModalEventDelete.ids[event.events[i].id] = false
    }
}

onMounted(() => {
    fetchEvents();
})

const DeleteEvent = (id) =>{
    fetch(`${config.url}/api/delete_event`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
            id: id
        })
    }).then((response) => {
        if (response.status == 200) {
            toast.success('Event Deleted Successfully');
            fetchEvents();
        } else {
            toast.error('Something went wrong');
        }
    })

}
const export_csv = async(id) =>{
    console.log("export csv")   
    const response = await fetch(`${config.url}/api/get_event_and_booking`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        },
        body: JSON.stringify({
        // admin_id: user.id
        event_id : id
        })
    });
    const data = await response.json();
    eventBooking.booking = data;
    console.log(eventBooking.booking)
    if (response.status != 200) {
        // throw new Error(data.message)
        toast.error(data.message);
    }
    csvParser().exportDataFromJSON(eventBooking.booking, "event-bookings-report-csv", "csv");
}
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