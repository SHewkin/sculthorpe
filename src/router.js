import Vue from "vue";
import Router from "vue-router";
import Individuals from "@/components/individuals/Individuals.vue";
import MedicationTypes from "@/components/medications/MedicationTypes.vue";
import Breeds from "@/components/breeds/Breeds.vue";
import Fields from "@/components/fields/Fields.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: Individuals,
    },
    {
      path: "/medication_types",
      name: "medication_types",
      component: MedicationTypes,
    },
    {
      path: "/breeds",
      name: "breeds",
      component: Breeds,
    },
    {
      path: "/fields",
      name: "fields",
      component: Fields,
    },
  ],
});
