<script>
	import EventTile from './EventTile.svelte';
	import events from '../data/events.json';
</script>

<svelte:head>
	<title>Mega Evolution Candy Calculatorr</title>
	<meta name="Mega Evolution Candy Calculatorr" content="Mega Evolution Candy Calculator" />
</svelte:head>

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

{#each events.reverse() as event, i}
	<EventTile {event} isOpen={i === 0} />
{/each}

<style>
	h2 {
		font-size: 2rem;
		font-weight: bold;
	}
	.introduction {
		font-size: 1.5rem;
		margin: 3rem;
	}
	.explanation {
		font-size: 1.5rem;
	}
</style>
