<template>
    <div class="card food-item-card">
        <div class="card-content is-unselectable food-item-content">
            <span class="has-text-dark is-size-6">{{ title }}</span>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'food-item',
        props: {
            title: String,
            price: Number
        },
        methods: {
            select() {
                console.log('Food: ' + this.$props.title)
            }
        }
    }
</script>

<style lang="sass">
.food-item-card
    cursor: pointer

.food-item-content
    padding: 0.7em
</style>