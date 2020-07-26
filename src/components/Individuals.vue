<template>
  <v-card>
    <v-card-title>
      Individuals
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on" text fab top x-small><v-icon>mdi-plus</v-icon></v-btn>
        </template>
        <IndividualForm @closeForm="dialog = false" />
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
    <v-data-table :headers="headers" :items="individuals" :search="search">

      <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    </v-data-table>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import IndividualForm from "@/components/IndividualForm.vue";
export default {
  name: "Individuals",
  mixins: [api_mixin],
  components: {
    IndividualForm,
  },
  props: {},
  data() {
    return {
      search: "",
      dialog: false,
      headers: [
        { text: "Breed", value: "species" },
        { text: "Name", value: "name" },
        { text: "Holding Number", value: "holding_number" },
        { text: "ID Number", value: "id_number" },
        { text: "Gender", value: "gender" },
        { text: "Date of Birth", value: "date_of_birth" },
        { text: "Mother", value: "mother" },
        { text: "Father", value: "father" },
        { text: 'Actions', value: 'actions' },
      ],
      individuals: [],
    };
  },
  mounted() {
    this.getIndividuals();
  },
};
</script>
