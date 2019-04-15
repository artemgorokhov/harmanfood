<template>
    <div class="card food-item-card is-unselectable">
        <div class="food-item-content">
            <span class="is-size-6">{{ title }}</span>
            <span class="food-item-price is-pulled-right">{{ price }} &#x20bd;</span>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'food-item',
        props: {
            title: String,
            price: Number,
            category: String,
            amount: Number,
            description: String
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
    background-color: rgba(250, 250, 250, 0.1)
    color: $light

.food-item-card.card:hover
    background-color: rgba(250, 250, 250, 0.2)

.food-item-card.card:active
    background-color: rgba(250, 250, 250, 0.4)

.card.food-item-card.selected
    background-color: rgba(250, 250, 250, 0.3)

</style>