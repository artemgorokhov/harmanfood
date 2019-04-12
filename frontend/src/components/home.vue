<template>
    <div class="container mainContent is-fluid columns">
        <div class="column is-8">
            <router-view/>
            <footer class="footer has-background-dark">
                <div class="content has-text-centered">
                    <a class="button is-success"
                       v-on:click="back">Back</a>
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
</style>