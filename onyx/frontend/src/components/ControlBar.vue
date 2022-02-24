<template>
  <Disclosure as="nav">
    <div class="max-w-7xl mx-auto px-4 lg:px-6 lg:px-8 border-b border-gray-600">
      <div class="flex items-center justify-between h-16">
        <div class="flex-1 flex items-center justify-center lg:items-stretch lg:justify-start">
          <div class="flex-shrink-0 flex items-baseline">
            <h1 class="text-gray-50">{{ title }}</h1>
            <span class="px-2 text-green-50">{{ subtitle }}</span>
          </div>
        </div>
      </div>
    </div>
  </Disclosure>
</template>

<script setup>
import { Disclosure } from "@headlessui/vue";

defineProps(["title", "subtitle"]);
</script>

<style scoped></style>
