<template>
    <AdminNavBar/>
    <div class="overflow-x-hidden">
        
        <div class="container" >
                <div  class="col-md-12" v-for="v in venue.venues" :id="v.revenue "> 
                    <SummeryLineChart 
                        :title="'Revenue'" 
                        :data="v.revenue"
                        :labels="v.venue_name"
                    />
                </div>
            <div class="row movies my-2"  v-for="s in show.shows" :id="s.id">
                
                <div class="col-md-12">
                    <h4 class="col-md-12 text-center ">{{ s.name }}</h4>
                </div>
                <div class="col-md-6">
                    <SummeryBarChart 
                        :title="'ratings'" 
                        :data="[s.user_rating, s.admin_rating,0]"
                        :labels="['User Rating', 'Admin Rating']"
                        :color="['#FFC107', '#3F51B5']"
                    />
                </div>
                <div class="row col-md-6">
                    <div class="col-md-6">
                        <div class="form-floating col-md-12 mb-2 d-flex ">
                            <select class="form-select" aria-label="Default select example" v-model="s.selectedDate" >
                                <option v-for="d in s.date" :key="d" :value="d">{{ d }}</option>
                            </select>
                            <label for="floatingInput">Date</label>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="form-floating col-md-12 mb-2 d-flex ">
                            <select class="form-select" aria-label="Default select example" v-model="s.selectedTime" >
                                <option v-for="t in s.times[s.selectedDate]" :key="t" :value="t">{{ ConvertTime(t) }}</option>
                            </select>
                            <label for="floatingInput">Time</label>
                        </div>
                    </div>
                    <div v-if="s.selectedDate != '' && s.selectedTime != '' ">
                        <SummeryBarChart 
                        :title="'booking'" 
                        :data="[s.booking_count,s.Unoccupied_seats[s.selectedDate][s.selectedTime],0]"
                        :labels="['Booked Seats', 'Unoccupied Seats']"
                        :color="['#99ff99', '#ff6666']"
                        style="height: 95%;"
                    />
                    </div>
                    <div v-else>
                        <h3 class=" text-center text-danger">Please Select Date & time</h3>
                    </div>
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import AdminNavBar from './AdminNavBar.vue';
import SummeryBarChart from './SummeryBarChart.vue';
import SummeryLineChart from './SummeryLineChart.vue';
import {config} from '../Constants.js';
import { ref,reactive,onMounted,computed,onUpdated } from 'vue'
import { useRouter,useRoute } from 'vue-router'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
// import VueJwtDecode from 'vue-jwt-decode';


const router = useRouter()
const show = reactive({
    shows: []
});
const venue = reactive({
    venues: []
});

const selectedDate = ref('');
const selectedTime = ref('');

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

const token = localStorage.getItem('isAdmin')
// const user = VueJwtDecode.decode(token)
console.log(token)

const fetchShow = async () => {
    const response = await fetch(`${config.url}/api/get_movie_for_summery`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        }
    });
    const data = await response.json();
    show.shows = data;
    console.log(show.shows)
    
}

const fetchVenue = async () => {
    const response = await fetch(`${config.url}/api/get_theatre_for_summery`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        }
    });
    const data = await response.json();
    venue.venues = data;
    console.log(venue.venues.reverse)
    venue.venues.forEach((v) => {
        console.log(v.revenue)
    });
}


onMounted(() => {
    fetchShow();
    fetchVenue();
});


</script>

<style scoped>
.movies{
    background: rgba(224, 252, 254, 0.226);
    /* backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px); */
    border-radius: 10px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

</style>