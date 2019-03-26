<template>
    <div class="container" id="theQuestion">
        <p class="has-text-centered
                   is-size-1">
               {{ username }}, хочешь пообедать?
        </p>
        <nav class="level buttons-level">
            <a v-on:click="load"
               class="button 
                    level-left
                    is-success
                    is-large">Да!</a>
            <a class="button 
                    level-right
                    is-danger
                    is-large
                    is-outlined">Не</a>
        </nav>
    </div>
</template>

<script>
import Vue from 'vue'
import Loading from './loading.vue'

export default {
    name: 'the-question',
    components: {
        Loading
    },
    methods: {
        load: function() {
            // this.$router.replace( {path: '/loading'} );
            console.log("Old name: " + Vue.getUserName())
            this.username = 'Артём'
            console.log("New name: " + Vue.getUserName())
        }
    },
    computed: {
        username: {
            get: Vue.getUserName,
            set: Vue.setUserName
        }
    }
}
</script>

<style lang="sass">
.buttons-level
    margin-left: 35%
    margin-right: 35%

.buttons-level a
    padding-left: 2em
    padding-right: 2em
#theQuestion
    margin-top: -10%
</style>