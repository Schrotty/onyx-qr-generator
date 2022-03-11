<template>
  <div>
		<label :for="id" class="block text-sm font-medium text-gray-700">{{ label }}</label>

		<input
			:id="id"
			:name="id"
			:value="modelValue"
			type="number"
			:min="min"
			:max="max"
			class="focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md shadow-sm"
			:placeholder="placeholder"
			@input="$emit('update:modelValue', $event.target.value)"
		/>
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
	min: {
		type: Number,
		default: 0
	},
	max: {
		type: Number,
		default: 100
	},
	modelValue: {
		type: String,
		default: "",
	}
});
</script>
