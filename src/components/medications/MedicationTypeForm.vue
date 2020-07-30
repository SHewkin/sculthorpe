<template>
  <v-card>
    <v-card-title>
      Add Medication Type
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
      <v-text-field v-model="newMedicationType.name" label="Medication Name"></v-text-field>
      <v-textarea
        v-model="newMedicationType.description"
        label="Description / Notes"
        auto-grow
        filled
      ></v-textarea>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeForm">Close</v-btn>
      <v-btn text right color="primary" @click="saveMedicationType">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import constants_mixin from "@/plugins/constants_mixin";

export default {
  name: "MedicationTypeForm",
  mixins: [api_mixin, constants_mixin],
  props: {
    medication_type: null,
  },
  data() {
    return {
      menu: false,
      newMedicationType: {
        name: null,
        description: null,
      },
    };
  },
  mounted() {
    this.loadInitialData();
  },
  methods: {
    loadInitialData: function () {
      if (this.medication_type) {
        this.newMedicationType = this.medication_type;
      }
    },
    closeForm: function () {
      this.$emit("closeForm");
    },
    saveMedicationType: function () {
      if (this.medication_type) {
        this.updateData(
          "medication_type",
          this.medication_type.pk,
          this.newMedicationType
        );
      } else {
        this.postData("medication_type", this.newMedicationType);
      }
    },
  },
};
</script>
