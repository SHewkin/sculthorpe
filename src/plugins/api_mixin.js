export default {
  data() {
    return {
      individuals: [],
      breeds: [],
      medicationTypes: [],
      fields: [],
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData: function() {
      this.getIndividuals();
      this.getBreeds();
      this.getMedicationTypes();
      this.getFields();
    },
    resetData: function() {
      Object.assign(this.$data, this.$options.data.call(this));
    },
    getIndividuals: function() {
      console.log("getting individuals");
      this.axios.get("/api/individual/").then((response) => {
        this.individuals = response.data;
      });
    },
    getIndividual: function(pk) {
      console.log("getting individuals");
      this.axios.get("/api/individual/" + pk + "/").then((response) => {
        this.individual = response.data;
      });
    },
    getBreeds: function() {
      console.log("getting breeds");
      this.axios.get("/api/breed/").then((response) => {
        this.breeds = response.data;
      });
    },
    getMedicationTypes: function() {
      console.log("getting medication types");
      this.axios.get("/api/medication_type/").then((response) => {
        this.medicationTypes = response.data;
      });
    },
    getFields: function() {
      console.log("getting fields");
      this.axios.get("/api/field/").then((response) => {
        this.fields = response.data;
      });
    },
    getIndividualTreatment: function(pk) {
      console.log("getting individual treatments");
      this.axios
        .get("/api/individual/" + pk + "/treatments/")
        .then((response) => {
          this.individualTreatments = response.data;
        });
    },
    getIndividualNote: function(pk) {
      console.log("getting individual notes");
      this.axios.get("/api/individual/" + pk + "/notes/").then((response) => {
        this.individualNotes = response.data;
      });
    },
    postData: function(url, data) {
      console.log("posting: " + url);
      this.axios
        .post("/api/" + url + "/", data)
        .catch((response) => {
          console.log("post failed");
          console.log(response);
        })
        .then(() => {
          console.log("posted");
          this.getData();
          this.closeForm();
        });
    },
    updateData: function(url, pk, data) {
      console.log("updating");
      this.axios
        .put("/api/" + url + "/" + pk + "/", data)
        .catch((response) => {
          console.log("update failed");
          console.log(response);
        })
        .then(() => {
          console.log("updated");
          this.getData();
          this.closeForm();
        });
    },
    deleteData: function(url, pk) {
      if (confirm("Do you really want to delete?")) {
        this.axios
          .delete("/api/" + url + "/" + pk + "/")
          .catch((response) => {
            console.log("delete failed");
            console.log(response);
          })
          .then(() => {
            console.log("deleted");
            this.getData();
          });
      }
    },
    getSingleObject: function(objectList, pk) {
      for (var item of objectList) {
        if (item.pk == pk) {
          return item;
        }
      }
    },
    getObjectDisplay: function(objectList, pk, objectParameter = null) {
      var singleObject = this.getSingleObject(objectList, pk);
      if (singleObject) {
        if (objectParameter && objectParameter in singleObject) {
          return singleObject[objectParameter];
        }
        return singleObject;
      }
    },
  },
};
