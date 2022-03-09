<template>
  <div class="h-full">
    <tab-group>
      <!-- Inputs/ Panels -->
      <div class="flex flex-col max-w-7xl mx-auto pb-6 px-6 lg:flex-row lg:flex-wrap">
        <!-- Navigation -->
        <div class="w-full justify-center mb-3 lg:items-stretch lg:justify-start">
          <TabList class="p-2 space-x-3 text-black w-full bg-white rounded-md text-center lg:text-left">
            <Tab
              v-for="tab in tabs"
              :key="tab.id"
              v-slot="{ selected }"
              as="template">

              <button class="rounded py-1 px-6 h-9 hover:bg-gray-100"
                :class="[
                  selected
                    ? 'text-indigo-800 bg-indigo-100 hover:bg-indigo-100/50'
                    : '',
                ]">

                <div class="flex flex-row items-center space-x-2">
                  <component
                    :is="tab.icon"
                    :size="24"
                    :class="[
                      selected ? 'stroke-indigo-700' : 'stroke-gray-600',
                    ]" />
                  <span>{{ tab.title }}</span>
                </div>
              </button>
            </Tab>
          </TabList>
        </div>

        <!-- Tabs -->
        <div class="w-full mb-3 lg:w-9/12 lg:base-9/12 lg:pr-1.5 lg:max-h-12 lg:overflow-visible">
          <div class="bg-white rounded-md shadow h-fit col-span-9">
            <div class="grid grid-cols-1 h-fit p-3">
              <TabPanels>
                <component
                  :is="tab.component"
                  v-for="tab in tabs"
                  :key="tab.id"
                  :desc="tab.description" />
							</TabPanels>
            </div>
          </div>
        </div>

        <!-- QR Code -->
        <div class="w-full lg:w-3/12 order-last lg:base-3/12 lg:pl-1.5 lg:order-none lg:mb-3">
          <code-display-component />
        </div>

        <!-- Spacer -->
        <div class="w-full lg:w-9/12 lg:base-9/12 lg:pr-1.5"></div>

        <!-- Options -->
        <div class="w-full mb-3 lg:w-3/12 lg:base-3/12 lg:pl-1.5">
          <options-panel />
        </div>
      </div>
    </tab-group>
  </div>
</template>

<script setup>
import { TabGroup, TabList, Tab, TabPanels } from "@headlessui/vue";
import OptionsPanel from "./OptionsPanel.vue";
import CodeDisplayComponent from "./CodeDisplayComponent.vue";

// Properties
defineProps({
	tabs: {
		type: Array,
		default() {
			return [];
		},
	},
});
</script>
