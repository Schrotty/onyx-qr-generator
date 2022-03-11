<template>
  <tab-panel class="grid space-y-3">
    <tab-header :title="desc" />
    <fancy-form-component>
			<fancy-layout-row>
				<template #first>
					<input-component
						id="ssid"
						v-model="ssid"
						label="Netzwerkname"
						placeholder="SSID"
					/>
				</template>

				<template #second>
					<fancy-form-checkbox
						id="hidden"
						v-model="hidden"
						label="Verstecktes Netzwerk"
					/>
				</template>
			</fancy-layout-row>

      <fancy-form-input
        id="pwd"
        v-model="pwd"
        label="Passwort"
        type="password"
      />
      <fancy-form-select
        id="sec"
        v-model="sec"
        label="Verschlüsselung"
        :options="securityOptions"
      />
    </fancy-form-component>

    <fetch-code-button :payload="connectionString" />
  </tab-panel>
</template>

<script setup>
import { TabPanel } from "@headlessui/vue";
import TabHeader from "../util/TabHeader.vue";
import FancyFormComponent from "../util/form/FancyFormComponent.vue";
import FancyFormInput from "../util/form/FancyFormInput.vue";
import FancyFormCheckbox from "../util/form/FancyFormCheckbox.vue";
import FancyFormSelect from "../util/form/FancyFormSelect.vue";
import { computed, reactive, ref } from "vue";
import FetchCodeButton from "../FetchCodeButton.vue";
import InputComponent from "../util/form/inline/InputComponent.vue";
import FancyLayoutRow from "../util/form/layout/FancyLayoutRow.vue";

defineProps({
	desc: {
		type: String,
		default: "",
	},
});

const securityOptions = reactive([
	{ name: "WEP", value: "WEP" },
	{ name: "WPA", value: "WPA" },
	{ name: "WPA2-EAP", value: "WPA2-EAP", default: true },
	{ name: "None", value: "nopass" },
]);

const ssid = ref("");
const hidden = ref(false);
const pwd = ref("");
const sec = ref(securityOptions[2].name);

const connectionString = computed(() => {
	return (
		"WIFI:T:" +
    sec.value +
    ";S:" +
    encodeURIComponent(ssid.value) +
    ";P:" +
    encodeURIComponent(pwd.value) +
    ";H:" +
    hidden.value +
    ";"
	);
});
</script>
