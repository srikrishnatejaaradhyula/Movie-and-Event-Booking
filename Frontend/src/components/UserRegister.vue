<template>
   <div class="container ">
        <div class="row align-items-center mx-0 my-5">
            <div class="register col-md-6 col-12 ">
                <div class="reg">
                    <form>
                        <h4 class="col-md-12 text-center ">Register</h4>
                        <div class="form-floating col-md-12  mb-3">
                            <input type="text" class="form-control" v-model="name" id="floatingInput" placeholder=" "
                                required />
                            <label for="floatingInput">Name</label>
                        </div>
                        <div class="flex row col-md-12 justify-content-around align-items-center ">
                            <div class="form-floating col-9 mb-3">
                                <input type="email" class="form-control" v-model="email" id="floatingInput" placeholder=" "
                                    required />
                                <label for="floatingInput">Email address</label>
                            </div>
                            <div class="col-3 ">
                                <!-- <input type="button" @click="openModal" id="butt" class="verify h-auto" value="verify"> -->
                                <button type="button" @click="openModal" id="butt" class="notverify h-auto " v-if="!verify">
                                    <i class="bi bi-person-x"> Verify</i>
                                </button>
                                <button type="button"  id="butt" class="verify h-auto " v-else>
                                    <i class="bi bi-person-check"> Verified</i>
                                </button>
                            </div>
                        </div> 
                    
                        <div class="form-floating col-md-12  mb-3">
                            <input type="password" class="form-control" v-model="password" id="floatingPassword"
                                placeholder=" " required />
                            <label for="floatingPassword">Password</label>
                        </div>
                        <div class="form-floating col-md-12  mb-3">
                            <input type="password" class="form-control" v-model="password_confirm" id="floatingPassword"
                                placeholder=" " required />
                            <label for="floatingPassword">Password confirm</label>
                        </div>
                        <div class="col-md-12 text-center pt-1">
                            <button type="submit" @click.prevent="handleSubmit" id="butt"
                                class="primary-button">Register</button>
                        </div>
                    </form>

                    <Teleport to="#modal">
                        <div class="modal-bg" v-if="IsModalOpen">

                            <!-- <BookingRating :id="b.id" v-model="IsModalOpen"/> -->

                                <div class="container h-auto w-auto  p-5" style="background-color: antiquewhite; border-radius: 10px;">
                                <h4>Please enter verification code </h4>
                                <div class="form-floating col-md-12  mb-3">
                                    <input type="number" class="form-control" v-model="otp"  id="floatingPassword"
                                        placeholder=" "   />
                                    <label for="floatingPassword"> Verification code </label>
                                </div>
                                
                                <div class="container d-flex justify-content-center align-center">
                                    <div class="row d-flex justify-content-evenly">
                                        <div class="col text-center " >
                                            <button type="button"  @click="verify_otp"  class="btn btn-success " >
                                                conform!
                                            </button>
                                        </div>
                                        <div class="col text-center ">
                                            <button type="button" @click="IsModalOpen = false"  class="btn btn-danger">Cancel</button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </Teleport>
                </div>
            </div>
            <div class="blank col-md-6 col-12 d-flex justify-content-center">
                <!-- <h3>Don't have an account? </h3> -->
                <div class="col-md-12 text-center position-absolute top-50 start-50 translate-middle">
                    <h3>If you have an account? </h3>
                    <!-- <router-link class="btn btn-success" to="/userlogin">Login here!</router-link> -->
                    <button class=" primary-button" @click="$router.push('/user_login')">Login here!</button>
                </div>
            </div>
        </div>
        <!-- {{ name }}
        {{ email }} -->
    </div>
</template>

<script setup>
import {config} from '../Constants.js';
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';


const router = useRouter()
const name = ref('')
const email = ref('')
const password = ref('')
const password_confirm = ref('')
const verify = ref(0)
const otp = ref()
const email_verification_otp = ref()

const openModal = async() => {
    if (email.value == ''){
        toast.warning('Please Enter the Email');
    }
    else{
        IsModalOpen.value = true;
        const response2 = await fetch(`${config.url}/api/send_verification_otp`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email.value
            })
        })
        const data = await response2.json()
        email_verification_otp.value = data.otp
    }
}

const verify_otp = async() =>{
    if( email_verification_otp.value == otp.value){
        toast.success('E-mail is verified ');
        verify.value = 1
        IsModalOpen.value = false;
    }
}

const IsModalOpen = ref(false);
const validatePassword = (password) =>{
    // Define a regular expression pattern
    var passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    
    // Test the password against the pattern
    return passwordPattern.test(password);
}
const handleSubmit = async() => {
    console.log("hello")
    if (name.value == ''){
        toast.warning('Please Enter the Name');
    }
    else if (email.value == ''){
        toast.warning('Please Enter the E-mail');
    }
    else if (password.value == ''){
        toast.warning('Please Enter the Password');
    }
    else if (password.value.length < 6){
        toast.warning('Password must be at least 6 characters');
    }
    else if (!validatePassword(password.value)){
        toast.warning('Password must contain at least one uppercase letter, one lowercase letter, one number and one special character');
    }
    else if (password_confirm.value == ''){
        toast.warning('Please Enter the Password confirm');
    }
    else if (password.value != password_confirm.value) {
        toast.error('Passwords do not match!');
    }
    else if (verify.value == 0){
        toast.warning('Please verify the E-mail');
    }
    else {
        console.log("hi")
        try {
            const response = await fetch(`${config.url}/api/user_register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name.value,
                email: email.value,
                verified: verify.value,
                password: password.value
            })
        })
        console.log(email.value)
        console.log(response);
        if (!response.ok) {
            console.log(response);
            toast.error(data.error);
        }
        else {
            toast.success('Registered Successfully!',{autoClose: 2000});
            setTimeout(() => {  router.push('/user_login'); }, 2000);
        }

        }
        catch (error) {
            console.log(error)
        }

    }
}

</script>

<style scoped>

.container {

    height: 100%;
  width: 100%;
  /* display: flex; */
}

.blank {
    height: 75vh;
    background: rgba(76, 172, 250, 0.36);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border: 1px solid rgba(255, 255, 255, 0.08);

}

.register {
    height: 75vh;
    background: rgba(230, 253, 253, 0.279);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(5.6px);
    -webkit-backdrop-filter: blur(5.6px);
    border: 1px solid rgba(255, 255, 255, 0.08);

}
.verify{
    background-color: #98ff8f;
    font-size: 1.2rem;
    font-weight: 500;
    border: 0;
    border-radius: 5px;
    color: rgb(36, 74, 24);
}

.notverify{
    background-color: #ffba8f;
    font-size: 1.2rem;
    font-weight: 500;
    border: 0;
    border-radius: 5px;
    color: rgb(74, 39, 24);
}

.reg {
    padding-top: 7vh;
}

.form-floating input[type="text"],
.form-floating input[type="email"],
.form-floating input[type="password"],
.form-floating textarea {
    border: none;
    border-radius: 0;
    border-bottom: 1px solid #a9b0b7;
    background-color: rgba(255, 255, 255, 0);
}

</style>