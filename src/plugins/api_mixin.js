export default {
  methods: {
    getIndividuals: function() {
      console.log('getting individuals')
      this.axios.get("/api/individual/").then((response) => {
        this.individuals = response.data;
      });
    },
  },
};
