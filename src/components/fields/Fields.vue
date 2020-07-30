<template>
  <v-card>
    <v-card-title>
      Field
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on" text fab top x-small>
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </template>
        <FieldForm @closeForm="closeForm" :field="editedField" />
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
    <v-data-table :headers="headers" :items="fields" :search="search">
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteData('field', item.pk)">mdi-delete</v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import FieldForm from "@/components/fields/FieldForm.vue";
export default {
  name: "fields",
  mixins: [api_mixin],
  components: {
    FieldForm,
  },
  props: {},
  data() {
    return {
      search: "",
      dialog: false,
      editedField: null,
      headers: [
        { text: "Name", value: "name" },
        { text: "Actions", value: "actions" },
      ],
    };
  },
  mounted() {
  },
  methods: {
    closeForm: function () {
      this.dialog = false;
      this.editedField = null;
      this.getFields();
    },
    editItem(item) {
      this.editedField = Object.assign({}, item);
      this.dialog = true;
    },
  },
};
</script>
