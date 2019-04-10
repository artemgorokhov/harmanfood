<template>
    <div class="container" id="theQuestion">
        <p class="has-text-centered
                   is-size-1">
               {{ username }}, хочешь пообедать?
        </p>
        <nav class="buttons-level">
            <a v-on:click="yesIWannaEat"
                :disabled="!!yesButtonDisabled"
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
import axios from 'axios'
import { MUTATION_NAMES } from '@/store/consts'

export default {
    name: 'the-question',
    data: function() {
        return {
            yesButtonDisabled: false
        }
    },
    methods: {
        yesIWannaEat: function() {
            this.yesButtonDisabled = true;
            var _this = this
            axios.post('/api/participate')
                .then(function() {
                    _this.$router.replace( {path: '/home/restaurants'} )
                })
                .catch(function() {
                    _this.yesButtonDisabled = false
                    console.error('Something went wrong with your participation')
                })
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