export default {
  methods: {
    getIndividuals: function() {
      console.log('getting individuals')
      this.axios.get("/api/individual/").then((response) => {
        this.individuals = response.data;
      });
    },
    getBreeds: function() {
      console.log('getting breeds')
      this.axios.get("/api/breed/").then((response) => {
        this.breeds = response.data;
      });
    },
    getMedicationTypes: function() {
      console.log('getting medication types')
      this.axios.get("/api/medication_type/").then((response) => {
        this.medicationTypes = response.data;
      });
    },
  },
};
