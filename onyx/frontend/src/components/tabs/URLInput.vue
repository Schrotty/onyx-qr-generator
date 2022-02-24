<template>
  <TabPanel>
    <div class="flex items-center space-x-6">
      <label class="block w-full h-full">
        <span>URL:</span>
        <input
          :value="modelValue"
          @input="$emit('update:modelValue', $event.target.value)"
          type="url"
          class="w-full h-full my-4"
          placeholder="https://wikipedia.org"
        />
      </label>
    </div>
  </TabPanel>
</template>

<script setup>
import { TabPanel } from "@headlessui/vue";

defineProps(["modelValue"]);
defineEmits(["update:modelValue"]);
</script>

<style scoped></style>
