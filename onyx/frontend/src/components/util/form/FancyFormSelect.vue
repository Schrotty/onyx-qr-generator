<template>
  <div>
		<label :for="id" class="block text-sm font-medium text-gray-700">{{ label }}</label>

		<div class="flex flex-col mt-1 items-start lg:items-center lg:flex-row">
			<select
				:id="id"
				:name="id"
				:value="modelValue"
				class="w-full focus:ring-indigo-500 focus:border-indigo-500 block pr-12 sm:text-sm border-gray-300 rounded-md"
				@change="$emit('update:modelValue', $event.target.value)"
			>
				<option
					v-for="option in options"
					:key="option.name"
					:value="option.value"
				>
					{{ option.name }}
				</option>
			</select>
		</div>
	</div>
</template>

<script setup>
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
		type: String,
		default: "",
	},
	options: {
		type: Array,
		default() {
			return [];
		}
	},
	defaultValue: {
		type: String,
		default: "",
	},
});
</script>
