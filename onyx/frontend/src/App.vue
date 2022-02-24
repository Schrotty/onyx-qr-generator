<script setup>
import ControlBar from "./components/ControlBar.vue";
import CentralControl from "./components/CentralControl.vue";
import PlainInput from "./components/tabs/PlainInput.vue";
import URLInput from "./components/tabs/URLInput.vue";

import { markRaw, ref } from "vue";

const tabs = ref([
  { id: 0, title: "Freitext", component: markRaw(PlainInput) },
  { id: 1, title: "URL", component: markRaw(URLInput) },
]);
</script>

<template>
  <div class="relative top-0 bg-indigo-800 h-1/3 shadow-lg"></div>
  <div class="absolute top-0 h-2/3 w-full">
    <ControlBar title="Onyx" subtitle="QR-Generator" />
    <CentralControl :tabs="tabs" />
  </div>
</template>

<style></style>
