<template>
  <div class="h-full">
    <TabGroup>
      <!-- Tabs -->
      <div class="max-w-7xl mx-auto py-t-3 px-6 flex lg:space-x-4 justify-center lg:items-stretch lg:justify-start">
        <TabList class="max-w-7xl p-2 my-4 max-auto space-x-2 text-black w-full bg-white rounded text-center lg:text-left">
          <Tab
            v-for="tab in tabs"
            :key="tab.id"
            v-slot="{ selected }"
            as="template">
            <button
              class="rounded py-1 px-6"
              :class="[selected ? 'font-bold text-indigo-800 bg-indigo-100' : '']">
              <div class="flex flex-row items-center space-x-2">
                <component
                  :is="tab.icon"
                  :size="24"
                  :class="[selected ? 'stroke-indigo-700' : 'stroke-gray-600']"
                />
                <span>{{ tab.title }}</span>
              </div>
            </button>
          </Tab>
        </TabList>
      </div>

      <!--<div class="max-w-7xl mx-auto py-t-3 px-4 lg:px-6 flex lg:space-x-4 justify-center lg:items-stretch lg:justify-start">
        <TabList class="max-w-7xl pt-2 max-auto space-x-2 text-black w-full">
          <Tab
            v-for="tab in tabs"
            :key="tab.id"
            v-slot="{ selected }"
            as="template">
            <button
              class="rounded-t py-1 px-6"
              :class="[selected ? 'underline text-red font-semibold bg-white' : 'bg-gray-200']">
              {{ tab.title }}
            </button>
          </Tab>
        </TabList>
      </div>-->

      <!-- Inputs/ Panels -->
      <div class="flex flex-col max-w-7xl space-y-4 mx-auto pb-6 px-6 justify-start h-fit lg:flex-row lg:space-y-0 lg:space-x-4">
        <div class="lg:w-9/12 p-6 bg-white rounded shadow">
          <div class="grid grid-cols-1 h-full space-y-4">
            <TabPanels>
              <component
                :is="tab.component"
                v-model="plainTextValue"
                v-for="tab in tabs"
                :key="tab.id"
              ></component>
            </TabPanels>

            <button
              @click="fetchImage"
              class="bg-violet-800 text-gray-100 rounded h-10 w-full place-self-end lg:w-1/4">
              Generate Code
            </button>
          </div>
        </div>

        <!-- QR Code -->
        <div class="lg:w-3/12 p-6 bg-white rounded-md shadow">
          <div class="flex flex-col items-center">
            <img :src="image" alt="qr-code" />
            <button
              @click="downloadImage"
              class="bg-violet-800 text-gray-100 rounded h-10 w-full">
              Download
            </button>
          </div>
        </div>
      </div>
    </TabGroup>
  </div>
</template>

<script setup>
import { TabGroup, TabList, Tab, TabPanels } from "@headlessui/vue";
import axios from "axios";
import { inject, onMounted, ref } from "vue";

// Props
defineProps(["tabs"]);

// Constants
const logger = inject("vuejs3-logger");
const image = ref("default_code.jpg");
const plainTextValue = ref("");
const apiEndpoint = ref("/api/static");

// Functions
async function fetchOptions(url) {
  await fetch(url)
    .then(async (response) => {
      const data = await response.json();

      if (!response.ok) {
        return Promise.reject((data && data.message) || response.statusText);
      }

      apiEndpoint.value = data["api-endpoint"];
      logger.debug(apiEndpoint.value);
    })
    .catch((error) => {
      logger.error(error);
    });
}

function downloadImage() {
  const a = document.createElement("a");
  a.href = image.value;
  a.download = "code.png";
  a.click();
}

function fetchImage() {
  fetchOptions("/config/onyx.json");

  axios
    .post(apiEndpoint.value, {
      payload: plainTextValue.value,
    })
    .then((response) => {
      logger.debug(response.data);
      image.value = response.data["image"]["image"];
    })
    .catch((error) => {
      logger.error(error);
    });
}

// Lifecycle Event Listener
onMounted(() => {
  fetchOptions("/config/onyx.json");
});
</script>

<style scoped></style>
