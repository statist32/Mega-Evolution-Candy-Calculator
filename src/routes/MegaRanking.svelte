<script>
	import { createEventDispatcher } from 'svelte';

	import allTypes from '../data/allTypes.json';
	import megaEvolutions from '../data/megaEvolutions.json';

	import PokemonCard from './PokemonCard.svelte';
	export let wildEncounters;
	export let backgroundColor;
	export let textColor;
	const dispatch = createEventDispatcher();

	const MEGA_PREVIEW_AMOUNT = 5;

	function getWildEncounterTypes(wildEncounters) {
		return wildEncounters.map((wildEncounter) => wildEncounter.types);
	}
	const wildEncounterTypes = getWildEncounterTypes(wildEncounters, allTypes);

	function affectsWildEncounter(boostedTypes, types) {
		for (const boostedType of boostedTypes) {
			if (types.includes(boostedType)) {
				return true;
			}
		}
		return false;
	}

	function rankMegaEvolutions(wildEncounterTypes, megaEvolutions) {
		let megaEvolutionsRanked = [];
		for (const megaEvolution of megaEvolutions) {
			let counter = 0;
			for (const types of wildEncounterTypes) {
				if (affectsWildEncounter(megaEvolution.boostedTypes, types)) {
					counter += 1;
				}
			}
			megaEvolutionsRanked.push({ ...megaEvolution, affectedAmount: counter });
		}
		megaEvolutionsRanked.sort((a, b) => b.affectedAmount - a.affectedAmount);
		return megaEvolutionsRanked;
	}
	let megaAmountToShow = MEGA_PREVIEW_AMOUNT;
	$: megaEvolutionsRanked = rankMegaEvolutions(wildEncounterTypes, megaEvolutions).slice(
		0,
		megaAmountToShow
	);
	function toggleShowCompleteRanking() {
		megaAmountToShow = megaAmountToShow === MEGA_PREVIEW_AMOUNT ? -1 : MEGA_PREVIEW_AMOUNT;
	}
	function onClickHandler(boostedTypes) {
		dispatch('megaClicked', { types: boostedTypes });
	}
</script>

<div class="mega-ranking-wrapper" style="background-color:{backgroundColor}; color:{textColor};">
	<h2>Candy Boosting Mega Evolutions</h2>
	<div class="mega-ranking">
		{#each megaEvolutionsRanked as megaEvolutionRanked}
			<PokemonCard
				pokemon={megaEvolutionRanked}
				affectedAmount={megaEvolutionRanked.affectedAmount}
				isHighlighted={false}
				highlightColor={textColor}
				on:click={() => onClickHandler(megaEvolutionRanked.boostedTypes)}
			/>
		{/each}
	</div>
	<button
		on:click={toggleShowCompleteRanking}
		style="background-color:{backgroundColor}; color:{textColor}; border-color: {textColor}"
	>
		{megaAmountToShow === MEGA_PREVIEW_AMOUNT ? 'Show all mega evolutions' : 'Show top five'}
	</button>
</div>

<style>
	button {
		outline: none;
		border: 2px solid;
		font-size: 1.5rem;
		border-radius: var(--border-radius);
		min-height: 3rem;
	}
	.mega-ranking-wrapper {
		background-color: backgroundColor;
		border-radius: var(--border-radius);
		padding: 2rem;
		display: flex;
		flex-direction: column;
	}
	.mega-ranking-wrapper > h2 {
		font-size: 1.5rem;
		text-align: center;
	}
	.mega-ranking {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		background-color: textColor;
		border-radius: var(--border-radius);
	}
</style>
