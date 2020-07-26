import Vue from 'vue'
import Router from 'vue-router'
import Individuals from '@/components/Individuals.vue'
import Medications from '@/components/Medications.vue'
import Breeds from '@/components/Breeds.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Individuals
    },
    {
      path: '/medications',
      name: 'medications',
      component: Medications
    },
    {
      path: '/breeds',
      name: 'breeds',
      component: Breeds
    }
  ]
})
