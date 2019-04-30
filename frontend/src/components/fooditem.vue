<template>
    <div class="card food-item-card is-unselectable">
        <div class="food-item-content">
            <span class="is-size-6">{{ dish.title }}</span>
            <span class="food-item-price is-pulled-right">{{ dish.price }} &#x20bd;</span>
            <p class="cat-of-item">{{ dish.category }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'food-item',
        props: {
            dish: Object
        },
        methods: {
            select() {
                console.log('Food: ' + this.$props.title)
            }
        }
    }
</script>

<style lang="sass">
@import "@/assets/css/contrast_theme.scss"
.food-item-card
    cursor: pointer
    margin-bottom: 0.3em
    padding: 0.7em

.food-item-price
    font-weight: bold

.food-item-card.card
    background-color: hsla(var(--hue), 100%, 80%, 0.1)
    color: $light

.food-item-card.card:hover
    background-color: hsla(var(--hue), 100%, 80%, 0.2)

.food-item-card.card:active
    background-color: hsla(var(--hue), 100%, 80%, 0.4)

.card.food-item-card.selected
    background-color: hsla(var(--hue), 100%, 80%, 0.3)

.card.food-item-card.selected:active
    background-color: hsla(var(--hue), 100%, 80%, 0.4)

.cat-of-item
    font-size: 0.5rem
    font-family: "Gill Sans MT", "Gill Sans", "My Gill Sans", sans-serif

</style>