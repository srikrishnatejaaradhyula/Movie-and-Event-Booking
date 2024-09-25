<template>
    <div>
    <AdminNavBar class=" sticky-top"/>
    <div class="container ">
         <div class="row align-items-center mx-0 my-3 d-flex justify-content-center">
             <div class="show h-auto col-md-6 col-12 shadow-lg  rounded-4">
                 <div class="sho mb-3 ">
                    <h4 class="col-md-12 text-center ">Update Movie</h4>
                     <form>
                     <div class="row">
                        <div class="col-md-6">
                            <div class="col-md-12 d-flex justify-content-center">
                                <div >
                                    <label class="custom-file-upload">
                                        <input type="file" @input="onFileSelected">
                                            <img :src="imageUrl" v-if="imageUrl" height="200" width="125">

                                            <i class="bi bi-camera" v-else style="font-size: 8rem; color: #ced4da;"></i>
                                    </label>
                                </div>
                            </div>
                            <div class="form-floating col-md-12  mb-2">
                                <input type="text" class="form-control" v-model="name" id="floatingInput" placeholder=" "
                                    required />
                                <label for="floatingInput">Movie Name</label>
                            </div>
                            <div class="form-floating col-md-12  mb-2">
                                <textarea type="text" class="form-control" v-model="description" id="floatingInput" placeholder=" "
                                    required></textarea>
                                <label for="floatingInput">Movie description</label>
                            </div>
                            <div class="form-floating col-md-12  mb-1">
                                <input type="text" class="form-control" v-model="movie_trailer" id="floatingInput" placeholder=" "
                                    required />
                                <label for="floatingInput">Movie Trailer Link</label>
                            </div>
                            <div class="form-floating col-md-12  mb-3">
                                <input type="time" class="form-control" v-model="duration" id="floatingPassword"  min="00:01" max="06:00"
                                    placeholder=" " required />
                                <label for="floatingPassword">duration</label>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="row col-md-12  mb-3">
                                <div class="form-floating col-6">
                                    <input type="date" class="form-control" v-model="release_date" id="floatingInput" placeholder=" "
                                    required />
                                    <label for="floatingInput">Release Date</label>
                                </div>
                                <div class="form-floating  col-6">
                                <input type="date" class="form-control" v-model="end_date" id="floatingInput" placeholder=" "
                                    required />
                                <label for="floatingInput">End Date</label>
                                </div>
                                
                            </div>
                            <div class="form-floating col-md-12  mb-3">
                                <input type="text" class="form-control" v-model="genre" id="floatingPassword"
                                    placeholder=" " required />
                                <label for="floatingPassword">Genre</label>
                            </div>
                            <div class="form-floating col-md-12  mb-3">
                                <input type="text" class="form-control" v-model="cast" id="floatingPassword"
                                    placeholder=" " required />
                                <label for="floatingPassword">Cast</label>
                            </div>
                            <div class="form-floating col-md-12 mb-2 d-flex ">
                                <select class="form-select" aria-label="Default select example" v-model="type">
                                    <option value="2D">2D</option>
                                    <option value="3D">3D</option>
                                </select>
                                <label for="floatingInput">Select Movie Type</label>
                            </div>
                            <div class="form-floating col-md-12 mb-2 d-flex ">
                                <select class="form-select" aria-label="Default select example" v-model="language">
                                    <option value="Telugu">Telugu</option>
                                    <option value="Hindi">Hindi</option>
                                    <option value="Tamil">Tamil</option>
                                    <option value="Kannada">Kannada</option>
                                    <option value="Malayalam">Malayalam</option>
                                    <option value="English">English</option>
                                </select>
                                <label for="floatingInput">Select Movie Language</label>
                            </div>
                            <div class="form-floating col-md-12  mb-3">
                                <input type="number" class="form-control" v-model="price" id="floatingPassword"
                                    placeholder=" " required />
                                <label for="floatingPassword">Price</label>
                            </div>
                            
                            <div class="form-floating col-md-12   mb-3 ">
                                <input type="number" min="0" max="5"  class="form-control" v-model="rating" id="floatingInput" placeholder=" "
                                    required />
                                <label for="floatingInput">Rating</label>
                            </div>
                        </div>
                     </div>
                
                         <div class="col-md-12 text-center pt-1">
                             <button type="submit" @click.prevent="handleSubmit" id="butt" class="primary-button">Update</button>
                         </div>
                     </form>
                 </div>
             </div>
         </div>
     </div>
    </div>
