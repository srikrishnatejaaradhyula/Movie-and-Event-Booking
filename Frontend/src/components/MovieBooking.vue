<template>
    <UserNavBar class=" sticky-top"/>
    <div class="container">
      <div class="row">
        <div class="col-md-8 col-12   boxs">
            <div v-for="r in rows" :key="r" class="col  d-flex flex-nowrap justify-content-evenly ">
                <div v-for="c in cols" :key="c" class="col mx-0 seat">
                    <input type="checkbox" :id="`${r}${c}`" v-model="seats" :value="`${getAlphabet(r)}${c}`" :disabled="!seats.includes(`${getAlphabet(r)}${c}`) && isMaxSeatsSelected || isBooked(`${getAlphabet(r)}${c}`)" />
                    <label :for="`${r}${c}`" :class="{ 'booked': isBooked(`${getAlphabet(r)}${c}`) }">{{`${getAlphabet(r)}${c}`}}</label>
                </div>
            </div>
            <div class="screen"></div>
        </div>
        <div class="col-md-4">
            <div class="booking-details">
                <h2>Booking Details</h2>
                <p>Selected Seats: {{displaySelectedSeats()}}</p>
                <p>Total Seats: {{totalSeats}}</p>
                <p>Amount: {{amount}}</p>
                <button @click="confirm()" class="primary-button">Book Now</button>
            </div>
        </div>
      </div>
      
      <Teleport to="#modal">
        <div class="modal-bg" v-if="IsModalOpen">
            <div class=" position-relative container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                <div class=" position-absolute top-0 end-0 "> 
                    <button @click="IsModalOpen = false" class="m-2 border-0 rounded-5 ">
                        <i class="bi bi-x-lg" style="color:brown"></i>
                    </button>
                </div>
                <h5 class="text-center">Conform the Tickets!</h5>
                <!-- <button class="close" @click="IsModalOpen = false">X</button> -->
                
                <div class="container d-flex justify-content-center align-center">
                    <div class="row d-flex justify-content-evenly" v-if="!isBooking">
                        <div class="col-12 mb-3 text-center">
                            {{displaySelectedSeats()}}
                        </div>
                        <div class="col-6 text-center " >
                            
                            <button type="button" @click="bookMovieTicket()"  class="btn btn-success " >
                                conform!
                            </button>
                            <!-- <span v-if="isBooking">
                                <SquareSpinner size="20" color="#ffffff" />
                            </span> -->
                        </div>
                        <div class="col-6 text-center ">
                            <button type="button" @click="IsModalOpen = false"  class="btn btn-danger">Cancel</button>
                        </div>
                    </div>
                    <div v-else>
                        <div class="spinner-grow text-success" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-success" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-success" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Teleport>
      
    </div>
</template>
  
<script setup>
import {config} from '../Constants.js';
import { ref, computed } from 'vue';
import UserNavBar from './UserNavBar.vue';
import VueJwtDecode from 'vue-jwt-decode'
import { toast } from 'vue3-toastify';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter();
const route = useRoute();

const token = localStorage.getItem('token');
const user = VueJwtDecode.decode(token);

const rows = ref();
const cols = ref();
const booked_seats = ref();
const seats = ref([]);
const seatPrice = ref(100);

const id = computed(() => route.params.id);
const date = computed(() => route.params.date);
const time = computed(() => route.params.time);

const totalSeats = computed(() => seats.value.length);
const amount = computed(() => totalSeats.value * seatPrice.value);

const IsModalOpen = ref(false);

const isBooking = ref(false);

const displaySelectedSeats = () => {
    return seats.value.join(', ');
}

const isBooked = (seat) => {
    return booked_seats.value.includes(seat);
}

const getAlphabet = (index) => {
const alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q','R','S','T','U','V','W','X','Y','Z'];
return alphabets[index - 1];
}

const isMaxSeatsSelected = computed(() => seats.value.length >= 6);

const confirm = ()=>{
    if(seats.value.length == 0){
        toast.warning('You not selected any seat');
    }
    else{
        IsModalOpen.value = true
    }
}

const fetchMovieBooking = async () => {
    const response = await fetch(`${config.url}/api/get_booking_by_movie`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
            movie_id: id.value,
            date: date.value,
            time: time.value
        })
    });
    const data = await response.json()
    rows.value = data.rows;
    cols.value = data.cols;
    booked_seats.value = data.booked_seats;
    seatPrice.value = data.price;  
    console.log(rows.value, cols.value, booked_seats.value, seatPrice.value)   
}


const bookMovieTicket = async () => {
    isBooking.value = true; 
    const response = await fetch(`${config.url}/api/create_booking`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
            movie_id: id.value,
            movie_date: date.value,
            movie_time: time.value,
            seats: totalSeats.value,
            seat_names: seats.value,
            total_price: amount.value,
            user_id: user.id
        })
    });
    const data = await response.json()
    console.log(data)
    if(response.status === 200){
        isBooking.value = false;
        IsModalOpen.value = false
        toast.success('Tickets booked Successfully!',{autoClose: 1000});
        setTimeout(() => {  router.push('/user_home'); }, 1000);
    }
    else{
        isBooking.value = false; 
        toast.error(data.message)
    }
}

onMounted(() => {
    fetchMovieBooking()
})



</script>
  
<style scoped>

.screen {
width: 100%;
height: 2%;
background-color: #333;
margin-top: 20px;
}

.boxs{
background: rgba(251, 251, 251, 0.279);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

input[type="checkbox"] {
display: none;
}

label {
/* width: 30px;
height: 30px; */
width: 2rem;
height:2rem;
margin: 2px;
border-radius: 25%;
background-color: #c0d7fae0;
text-align: center;
line-height: 30px;
cursor: pointer;
font-size: 90%;
}

/* @media (max-width: 768px) {
label {
    width: 20px;
    height: 20px;
    line-height: 20px;
    font-size: 2%;
}
}*/

@media (max-width: 480px) {
label {
    width: 20px;
    height: 20px;
    line-height: 15px;
    font-size: 50%;
}
} 

input[type="checkbox"]:checked + label {
background-color: rgb(0, 194, 29);
color: #ffffff;
}

label.booked {
background-color: red;
cursor: not-allowed;
}

.booking-details {
margin-top: 20px;
text-align: center;
}
</style>
  