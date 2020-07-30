<template>
  <v-card>
    <v-card-title>
      Notes
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="primary" dark v-bind="attrs" v-on="on" text fab top x-small>
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </template>
        <IndividualNoteForm @closeForm="closeForm" :note="editedNote" :individual="individual" />
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
    <v-data-table :headers="headers" :items="individualNotes" :search="search">
      <template v-slot:item.note="{ item }">
        <pre>{{item.note}}</pre>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteData('note', item.pk)">mdi-delete</v-icon>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import IndividualNoteForm from "@/components/notes/IndividualNoteForm.vue";
export default {
  name: "IndividualNotes",
  mixins: [api_mixin],
  components: {
    IndividualNoteForm,
  },
  props: {
    individual: null,
  },
  data() {
    return {
      search: "",
      dialog: false,
      editedNote: null,
      individualNotes: [],
      headers: [{ text: "Note", value: "note" }],
    };
  },
  mounted() {
    this.getIndividualNote(this.individual.pk);
  },
  watch: {
    individual: function () {
      this.getIndividualNote(this.individual.pk);
    },
  },
  methods: {
    closeForm: function () {
      this.dialog = false;
      this.editedNote = null;
    },
    editItem(item) {
      this.editedNote = Object.assign({}, item);
      this.dialog = true;
    },
  },
};
</script>
