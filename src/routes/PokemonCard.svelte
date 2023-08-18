<script>
	export let pokemon;
	export let affectedAmount;
	export let isHighlighted;
	export let highlightColor;
	const { name, types, imgUrl } = pokemon;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
	class="pokemon-card"
	on:click
	style={isHighlighted ? `filter: drop-shadow(0rem 0rem 1rem ${highlightColor})` : ''}
>
	<img src={imgUrl} alt="An image of the pokemon {name}" class="pokemon-image" />
	<div>
		<div class="pokemon-name">
			{name}
		</div>
		<div class="pokemon-types">
			{#each types as type}
				<div class="pokemon-type {type.toLowerCase()}">
					{type}
				</div>
			{/each}
		</div>
		{#if !isNaN(affectedAmount)}
			<div class="affect-amount">{affectedAmount}</div>
		{/if}
	</div>
</div>

<style>
	.affect-amount {
		--bubble-size: 2rem;
		border-radius: 50%;
		background-color: white;
		border: 1px solid black;
		color: black;
		width: var(--bubble-size);
		height: var(--bubble-size);
		line-height: var(--bubble-size);
		text-align: center;
		position: relative;
		top: calc(-5rem - 2 * 1.5rem);
		font-size: 1.5rem;
	}
	img {
		width: 5rem;
		height: 5rem;
		min-width: 5rem;
		min-height: 5rem;
		max-width: 5rem;
		max-height: 5rem;
	}
	.pokemon-card {
		margin: 0.2rem;
		padding: 0.2rem;
		color: white;
		display: flex;
		flex-flow: column;
		align-items: center;
		min-width: calc(2 * 3.9rem + 0.2rem);
	}

	.pokemon-name {
		text-align: center;
	}
	.pokemon-types {
		margin: 0.3rem 0;
		display: flex;
		justify-content: center;
		width: 100%;
	}
	.pokemon-type {
		border: 1px solid black;
		border-radius: 40px;
		padding: 0.1rem;
		width: 3.3rem;
		font-size: 0.8rem;
		text-align: center;
		color: white;
	}
	.pokemon-type + .pokemon-type {
		margin-left: 0.2rem;
	}
	.pokemon-type.bug {
		background-color: var(--color-type-bug);
	}
	.pokemon-type.dark {
		background-color: var(--color-type-dark);
	}
	.pokemon-type.dragon {
		background-color: var(--color-type-dragon);
	}
	.pokemon-type.electric {
		background-color: var(--color-type-electric);
	}
	.pokemon-type.fairy {
		background-color: var(--color-type-fairy);
	}
	.pokemon-type.fighting {
		background-color: var(--color-type-fighting);
	}
	.pokemon-type.fire {
		background-color: var(--color-type-fire);
	}
	.pokemon-type.flying {
		background-color: var(--color-type-flying);
	}
	.pokemon-type.ghost {
		background-color: var(--color-type-ghost);
	}
	.pokemon-type.grass {
		background-color: var(--color-type-grass);
	}
	.pokemon-type.ground {
		background-color: var(--color-type-ground);
	}
	.pokemon-type.ice {
		background-color: var(--color-type-ice);
	}
	.pokemon-type.normal {
		background-color: var(--color-type-normal);
	}
	.pokemon-type.poison {
		background-color: var(--color-type-poison);
	}
	.pokemon-type.psychic {
		background-color: var(--color-type-psychic);
	}
	.pokemon-type.rock {
		background-color: var(--color-type-rock);
	}
	.pokemon-type.steel {
		background-color: var(--color-type-steel);
	}
	.pokemon-type.water {
		background-color: var(--color-type-water);
	}
</style>