</template>

<script setup>
import {config} from '../Constants.js';
import AdminNavBar from '@/components/AdminNavBar.vue'
import { ref,reactive,onMounted,onUpdated} from 'vue'
import { useRouter,useRoute } from 'vue-router'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import VueJwtDecode from 'vue-jwt-decode';


const router = useRouter()
const route = useRoute()

const movie1 = reactive({
    movies: []
});
const movie = reactive({
    movies: []
});
const imageUrl = ref(null);
const file = ref(null);
const name = ref('')
const description = ref('')
const duration = ref('')
const language = ref('')
const movie_trailer = ref('')
const genre = ref('')
const price = ref()
const rating = ref()
const release_date = ref('')
const end_date = ref('')
const type = ref('')
const cast = ref('')

// console.log(starting_time.value)
console.log(release_date.value)
// console.log(ending_time.value)
console.log(rating.value)

const id = computed(() => route.params.id);
console.log(id.value)

const token = localStorage.getItem('isAdmin')
const user = VueJwtDecode.decode(token)

const onFileSelected = (e) => {

    file.value = e.target.files[0];
    const reader = new FileReader();
    // reader.readAsDataURL(file.value)
    reader.onload = e => {
        imageUrl.value = e.target.result;
    };
    reader.readAsDataURL(file.value);
}

const handleSubmit = async() => {
    console.log(rating.value)
    if (name.value == '' || genre.value == '' || price.value == '' || rating.value == ''|| release_date.value == ''|| end_date.value == '' || cast.value == ''|| movie_trailer.value == ''|| type.value == ''|| file.value == null || description.value == '' || duration.value == '' || language.value == '' ) {
        toast.warning('Please fill all the fields');
    }
    else {
        var youtubeRegExp = /(?:https?:\/\/)?(?:www\.)?(?:m\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=|embed\/|v\/|u\/\w\/|shorts\/)?([\w-]{11})/;

        // Test if the provided link matches the regular expression
        var match = movie_trailer.value.match(youtubeRegExp);

        if (match) {
            var videoId = match[1];
            var embedLink = "https://www.youtube.com/embed/" + videoId;
            movie_trailer.value = embedLink;
        } else {
            toast.warning('Invalid YouTube link');
            return
        }
        
        const reader = new FileReader()
        reader.readAsDataURL(file.value)
        reader.onload = async () => {
            const base64 = reader.result.split(',')[1]
            console.log("this is base64",base64)
            try {
                const response = await fetch(`${config.url}/api/update_movie`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'x-access-tokens': token  
                    },
                    body: JSON.stringify({
                        movie_id: id.value,
                        name: name.value,
                        description: description.value,
                        duration: duration.value,
                        language: language.value,
                        release_date: release_date.value,
                        end_date: end_date.value,
                        genre: genre.value,
                        movie_trailer: movie_trailer.value,
                        price: price.value,
                        rating: rating.value,
                        cast: cast.value,
                        type: type.value,
                        image: base64
                    })
                })
                console.log(response);
                if (!response.ok) {
                    console.log(response);
                    throw new Error(`${alert(data.error)}`);
                }
                else {
                    toast.success('Movie Updated Successfully!',{autoClose: 1000});
                    setTimeout(() => {  router.push('/admin_home'); }, 1000);
                }
            }
            catch (error) {
                console.log(error)
                // alert("E-mail is already used!")
            }
        }
    }
}

