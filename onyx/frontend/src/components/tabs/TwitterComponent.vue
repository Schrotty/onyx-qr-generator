<template>
  <tab-panel class="grid space-y-3">
    <tab-header :title="desc" />

    <fancy-form-component>
      <fancy-form-input
        id="url"
        v-model="url"
        label="Username"
        placeholder="@Wikipedia"
      />
    </fancy-form-component>

    <fetch-code-button :payload="twitterString" />
  </tab-panel>
</template>

<script setup>
import { TabPanel } from "@headlessui/vue";
import TabHeader from "../util/TabHeader.vue";
import FancyFormComponent from "../util/form/FancyFormComponent.vue";
import FancyFormInput from "../util/form/FancyFormInput.vue";
import FetchCodeButton from "../FetchCodeButton.vue";
import { computed, ref } from "vue";

defineProps({
	desc: {
		type: String,
		default: "",
	},
});

const url = ref("");
const twitterString = computed(() => {
	return "https://twitter.com/" + url.value;
});
</script>
