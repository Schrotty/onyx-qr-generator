<script setup>
import ControlBar from "./components/ControlBar.vue";
import CentralControl from "./components/CentralControl.vue";
import PlainInput from "./components/tabs/PlainInput.vue";
import URLInput from "./components/tabs/URLInput.vue";

import { markRaw, ref } from "vue";
import { Facebook, Instagram, Link, Mail, Twitter, Type} from "lucide-vue-next";

const tabs = ref([
  { id: 0, title: "URL", icon: markRaw(Link), component: markRaw(URLInput) },
  { id: 1, title: "Text", icon: markRaw(Type), component: markRaw(PlainInput) },
  { id: 2, title: "Twitter", icon: markRaw(Twitter), component: markRaw(URLInput) },
  { id: 3, title: "Facebook", icon: markRaw(Facebook), component: markRaw(PlainInput) },
  { id: 4, title: "Instagram", icon: markRaw(Instagram), component: markRaw(URLInput) },
  { id: 5, title: "E-Mail", icon: markRaw(Mail), component: markRaw(PlainInput) },
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
