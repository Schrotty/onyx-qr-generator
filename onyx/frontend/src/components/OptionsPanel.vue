<template>
  <div class="p-3 bg-white rounded-md shadow h-fit col-start-10 col-span-3 space-y-3 lg:order-last">
    <tab-header title="Design Optionen" />

    <fancy-form-select
      id="style"
      v-model="data.qrStyle"
      label="QR-Style"
      :options="styleOptions"
    />

		<fancy-form-inline>
			<template #fir>
				<fancy-form-number
					id="size"
					v-model="data.qrSize"
					label="QR-Komplexität"
					min="1"
					max="40"
				/>
			</template>

			<template #sec>
				<fancy-form-number
					id="size"
					v-model="data.qrBorderSize"
					label="Rand"
					min="0"
					max="10"
				/>
			</template>
		</fancy-form-inline>

		<fancy-form-inline>
			<template #fir>
				<fancy-form-input
					id="back_color"
					v-model="data.qrBackColor"
					label="Hintergrund"
					type="color"
				/>
			</template>

			<template #sec>
				<fancy-form-input
					id="fill_color"
					v-model="data.qrFillColor"
					label="Vordergrund"
					type="color"
				/>
			</template>
		</fancy-form-inline>
  </div>
</template>

<script setup>
import { data } from "../data";
import TabHeader from "./util/TabHeader.vue";
import FancyFormInput from "./util/form/FancyFormInput.vue";
import FancyFormSelect from "./util/form/FancyFormSelect.vue";
import { reactive } from "vue";
import FancyFormNumber from "./util/form/FancyFormNumber.vue";
import FancyFormInline from "./util/form/FancyFormInline.vue";

const styleOptions = reactive([
	{ name: "Square", value: "square" },
	{ name: "Gaped Square", value: "gaped" },
	{ name: "Circle", value: "circle" },
	{ name: "Round", value: "round" },
	{ name: "Vertical", value: "vertical" },
	{ name: "Horizontal", value: "horizontal" },
]);
</script>
