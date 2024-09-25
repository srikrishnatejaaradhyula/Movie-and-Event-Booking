<template>
    <div>
    <AdminNavBar class="sticky-top"/>
    <div class="container">
        <div class="row align-items-center mx-0 my-5 d-flex justify-content-center">
            <div class="venue col-md-6 col-12 ">
                <div class="ven">
                <h4 class="col-md-12 text-center ">Create Theatre</h4>
                    <form>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-floating col-md-12  mb-3">
                                    <input type="text" class="form-control" v-model="name" id="floatingInput" placeholder=" "
                                        required />
                                    <label for="floatingInput">Theatre Name</label>
                                </div>
                                <div class="form-floating col-md-12  mb-3">
                                    <input type="text" class="form-control" v-model="address" id="floatingInput" placeholder=" "
                                        required />
                                    <label for="floatingInput">Address</label>
                                </div>
                                <div class="form-floating col-md-12  mb-3">
                                    <input type="text" class="form-control" v-model="location" id="floatingPassword"
                                        placeholder=" " required />
                                    <label for="floatingPassword">Loccation</label>
                                </div>
                                <div class="row col-md-12  mb-3">
                                    <div class="form-floating col-6">
                                        <input type="number" class="form-control" v-model="rows" id="floatingInput" placeholder=" "
                                            required />
                                        <label for="floatingInput">Number Of Rows</label>
                                    </div>
                                    <div class="form-floating  col-6">
                                        <input type="number" class="form-control" v-model="cols" id="floatingInput" placeholder=" "
                                            required />
                                        <label for="floatingInput">Number Of Cols</label>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">

                                <div class="form-floating col-md-12  mb-3">
                                    <input type="time" class="form-control" v-model="morning_show_time" id="floatingPassword"
                                        placeholder=" " required />
                                    <label for="floatingPassword">Morning Show Time</label>
                                </div>
                                <div class="form-floating col-md-12  mb-3">
                                    <input type="time" class="form-control" v-model="matinee_show_time" id="floatingPassword"
                                        placeholder=" " required />
                                    <label for="floatingPassword">Matinee Show Time</label>
                                </div>
                                <div class="form-floating col-md-12  mb-3">
                                    <input type="time" class="form-control" v-model="first_show_time" id="floatingPassword"
                                        placeholder=" " required />
                                    <label for="floatingPassword">First Show Time</label>
                                </div>
                                <div class="form-floating col-md-12  mb-3">
                                    <input type="time" class="form-control" v-model="second_show_time" id="floatingPassword"
                                        placeholder=" " required />
                                    <label for="floatingPassword">Second Show Time</label>
                                </div>
                            </div>
                        </div>
                            
                        <div class="col-md-12 text-center pt-1">
                            <button type="submit" @click.prevent="handleSubmit" id="butt" class="primary-button">Create</button>
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
import { useRouter } from 'vue-router'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import VueJwtDecode from 'vue-jwt-decode';


const router = useRouter()
const theatre = reactive({
    theatres: []
});
const name = ref('')
const address = ref('')
const location = ref('')
const rows = ref()
const cols = ref()
// const morning_show_starting_time = ref('')
// const morning_show_ending_time = ref('')
// const matinee_show_starting_time = ref('')
// const matinee_show_ending_time = ref('')
// const first_show_starting_time = ref('')
// const first_show_ending_time = ref('')
// const second_show_starting_time = ref('')
// const second_show_ending_time = ref('')

const morning_show_time = ref('')
const matinee_show_time = ref('')
const first_show_time = ref('')
const second_show_time = ref('')

// morning_show_time.value = morning_show_starting_time.value + ' - ' + morning_show_ending_time.value
// matinee_show_time.value = matinee_show_starting_time.value + ' - ' + matinee_show_ending_time.value
// first_show_time.value = first_show_starting_time.value + ' - ' + first_show_ending_time.value
// second_show_time.value = second_show_starting_time.value + ' - ' + second_show_ending_time.value

const token = localStorage.getItem('isAdmin');
const user = VueJwtDecode.decode(token);

console.log(user)

const handleSubmit = async() => {
    if (name.value == '' || address.value == '' || location.value == '' || rows.value == '' || cols.value == '' || morning_show_time.value == '' || matinee_show_time.value == ''  || first_show_time.value == '' || second_show_time.value == '' ) {
        toast.warning('Please fill all the fields!');
        return;
    }
    else{
        console.log(morning_show_time.value)
        console.log(matinee_show_time.value)
        console.log(first_show_time.value)
        console.log(second_show_time.value)
        try {
            const response = await fetch(`${config.url}/api/create_theatre`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-access-tokens': token           
            },
            body: JSON.stringify({
                name: name.value,
                address: address.value,
                location: location.value,
                rows: rows.value,
                cols: cols.value,
                morning_show_time: morning_show_time.value,
                matinee_show_time: matinee_show_time.value,
                first_show_time: first_show_time.value,
                second_show_time: second_show_time.value,
                admin_id: user.id
            })
        })
        console.log(response);
        if (!response.ok) {
            toast.error(data.error);
        }
        else {
            toast.success('Venue Created Successfully!',{autoClose: 2000});
                setTimeout(() => {  router.push('/admin_home'); }, 2000);
        }

        }
        catch (error) {
            console.log(error)
        }
    }
    
    
}

const fetchTheatreData = async () => {
    const response = await fetch(`${config.url}/api/get_theatre`, {
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
    theatre.theatres = data;
};
onMounted(() => {
    fetchTheatreData()
});

onUpdated(() => {
    // for (let i = 0; i < venue.venues.length; i++) {
    //     if (venue.venues[i].name == name.value) {
    //         toast.warning('Venue Already Exists!');
    //         name.value = '';
    //     }
    // }
    for(let i = 0;i < theatre.theatres.length;i++){
        if(theatre.theatres[i].name == name.value){
            toast.warning('Theatre Already Exists!');
            name.value = '';
        }
    }
    if(matinee_show_time.value < morning_show_time.value && matinee_show_time.value != '' && morning_show_time.value != ''){
        toast.warning('Matinee show time must be greater then morning show time');
        matinee_show_time.value = '';
        morning_show_time.value = '';
    }
    if(first_show_time.value < matinee_show_time.value && first_show_time.value != '' && matinee_show_time.value != ''){
        toast.warning('First show time must be greater then matinee show time');
        first_show_time.value = '';
        matinee_show_time.value = '';
    }
    if(second_show_time.value < first_show_time.value && second_show_time.value != '' && first_show_time.value != ''){
        toast.warning('Second show time must be greater then first show time');
        second_show_time.value = '';
        first_show_time.value = '';
    }
    if(rows.value <= 0){
        toast.warning("rows must be Positive");
        rows.value = ''
    }
});


</script>





 <style scoped>

.container {
    height: 100%;
    width: 100%;
}


.venue {
    /* height: 75vh; */
    width: 75%;
    height: max-content;
    background: rgba(255, 255, 255, 0.279);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border: 1px solid rgba(255, 255, 255, 0.08);

}

.ven {
    padding-top: 7vh;
    padding-bottom: 7vh;
}

.form-floating input[type="text"],
.form-floating input[type="number"],
.form-floating input[type="password"],
.form-floating input[type="time"],
.form-floating textarea {
    border: none;
    border-radius: 0;
    border-bottom: 1px solid #a9b0b7;
    background-color: rgba(255, 255, 255, 0);
}

</style>