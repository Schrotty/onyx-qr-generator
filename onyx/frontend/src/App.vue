<script setup>
import ControlBar from "./components/ControlBar.vue";
import CentralControl from "./components/CentralControl.vue";
import PlainInput from "./components/tabs/TextComponent.vue";
import URLInput from "./components/tabs/URLComponent.vue";
import MailInput from "./components/tabs/MailComponent.vue";
import VCardInput from "./components/tabs/VCardComponent.vue";
import WIFITabComponent from "./components/tabs/WIFIComponent.vue";
import TwitterTabComponent from "./components/tabs/TwitterComponent.vue";

import { markRaw, ref } from "vue";
import {
	Contact,
	Link,
	Mail,
	Twitter,
	Type,
	Wifi,
} from "lucide-vue-next";

const tabs = ref([
	{
		id: 0,
		title: "URL",
		description: "Auf eine Webseite verlinken",
		icon: markRaw(Link),
		component: markRaw(URLInput),
	},
	{
		id: 1,
		title: "Text",
		description: "Einen beliebigen Freitext anzeigen",
		icon: markRaw(Type),
		component: markRaw(PlainInput),
	},
	{
		id: 2,
		title: "E-Mail",
		description: "Eine E-Mail verschicken",
		icon: markRaw(Mail),
		component: markRaw(MailInput),
	},
	/*{
		id: 3,
		title: "VCard",
		description: "Kontaktdaten hinterlegen",
		icon: markRaw(Contact),
		component: markRaw(VCardInput),
	},*/
	{
		id: 4,
		title: "Wifi",
		description: "In ein WLAN einwählen",
		icon: markRaw(Wifi),
		component: markRaw(WIFITabComponent),
	},
	{
		id: 5,
		title: "Twitter",
		description: "Auf einen Twitter Account verlinken",
		icon: markRaw(Twitter),
		component: markRaw(TwitterTabComponent),
	},
]);
</script>

<template>
  <div class="relative top-0 bg-indigo-800 h-1/3 shadow-lg"></div>
  <div class="absolute top-0 h-2/3 w-full">
    <control-bar title="Onyx" subtitle="QR-Generator" />
    <central-control :tabs="tabs" />
  </div>
</template>

<style></style>
