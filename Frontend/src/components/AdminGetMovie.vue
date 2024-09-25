<template>
    <div  class="show card w-100 my-4 " v-for="s in movie.movies" :key="s.id" >
       

        <div class="card-body w-auto" >
            <div class="row">
                <div class="col-md-5">
                    <GetPoster :id="s.id" height="175" width="125" />
                </div>
                <div class="col-md-6">
                    <div class="col-md-12 mb-2">
                        <h3 class=" ms-1 " >{{ s.name }}</h3>
                    </div>
                    <div class="col-md-12 mb-2">
                        <button @click="IsModalMovie.ids[s.id] = true"  class="border-0 " style="background-color: transparent; font-size: large; font-weight: 700; color:rgb(79, 44, 112)">
                           Movie Details <i class="bi bi-box-arrow-up-right"></i>
                        </button>
                    </div>
                    <div class="col-md-12 mb-2">
                        <button @click="defaultDateTime(s.release_date,s.theatre_morning_show_time,s.id)"  class="border-0 " style="background-color: transparent; font-size: large; font-weight: 700; color:rgb(35, 60, 82)">
                           Seats Details <i class="bi bi-box-arrow-up-right"></i>
                        </button>
                    </div>
                    <div class="col-md-12">
                        <button @click="IsModalMovieTrailer.ids[s.id] = true"  class="border-0 " style="background-color: transparent; font-size: large; font-weight: 700; color:rgb(137, 35, 35)">
                           <i class="bi bi-youtube"> Watch Trailer </i> 
                        </button>
                    </div>
                </div>
            
            </div>
                <!-- <StarRating :rating="s.rating"  /> -->
        </div>

        <!-- Model for Theatre details  -->
        <Teleport to="#modal">
            <div class="modal-bg z-2" v-if="IsModalMovie.ids[s.id]">
                <div class="position-relative container h-auto w-auto modal_box p-5" style="background-color: antiquewhite; border-radius: 10px;">
                    <div class=" position-absolute top-0 end-0 "> 
                        <button @click="IsModalMovie.ids[s.id] = false" class="m-2 border-0 rounded-5 ">
                            <i class="bi bi-x-lg" style="color:brown"></i>
                        </button>
                    </div>
                        
                    <h4> Movie details </h4>
                    <div class="row">
                        <div class="col-md-10">
                            <table class="table table-striped-columns " >
                                <tbody >
                                    <tr>
                                        <th>Name</th>
                                        <td>{{ s.name }}</td>
                                    </tr>
                                    <tr>
                                        <th>Description</th>
                                        <td>{{ s.description}}</td>
                                    </tr>
                                    <tr>
                                        <th>Genre</th>
                                        <td>{{ s.genre }}</td>
                                    </tr>
                                    <tr>
                                        <th>Language</th>
                                        <td>{{ s.language }}</td>
                                    </tr>
                                    <tr>
                                        <th>Duration</th>
                                        <td>{{ s.duration }}:00</td>
                                    </tr>
                                    <tr>
                                        <th>Rating</th>
                                        <td><StarRating :rating="s.rating"  /></td>
                                    </tr>
                                    <tr>
                                        <th>Release Date</th>
                                        <td>{{ s.release_date }}</td>
                                    </tr>
                                    <tr>
                                        <th>End Date</th>
                                        <td>{{ s.end_date }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="col-md-2 ">
                            <div class="col-md-12 m-2">
                                <button @click="$router.push('/update_movie/'+ s.id)" class=" rounded-2 border-0" style="color:aliceblue; background-color: rgb(88, 88, 255); font-size: xx-large;">
                                    <i class="bi bi-pencil-square"></i>
                                </button>
                            </div>
                            <div class="col-md-12 m-2">
                                <button @click="IsModalMovieDelete.ids[s.id] = true" class=" rounded-2 border-0" style="color:aliceblue; background-color: rgb(255, 87, 87); font-size: xx-large;">
                                    <i class="bi bi-trash-fill"></i>
                                </button>
                            </div>
                        </div>
                        
                    </div>
                </div>

            </div>
        </Teleport>

        <Teleport to="#modal1">
            <div class="modal-bg z-3" v-if="IsModalMovieDelete.ids[s.id]">
                <div class=" position-relative container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                    <div class=" position-absolute top-0 end-0 "> 
                        <button @click="IsModalMovieDelete.ids[s.id] = false" class="m-2 border-0 rounded-5 ">
                            <i class="bi bi-x-lg" style="color:brown"></i>
                        </button>
                    </div>
                    <h5 class="text-center">Are you sure you want to Delete Movie?</h5>
                    
                    <div class="container d-flex justify-content-center align-center">
                        <div class="row d-flex justify-content-evenly" >
                            <div class="col text-center " >
                                <button type="button" @click="DeleteMovie(s.id)"  class="btn btn-success " >
                                    conform!
                                </button>
                            </div>
                            <div class="col text-center ">
                                <button type="button" @click="IsModalMovieDelete.ids[s.id] = false"  class="btn btn-danger">Cancel</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </Teleport>

        <Teleport to="#modal2">
            <div class="modal-bg z-3" v-if="IsModalMovieTrailer.ids[s.id]">
                <div class=" position-relative container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                    <div class=" position-absolute top-0 end-0 "> 
                        <button @click="IsModalMovieTrailer.ids[s.id] = false " class="m-2 border-0 rounded-5 ">
                            <i class="bi bi-x-lg" style="color:brown"></i>
                        </button>
                    </div>
                    <iframe width="560" height="315" :src="s.movie_trailer" title="YouTube video player" 
                        frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
                    </iframe>
                </div>
            </div>
        </Teleport>

        <Teleport to="#ticket">
            <div class="modal-bg" v-if="IsModalMovieTicket.ids[s.id]">
                <div class="position-relative container h-75 w-auto modal_box p-5 z-3 overflow-auto" style="background-color: antiquewhite; border-radius: 10px;">
                    <div class=" position-absolute top-0 end-0 "> 
                        <button @click="IsModalMovieTicket.ids[s.id] = false" class="m-2 border-0 rounded-5 ">
                            <i class="bi bi-x-lg" style="color:brown"></i>
                        </button>
                    </div>
                    <!-- <h5>Select a date and time for your booking:</h5> -->
                        
                    <div class="row d-flex">
                        <div class="form-floating col-md-12 mb-2 d-flex flex-nowrap overflow-y-scroll">
                            <div class="form-check d-flex form-check-inline" v-for=" date in availableDates(s.release_date,s.end_date)" :key="date">
                                <input class="form-check-input btn-check"  type="radio" :id="date" :value="formatDate(date)" v-model="selectedDate" v-on:change="defaultDateTime(selectedDate,selectedTime,s.id)">
                                <label class="form-check-label btn btn-outline-info d-flex" :for="date" style="font-weight: 600;">
                                    <div class="month p-0 " style="transform: rotate(270deg); font-size: small;">
                                        {{ splitDate(date)[1] }}
                                    </div>
                                    <div class=" p-0 ">
                                        {{ splitDate(date)[0] }} <br> {{ splitDate(date)[2]  }}
                                    </div>
                                </label>
                            </div>
                        </div>
                        <div class="form-floating col-md-12 mb-2 d-flex">
                            <div class="form-check form-check-inline" >
                                <input class="form-check-input btn-check"  type="radio" :id="s.theatre_morning_show_time" :value="s.theatre_morning_show_time" v-model="selectedTime" v-on:change="defaultDateTime(selectedDate,selectedTime,s.id)">
                                <label class="form-check-label btn btn-outline-success" :for="s.theatre_morning_show_time">{{ ConvertTime(s.theatre_morning_show_time) }}</label>
                            </div>
                            <div class="form-check form-check-inline" >
                                <input class="form-check-input btn-check"  type="radio" :id="s.theatre_matinee_show_time" :value="s.theatre_matinee_show_time" v-model="selectedTime" v-on:change="defaultDateTime(selectedDate,selectedTime,s.id)">
                                <label class="form-check-label btn btn-outline-success" :for="s.theatre_matinee_show_time">{{ ConvertTime(s.theatre_matinee_show_time) }}</label>
                            </div>
                            <div class="form-check form-check-inline" >
                                <input class="form-check-input btn-check"  type="radio" :id="s.theatre_first_show_time" :value="s.theatre_first_show_time" v-model="selectedTime" v-on:change="defaultDateTime(selectedDate,selectedTime,s.id)">
                                <label class="form-check-label btn btn-outline-success" :for="s.theatre_first_show_time">{{ ConvertTime(s.theatre_first_show_time) }}</label>
                            </div>
                            <div class="form-check form-check-inline" >
                                <input class="form-check-input btn-check"  type="radio" :id="s.theatre_second_show_time" :value="s.theatre_second_show_time" v-model="selectedTime" v-on:change="defaultDateTime(selectedDate,selectedTime,s.id)">
                                <label class="form-check-label btn btn-outline-success" :for="s.theatre_second_show_time">{{ ConvertTime(s.theatre_second_show_time) }}</label>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-8 col-12 overflow-visible  boxs">
                        <div v-for="r in s.theatre_rows" :key="r" class="col  d-flex flex-nowrap justify-content-evenly ">
                            <div v-for="c in s.theatre_cols" :key="c" class="col mx-0 seat">
                                <input class="checkbox" type="checkbox" :id="`${r}${c}`" v-model="seats" :value="`${getAlphabet(r)}${c}`" disabled />
                                <label class="checkboxlabel" :for="`${r}${c}`" :class="{ 'booked': isBooked(`${getAlphabet(r)}${c}`) }">{{`${getAlphabet(r)}${c}`}}</label>
                            </div>
                        </div>
                        <div class="screen"></div>
                    </div>

                </div>
            </div>
        </Teleport>

        

    </div>
</template>

<script setup>
import {config} from '../Constants.js';
import StarRating from './StarRating.vue';
import { ref, onMounted, reactive,defineProps } from "vue";
import VueJwtDecode from 'vue-jwt-decode'
import { toast } from 'vue3-toastify';
import GetPoster from './GetPoster.vue';


const props = defineProps({
    id: Number,
})

const selectedDate = ref("");
const selectedTime = ref("");

const seats = ref();
const booked_seats = ref();

const movie = reactive({
    movies: []
});

const IsModalMovie = reactive({
    ids: []
});
const IsModalMovieDelete = reactive({
    ids: []
});
const IsModalMovieTrailer = reactive({
    ids: []
});

const IsModalMovieTicket = reactive({
    ids: []
});

const isBooked = (seat) => {
    return booked_seats.value.includes(seat);
}

const getAlphabet = (index) => {
    const alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q','R','S','T','U','V','W','X','Y','Z'];
    return alphabets[index - 1];
}

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


const  formatDate = (inputDate) => {
    const months = {
        Jan: '01',
        Feb: '02',
        Mar: '03',
        Apr: '04',
        May: '05',
        Jun: '06',
        Jul: '07',
        Aug: '08',
        Sep: '09',
        Oct: '10',
        Nov: '11',
        Dec: '12',
    }


    const parts = inputDate.split(' ');
    if (parts.length === 4) {
        const year = parts[3];
        const month = months[parts[1]];
        const day = parts[2];
        return `${year}-${month}-${day}`;
    } else {
        return 'Invalid date format';
    }
}

const splitDate = (inputDate) =>{
  const parts = inputDate.split(' ');
  return parts;
}



const availableDates = (releaseDate, endingDate) => {
    const dates = [];
    let releaseDates = new Date(releaseDate);
    endingDate = new Date(endingDate);

    while (releaseDates <= endingDate) {
        const currentDate = new Date();
        // if (releaseDates.toDateString() >= currentDate.toDateString()) {
            dates.push(releaseDates.toDateString());
            // console.log(releaseDates.toDateString())
        // }
        releaseDates.setDate(releaseDates.getDate() + 1);
        // console.log(releaseDates)
    }

    return dates;
}


const defaultDateTime = (date,time,id) => {
    selectedDate.value = date;
    selectedTime.value = time;
    fetchMovieBooking(id,date,time);
    IsModalMovieTicket.ids[id] = true 
    console.log(date)
}


const fetchMovieBooking = async (id,date,time) => {
    const response = await fetch(`${config.url}/api/get_booking_by_movie`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
            movie_id: id,
            date: date,
            time: time
        })
    });
    const data = await response.json()
    booked_seats.value = data.booked_seats;
    console.log(booked_seats.value)   
}



