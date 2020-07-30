<template>
  <v-card>
    <v-card-title>
      Add Treatment
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
      <v-autocomplete
        v-model="newTreatment.individual"
        :items="individuals"
        label="Individual"
        item-value="pk"
      >
        <template v-slot:item="{ item }">
          <span>{{item.holding_number}}/{{item.id_number}}: {{item.name}}</span>
        </template>
        <template v-slot:selection="{ item }">
          <span>{{item.holding_number}}/{{item.id_number}}: {{item.name}}</span>
        </template>
      </v-autocomplete>

      <v-autocomplete
        v-model="newTreatment.medication_type"
        :items="medicationTypes"
        label="Medication Administered"
        item-text="name"
        item-value="pk"
      ></v-autocomplete>

      <v-text-field v-model="newTreatment.amount_administered" label="Amount Administered"></v-text-field>

      <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="newTreatment.date_of_administration"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="newTreatment.date_of_administration"
            label="Date Administered"
            prepend-icon="mdi-calendar-month"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="newTreatment.date_of_administration"
          :max="new Date().toISOString().substr(0, 10)"
          min="2000-01-01"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.menu.save(newTreatment.date_of_administration)"
          >OK</v-btn>
        </v-date-picker>
      </v-menu>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeForm">Close</v-btn>
      <v-btn text right color="primary" @click="saveTreatment">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import constants_mixin from "@/plugins/constants_mixin";

export default {
  name: "IndividualTreatmentForm",
  mixins: [api_mixin, constants_mixin],
  props: {
    treatment: null,
    individual: null,
  },
  data() {
    return {
      menu: false,
      newTreatment: {
        medication_type: null,
        amount_administered: null,
        date_of_administration: null,
        individual: null,
      },
    };
  },
  mounted() {
    this.loadInitialData();
  },
  methods: {
    loadInitialData: function () {
      this.newTreatment.individual = this.individual.pk;
      if (this.treatment) {
        this.newTreatment = this.treatment;
      }
    },
    closeForm: function () {
      this.$emit("closeForm");
    },
    saveTreatment: function () {
      if (this.treatment) {
        this.updateData("treatment", this.treatment.pk, this.newTreatment);
      } else {
        this.postData("treatment", this.newTreatment);
      }
    },
  },
};
</script>
