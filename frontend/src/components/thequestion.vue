<template>
    <div class="container" id="theQuestion">
        <p class="has-text-centered
                   is-size-1">
               {{ username }}, хочешь пообедать?
        </p>
        <nav class="buttons-level">
            <a v-on:click="yesIWannaEat"
               class="button 
                    is-pulled-left
                    is-success
                    is-large">Да!</a>
            <a v-on:click="NoIDont"
               class="button 
                    is-pulled-right
                    is-danger
                    is-large
                    is-outlined">Не</a>
        </nav>
    </div>
</template>

<script>
import Vue from 'vue'
import { MUTATION_NAMES } from '@/store/consts'

export default {
    name: 'the-question',
    methods: {
        yesIWannaEat: function() {
            this.$router.replace( {path: '/home/restaurants'} );
        },
        NoIDont: function() {
            this.$router.replace( {path: '/info'} );
        }
    },
    computed: {
        username() {
            return this.$store.state.main.user.firstName
        }
    }
}
</script>

<style lang="sass">
.buttons-level
    margin: auto
    width: 50%
    max-width: 300px

.buttons-level a
    padding-left: 2em
    padding-right: 2em
#theQuestion
    margin-top: -10%
</style>