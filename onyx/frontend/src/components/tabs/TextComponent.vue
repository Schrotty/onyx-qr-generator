<template>
  <tab-panel class="grid space-y-3">
    <tab-header :title="desc" />
    <fancy-form-component>
      <fancy-form-textarea
        id="text"
        v-model="text"
        label="Freitext"
        placeholder="Lorem Ipsum..."
      />
    </fancy-form-component>

    <fetch-code-button :payload="text" :persistence="true" />
  </tab-panel>
</template>

<script setup>
import { TabPanel } from "@headlessui/vue";
import TabHeader from "../util/TabHeader.vue";
import FancyFormComponent from "../util/form/FancyFormComponent.vue";
import FancyFormTextarea from "../util/form/FancyFormTextarea.vue";
import FetchCodeButton from "../FetchCodeButton.vue";
import { ref } from "vue";

defineProps({
	desc: {
		type: String,
		default: "",
	},
});

const text = ref("");
</script>

<style scoped></style>
