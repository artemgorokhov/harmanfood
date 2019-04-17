<template>
    <div class="container mainContent is-fluid columns">
        <div class="column is-8">
            <router-view/>
            <footer class="has-background-dark status-footer">
                <div class="content has-text-centered">
                    <a class="button"
                        v-on:click="back">Back</a>
                    <a class="button is-success"
                        v-on:click="ready">Я готов</a>
                </div>
            </footer>
        </div>
        <information-block class="column"/>
    </div>
</template>

<script>
import InformationBlock from './information/info.vue'
import MainContent from './maincontent.vue'

export default{
	components: {
        InformationBlock,
        MainContent
	},
    methods: {
        back: function() {
            this.$router.replace( {path: '/home/restaurants'} )
        },
        ready: function() {
            console.log("I am ready")
        }
    }
}
</script>

<style lang="sass">
.mainContent
    padding: 1em
    height: 90vh

.flexHome
    flex: 1 1 100%

.status-footer
    padding: 1rem
    height: 2rem
    position: absolute
    bottom: 3rem
</style>