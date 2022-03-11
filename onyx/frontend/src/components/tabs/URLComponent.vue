<template>
  <tab-panel class="grid space-y-3">
    <tab-header :title="desc" />

    <fancy-form-component>
      <fancy-form-input
        id="url"
        v-model="url"
        label="URL"
        placeholder="https://wikipedia.org"
      />
    </fancy-form-component>

    <fetch-code-button :payload="url" />
  </tab-panel>
</template>

<script setup>
import { TabPanel } from "@headlessui/vue";
import TabHeader from "../util/TabHeader.vue";
import FancyFormComponent from "../util/form/FancyFormComponent.vue";
import FancyFormInput from "../util/form/FancyFormInput.vue";
import { ref } from "vue";
import FetchCodeButton from "../FetchCodeButton.vue";

defineProps({
	desc: {
		type: String,
		default: "",
	},
	qr: {
		type: String,
		default: ""
	}
});

const url = ref("");
</script>
