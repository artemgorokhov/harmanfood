<template>
	<div class="status-footer">
        <div class="content has-text-centered">
            <a v-if="$store.getters.isChoosingFood()"
                class="button"
                v-on:click="backToRestaurants">Другой ресторан</a>
            <a v-if="$store.getters.hasSomethingForDinner()"
                class="button is-success"
                v-on:click="ready">Я готов</a>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'status-block',
        data: function () {
            return {

            }
        },
        methods: {
            backToRestaurants: function() {
                let provider_on_view = this.$store.state.dishes.restaurant_on_view.provider
                this.$router.replace( {path: '/home/restaurants'} )
            },
            ready: function() {
                console.log("I am ready")
            }
        }
    }
</script>

<style lang="sass">

.status-footer
    padding: 1rem
    height: 2rem
    position: absolute
    bottom: 3rem

</style>