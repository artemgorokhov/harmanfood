<template>
    <div class="container" id="theQuestion">
        <p class="has-text-centered
                   is-size-1">
               {{ username }}, хочешь пообедать?
        </p>
        <nav class="buttons-level">
            <a @click="sendAnswer(true)"
                :disabled="!!decisionButtonDisabled"
                class="button 
                    is-pulled-left
                    is-success
                    is-large">Да!</a>
            <a @click="sendAnswer(false)"
                :disabled="!!decisionButtonDisabled"
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
            decisionButtonDisabled: false
        }
    },
    methods: {
        sendAnswer: function(iWannaEat) {
            this.decisionButtonDisabled = true;
            var _this = this
            if (process.env.NODE_ENV === 'development') {
                if (iWannaEat)
                    _this.$router.replace( {path: '/home/restaurants'})
                else
                    _this.$router.replace( {path: '/summary'})
                return
            }
            axios.post('/api/participate', {the_answer: iWannaEat})
                .then(function(response) {
                    console.log('Participate response: ' + Object.keys(response.data))
                    console.log('RESULT: ' + response.data.participate)
                    if (!response.data.participate) {
                        _this.$router.replace( {path: '/summary'} )
                    } else {
                        _this.$router.replace( {path: '/home/restaurants'} )
                    }
                    _this.decisionButtonDisabled = false
                })
                .catch(function() {
                    _this.decisionButtonDisabled = false
                    console.error('Something went wrong with your participation')
                    _this.$router.replace( {path: '/error'} )
                })
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