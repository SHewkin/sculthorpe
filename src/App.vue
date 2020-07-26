<template>
  <v-app>
    <NavBar/>
    <router-view/>
  </v-app>
</template>

<script>
import NavBar from "@/components/NavBar.vue"
export default {
  name: "App",
  components: {
    NavBar
  },
  props: {},
  data() {
    return {
      drawer: false,
    };
  },
};
</script>

