<template>
	<div>
		<label :for="id" class="w-hit block text-sm font-medium text-gray-700">{{ label }}</label>

		<div class="flex flex-col items-start lg:items-center lg:flex-row">
			<input
				:id="id"
				:name="id"
				:value="modelValue"
				type="checkbox"
				class="focus:ring-indigo-500 focus:border-indigo-500 block border-gray-300 rounded-md"
				@change="$emit('update:modelValue', $event.target.checked)"
			/>
		</div>
	</div>
</template>

<script setup>
import { defineEmits, defineProps } from "vue";

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
	modelValue: {
		type: Boolean,
		default: false,
	},
});
</script>
