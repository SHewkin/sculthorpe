<template>
  <v-tabs background-color="teal darken-3" show-arrows dark>
    <v-tab>
      <v-icon left>mdi-needle</v-icon>Treatments
    </v-tab>
    <v-tab>
      <v-icon left>mdi-notebook</v-icon>Notes
    </v-tab>

    <v-tab-item>
      <IndividualTreatments :individual="individual" />
    </v-tab-item>
    <v-tab-item>
      <IndividualNotes :individual="individual" />
    </v-tab-item>

    <v-tab-item>notes</v-tab-item>
  </v-tabs>
</template>

<script>
import api_mixin from "@/plugins/api_mixin";
import IndividualTreatments from "@/components/treatments/IndividualTreatments.vue";
import IndividualNotes from "@/components/notes/IndividualNotes.vue";
export default {
  name: "IndividualDetail",
  mixins: [api_mixin],
  components: {
    IndividualTreatments,
    IndividualNotes,
  },
  props: {
    pk: null,
  },
  data() {
    return {
      individual: null,
    };
  },
  mounted() {
    this.getIndividual(this.pk);
  },
  watch: {
    pk() {
      this.getIndividual(this.pk);
    },
  },
};
</script>
