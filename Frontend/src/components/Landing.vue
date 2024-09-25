<template>
  <div class="back"> 
    <div class="container my-auto d-flex align-content-center "  style="right: 0px;left: 0px;">
      <div class="row mt-5">
        <div class="col-12 col-lg-6 m-auto text-center">
          <h1 class="  fw-bold lh-base ">
            Welcome👋 to Your Ultimate Movie Ticket Booking Destination!
            </h1>
        </div>
        <!-- <div class="col-sm-10">
        </div> -->
        <div class="col-8 col-lg-6   m-auto   login-buttons">

          <!-- <button class="my-4 primary-button" @click="$router.push('/user_login')">Login</button> -->
          <button class="my-4 primary-button" @click="login">Login</button>


          <button class="my-4 primary-button" @click="$router.push('/user_register')">Register</button>
      
          <!-- <button class="my-4 primary-button" @click="$router.push('/admin_login')">Admin</button> -->

          <button class="my-4 primary-button" @click="admin">Admin</button>

          
          
        </div>
      </div>
    </div>
  </div>
  
</template>

<script setup>
import { useRouter } from "vue-router";

const token = localStorage.getItem('token');
const isAdmin = localStorage.getItem('isAdmin');
const router = useRouter()

const login = () => {
  // if (token) {
  //   router.push('/user_home')
  // } else {
  //   router.push('/user_login')
  // }
  router.push('/user_login')
}

const admin = () => {
  // if (isAdmin) {
  //   router.push('/admin_home')
  // } else {
  //   router.push('/admin_login')
  // }
  router.push('/admin_login')
}

const json_data = ref([
  {
    name: "naveen"
  },
  {
    name: "naveen"
  },
  {
    name: "naveen"
   }
])

</script>

<style scoped>
.container{
  height: 100%;
  width: 70%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  position: absolute;
  z-index: 1;
}
.back{
  height: 100%;
  width: 100%;
  background-image: url("../assets/MovieBackGround_2.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  position: absolute;
  z-index: -1;
}
.login-buttons{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  height: 50%;
  width: 35%;
  border-radius: 10px;
  background-color: #e5fffa5e;
  -webkit-box-shadow: 0px 28px 65px 14px rgba(74,24,24,0.5);
  -moz-box-shadow: 0px 28px 65px 14px rgba(74,24,24,0.5);
  box-shadow: 0px 28px 65px 14px rgba(74,24,24,0.5);
}


@media (max-width: 480px) {
  .container{
    width: 100%;
  }
  .login-buttons{
    width: 75%;
  }
}

/* button{
  padding: 4% 8%;
  border-radius: 10px;
  border: none;
  background-color: #ff8f8f;
  font-size: 1.5rem;
  font-weight: bold;
  color: rgb(74,24,24);
  transition: all 0.5s ease;
} */

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
    font-size: 6vh;
}

@keyframes textclip {
    to {
        background-position: 200% center;
    }
}
</style>