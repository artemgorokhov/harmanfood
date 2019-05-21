<template>
	<div class="status-footer">
        <div class="content has-text-centered">
            <a v-if="$store.getters.isChoosingFood()"
                class="button"
                :disabled="!!buttonsDisabled"
                v-on:click="backToRestaurants">Другой ресторан</a>
            <a v-if="$store.getters.hasSomethingForDinner()"
                class="button is-success"
                :disabled="!!buttonsDisabled"
                v-on:click="ready">Я готов</a>
        </div>
    </div>
</template>

<script>
    import { MUTATION_NAMES, ACTION_NAMES } from '@/store/consts'
    
    export default {
        name: 'status-block',
        data: function () {
            return {
                buttonsDisabled: false
            }
        },
        methods: {
            backToRestaurants: function() {
                let provider_on_view = this.$store.state.dishes.restaurant_on_view.provider
                this.$router.replace( {path: '/home/restaurants'} )
            },
            ready: function() {
                this.buttonsDisabled = true
                let _this = this
                this.$store.dispatch(ACTION_NAMES.READY_TO_EAT)
                .then(() => {
                    let thepage = _this.$store.state.stage.userstage.page
                    console.log('The page: ' + thepage)
                    _this.$router.replace(thepage)
                    _this.buttonsDisabled = false
                })
                .catch(function(error) {
                    _this.decisionButtonDisabled = false
                    console.error('Something went wrong with your ready request: ' + error)
                    _this.$router.replace( {path: '/error'} )
                })
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