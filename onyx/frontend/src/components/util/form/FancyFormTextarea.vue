<template>
  <div>
		<label :for="id" class="block text-sm font-medium text-gray-700">{{ label }}</label>

		<div class="flex flex-col mt-1 lg:flex-row">
    <textarea
			:id="id"
			:name="id"
			:value="modelValue"
			rows="5"
			class="focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md shadow-sm"
			:placeholder="placeholder"
			@input="$emit('update:modelValue', $event.target.value)"
		/>

			<slot></slot>
		</div>
	</div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";

defineEmits(["update:modelValue"]);
defineProps({
	id: {
		type: String,
		default: "",
		required: true,
	},
	label: {
		type: String,
		default: "",
	},
	placeholder: {
		type: String,
		default: "",
	},
	modelValue: {
		type: String,
		default: "",
	},
});
</script>
