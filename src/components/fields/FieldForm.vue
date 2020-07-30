<template>
  <v-card>
    <v-card-title>
      Add Field
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
      <v-text-field v-model="newField.name" label="Name"></v-text-field>

      <v-textarea
        v-model="newField.description"
        label="Description / Notes"
        auto-grow
        filled
      ></v-textarea>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeForm">Close</v-btn>
      <v-btn text right color="primary" @click="saveField">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import constants_mixin from "@/plugins/constants_mixin";

export default {
  name: "FieldForm",
  mixins: [api_mixin, constants_mixin],
  props: {
    field: null,
  },
  data() {
    return {
      menu: false,
      newField: {
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
      if (this.field) {
        this.newField = this.field;
      }
    },
    closeForm: function () {
      this.$emit("closeForm");
    },
    saveField: function () {
      if (this.field) {
        this.updateData("field", this.field.pk, this.newField);
      } else {
        this.postData("field", this.newField);
      }
    },
  },
};
</script>
