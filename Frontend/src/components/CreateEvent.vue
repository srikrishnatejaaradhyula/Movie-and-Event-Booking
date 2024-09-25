<template>
    <div>
    <AdminNavBar class=" sticky-top"/>
    <div class="container ">
         <div class="row align-items-center mx-0 my-3 d-flex justify-content-center">
             <div class="show h-auto col-md-6 col-12 shadow-lg  rounded-4">
                 <div class="sho mb-3 ">
                    <h4 class="col-md-12 text-center ">Create Event</h4>
                     <form>
                     <div class="row">
                        <div class="col-md-6">
                            <div class="col-md-12 form-floating ">
                                <input class="form-control" type="file" id="formFile" @input="onFileSelected" accept="application/pdf">
                                <label for="formFile"> Upload Event Brochure </label>

                            </div>
                            <div class="form-floating col-md-12  mb-2">
                                <input type="text" class="form-control" v-model="name" id="floatingInput" placeholder=" " />
                                <label for="floatingInput">Event Name</label>
                            </div>
                            <div class="form-floating col-md-12  mb-2">
                                <textarea type="text" class="form-control" v-model="description" id="floatingInput" placeholder=" "></textarea>
                                <label for="floatingInput">Event description</label>
                            </div>
                            <div class="form-floating col-md-12  mb-1">
                                <input type="text" class="form-control" v-model="address" id="floatingInput" placeholder=" " />
                                <label for="floatingInput">Event Address</label>
                            </div>
                            <div class="form-floating col-md-12  mb-1">
                                <input type="text" class="form-control" v-model="location" id="floatingInput" placeholder=" " />
                                <label for="floatingInput">Event Location Link</label>
                            </div>
                            <div class="form-floating col-md-12  mb-1">
                                <input type="date" class="form-control" v-model="date" id="floatingPassword"  placeholder=" "  />
                                <label for="floatingPassword">Event Date</label>
                            </div>
                            <div class="form-floating col-md-12  mb-3">
                                <input type="number" class="form-control" v-model="price" id="floatingPassword" placeholder=" "  />
                                <label for="floatingPassword">Event Ticket Price</label>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="row">
                                <div class="col-md-12">
                                    <button class="primary-button" type="button" @click="IsModalForm = true">Add Field</button>
                                </div>
                                <div class="row col-md-12" v-for="f in form">
                                    <div class="col-md-12" v-if="f.type == 'checkbox'">
                                        <div class="row col-md-12 input-group">
                                            <div class="row col-10">
                                                <div class="col-4" v-for="c in f.checkboxCount">
                                                    <input class="form-check-input" type="checkbox" :value="f.checkboxName[c-1]" v-model="f.value" name="checkbox" id="check">
                                                    <label class="form-check-label" for="check">{{ f.checkboxLabel[c-1] }}</label>
                                                </div>
                                            </div>
                                            <div class="col-2">
                                                <button class="btn btn-outline-secondary dropdown-toggle h-auto w-auto" type="button" data-bs-toggle="dropdown" aria-expanded="false"></button>
                                                <ul class="dropdown-menu dropdown-menu-end h-auto " style="width: min-content;">
                                                    <li class="d-flex justify-content-center">
                                                        <button class="btn  btn-outline-primary " type="button" @click="moveUp(form,f)">
                                                            <i class="bi bi-caret-up" ></i>
                                                        </button>
                                                        <button class="btn btn-outline-primary" type="button" @click="moveDown(form,f)">
                                                            <i class="bi bi-caret-down" ></i>
                                                        </button>
                                                        <button class="btn btn-outline-danger " type="button" @click="form = removeField(form,f)">
                                                            <i class="bi bi-trash"></i>
                                                        </button>
                                                    </li>
                                                </ul>
                                                
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-12" v-else-if="f.type == 'radio'">
                                        <div class="row col-md-12 input-group">
                                            <div class="row col-10">
                                                <div class="col-4" v-for="r in f.radioCount">
                                                    <input class="form-check-input" type="radio" :value="f.radioName[r-1]" v-model="f.value" name="radio" id="radio">
                                                    <label class="form-check-label" for="radio">{{ f.radioLabel[r-1] }}</label>
                                                </div>
                                            </div>
                                            <div class="col-2">
                                                <button class="btn btn-outline-secondary dropdown-toggle h-auto w-auto" type="button" data-bs-toggle="dropdown" aria-expanded="false"></button>
                                                <ul class="dropdown-menu dropdown-menu-end h-auto " style="width: min-content;">
                                                    <li class="d-flex justify-content-center">
                                                        <button class="btn  btn-outline-primary " type="button" @click="moveUp(form,f)">
                                                            <i class="bi bi-caret-up" ></i>
                                                        </button>
                                                        <button class="btn btn-outline-primary"  type="button" @click="moveDown(form,f)">
                                                            <i class="bi bi-caret-down" ></i>
                                                        </button>
                                                        <button class="btn btn-outline-danger " type="button" @click="form = removeField(form,f)">
                                                            <i class="bi bi-trash"></i>
                                                        </button>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-12" v-else-if="f.type == 'select'">
                                        <div class="input-group form-floating col-md-12">
                                            <select class="form-select" aria-label="Default select example" v-model="f.value">
                                                <option v-for="o in f.optionCount" :value="f.optionName[o-1]">{{ f.optionLabel[o-1] }}</option>
                                            </select>
                                            <button class="btn btn-outline-secondary dropdown-toggle h-auto w-auto" type="button" data-bs-toggle="dropdown" aria-expanded="false"></button>
                                            <ul class="dropdown-menu dropdown-menu-end h-auto " style="width: min-content;">
                                                <li class="d-flex justify-content-center">
                                                    <button class="btn  btn-outline-primary " type="button" @click="moveUp(form,f)">
                                                        <i class="bi bi-caret-up" ></i>
                                                    </button>
                                                    <button class="btn btn-outline-primary" type="button" @click="moveDown(form,f)">
                                                        <i class="bi bi-caret-down" ></i>
                                                    </button>
                                                    <button class="btn btn-outline-danger " type="button" @click="form = removeField(form,f)">
                                                        <i class="bi bi-trash"></i>
                                                    </button>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="row col-md-12 m-1" v-else-if="f.type == 'textarea'">
                                        <div class="input-group form-floating col-md-12">
                                            <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px" v-model="f.value"></textarea>
                                            <label for="floatingTextarea2">{{ f.inputLabel }}</label>
                                            <button class="btn btn-outline-secondary dropdown-toggle h-auto w-auto" type="button" data-bs-toggle="dropdown" aria-expanded="false"></button>
                                            <ul class="dropdown-menu dropdown-menu-end h-auto " style="width: min-content;">
                                                <li class="d-flex justify-content-center">
                                                    <button class="btn  btn-outline-primary " type="button" @click="moveUp(form,f)">
                                                        <i class="bi bi-caret-up" ></i>
                                                    </button>
                                                    <button class="btn btn-outline-primary" type="button" @click="moveDown(form,f)">
                                                        <i class="bi bi-caret-down" ></i>
                                                    </button>
                                                    <button class="btn btn-outline-danger " type="button" @click="form = removeField(form,f)">
                                                        <i class="bi bi-trash"></i>
                                                    </button>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="row col-md-12" v-else>
                                        <div class="input-group form-floating col-md-12 h-auto">
                                            <input :type=f.type class="form-control" aria-label="Text input with dropdown button" id="floatingInput" placeholder=" " v-model="f.value" :placeholder="f.inputLabel">
                                            <label for="floatingInput">{{ f.inputLabel }}</label>
                                            <button class="btn btn-outline-secondary dropdown-toggle h-auto w-auto" type="button" data-bs-toggle="dropdown" aria-expanded="false"></button>
                                            <ul class="dropdown-menu dropdown-menu-end h-auto " style="width: min-content;">
                                                <li class="d-flex justify-content-center">
                                                    <button class="btn  btn-outline-primary " type="button" @click="moveUp(form,f)">
                                                        <i class="bi bi-caret-up" ></i>
                                                    </button>
                                                    <button class="btn btn-outline-primary" type="button" @click="moveDown(form,f)">
                                                        <i class="bi bi-caret-down" ></i>
                                                    </button>
                                                    <button class="btn btn-outline-danger " type="button" @click="form = removeField(form,f)">
                                                        <i class="bi bi-trash"></i>
                                                    </button>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>

                                <Teleport to="#modal2">
                                    <div class="modal-bg  " v-if="IsModalForm">
                                        <div class="mt-4 overflow-y-auto position-relative container h-50 w-50  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                            <div class=" position-absolute top-0 end-0 "> 
                                                <button @click="IsModalForm = false" class="m-2 border-0 rounded-5 ">
                                                    <i class="bi bi-x-lg" style="color:brown"></i>
                                                </button>
                                            </div>
                                            <div class=" container">
                                                <div class="row">
                                                    <div class="form-floating col-md-12 " >
                                                        <select class="form-select" id="forType" aria-label="Default select example" v-model="type" >
                                                            <option value="text">Text</option>
                                                            <option value="email">E-mail</option>
                                                            <option value="number">Number</option>
                                                            <option value="date">Date</option>
                                                            <option value="time">Time</option>
                                                            <option value="password">Password</option>
                                                            <option value="textarea">Textarea</option>
                                                            <option value="select">Select</option>
                                                            <option value="checkbox">Checkbox</option>
                                                            <option value="radio">Radio</option>
                                                        </select>
                                                        <label for="forType" >Select Type of Input Field </label>
                                                    </div>
                                                    <div class="col-md-12 m-1" v-if="type =='checkbox'" onchange="type">
                                                        
                                                        <div class="form-floating col-md-12 m-1">
                                                            <input type="text" class="form-control"  id="floatingInput" v-model="inputName" placeholder="Select name">
                                                            <label for="floatingInput">Select name</label>
                                                        </div>
                                                        <div class="form-floating col-md-12 m-1" >
                                                            <input type="number" class="form-control" id="floatingInput" v-model="checkboxCount" placeholder="Number of checkbox">
                                                            <label for="floatingInput">Number of checkbox</label>
                                                        </div>
                                                        <!-- {{ checkboxLabel }} -->
                                                        <div class="row col-md-12 m-1" v-for="c in checkboxCount">
                                                            <div class="form-floating col-md-6">
                                                                <input type="text" class="form-control" id="floatingInput" v-model="checkboxLabel[c-1]" placeholder="Checkbox label">
                                                                <label for="floatingInput">Checkbox label</label>
                                                            </div>
                                                            <div class="form-floating col-md-6">
                                                                <input type="text" class="form-control" id="floatingInput" v-model="checkboxName[c-1]" placeholder="Checkbox name">
                                                                <label for="floatingInput">Checkbox name</label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-12 m-1"  v-else-if="type =='radio'" onchange="type">
                                                        <div class="form-floating col-md-12 m-1">
                                                            <input type="text" class="form-control"  id="floatingInput" v-model="inputName" placeholder="Select name">
                                                            <label for="floatingInput">Select name</label>
                                                        </div>
                                                        <div class="form-floating  col-md-12 m-1" >
                                                            <input type="number" class="form-control" id="floatingInput" v-model="radioCount" placeholder="Number of radio">
                                                            <label for="floatingInput">Number of radio</label>
                                                        </div>
                                                        <div class="row col-md-12 m-1" v-for="r in radioCount">
                                                            <div class="form-floating  col-md-6">
                                                                <input type="text" class="form-control" id="floatingInput" v-model="radioLabel[r-1]" placeholder="Radio label">
                                                                <label for="floatingInput">Radio label</label>
                                                            </div>
                                                            <div class="form-floating col-md-6">
                                                                <input type="text" class="form-control" id="floatingInput" v-model="radioName[r-1]" placeholder="Radio name">
                                                                <label for="floatingInput">Radio name</label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-12 m-1"  v-else-if="type =='select'" onchange="type">
                                                        <div class="form-floating col-md-12 m-1">
                                                            <input type="text" class="form-control"  id="floatingInput" v-model="inputName" placeholder="Select name">
                                                            <label for="floatingInput">Select name</label>
                                                        </div>

                                                        <div class="form-floating col-md-12 m-1" >
                                                            <input type="number" class="form-control" id="floatingInput" v-model="optionCount" placeholder="Number of select">
                                                            <label for="floatingInput">Number of select</label>
                                                        </div>
                                                        <div class="row col-md-12 m-1" v-for="s in optionCount">
                                                            <div class="form-floating  col-md-6">
                                                                <input type="text" class="form-control" id="floatingInput" v-model="optionLabel[s-1]" placeholder="Select label">
                                                                <label for="floatingInput">Select label</label>
                                                            </div>
                                                            <div class="form-floating col-md-6">
                                                                <input type="text" class="form-control" id="floatingInput" v-model="optionName[s-1]" placeholder="Select name">
                                                                <label for="floatingInput">Select name</label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    
                                                    <div class="row col-md-12 m-1" v-else>
                                                        <div class="form-floating col-md-6">
                                                            <input type="text" class="form-control" id="floatingInput" v-model="inputLabel" placeholder="Select label">
                                                            <label for="floatingInput">Select label</label>
                                                        </div>
                                                        <div class="form-floating col-md-6">
                                                            <input type="text" class="form-control"  id="floatingInput" v-model="inputName" placeholder="Select name">
                                                            <label for="floatingInput">Select name</label>
                                                        </div>
                                                    </div>

                                                    <div class="form-check form-switch">
                                                        <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-model="require">
                                                        <label class="form-check-label" for="flexSwitchCheckDefault"> Input field is required </label>
                                                    </div>

                                                </div>
                                            </div>
                                            
                                            <div class="container mt-4">
                                                <div class="row " >
                                                    <div class="col-6 text-center " >
                                                        <button type="button" @click="AddToForm"  class="btn btn-success " >
                                                            Add form
                                                        </button>
                                                    </div>
                                                    <div class="col-6 text-center ">
                                                        <button type="button" @click="IsModalForm = false"  class="btn btn-danger">Cancel</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </Teleport>

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
import { useRouter,useRoute } from 'vue-router'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import VueJwtDecode from 'vue-jwt-decode';


