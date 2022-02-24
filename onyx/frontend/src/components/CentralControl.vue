<template>
  <div class="h-full">
    <TabGroup>
      <!-- Tabs -->
      <div
        class="max-w-7xl mx-auto py-3 px-4 lg:px-6 lg:px-8 flex lg:space-x-4 justify-center lg:items-stretch lg:justify-start"
      >
        <TabList class="max-w-7xl py-2 max-auto space-x-4 text-gray-200">
          <Tab
            v-for="tab in tabs"
            :key="tab.id"
            v-slot="{ selected }"
            as="template"
          >
            <button
              :class="[selected ? 'underline text-white font-semibold' : '']"
            >
              {{ tab.title }}
            </button>
          </Tab>
        </TabList>
      </div>

      <!-- Inputs/ Panels -->
      <div
        class="flex flex-col space-y-4 lg:flex-row max-w-7xl mx-auto pb-6 px-4 sm:px-6 lg:space-y-0 lg:space-x-4 justify-start h-fit"
      >
        <div class="lg:w-9/12 p-6 bg-white rounded-md shadow">
          <div class="grid grid-cols-1 h-full">
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
              class="bg-violet-800 text-gray-100 rounded h-10 w-full place-self-end lg:w-1/4"
            >
              Generate Code
            </button>
          </div>
        </div>
        <div class="lg:w-3/12 p-6 bg-white rounded-md shadow">
          <div class="flex flex-col items-center">
            <img :src="image" alt="qr-code" />
            <button
              @click="downloadImage"
              class="bg-violet-800 text-gray-100 rounded h-10 w-full"
            >
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
import { inject, ref } from "vue";

// Props
defineProps(["tabs"]);

// Constants
const logger = inject("vuejs3-logger");
const image = ref("default_code.jpg");
const plainTextValue = ref("");
const apiEndpoint = ref("");

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
  fetchOptions("config/onyx.json");

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
</script>

<style scoped></style>
