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
        <MedicationTypeForm @closeForm="closeForm" :medication_type="editedMedicationType" />
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
    <v-data-table :headers="headers" :items="medicationTypes" :search="search">
      <template v-slot:item.description="{ item }">
        <span style="white-space: pre;">{{item.description}}</span>
      </template>

      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteData('medication_type', item.pk)">mdi-delete</v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import MedicationTypeForm from "@/components/medications/MedicationTypeForm.vue";
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
      editedMedicationType: null,
      headers: [
        { text: "Name", value: "name" },
        { text: "Description / Notes", value: "description" },
        { text: "Actions", value: "actions" },
      ],
    };
  },
  methods: {
    closeForm: function () {
      this.dialog = false;
      this.editedMedicationType = null;
      this.getMedicationTypes();
    },

    editItem(item) {
      this.editedMedicationType = Object.assign({}, item);
      this.dialog = true;
    },
  },
};
</script>
