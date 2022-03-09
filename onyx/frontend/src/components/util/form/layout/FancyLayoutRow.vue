<template>
	<div class="flex flex-row w-full mt-1 space-x-3 lg:flex-row">
		<div class="w-9/12">
			<slot name="first" />
		</div>
		<div class="w-3/12">
			<slot name="second" />
		</div>
	</div>
</template>