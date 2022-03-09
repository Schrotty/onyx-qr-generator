<template>
  <h2 class="font-bold text-lg text-slate-900">{{ title }}</h2>
</template>

<script setup>
defineProps({
	title: {
		type: String,
		default: ""
	}
});
</script>
