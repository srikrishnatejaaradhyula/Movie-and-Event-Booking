<template>
    <AdminNavBar class="sticky-top z-1" />
    <div class="overflow-y-hidden" >
            <!-- Add New venue Button -->
        <div class="d-grid gap-2 d-md-flex justify-content-md-end d-grid gap-2 w-auto" >
            <button class=" primary-button m-2" @click="$router.push('/create_theatre')">Add Theatre</button>
        </div>

        <div class="container-fluid">
            <div class="row">
                <div class="card_style col-lg-6 col-md-6 col-12 my-5 d-flex justify-content-evenly" v-for="v in theatre.theatres" :key="v.id" >
                    
                    <!-- Card for Theatre -->
                    <div class="card " >
                        <div class="card-header">
                            <div class="d-flex justify-content-between">
                                <div class="d-flex">
                                    <h3  >{{ v.name }}</h3>
                                    <a :href="v.location" class="m-2 h-auto" target="_blank" data-bs-toggle="tooltip" data-bs-placement="top" title="Tooltip on top">
                                        <i class="bi bi-geo-alt"></i>
                                    </a>
                                </div>
                                <div>
                                    <button @click="IsModal.ids[v.id] = true"  class=" border-0 m-2" style="background-color: transparent; font-size: large; font-weight: 700; color:rgb(122, 68, 172)">
                                    Details <i class="bi bi-box-arrow-up-right"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Model for Theatre details  -->

                        <Teleport to="#modal">
                            <div class="modal-bg" v-if="IsModal.ids[v.id]">
                                <div class="position-relative container h-auto w-auto modal_box p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                    <div class=" position-absolute top-0 end-0 "> 
                                        <button @click="IsModal.ids[v.id] = false" class="m-2 border-0 rounded-5 ">
                                            <i class="bi bi-x-lg" style="color:brown"></i>
                                        </button>
                                    </div>
                                        
                                    <h4> Theatre details </h4>
                                    <div class="row">
                                        <div class="col-md-10">
                                            <h5>Name : {{ v.name }}</h5>
                                            <h5>Address : {{ v.address }}</h5>
                                            <h5>Capacity : {{ v.rows * v.cols }}</h5>

                                            
                                        </div>
                                        <div class="col-md-2 ">
                                            <div class="col-md-12 m-2">
                                                <button @click="$router.push('/update_theatre/'+ v.id)" class=" rounded-2 border-0" style="color:aliceblue; background-color: rgb(88, 88, 255); font-size: xx-large;">
                                                    <i class="bi bi-pencil-square"></i>
                                                </button>
                                            </div>
                                            <div class="col-md-12 m-2">
                                                <button @click="IsModalDelete.ids[v.id] = true" class=" rounded-2 border-0" style="color:aliceblue; background-color: rgb(255, 87, 87); font-size: xx-large;">
                                                    <i class="bi bi-trash-fill"></i>
                                                </button>
                                            </div>
                                        </div>
                                        
                                        <div class="col-md-10">
                                            <table class="table table-striped-columns ">
                                                <thead>
                                                    <tr>
                                                        <th scope="col">Shows</th>
                                                        <th scope="col">Timing</th>
                                                        <th scope="col">Shows</th>
                                                        <th scope="col">Timing</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <th>Morning Show</th>
                                                        <td>{{ ConvertTime(v.morning_show_time) }}</td>
                                                        <th>First Show</th>
                                                        <td>{{ ConvertTime(v.first_show_time) }}</td>
                                                    </tr>
                                                    <tr>
                                                        <th>Matinee Show</th>
                                                        <td>{{ ConvertTime(v.matinee_show_time) }}</td>
                                                        <th>Second Show</th>
                                                        <td>{{ ConvertTime(v.second_show_time) }}</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </Teleport>


                        <!-- Model for delete conformation  -->
                        <Teleport to="#modal2">
                            <div class="modal-bg" v-if="IsModalDelete.ids[v.id]">
                                <div class=" position-relative container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                    <div class=" position-absolute top-0 end-0 "> 
                                        <button @click="IsModalDelete.ids[v.id] = false" class="m-2 border-0 rounded-5 ">
                                            <i class="bi bi-x-lg" style="color:brown"></i>
                                        </button>
                                    </div>
                                    <h5 class="text-center">Are you sure you want to Delete?</h5>
                                    
                                    <div class="container d-flex justify-content-center align-center">
                                        <div class="row d-flex justify-content-evenly" >
                                            <div class="col text-center " >
                                                <button type="button" @click="DeleteTheatre(v.id)"  class="btn btn-success " >
                                                    conform!
                                                </button>
                                            </div>
                                            <div class="col text-center ">
                                                <button type="button" @click="IsModalDelete.ids[v.id] = false"  class="btn btn-danger">Cancel</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </Teleport>


                        
                        <div class="card-body overflow-auto" style="height: 55vh;" >
                            
                            <AdminGetMovie :id="v.id" />

                        </div>


                        <!-- footer -->

                        <div class="card-footer">
                            <div class="d-flex justify-content-around">
                                
                                    <button class=" primary-button w-auto"  @click="create_movie(v.id)">Add Show</button>
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

