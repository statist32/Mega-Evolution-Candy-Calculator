<script>
	import PokemonCard from './PokemonCard.svelte';
	export let wildEncounters;
	export let backgroundColor;
	export let textColor;
	export let boostedTypes = [];
</script>

<div class="wild-encounter-wrapper" style="background-color:{backgroundColor}; color:{textColor};">
	<h2>Wild Encounters</h2>
	<div class="wild-encounter">
		{#each wildEncounters as wildEncounter}
			<PokemonCard
				pokemon={wildEncounter}
				affectedAmount={undefined}
				isHighlighted={boostedTypes?.filter((boostedType) =>
					wildEncounter.types.includes(boostedType)
				).length}
				textColor={textColor}
			/>
		{/each}
	</div>
</div>

<style>
	.wild-encounter-wrapper {
		border-radius: var(--border-radius);
		padding: 2rem;
		margin-top: 3rem;
	}
	h2 {
		font-size: 1.5rem;
		text-align: center;
	}
	.wild-encounter {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		border-radius: var(--border-radius);
	}
</style>