const router = useRouter()
const route = useRoute()

const file = ref(null);
const fileUrl = ref(null);
const name = ref('')
const description = ref('')
const address = ref('')
const location = ref('')
const date = ref('')
const price = ref()

const type = ref()
const IsModalForm = ref(false)
const checkboxCount = ref()
const radioCount = ref()
const optionCount = ref()
const checkboxLabel = ref([])
const checkboxName = ref([])
const radioLabel = ref([])
const radioName = ref([])
const optionLabel = ref([])
const optionName = ref([])
const inputLabel = ref()
const inputName = ref()

const require = ref(false)

const token = localStorage.getItem('isAdmin')
const user = VueJwtDecode.decode(token)

const event = reactive({
        events: []
})

const form = ref([])

const AddToForm = () =>{
    if (type.value == 'checkbox') {
        form.value.push({
            type: type.value,
            name: inputName.value,
            checkboxCount: checkboxCount.value,
            checkboxLabel: checkboxLabel.value,
            checkboxName: checkboxName.value,
            require: require.value,
            value: []
        })
        console.log(form.value)
        type.value = ''
        inputName.value = ''
        checkboxCount.value = ''
        checkboxLabel.value = []
        checkboxName.value = []
        IsModalForm.value = false
        require.value = false
    }
    if (type.value == 'radio') {
    
        form.value.push({
            type: type.value,
            name: inputName.value,
            radioCount: radioCount.value,
            radioLabel: radioLabel.value,
            radioName: radioName.value,
            require: require.value,
            value: ''
        })
        console.log(form.value)
        type.value = ''
        inputName.value = ''
        radioCount.value = ''
        radioLabel.value = []
        radioName.value = []
        IsModalForm.value = false
        require.value = false
    }
    if (type.value == 'select') {
        form.value.push({
            type: type.value,
            name: inputName.value,
            optionCount: optionCount.value,
            optionLabel: optionLabel.value,
            optionName: optionName.value,
            require: require.value,
            value: ''
        })
        console.log(form.value)
        type.value = ''
        inputName.value = ''
        optionCount.value = ''
        optionLabel.value = []
        optionName.value = []
        IsModalForm.value = false
        require.value = false
    }
    if (type.value == 'text' || type.value == 'email' || type.value == 'number' || type.value == 'date' || type.value == 'password' || type.value == 'textarea'){
        form.value.push({
            type: type.value,
            inputLabel: inputLabel.value,
            inputName: inputName.value,
            require: require.value,
            value: ''
        })
        console.log(form.value)
        type.value = ''
        inputLabel.value = ''
        inputName.value = ''
        IsModalForm.value = false
        require.value = false
    }

}

