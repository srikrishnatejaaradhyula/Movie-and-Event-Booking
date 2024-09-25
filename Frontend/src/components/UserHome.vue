<template>
    <div>
        <UserNavBar />
        <div class="d-flex justify-content-center my-2" >
            <input type="search" v-model="search" placeholder="Search" class="form-control" style="width: min-content;">
        </div>
        <div class="d-flex justify-content-center my-2" style="display: inline;" >
            <div class="px-2">
                <input type="date" v-model="search" class="form-control" style="width: min-content;">
            </div>
            <div >
                <button class="btn btn-primary" @click="search = ''"> Clear Date</button>
            </div>
        </div>
        <div class="container">
            <div class=" row "  >
                <div class="col-md-3 card p-0 mx-3 my-2 d-flex justify-content-sm-center" style="width: 18rem;" v-for="m in filterMovie" :key="m.id">
                    <GetPoster class="card-img-top"  :id="m.id" height=150  />
                    <div class="card-body col-md-12">
                        <div class="row d-flex justify-content-center">
                            <div class=" col-md-12 p-1 d-flex justify-content-evenly">
                                <div class="col-5 mt-2 ps-1">
                                    
                                    <h5> {{m.name}}<a :href="m.theatre_location" class="m-2 h-auto" target="_blank" data-bs-toggle="tooltip" data-bs-placement="top" title="Tooltip on top">
                                            <i class="bi bi-geo-alt"></i>
                                        </a>
                                    </h5>
                                </div>
                                <div class="col-7">
                                    <button @click="IsModal.ids[m.id] = true"  class=" border-0 m-2" style="background-color: transparent; font-size: large; font-weight: 700; color:rgb(122, 68, 172)">
                                        Details<i class="bi bi-box-arrow-up-right"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row col-md-12 d-flex justify-content-evenly">
                                <div class="col-md-5 p-0 ">
                                    <h6 style="color:rgb(105, 105, 105)"> {{m.language}} </h6>
                                    <p class=" border-1"  style="font-size: 10px;">
                                        {{m.type}}
                                    </p>
                                </div>
                                <div class="col-md-7">
                                    <button @click="IsModalBook.ids[m.id] = true"  class="btn btn-outline-info rounded-5 m-2" >
                                        Book Now
                                    </button>
                                </div>
                            </div>

                            
                        </div>
                    
                    </div>

                    <Teleport to="#modal">
                        <div class="modal-bg" v-if="IsModal.ids[m.id]">
                            <div class="position-relative container h-75 w-auto modal_box p-5 overflow-auto" style="background-color: antiquewhite; border-radius: 10px;">
                                <div class=" position-absolute top-0 end-0 "> 
                                    <button @click="IsModal.ids[m.id] = false" class="m-2 border-0 rounded-5 ">
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
                                                    <td>{{ m.name }}</td>
                                                </tr>
                                                <tr>
                                                    <th>Theatre Name</th>
                                                    <td>{{ m.theatre_name }}</td>
                                                </tr>
                                                <tr>
                                                    <th>Theatre Address</th>
                                                    <td>{{ m.theatre_address }}</td>
                                                </tr>
                                                <tr>
                                                    <th>Description</th>
                                                    <td>{{ m.description}}</td>
                                                </tr>
                                                <tr>
                                                    <th>Genre</th>
                                                    <td>{{ m.genre }}</td>
                                                </tr>
                                                <tr>
                                                    <th>Language</th>
                                                    <td>{{ m.language }}</td>
                                                </tr>
                                                <tr>
                                                    <th>Duration</th>
                                                    <td>{{ m.duration }}:00</td>
                                                </tr>
                                                <tr>
                                                    <th>Rating</th>
                                                    <td><StarRating :rating="m.rating"  /></td>
                                                </tr>
                                                <tr>
                                                    <th>Release Date</th>
                                                    <td>{{ m.release_date }}</td>
                                                </tr>
                                                <tr>
                                                    <th>End Date</th>
                                                    <td>{{ m.end_date }}</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                        
                                    </div>
                                    <div class="col-md-12">
                                        <button @click="IsModalMovieTrailer.ids[m.id] = true"  class="border-0 " style="background-color: transparent; font-size: large; font-weight: 700; color:rgb(137, 35, 35)">
                                            <i class="bi bi-youtube"> Watch Trailer </i> 
                                        </button>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </Teleport>

                    <Teleport to="#modal2">
                        <div class="modal-bg" v-if="IsModalBook.ids[m.id]">
                            <div class="position-relative container h-auto w-auto modal_box p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                <div class=" position-absolute top-0 end-0 "> 
                                    <button @click="IsModalBook.ids[m.id] = false" class="m-2 border-0 rounded-5 ">
                                        <i class="bi bi-x-lg" style="color:brown"></i>
                                    </button>
                                </div>
                                <h5>Select a date and time for your booking:</h5>
                                    
                                <div class="row d-flex">
                                    <div class="form-floating col-md-12 mb-2 d-flex flex-nowrap overflow-y-scroll">
                                        <div class="form-check d-flex form-check-inline" v-for=" date in availableDates(m.release_date,m.end_date)" :key="date">
                                            <input class="form-check-input btn-check"  type="radio" :id="date" :value="formatDate(date)" v-model="selectedDate">
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
                                        <div class="form-check form-check-inline" v-if="isCurrentTime(m.theatre_morning_show_time,selectedDate)">
                                            <input class="form-check-input btn-check"  type="radio" :id="m.theatre_morning_show_time" :value="m.theatre_morning_show_time" v-model="selectedTime">
                                            <label class="form-check-label btn btn-outline-success" :for="m.theatre_morning_show_time">{{ ConvertTime(m.theatre_morning_show_time) }}</label>
                                        </div>
                                        <div class="form-check form-check-inline" v-if="isCurrentTime(m.theatre_matinee_show_time,selectedDate)" >
                                            <input class="form-check-input btn-check"  type="radio" :id="m.theatre_matinee_show_time" :value="m.theatre_matinee_show_time" v-model="selectedTime">
                                            <label class="form-check-label btn btn-outline-success" :for="m.theatre_matinee_show_time">{{ ConvertTime(m.theatre_matinee_show_time) }}</label>
                                        </div>
                                        <div class="form-check form-check-inline"  v-if="isCurrentTime(m.theatre_first_show_time,selectedDate)">
                                            <input class="form-check-input btn-check"  type="radio" :id="m.theatre_first_show_time" :value="m.theatre_first_show_time" v-model="selectedTime">
                                            <label class="form-check-label btn btn-outline-success" :for="m.theatre_first_show_time">{{ ConvertTime(m.theatre_first_show_time) }}</label>
                                        </div>
                                        <div class="form-check form-check-inline"  v-if="isCurrentTime(m.theatre_second_show_time,selectedDate)">
                                            <input class="form-check-input btn-check"  type="radio" :id="m.theatre_second_show_time" :value="m.theatre_second_show_time" v-model="selectedTime">
                                            <label class="form-check-label btn btn-outline-success" :for="m.theatre_second_show_time">{{ ConvertTime(m.theatre_second_show_time) }}</label>
                                        </div>

                                    </div>
                                    <button @click="GoToBooking(m.id,availableDates(m.release_date,m.end_date).length)" class="primary-button w-auto">Book Show</button>
                                </div>
                            </div>

                        </div>
                    </Teleport>

                    <Teleport to="#ticket">
                        <div class="modal-bg z-3" v-if="IsModalMovieTrailer.ids[m.id]">
                            <div class=" position-relative container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                <div class=" position-absolute top-0 end-0 "> 
                                    <button @click="IsModalMovieTrailer.ids[m.id] = false " class="m-2 border-0 rounded-5 ">
                                        <i class="bi bi-x-lg" style="color:brown"></i>
                                    </button>
                                </div>
                                <iframe width="560" height="315" :src="m.movie_trailer" title="YouTube video player" 
                                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
                                </iframe>
                            </div>
                        </div>
                    </Teleport>



                </div>

                

            </div>
        </div>
    </div>
