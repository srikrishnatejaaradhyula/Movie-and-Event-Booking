import { createRouter, createWebHistory } from 'vue-router'
import Landing from "../components/Landing.vue";
import UserLogin from "../components/UserLogin.vue";
import UserRegister from "../components/UserRegister.vue";
import AdminLogin from "../components/AdminLogin.vue";
import AdminHome from "../components/AdminHome.vue";
import AdminSummery from '../components/AdminSummery.vue';
import CreateTheatre from "../components/CreateTheatre.vue";
import UpdateTheatre from "../components/UpdateTheatre.vue";
import CreateMovie from "../components/CreateMovie.vue";
import UpdateMovie from "../components/UpdateMovie.vue";
import UserHome from "../components/UserHome.vue";
import BookingShow from "../components/BookingShow.vue";
import UserBookings from "../components/UserBookings.vue";
import ForgetPassword from "../components/ForgetPassword.vue";
import Unauthorized from "../components/Unauthorized.vue";
import ErrorPage404 from "../components/ErrorPage404.vue";
import MovieBooking from "../components/MovieBooking.vue";
import DynamicForm  from "../components/DynamicForm.vue";
import AdminEvent from "../components/AdminEvent.vue";
import CreateEvent from "../components/CreateEvent.vue";
import UpdateEvent from "../components/UpdateEvent.vue";
import UserEvent from "../components/UserEvent.vue";
import EventBooking from "../components/EventBooking.vue";
import UserEventBooking from "../components/UserEventBooking.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: Landing,
    },
    {
      path: "/user_login",
      component: UserLogin,
    },
    {
      path: "/user_register",
      component: UserRegister,
    },
    {
      path: "/admin_login",
      component: AdminLogin,
    },
    {
      path: "/admin_home",
      component: AdminHome,
      meta: { adminOnly: true },
    },
    {
      path: "/create_theatre",
      component: CreateTheatre,
      meta: { adminOnly: true },
    },
    {
      path: "/update_theatre/:id",
      component: UpdateTheatre,
      meta: { adminOnly: true },
    },
    {
      path: "/create_movie/:id",
      component: CreateMovie,
      meta: { adminOnly: true },
    },
    {
      path: "/update_movie/:id",
      component: UpdateMovie,
      meta: { adminOnly: true },
    },
    {
      path: "/admin_summery",
      component: AdminSummery,
      meta: { adminOnly: true },
    },
    {
      path: "/user_home",
      component: UserHome,
      meta: { requiresAuth: true },
    },
    {
      path: "/movie_booking/:id/:date/:time",
      component: MovieBooking,
      meta: { requiresAuth: true },
    },
    {
      path: "/booking_Show/:id",
      component: BookingShow,
      meta: { requiresAuth: true },
    },
    {
      path: "/user_bookings",
      component: UserBookings,
      meta: { requiresAuth: true },
    },
    {
      path: "/forget_password",
      component: ForgetPassword,
    },
    {
      path: "/dynamic_form",
      component: DynamicForm,
    },
    {
      path: "/admin_event",
      component: AdminEvent,
      meta: { adminOnly: true },
    },
    {
      path: "/create_event",
      component: CreateEvent,
      meta: { adminOnly: true },
    },
    {
      path: "/user_event",
      component: UserEvent,
      meta: { requiresAuth: true },
    },
    {
      path:"/update_event/:id",
      component: UpdateEvent,
      meta: { adminOnly: true },
    },
    {
      path: "/event_booking/:id",
      component: EventBooking,
      meta: { requiresAuth: true },
    },
    {
      path: "/user_event_booking",
      component: UserEventBooking,
      meta: { requiresAuth: true },
    },
    {
      path: "/unauthorized",
      component: Unauthorized,
    },
    {
      path: "/:catchAll(.*)",
      component: ErrorPage404,
    }
  ]
})



router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  const isAdmin = localStorage.getItem('isAdmin'); // Assuming isAdmin is stored in local storage

  if ((to.meta.requiresAuth && !token) ) {
    // Redirect to the unauthorized page if the token is missing
    next('/unauthorized');
  }
  else if(to.meta.adminOnly && !isAdmin){
    // Redirect to the admin home page if the user is an admin
    next('/unauthorized');
  }
  else{
    // Continue to the next page
    next();
  }
});



export default router;