const removeField = (arr, value) =>{
 
    return arr.filter((i)=> {
        return i != value;
    });
 
}

const moveUp = (array, element) => {
    const index = array.indexOf(element);

    if (index > 0) {
        const temp = array[index - 1];
        array[index - 1] = array[index];
        array[index] = temp;
    }

    return array;
}
const moveDown = (array, element) => {
    const index = array.indexOf(element);

    if (index < array.length - 1 && index !== -1) {
        const temp = array[index + 1];
        array[index + 1] = array[index];
        array[index] = temp;
    }

    return array;
}

const onFileSelected = (e) => {
    file.value = e.target.files[0];
}

const handleSubmit = () => {
    if (name.value == ''  || price.value == '' || date.value == '' || description.value == '' || address.value == '' || location.value == ''|| file.value == '' || form.value == '' ) {
        toast.warning('Please fill all the fields');
    }
    else {
        const reader = new FileReader()
        reader.readAsDataURL(file.value)
        reader.onload = async () => {
            const base64 = reader.result.split(',')[1]
            console.log("this is base64",base64)
            try {
                const response = await fetch(`${config.url}/api/create_event`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'x-access-tokens': token 
                    },
                    body: JSON.stringify({
                        admin_id: user.id,
                        name: name.value,
                        description: description.value,
                        address: address.value,
                        location: location.value,
                        date: date.value,
                        price: price.value,
                        file: base64,
                        form:form.value
                    })
                })
                console.log(response);
                if (!response.ok) {
                    console.log(response);
                    throw new Error(`${alert(data.error)}`);
                }
                else {
                    toast.success('Event Created Successfully!',{autoClose: 1000});
                    setTimeout(() => {  router.push('/admin_event'); }, 1000);
                }
            }
            catch (error) {
                console.log(error)
                // alert("E-mail is already used!")
            }
        }
    }
}
const fetchEvents = async () => {
    const response = await fetch(`${config.url}/api/get_event_all`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-tokens': token
        },
        body: JSON.stringify({
        })
    });
    const data = await response.json();
    event.events = data;
}

onMounted(() => {
    fetchEvents();
})
const today = new Date()

onUpdated(() => {
    if (date.value < today.toISOString().slice(0,10) && date.value != '') {
        toast.warning('Event date must be greater then current date');
        date.value = '';
    }
})
</script>


<style  scoped>

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

/* input[type="file"] {
    display: none;
} */

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