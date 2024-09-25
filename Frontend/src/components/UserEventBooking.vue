<template>
    <UserNavBar/>
    <div>
        <div class="container ">
            <div class="row" >
                <div class="col-md-6" v-for="e in event.events" :key="e.id">
                    <div class="booking-card card  my-3 z-0">
                        <div class="card-body">
                                <div class="row col-md-12">
                                    <div class="col-6">
                                        <h3>{{ e.name }}
                                            <a :href="e.location" class="m-2 h-auto" target="_blank" data-bs-toggle="tooltip" data-bs-placement="top" title="Tooltip on top">
                                                <i class="bi bi-geo-alt"></i>
                                            </a> 
                                        </h3>

        
                                        <h6>{{ e.address}}</h6>
                                        <h6>{{ e.date }}   </h6>
                                    </div>
                                    <div class="col-6">
                                        <h6>{{ e.price }}<i class="bi bi-currency-rupee"></i> Payed </h6>
                                        <!-- <h6>Rating: {{ b.rating }}</h6> -->
                                        <StarRating :rating="e.rating" :id="e.id" />
                                        <button type="button"   @click="openModal(e.id)" class=" btn btn-warning" style="height: min-content;">Give Rating</button>

                                    </div>
                                </div>
                                
                                        
                                        <Teleport to="#modal">
                                            <div class="modal-bg" v-if="IsModalOpen">

                                                <!-- <BookingRating :id="b.id" v-model="IsModalOpen"/> -->

                                                  <div class="container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                                    <h4>Please proved rating </h4>
                                                    <div class="form-floating col-md-12  mb-3">
                                                        <input type="number" class="form-control" v-model="rating"  id="floatingPassword"
                                                            placeholder=" "   />
                                                        <label for="floatingPassword">rating</label>
                                                    </div>
                                                    
                                                    <div class="container d-flex justify-content-center align-center">
                                                        <div class="row d-flex justify-content-evenly">
                                                            <div class="col text-center " >
                                                                <button type="button"  @click="update(currentBookingId,rating)"  class="btn btn-success " >
                                                                    conform!
                                                                </button>
                                                            </div>
                                                            <div class="col text-center ">
                                                                <button type="button" @click="IsModalOpen = false"  class="btn btn-danger">Cancel</button>
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
    </div>
</template>

<script setup>
import UserNavBar from './UserNavBar.vue';
import StarRating from './StarRating.vue';
import {config} from '../Constants.js';
import { ref, onMounted,reactive,onUpdated} from "vue";
import VueJwtDecode from 'vue-jwt-decode'
import { toast } from 'vue3-toastify';


const event = reactive({
    events: []
});
const rating = ref();
const currentBookingId = ref(null);
// const renderComponent = ref(true);

const ConvertTime = (time) => {
    let hour = time.slice(0,2);
    let min = time.slice(3,5);
    let ampm = 'AM';
    if (hour > 12) {
        hour -= 12;
        ampm = 'PM';
    }
    return `${hour}:${min} ${ampm}`;
}

const displaySelectedSeats = (seats) => {
    return seats.join(', ');
}

const openModal = (bookingId) => {
    currentBookingId.value = bookingId;
    IsModalOpen.value = true;
};

const IsModalOpen = ref(false);
const token = localStorage.getItem('token')
const user = VueJwtDecode.decode(token)


const fetchBookingData = async () => {
    const response = await fetch(`${config.url}/api/get_user_event_booking`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        },
        body: JSON.stringify({
        user_id: user.id
        })
    });
    const data = await response.json();
    event.events = data;
    // console.log(booking.bookings);
};
// Fetch venue data on initial mount
onMounted(fetchBookingData);


const update = async (id,rate) => {
    const response = await fetch(`${config.url}/api/update_event_rating`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        },
        body: JSON.stringify({
            event_id: id,
            rating: rate
        })
    });
    const data = await response.json();
    if (response.status === 200) {
        // toast.success('Rating updated successfully');
        toast.success('Rating updated  Successfully!',{autoClose: 1000});
        IsModalOpen.value = false;
        rating.value = 0;
        console.log("booking id :",id);
        console.log("rating :",rate);
        fetchBookingData();
        
    } else {
        toast.error('Rating update failed');
    }
}

onUpdated(() => {
    if (rating.value > 5) {
        toast.warning('Rating must be less then 5');
        rating.value = 5;
    }
    if (rating.value < 0) {
        toast.warning('Rating must be greater then 0');
        rating.value = 0;
    }
    if (rating.value%1 != 0 && rating.value != null) {
        toast.warning('Rating must be an integer');
        rating.value = rating.value - rating.value%1 ;
    }
})


</script>

<style scoped>
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
.modal-bg{
    background-color: rgba(0, 0, 0, 0.224);
}
</style>