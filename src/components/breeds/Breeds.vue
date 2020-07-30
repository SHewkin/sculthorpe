<template>
  <v-card>
    <v-card-title>
      Breed
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on" text fab top x-small>
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </template>
        <BreedForm @closeForm="closeForm" :breed="editedBreed" />
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
    <v-data-table :headers="headers" :items="breeds" :search="search">
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteData('breed', item.pk)">mdi-delete</v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import BreedForm from "@/components/breeds/BreedForm.vue";
export default {
  name: "Breeds",
  mixins: [api_mixin],
  components: {
    BreedForm,
  },
  props: {},
  data() {
    return {
      search: "",
      dialog: false,
      editedBreed: null,
      headers: [
        { text: "Type", value: "species" },
        { text: "Breed", value: "breed" },
        { text: "Actions", value: "actions" },
      ],
    };
  },
  mounted() {
    this.getBreeds();
  },
  methods: {
    closeForm: function () {
      this.dialog = false;
      this.editedBreed = null;
      this.getBreeds();
    },
    editItem(item) {
      this.editedBreed = Object.assign({}, item);
      this.dialog = true;
    },
  },
};
</script>
