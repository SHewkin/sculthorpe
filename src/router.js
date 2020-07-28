import Vue from 'vue'
import Router from 'vue-router'
import Individuals from '@/components/Individuals.vue'
import MedicationTypes from '@/components/MedicationTypes.vue'
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
      path: '/medication_types',
      name: 'medication_types',
      component: MedicationTypes
    },
    {
      path: '/breeds',
      name: 'breeds',
      component: Breeds
    }
  ]
})