const fetchMovie = async () => {
    const response = await fetch(`${config.url}/api/get_movie_all`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        },
        body: JSON.stringify({
            admin_id: user.id
        })
    });
    const data = await response.json();
    name.value = data[0].name;
    description.value = data[0].description;
    duration.value = data[0].duration;
    language.value = data[0].language;
    release_date.value = data[0].release_date;
    end_date.value = data[0].end_date;
    genre.value = data[0].genre;
    movie_trailer.value = data[0].movie_trailer;
    price.value = data[0].price;
    rating.value = data[0].rating;
    cast.value = data[0].cast;
    type.value = data[0].type;
};

const fetchMovieById = async () => {
    const response = await fetch(`${config.url}/api/get_movie_by_id`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        },
        body: JSON.stringify({
            movie_id: id.value
        })
    });
    const data = await response.json();
    movie.movies = data;
};

const fetchMoviePoster = async () => {
    const response = await fetch(`${config.url}/api/get_poster_img`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        },
        body: JSON.stringify({
            id: id.value
        })
    });
    const blob = await response.blob()
    const objectUrl = URL.createObjectURL(blob)
    imageUrl.value = objectUrl
};

onMounted(() => {
    fetchMovie();
    fetchMovieById();
    fetchMoviePoster();
});

const date = new Date();
var time = date.getHours() + ":" + date.getMinutes()

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
    if (price.value < 0) {
        toast.warning('Price must be greater then 0');
        price.value = 0;
    }
    if (release_date.value < date.toISOString().slice(0,10) && release_date.value != '') {
        toast.warning('Show date must be greater then current date');
        release_date.value = '';
    }
    if (end_date.value < release_date.value && end_date.value != '') {
        toast.warning('End date must be greater then release date');
        end_date.value = '';
    }
    for (let i = 0; i < movie1.movies.length; i++) {
        if (name.value == movie1.movies[i].name) {
            toast.warning('movie name already exists');
            name.value = '';
        }
    }
    for (let i = 0; i < movie.movies.length; i++) {
        if (release_date.value <= movie.movies[i].end_date) {
            toast.warning('movie already exists on this date');
            release_date.value = '';
        }
    }
    for (let i = 0; i < movie.movies.length; i++) {
        if (end_date.value <= movie.movies[i].end_date) {
            toast.warning('movie already exists on this date');
            end_date.value = '';
        }
    }

})


</script>





<style scoped>

.container {
    height: 100%;
    width: 100%;
}

input[type="file"] {
    display: none;
}

.show{
    height: 100vh;
    width: 75%;
    background: rgba(230, 253, 253, 0.279);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border: 1px solid rgba(255, 255, 255, 0.08);

}


.sho{
    padding-top: 7vh;
}

.form-floating input[type="text"],
.form-floating input[type="number"],
.form-floating input[type="date"],
.form-floating select,

.form-floating textarea {
    border: none;
    border-radius: 0;
    border-bottom: 1px solid #a9b0b7;
    background-color: rgba(255, 255, 255, 0);
}


.rate {
    float: left;
    height: 46px;
    padding: 0 10px;
}
.rate:not(:checked) > input {
    position:absolute;
    top:-9999px;
}
.rate:not(:checked) > label {
    float:right;
    width:1em;
    overflow:hidden;
    white-space:nowrap;
    cursor:pointer;
    font-size:30px;
    color:#ccc;
}
.rate:not(:checked) > label:before {
    content: '★ ';
}
.rate > input:checked ~ label {
    color: #ffc700;    
}
.rate:not(:checked) > label:hover,
.rate:not(:checked) > label:hover ~ label {
    color: #deb217;  
}
.rate > input:checked + label:hover,
.rate > input:checked + label:hover ~ label,
.rate > input:checked ~ label:hover,
.rate > input:checked ~ label:hover ~ label,
.rate > label:hover ~ input:checked ~ label {
    color: #c59b08;
}

</style>