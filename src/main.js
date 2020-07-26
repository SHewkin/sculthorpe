import Vue from 'vue'
import Vuetify from "vuetify"
import 'vuetify/dist/vuetify.min.css'
import App from '@/App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from '@/store' 
import router from '@/router'

Vue.use(Vuetify)
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  vuetify: new Vuetify(),
  render: h => h(App)
})

vue.$mount('#app')
