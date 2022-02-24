<template>
  <TabPanel>
    <div class="flex items-center space-x-6">
      <label class="block w-full h-full">
        <span>Freitext:</span>
        <textarea
          :value="modelValue"
          @input="$emit('update:modelValue', $event.target.value)"
          rows="5"
          type="text"
          class="w-full h-full my-4"
          placeholder="Lorem Ipsum"
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
