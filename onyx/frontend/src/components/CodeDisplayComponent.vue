<template>
  <div class="p-3 bg-white rounded-md shadow h-fit order-last">
    <div class="flex flex-col items-center">
			<img id="generated-qr-code" :src="modelValue" alt="qr-code" class="rounded" />
				<button class="bg-violet-800 text-gray-100 rounded h-10 w-full mt-3" @click="downloadImage">
					Download
				</button>
    </div>
  </div>
</template>

<script setup>
defineProps({
	image: {
		type: String,
		default: "",
	},
	modelValue: {
		type: String,
		default: "default_code.jpg",
	}
});

function downloadImage() {
	const a = document.createElement("a");
	a.href = document.getElementById("generated-qr-code").src;
	a.download = "QR.png";
	a.click();
}
</script>
