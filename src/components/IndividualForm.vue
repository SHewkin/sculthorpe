<template>
  <v-card>
    <v-card-title>
      Individuals
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
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
            prepend-icon="mdi-event"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker v-model="newIndividual.date_of_birth" no-title scrollable>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
          <v-btn text color="primary" @click="$refs.menu.save(newIndividual.date_of_birth)">OK</v-btn>
        </v-date-picker>
      </v-menu>

      <v-select v-model="newIndividual.parent" :items="individuals" label="Gender"></v-select>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "IndividualForm",
  props: {},
  data() {
    return {
      menu: false,
      individuals: [],
      newIndividual: {
        name: null,
        holding_number: null,
        id_number: null,
        gender: null,
        date_of_birth: null,
        parent: null,
      },
      genders: ["Male", "Female"],
    };
  },
  mounted() {
    this.getIndividuals();
  },
  methods: {
    getIndividuals: function () {
      this.axios.get("/api/individual/").then((response) => {
        this.individuals = response.data;
        console.log(response.data);
      });
    },
  },
};
</script>
