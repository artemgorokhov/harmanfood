<template>
    <div class="card food-item-card">
        <div class="is-unselectable food-item-content">
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
            category: String
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
    color: $light
    margin-bottom: 0.3em

.food-item-content
    padding: 0.7em

.food-item-price
    font-weight: bold
    // color: $dark

.food-item-card.card
    background-color: rgba(250, 250, 250, 0.2)
    color: $light
</style>