</template>

<script setup>
import {config} from '../Constants.js';
import UserNavBar from './UserNavBar.vue'
import StarRating from './StarRating.vue'
import { ref, onMounted, reactive,computed} from "vue";
import VueJwtDecode from 'vue-jwt-decode'
import { toast } from 'vue3-toastify';
import { useRouter } from 'vue-router';
import { f } from 'awesome-vue-star-rating';
import GetPoster from './GetPoster.vue';



const movie = reactive({
    movies: []
});
const IsModal = reactive({
    ids: []
});
const IsModalBook = reactive({
    ids: []
});
const IsModalMovieTrailer = reactive({
    ids: []
});
const search = ref("");

const selectedDate = ref("");
const selectedTime = ref("");



const router = useRouter()
const token = localStorage.getItem('token')
const user = VueJwtDecode.decode(token)

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


const currentDate = new Date();
selectedDate.value = formatDate(currentDate.toDateString());

const splitDate = (inputDate) =>{
  const parts = inputDate.split(' ');
  return parts;
}


const isCurrentTime = (time,customDate) =>{
    const currentTime = new Date();
    const givenTimeParts = time.split(":");
    const date = formatDate(currentTime.toDateString());
    console.log(date)
    console.log(customDate)
    if (givenTimeParts.length === 2) {
        const givenHours = parseInt(givenTimeParts[0]);
        const givenMinutes = parseInt(givenTimeParts[1]);

        currentTime.setSeconds(0); // Reset seconds and milliseconds to 0

        const givenDateTime = new Date();
        givenDateTime.setHours(givenHours);
        givenDateTime.setMinutes(givenMinutes);
        givenDateTime.setSeconds(0);

        console.log(date)
        console.log(customDate)

        if(givenDateTime > currentTime || date != customDate){
            return true;
        }
        // else{
        //     return false;
        // }
    }

    return false; //Invalid time format
}

