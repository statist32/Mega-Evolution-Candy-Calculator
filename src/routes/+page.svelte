<script>
	import EventTile from './EventTile.svelte';
	import events from '../data/events.json';
	let showIntro = false

	function toggleShowIntro(){
		showIntro = !showIntro
	}

	function compareEventDateString(a, b, order = 1) {
		const aUTC = Date.parse(a.startDate);
		const bUTC = Date.parse(b.startDate);
		return order * (aUTC - bUTC);
	}
	function getCurrentDate() {
		return new Date();
	}
	function isCurrentEvent(event) {
		const startDate = Date.parse(event.startDate);
		const endDate = Date.parse(event.endDate);
		const currentDate = getCurrentDate();
		return startDate <= currentDate && currentDate <= endDate;
	}
	function isFutureEvent(event) {
		const startDate = Date.parse(event.startDate);
		const currentDate = getCurrentDate();
		return startDate > currentDate;
	}
	function isPastEvent(event) {
		const endDate = Date.parse(event.endDate);
		const currentDate = getCurrentDate();
		return endDate < currentDate;
	}
	const currentEvents = events
		.filter((event) => isCurrentEvent(event))
		.sort((a, b) => compareEventDateString(a, b, -1));
	const futureEvents = events
		.filter((event) => isFutureEvent(event))
		.sort((a, b) => compareEventDateString(a, b));
	const pastEvents = events
		.filter((event) => isPastEvent(event))
		.sort((a, b) => compareEventDateString(a, b, -1));
</script>

<svelte:head>
	<title>Mega Evolution Candy Calculatorr</title>
	<meta name="Mega Evolution Candy Calculatorr" content="Mega Evolution Candy Calculator" />
</svelte:head>

{#if showIntro}
	<section class="introduction">
		<h2>Ready to boost your candy gains?</h2>
		<p>
			Discover the ultimate mega evolutions that will supercharge your candy collection. Say goodbye
			to guesswork and hello to optimized gameplay. Let's maximize those sweet rewards together!
		</p>
		<p class="explanation">
			The number in the white bubble is the amount of affected Pokemon by the respective mega
			evolution. To gain the maximum candy boost just chose the mega evolution with the highest
			number. You can click on the mega evolution to highlight the affected Pokemon.
		</p>
	</section>
{/if}
<button
	on:click={toggleShowIntro}
	>
	{showIntro ? 'Hide Introduction' : 'Show Introduction'}
</button>

<h2>Current Events</h2>
{#each currentEvents as event}
	<EventTile {event} isOpen={true} />
{/each}
<h2>Future Events</h2>
{#each futureEvents as event}
	<EventTile {event} isOpen={false} />
{/each}
<h2>Past Events</h2>
{#each pastEvents as event}
	<EventTile {event} isOpen={false} />
{/each}

<style>
	h2 {
		font-size: 2rem;
		font-weight: bold;
		text-align: center;
	}
	.introduction {
		font-size: 1.5rem;
		margin: 3rem;
	}
	.explanation {
		font-size: 1.5rem;
	}
	button {
		outline: none;
		border: 2px solid;
		font-size: 1.5rem;
		border-radius: var(--border-radius);
		min-height: 3rem;
	}
</style>
