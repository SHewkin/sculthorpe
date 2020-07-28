<template>
  <v-card>
    <v-card-title>
      Add Individual
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
      <v-select
        v-model="newIndividual.species"
        :items="species"
        label="Type"
        item-text="species"
        item-value="pk"
      ></v-select>

      <v-text-field v-model="newIndividual.name" label="Name"></v-text-field>

      <v-text-field v-model="newIndividual.holding_number" label="Holding Number"></v-text-field>

      <v-text-field v-model="newIndividual.id_number" label="ID Number"></v-text-field>

      <v-select v-model="newIndividual.gender" :items="genders" label="Gender"></v-select>

      <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="newIndividual.date_of_birth"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="newIndividual.date_of_birth"
            label="Date of Birth"
            prepend-icon="mdi-calendar-month"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="newIndividual.date_of_birth"
          :max="new Date().toISOString().substr(0, 10)"
          min="2000-01-01"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
          <v-btn text color="primary" @click="$refs.menu.save(newIndividual.date_of_birth)">OK</v-btn>
        </v-date-picker>
      </v-menu>

      <v-select
        v-model="newIndividual.mother"
        :items="mothers"
        label="Mother"
        item-text="id_number"
        item-value="pk"
      ></v-select>
      <v-select
        v-model="newIndividual.father"
        :items="fathers"
        label="Father"
        item-text="id_number"
        item-value="pk"
      ></v-select>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeForm">Close</v-btn>
      <v-btn text right color="primary" @click="saveIndividual">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import constants_mixin from "@/plugins/constants_mixin";

export default {
  name: "IndividualForm",
  mixins: [api_mixin, constants_mixin],
  props: {},
  data() {
    return {
      menu: false,
      individuals: [],
      species: [],
      newIndividual: {
        species: null,
        name: null,
        holding_number: null,
        id_number: null,
        gender: null,
        date_of_birth: null,
        mother: null,
        father: null,
      },
    };
  },
  mounted() {
    this.getBreeds();
    this.getIndividuals();
  },
  computed: {
    mothers: function () {
      return this.individuals.filter((individual) => {
        return individual.gender == "F";
      });
    },
    fathers: function () {
      return this.individuals.filter((individual) => {
        return individual.gender == "M";
      });
    },
  },
  methods: {
    closeForm: function () {
      this.$emit("closeForm");
    },
    saveIndividual: function () {
      console.log("posting");
      this.axios
        .post("/api/individual/", this.newIndividual)
        .catch((response) => {
          console.log("post failed");
          console.log(response);
        })
        .then(() => {
          console.log("posted");
          this.closeForm();
        });
    },
  },
};
</script>
