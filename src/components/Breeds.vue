<template>
  <v-card>
          <IndividualForm />

    <v-card-title>
      Add Indivudal
      <v-spacer></v-spacer>

      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
   <v-data-table
    :headers="headers"
    :items="individuals"
    :search="search"
  ></v-data-table>
  </v-card>
 
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import IndividualForm from "@/components/IndividualForm.vue"
export default {
  name: "Individuals",
  mixins: [api_mixin],
  components: {
    IndividualForm
  },
  props: {},
  data() {
    return {
      search: "",
      headers: [
        { text: "Name", value: "name" },
        { text: "Holding Number", value: "holding_number" },
        { text: "ID Number", value: "id_number" },
        { text: "Gender", value: "gender" },
        { text: "Date of Birth", value: "date_of_birth" },
        { text: "Mother", value: "parent" },
      ],
      individuals: [],
    };
  },
  mounted() {
    this.getIndividuals();
  },
};
</script>
