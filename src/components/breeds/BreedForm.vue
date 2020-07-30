<template>
  <v-card>
    <v-card-title>
      Add Breed
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
      <v-select v-model="newBreed.species" :items="species" label="Type"></v-select>

      <v-text-field v-model="newBreed.breed" label="Breed"></v-text-field>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeForm">Close</v-btn>
      <v-btn text right color="primary" @click="saveBreed">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import constants_mixin from "@/plugins/constants_mixin";

export default {
  name: "BreedForm",
  mixins: [api_mixin, constants_mixin],
  props: {
    breed: null,
  },
  data() {
    return {
      menu: false,
      newBreed: {
        species: null,
        breed: null,
      },
    };
  },
  mounted() {
    this.loadInitialData();
  },
  methods: {
    loadInitialData: function () {
      if (this.breed) {
        this.newBreed = this.breed;
      }
    },
    closeForm: function () {
      this.$emit("closeForm");
    },
    saveBreed: function () {
      if (this.breed) {
        this.updateData("breed", this.breed.pk, this.newBreed);
      } else {
        this.postData("breed", this.newBreed);
      }
    },
  },
};
</script>
