<template>
  <tab-panel class="grid space-y-3">
    <tab-header :title="desc" />
    <fancy-form-component>
      <fancy-form-input
        id="mail"
        v-model="mail"
        label="E-Mail"
        placeholder="E-Mail Adresse"
      />

      <fancy-form-input
        id="subject"
        v-model="subject"
        label="Betreff"
        placeholder="Betreff"
      />

      <fancy-form-textarea
        id="content"
        v-model="content"
        label="Inhalt"
        placeholder="Ihr Nachrichtentext"
      />
    </fancy-form-component>

    <fetch-code-button :payload="mailString" />
  </tab-panel>
</template>

<script setup>
import { computed, ref } from "vue";
import { TabPanel } from "@headlessui/vue";
import TabHeader from "../util/TabHeader.vue";
import FancyFormComponent from "../util/form/FancyFormComponent.vue";
import FancyFormInput from "../util/form/FancyFormInput.vue";
import FancyFormTextarea from "../util/form/FancyFormTextarea.vue";
import FetchCodeButton from "../FetchCodeButton.vue";

defineProps({
	desc: {
		type: String,
		default: "",
	},
});

const mail = ref("");
const subject = ref("");
const content = ref("");

const mailString = computed(() => {
	return (
		"mailto:" +
    mail.value +
    "?subject=" +
    encodeURIComponent(subject.value) +
    "&body=" +
    encodeURIComponent(content.value)
	);
});
</script>