const availableDates = (releaseDate, endingDate) => {
     const current = new Date();
    const dates = [];
    

    let releaseDates = new Date(releaseDate);
    endingDate = new Date(endingDate);
    if(endingDate >= current){
         dates.push(current.toDateString());

    }

    console.log(releaseDates)
    console.log(endingDate)

    while (releaseDates <= endingDate) {
        const currentDate = new Date();
        // console.log(currentDate.toDateString())
        // console.log(releaseDates >= currentDate)
        if (releaseDates >= currentDate) {
        
            dates.push(releaseDates.toDateString());
            console.log(releaseDates.toDateString())
        }
        releaseDates.setDate(releaseDates.getDate() + 1);
        // console.log(releaseDates)
    }
        return dates;
    

}




const GoToBooking = (id,dates) => {
    if (selectedDate.value == "" || selectedTime.value == "") {
        toast.error('Please select a date and time',{position:'top-right',autoClose: 1500});  
        return
    }
    if(dates == 0){
        toast.warning('Movie dates are not available')
        return
    }
    router.push(`/movie_booking/${id}/${selectedDate.value}/${selectedTime.value}`)
}

const fetchMovieData = async() =>{
    const response = await fetch(`${config.url}/api/get_movie_and_theatre`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        },
        body: JSON.stringify({
        // admin_id: user.id
        })
    });
    const data = await response.json();
    movie.movies = data;
    for(let i=0; i<movie.movies.length; i++){
        IsModal.ids[movie.movies[i].id] = false;
        IsModalBook.ids[movie.movies[i].id] = false;
        IsModalMovieTrailer.ids[movie.movies[i].id] = false;
    }
    console.log(movie.movies);
}

// Fetch venue data on initial mount
onMounted(fetchMovieData);



const filterMovie = computed(() => {
    return movie.movies.filter((m) =>{
        const nameMatch = m.name.toLowerCase().includes(search.value.toLowerCase());
        const tagMatch = m.genre.toLowerCase().includes(search.value.toLowerCase());
        const theatre_name = m.theatre_name.toLowerCase().includes(search.value.toLowerCase());
        const ratingMatch = m.rating.toString().includes(search.value.toString());
        const startDate = new Date(m.release_date);
        const endDate = new Date(m.end_date);
        const searchDate = new Date(search.value);

        if (!isNaN(searchDate.getTime())) {
            // If search value is a valid date, check if it falls within the movie's release date range
            for (let i = startDate; i <= endDate; i.setDate(i.getDate() + 1)) {
                if (i.getTime() === searchDate.getTime()) {
                    return true;
                }
            }
        }

        // If search value is not a valid date or does not fall within the movie's release date range, check other fields
        return nameMatch || tagMatch || ratingMatch || theatre_name;
    });
});




</script>

<style scoped>
 .form-floating select {
    border: none;
    border-radius: 0;
    border-bottom: 1px solid #a9b0b7;
    background-color: rgba(255, 255, 255, 0);
}
label{
    color: #101010;
    background-color: transparent;
}

input[type="search"] {
    border: none;
    border-radius: 0;
    border-bottom: 1px solid #a9b0b7;
    background-color: rgba(255, 255, 255, 0);
}
input[type="radio"] {
    border: none;
    border-radius: 0;
    border-bottom: 1px solid #a9b0b7;
    background-color: rgba(255, 255, 255, 0);
}
</style>