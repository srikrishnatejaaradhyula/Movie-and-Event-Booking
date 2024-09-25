<template>
    <div>
    <UserNavBar/>
    <div class="container">
         <div class="row align-items-center mx-0 my-5 d-flex justify-content-center">
             <div class="show col-md-6 col-12 ">
                 <div class="sho">
                     <form>
                        <h4 class="col-md-12 text-center ">Booking Show</h4>
                        <div class="form-floating col-md-12  mb-3">
                             <input type="text" class="form-control" v-model="name" id="floatingInput" placeholder=" "
                                 required readonly />
                             <label for="floatingInput">Event Name</label> 
                        </div> 
                        <div class="form-floating col-md-12  mb-3">
                             <input type="number" class="form-control" v-model="price" id="floatingPassword" 
                                 placeholder=" " readonly />
                             <label for="floatingPassword">Ticket Price </label>
                        </div>
                        <div class="col-md-12" v-for="f in form">
                            <div class="col-md-12 md-2" v-if="f.type == 'checkbox'">
                                <div class="row col-md-12 input-group">
                                    <div class="row col-10">
                                        <div class="col-4" v-for="c in f.checkboxCount">
                                            <input class="form-check-input" type="checkbox" :value="f.checkboxName[c-1]" v-model="f.value" name="checkbox" id="check">
                                            <label class="form-check-label" for="check">{{ f.checkboxLabel[c-1] }}</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-12 md-2" v-else-if="f.type == 'radio'">
                                <div class="row col-md-12 input-group">
                                    <div class="row col-10">
                                        <div class="col-4" v-for="r in f.radioCount">
                                            <input class="form-check-input" type="radio" :value="f.radioName[r-1]" v-model="f.value" name="radio" id="radio">
                                            <label class="form-check-label" for="radio">{{ f.radioLabel[r-1] }}</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-12 md-2" v-else-if="f.type == 'select'">
                                <div class="input-group form-floating col-md-12">
                                    <select class="form-select" aria-label="Default select example" v-model="f.value">
                                        <option v-for="o in f.optionCount" :value="f.optionName[o-1]">{{ f.optionLabel[o-1] }}</option>
                                    </select>
                                </div>
                            </div>
                            <div class="row col-md-12 md-2" v-else-if="f.type == 'textarea'">
                                <div class="input-group form-floating col-md-12">
                                    <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px" v-model="f.value"></textarea>
                                    <label for="floatingTextarea2">{{ f.inputLabel }}</label>
                                    
                                </div>
                            </div>
                            <div class="row col-md-12 md-2" v-else>
                                <div class="input-group form-floating col-md-12 h-auto">
                                    <input :type=f.type class="form-control" aria-label="Text input with dropdown button" id="floatingInput" placeholder=" " v-model="f.value" 
                                    :required="f.required"   :placeholder="f.inputLabel">
                                    <label for="floatingInput">{{ f.inputLabel }}</label>
                                    
                                </div>
                            </div>
                        </div>

                        <div class="col-md-12 text-center pt-1">
                             <button type="button" @click="IsModalOpen = true"  class="primary-button">Book</button>

                            <Teleport to="#modal">
                                <!-- <h2>hello world</h2> -->
                                <div class="modal-bg" v-if="IsModalOpen">
                                    <div class="container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                        <h5 class="text-center">Are you sure you want to book?</h5>
                                        <!-- <button class="close" @click="IsModalOpen = false">X</button> -->
                                        
                                        <div class="container d-flex justify-content-center align-center">
                                            <div class="row d-flex justify-content-evenly" v-if="!isBooking">
                                                <div class="col text-center " >
                                                    <button type="button" @click="bookShow"  class="btn btn-success " >
                                                        conform!
                                                    </button>
                                                    <!-- <span v-if="isBooking">
                                                        <SquareSpinner size="20" color="#ffffff" />
                                                    </span> -->
                                                </div>
                                                <div class="col text-center ">
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

const name = ref('');
const price = ref(0);
const IsModalOpen = ref(false);
const isBooking = ref(false);
const form = ref(null);
const id = computed(() => route.params.id);
console.log(id.value)
const newForm = ref([])
const token = localStorage.getItem('token')
const user = VueJwtDecode.decode(token)
console.log(token)

const bookShow = async () => {
    isBooking.value = true;
    console.log(form.value)
    for(let i=0;i<form.value.length;i++){
        // if(form.value[i].required && form.value[i].value == ''){
        //     toast.error(`${form.value[i].inputLabel} is required`);
        //     return;
        // }
        newForm.value.push({
            name:form.value[i].inputName,
            value:form.value[i].value
        })
        console.log(newForm.value)
    }
    console.log(form.value)
    const response = await fetch(`${config.url}/api/book_event`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
            id:id.value,
            user_id:user.id,
            price:price.value,
            form:newForm.value,
        })
    });
    const data = await response.json();
    console.log(data)
    if (response.status === 400) {
        console.log(response);
        toast.error(data.error);
    }
    else {
        toast.success('Booking Successful',{position:'top-right',autoClose: 1500});  
        setTimeout(() => {  router.push('/user_home'); }, 1000);
    }
}

const fetchEvents = async () => {
    console.log(id.value)
    const response = await fetch(`${config.url}/api/get_event_by_id`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
            id:id.value
        })
    });
    const data = await response.json();
    name.value = data.name
    price.value = data.price
    form.value = data.form
    console.log(data.form)

}

onMounted(() => {
    fetchEvents();
})
</script>

<style scoped>
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
.form-floating input[type="password"],
.form-floating input[type="time"],
.form-floating input[type="date"],
.form-floating input[type="email"],
.form-floating select,
.form-floating textarea {
    border: none;
    border-radius: 0;
    border-bottom: 1px solid #a9b0b7;
    background-color: rgba(255, 255, 255, 0.21);
}

</style>