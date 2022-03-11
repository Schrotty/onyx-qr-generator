<template>
  <tab-panel class="grid space-y-3">
    <tab-header :title="desc" />
    <fancy-form-component>
      <fancy-form-select
        id="title"
        v-model="title"
        label="Anrede"
        :options="titleOptions"
      />

      <fancy-form-inline>
        <template #fir>
          <fancy-inline-input
            id="surname"
            v-model="surname"
            label="Vorname"
            placeholder="Vorname"
          />
        </template>

        <template #sec>
          <fancy-inline-input
            id="name"
            v-model="name"
            label="Nachname"
            placeholder="Nachname"
          />
        </template>
      </fancy-form-inline>
    </fancy-form-component>

    <fetch-code-button :payload="cardString" />
  </tab-panel>
</template>

<script setup>
import { TabPanel } from "@headlessui/vue";
import TabHeader from "../util/TabHeader.vue";
import FancyFormComponent from "../util/form/FancyFormComponent.vue";
import FancyFormSelect from "../util/form/FancyFormSelect.vue";
import FancyFormInline from "../util/form/FancyFormInline.vue";
import FancyInlineInput from "../util/form/inline/InputComponent.vue";
import FetchCodeButton from "../FetchCodeButton.vue";
import { computed, ref } from "vue";

defineProps({
	desc: {
		type: String,
		default: "",
	},
});

const title = ref("");
const surname = ref("");
const name = ref("");

const cardString = computed(() => {
	return "BEGIN:VCARD" + "VERSION:4.0" + "END:VCARD";
});
</script>
