<script>
	import WildEncounters from './WildEncounters.svelte';
	import MegaRanking from './MegaRanking.svelte';
	export let event;
	export let isOpen = true;

	let showRankingAndEncounters = isOpen;
	function toggleShowRankingAndEncounters() {
		showRankingAndEncounters = !showRankingAndEncounters;
	}
	$: boostedTypes = [];
	function handleMegaClicked(event) {
		boostedTypes = event.detail.types;
	}
</script>

<section
	class="event-tile"
	style="background-color: {event.backgroundColor}; color: {event.textColor};"
>
	<div class="general-event-information">
		<h2>{event.name}</h2>
		<div class="event-dates">
			<h3>Starting: {event.startDate}</h3>
			<h3>Ending: {event.endDate}</h3>
		</div>
	</div>
	{#if showRankingAndEncounters}
		<MegaRanking
			wildEncounters={event.wildEncounters}
			backgroundColor={event.tileBackgroundColor}
			textColor={event.tileTextColor}
			on:megaClicked={handleMegaClicked}
		/>
		<WildEncounters
			wildEncounters={event.wildEncounters}
			backgroundColor={event.tileBackgroundColor}
			textColor={event.tileTextColor}
			{boostedTypes}
		/>
	{/if}
	<div class="button-wrapper">
		<button
			on:click={toggleShowRankingAndEncounters}
			style="background-color:{event.tileBackgroundColor}; color:{event.tileTextColor}; border-color:{event.tileBackgroundColor} "
		>
			{showRankingAndEncounters ? 'Hide ranking and encounters' : 'Show ranking and encounters'}
		</button>
	</div>
</section>

<style>
	.event-tile {
		padding: 2rem;
		border-radius: var(--border-radius);
		margin-bottom: 3rem;
	}
	h2 {
		font-size: 2rem;
		text-align: center;
	}
	.event-dates {
		display: flex;
		justify-content: space-around;
		flex-wrap: wrap;
	}
	.button-wrapper {
		display: flex;
		justify-content: center;
	}
	button {
		outline: none;
		border: 2px solid;
		font-size: 1.5rem;
		border-radius: var(--border-radius);
		min-height: 3rem;
		margin-top: 2rem;
	}
	@media (max-width: 500px) {
		.event-tile {
			padding-left: 0.5rem;
			padding-right: 0.5rem;
		}
	}
</style>
