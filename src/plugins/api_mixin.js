export default {
  methods: {
    getIndividuals: function() {
      console.log('getting individuals')
      this.axios.get("/api/individual/").then((response) => {
        this.individuals = response.data;
      });
    },
    getSpecies: function() {
      console.log('getting species')
      this.axios.get("/api/species/").then((response) => {
        this.species = response.data;
      });
    },
  },
};
