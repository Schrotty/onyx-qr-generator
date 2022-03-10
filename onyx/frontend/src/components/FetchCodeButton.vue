<template>
  <button
    class="bg-violet-800 text-gray-100 rounded h-10 w-full mt-3 place-self-end lg:w-1/4"
		@click="fetchCode(payload, persistence)">
    Generate Code
  </button>
</template>

<script setup>

import { data, hexToRgb } from "../data";
import axios from "axios";

defineProps({
	payload: {
		type: String,
		default: "-1",
	},
	persistence: {
		type: Boolean,
		default: false
	}
});

async function fetchCode(payload, persistence) {
	let image = "default_code.jpg";
	await fetchOptions("/config/onyx.json").then(async (endpoints) => {
		console.debug("Endpoint (Static): " + endpoints["static_endpoint"]);
		console.debug("Endpoint (Persistence): " + endpoints.persistence_endpoint);

		// convert colors
		const bc = hexToRgb(data.qrBackColor);
		const fc = hexToRgb(data.qrFillColor);

		// build request data
		const requestData = {
			payload: payload,
			style: {
				qr_size: data.qrSize,
				qr_code_style: data.qrStyle,
				qr_border_size: data.qrBorderSize,
				qr_background_color: {
					red: bc.r,
					green: bc.g,
					blue: bc.b,
				},
				qr_code_color: {
					red: fc.r,
					green: fc.g,
					blue: fc.b,
				},
			},
		};

		// determine which endpoint to use
		const endpoint = persistence ? endpoints.persistence_endpoint : endpoints.static_endpoint;
		if (persistence) {
			requestData["mime_type"] = "plain/text";
		}

		console.debug("Request with data: ");
		console.debug(requestData);
		await axios
			.post(endpoint, requestData)
			.then((response) => {
				console.debug("Received data:");
				console.debug(response);

				const tmp = response.data["image"];

				if (tmp !== null) {
					image = tmp;
				}
			})
			.catch(function (error) {
				if (error.response) {
					console.error(error.response);
				}
			});
	});

	console.debug(image);
	document.getElementById("generated-qr-code").src = image;
}

async function fetchOptions(url) {
	await fetch(url)
		.then(async (response) => {
			console.debug(response.ok);
			if (response.ok) {
				const data = await response.json();

				return {
					static_endpoint: data["api-endpoint-static"],
					persistence_endpoint: data["api-endpoint-persistence"]
				};
			}
		})
		.catch((error) => {
			console.error(error);
			console.debug("Fallback to default endpoints!");
		});

	return {
		static_endpoint: "/api/static",
		persistence_endpoint: "/api/persistence"
	};
}
</script>
