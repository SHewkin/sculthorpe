<template>
  <v-card>
    <v-card-title>
      Add Individual
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
      <v-select
        v-model="newIndividual.breed"
        :items="breeds"
        label="Type"
        item-text="breed"
        item-value="pk"
      >
        <template v-slot:item="{ item }">
          <span>{{item.breed}} ({{item.species}})</span>
        </template>
      </v-select>

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

      <v-select
        v-model="newIndividual.field"
        :items="fields"
        label="Field"
        item-text="name"
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
  props: {
    individual: null,
  },
  data() {
    return {
      menu: false,
      individuals: [],
      breeds: [],
      newIndividual: {
        breed: null,
        name: null,
        holding_number: null,
        id_number: null,
        gender: null,
        date_of_birth: null,
        mother: null,
        father: null,
        field: null,
      },
    };
  },
  mounted() {
    this.loadInitialData();
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
    loadInitialData: function () {
      if (this.individual) {
        this.newIndividual = this.individual;
      }
    },
    closeForm: function () {
      this.$emit("closeForm");
    },
    saveIndividual: function () {
      if (this.individual) {
        this.updateData("individual", this.individual.pk, this.newIndividual);
      } else {
        this.postData("individual", this.newIndividual);
      }
    },
  },
};
</script>