const token = localStorage.getItem('isAdmin')
const user = VueJwtDecode.decode(token)

const fetchMovie = async () => {
    const response = await fetch(`${config.url}/api/get_movie`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
            theatre_id: props.id
        })
    });
    const data = await response.json()
    movie.movies = data
    for(let i=0; i<movie.movies.length; i++){
        IsModalMovie.ids[movie.movies[i].id] = false
        IsModalMovieDelete.ids[movie.movies[i].id] = false
        IsModalMovieTrailer.ids[movie.movies[i].id] = false
        IsModalMovieTicket.ids[movie.movies[i].id] = false
    }
    console.log(movie.movies)
    console.log(IsModalMovieTicket.ids)
    console.log(IsModalMovie)
}


onMounted(() => {
    fetchMovie()
});

const DeleteMovie = async (id) => {
    const response = await fetch(`${config.url}/api/delete_movie`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
            movie_id: id
        })
    });
    const data = await response.json()
    console.log(data)
    if (response.status === 200) {
        toast.success('Movie Deleted Successfully');
        // Fetch fresh data after successful deletion
        fetchMovie();
    }
    else if (response.status === 400) {
        toast.error(data.error); 
    }else {
        alert("Something went wrong");
    }
}




</script>

<style scoped>

.show {
    background-color: rgba(213, 253, 250, 0.5);
    border-radius: 10px;
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    box-shadow: 0px 0px 10px 0px rgba(59, 87, 81, 0.893);
    width: 100%;
}

.boxs{
background: rgba(213, 247, 237, 0.279);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

.checkbox{
display: none;
}

.checkboxlabel{
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
    .checkboxlabel {
    width: 20px;
    height: 20px;
    line-height: 15px;
    font-size: 50%;
}
} 

.checkbox:checked + .checkboxlabel {
background-color: rgb(0, 194, 29);
color: #ffffff;
}

label.booked {
background-color: red;
cursor: not-allowed;
}
</style>
