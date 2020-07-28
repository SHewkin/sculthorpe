<template>
  <v-card>
    <v-card-title>
      Medication Types
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on" text fab top x-small>
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </template>
        <MedicationTypeForm @closeForm="closeForm" />
      </v-dialog>
      <v-spacer></v-spacer>

      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table :headers="headers" :items="medicationTypes" :search="search"></v-data-table>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import MedicationTypeForm from "@/components/MedicationTypeForm.vue";
export default {
  name: "MedicationTypes",
  mixins: [api_mixin],
  components: {
    MedicationTypeForm,
  },
  props: {},
  data() {
    return {
      search: "",
      dialog: false,
      headers: [
        { text: "Type", value: "species" },
        { text: "Breed", value: "breed" },
      ],
      medicationTypes: [],
    };
  },
  mounted() {
    this.getMedicationTypes();
  },
  methods: {
    closeForm: function () {
      this.dialog = false;
      this.getMedicationTypes();
    },
  },
};
</script>
