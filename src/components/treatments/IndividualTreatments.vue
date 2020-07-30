<template>
  <v-card>
    <v-card-title>
      Treatments
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on" text fab top x-small>
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </template>
        <IndividualTreatmentForm
          @closeForm="closeForm"
          :treatment="editedTreatment"
          :individual="individual"
        />
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
    <v-data-table :headers="headers" :items="individualTreatments" :search="search">
      <template
        v-slot:item.medication_type="{ item }"
      >{{getObjectDisplay(medicationTypes, item.medication_type, "name")}}</template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteData('treatment', item.pk)">mdi-delete</v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import IndividualTreatmentForm from "@/components/treatments/IndividualTreatmentForm.vue";
export default {
  name: "IndividualTreatments",
  mixins: [api_mixin],
  components: {
    IndividualTreatmentForm,
  },
  props: {
    individual: null,
  },
  data() {
    return {
      search: "",
      dialog: false,
      editedTreatment: null,
      individualTreatments: [],
      headers: [
        { text: "Medication", value: "medication_type" },
        { text: "Amount administered", value: "amount_administered" },
        { text: "Date Administered", value: "date_of_administration" },
        { text: "Actions", value: "actions" },
      ],
    };
  },
  watch: {
    individual: function () {
      this.getIndividualTreatment(this.individual.pk);
    },
  },
  methods: {
    closeForm: function () {
      this.dialog = false;
      this.editedTreatment = null;
    },
    editItem(item) {
      this.editedTreatment = Object.assign({}, item);
      this.dialog = true;
    },
  },
};
</script>
