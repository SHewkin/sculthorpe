<template>
  <v-card>
    <v-card-title>
      Individuals
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on" text fab top x-small>
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </template>
        <IndividualForm @closeForm="dialog = false" :individual="editedIndividual" />
      </v-dialog>

      <v-spacer></v-spacer>

      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="individuals"
      :search="search"
      show-expand
      item-key="pk"
      single-expand
      :expanded.sync="expanded"
    >
      <template v-slot:item.breed="{ item }">{{getBreedDisplay(item)}}</template>

      <template v-slot:item.field="{ item }">{{getObjectDisplay(fields, item.field, "name")}}</template>

      <template v-slot:expanded-item="{ headers, item }">
        <td :colspan="headers.length">
          <IndividualDetail :pk="item.pk" />
        </td>
      </template>

      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteData('individual', item.pk)">mdi-delete</v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import IndividualForm from "@/components/individuals/IndividualForm.vue";
import IndividualDetail from "@/components/individuals/IndividualDetail.vue";
export default {
  name: "Individuals",
  mixins: [api_mixin],
  components: {
    IndividualForm,
    IndividualDetail,
  },
  props: {},
  data() {
    return {
      expanded: [],
      search: "",
      dialog: false,
      editedIndividual: null,
      headers: [
        { text: "Breed", value: "breed" },
        { text: "Name", value: "name" },
        { text: "Holding Number", value: "holding_number" },
        { text: "ID Number", value: "id_number" },
        { text: "Gender", value: "gender" },
        { text: "Date of Birth", value: "date_of_birth" },
        { text: "Mother", value: "mother" },
        { text: "Father", value: "father" },
        { text: "Field", value: "field" },
        { text: "Actions", value: "actions" },
      ],
    };
  },
  methods: {
    closeForm: function () {
      this.dialog = false;
      this.editedIndividual = null;
      this.getIndividuals();
    },
    editItem(item) {
      this.editedIndividual = Object.assign({}, item);
      this.dialog = true;
    },
    getBreedDisplay: function (item) {
      var breed = this.getSingleObject(this.breeds, item.breed);
      if (breed) {
        return breed.breed;
      }
    },
  },
};
</script>