</template>

<script setup>
import {config} from '../Constants.js';
import AdminGetMovie from './AdminGetMovie.vue';
import { ref, onMounted, reactive,getCurrentInstance } from "vue";
import VueJwtDecode from 'vue-jwt-decode'
import { toast } from 'vue3-toastify';
import { useRouter } from 'vue-router';


const IsModal = reactive({
    ids: []
});
const IsModalDelete = reactive({
    ids: []
});
const openModal = () => {
    IsModalOpen.value = true;
}
// const ModalTheatre = (id) => {
//     return IsModal.id =! IsModal.id;
// } 

const theatre = reactive({
    theatres: []
});

const router = useRouter()
const token = localStorage.getItem('isAdmin')
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
};
            // Function to fetch venue data
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
    console.log(theatre.theatres[0].id);
    for(let i=0; i<theatre.theatres.length; i++){
        IsModal.ids[theatre.theatres[i].id] = false;
        IsModalDelete.ids[theatre.theatres[i].id] = false;
    }
    console.log(IsModal.ids);
    console.log(theatre.theatres)
};

// Fetch venue data on initial mount
onMounted(fetchTheatreData);

// Function to delete a venue
const DeleteTheatre = async (id) => {
    const response = await fetch(`${config.url}/api/delete_theatre`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'x-access-tokens': token
        },
        body: JSON.stringify({
            theatre_id: id
        })
    });
    const data = await response.json();
    console.log(data);
    if (response.status === 200) {
        toast.success('Theatre Deleted Successfully');
        // Fetch fresh data after successful deletion
        fetchTheatreData();
    } else {
        alert("Something went wrong");
    }
};


const update_theatre = (id) => {
    router.push('/update_theatre/'+ id)
}

const create_movie = (id) => {
    router.push('/create_movie/'+ id)
}

</script>

<style scoped>
.card {
    background: rgba(253, 253, 232, 0.226);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border-radius: 10px;
    box-shadow: 0px 0px 10px 0px rgba(61, 57, 30, 0.683);
    width: 80vh;
}



.modal_box{
    height: 50%;
    width: 70%;
    position: relative;
    background-color: white;
    /* padding:50px 100px; */
    border-radius: 5px;
    box-shadow: 0px 5px 5px 2px rgba(0, 0, 0, 0.2);
}

.primary-button{
    padding: 0.5% 1.5%;
}
    /* width */
    ::-webkit-scrollbar {
        width: 10px;
    }

    /* Track */
    ::-webkit-scrollbar-track {
        box-shadow: inset 0 0 5px rgba(253, 253, 253, 0.219); 
        border-radius: 10px;
    }

    /* Handle */
    ::-webkit-scrollbar-thumb {
        background: #8fb0ff;
        border-radius: 10px;
    }

    /* Handle on hover */
    ::-webkit-scrollbar-thumb:hover {
        background: #8fb0ff;
    }
</style>