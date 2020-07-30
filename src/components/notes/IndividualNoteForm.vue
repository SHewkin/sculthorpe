<template>
  <v-card>
    <v-card-title>
      Add Treatment
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
      <v-autocomplete
        v-model="newNote.individual"
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

      <v-textarea v-model="newNote.note" label="Notes" auto-grow filled></v-textarea>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="closeForm">Close</v-btn>
      <v-btn text right color="primary" @click="saveNote">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import constants_mixin from "@/plugins/constants_mixin";

export default {
  name: "IndividualNoteForm",
  mixins: [api_mixin, constants_mixin],
  props: {
    note: null,
    individual: null,
  },
  data() {
    return {
      menu: false,
      newNote: {
        individual: null,
        note: null,
      },
    };
  },
  mounted() {
    this.loadInitialData();
  },
  methods: {
    loadInitialData: function () {
      this.newNote.individual = this.individual.pk;
      if (this.note) {
        this.newNote = this.note;
      }
    },
    closeForm: function () {
      this.$emit("closeForm");
    },
    saveNote: function () {
      if (this.note) {
        this.updateData("note", this.note.pk, this.newNote);
      } else {
        this.postData("note", this.newNote);
      }
    },
  },
};
</script>
