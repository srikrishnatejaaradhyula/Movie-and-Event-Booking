<template>
    <div  >
        <header>
            <nav class="navbar sticky-top navbar-expand-lg ">
                <div class="container-fluid px-4">
                    <a class="navbar-brand animate-charcter" href="#">Ticket Show</a>

                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                        data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse h-auto" id="navbarSupportedContent">
                        <ul class="navbar-nav  ms-auto ps-auto">
                            <li class="nav-item px-3">
                                <router-link to="/admin_home" class="nav-link">
                                    <i class="bi bi-house"></i> Movie
                                </router-link>
                            </li>
                            <li class="nav-item px-3">
                                <router-link to="/admin_event" class="nav-link">
                                    <i class="bi bi-calendar-event"></i> Events
                                </router-link>
                            </li>
                            <li class="nav-item px-3">
                                <router-link to="/admin_summery" class="nav-link">
                                    <i class="bi bi-bar-chart-line"></i> Summery
                                </router-link>
                            </li>
                            <li class="nav-item dropdown ">
                                <a class="nav-link dropdown-toggle h-auto align-middle" href="#" role="button"
                                    data-bs-toggle="dropdown" aria-expanded="false">

                                    <p class="text-end align-top ms-2 fw-bolder" style="display: inline">
                                        {{ username }}
                                    </p>
                                </a>
                                <ul class="dropdown-menu h-auto dropdown-menu-lg-end ">
                                    
                                    <li>
                                        <button class="dropdown-item btn btn-outline-light" @click="export_csv()"
                                            style="color: rgb(85, 160, 103) ;">
                                            <i class="bi bi-download"></i> export csv
                                        </button>
                                    </li>
                                    <li>
                                        <button class="dropdown-item btn btn-outline-light" @click="logout()"
                                            style="color: red ;">
                                            <i class="bi bi-box-arrow-left"></i> Logout
                                        </button>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
    </div>
</template>    

<script setup>
import {csvParser} from '../csv-parser.js'
import {config} from '../Constants.js';
import { useRouter } from 'vue-router'
import { ref, onMounted,reactive } from 'vue'
import VueJwtDecode from 'vue-jwt-decode'
import { toast } from 'vue3-toastify';


const username = ref('')

const movie = reactive({
    movies: []
});


const token = localStorage.getItem('isAdmin')
const user = VueJwtDecode.decode(token)

username.value = user.name
console.log(username.value)
const router = useRouter()
const logout = () => {
    localStorage.removeItem('isAdmin');

    router.push('/')
}

const export_csv = async() =>{
    console.log("export csv")   
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
    console.log(data)
    if (response.status != 200) {
        // throw new Error(data.message)
        toast.error(data.message);
    }
    csvParser().exportDataFromJSON(movie.movies, "report-csv", "csv");
}

</script>

<style scoped>

.animate-charcter {
    text-transform: uppercase;
    background-image: linear-gradient(-225deg,
            #231557 0%,
            #44107a 29%,
            #ff1361 67%,
            #fff800 100%);
    background-size: auto auto;
    background-clip: border-box;
    background-size: 50% auto;
    color: #fff;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textclip 2s linear infinite;
    display: inline-block;
    font-size: 25px;
    font-weight: 600;
}

@keyframes textclip {
    to {
        background-position: 200% center;
    }
}
</style>