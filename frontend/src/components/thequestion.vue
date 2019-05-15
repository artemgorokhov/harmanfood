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
import { MUTATION_NAMES, ACTION_NAMES } from '@/store/consts'

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
            this.$store.dispatch(ACTION_NAMES.SEND_THE_ANSWER, {the_answer: iWannaEat})
            .then(() => {
                let thepage = _this.$store.state.stage.userstage.page
                console.log('The page: ' + thepage)
                _this.$router.replace(thepage)
                _this.decisionButtonDisabled = false
            })
            .catch(function(error) {
                _this.decisionButtonDisabled = false
                console.error('Something went wrong with your participation: ' + error)
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