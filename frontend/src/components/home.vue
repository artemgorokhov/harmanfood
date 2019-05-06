<template>
    <div class="container mainContent is-fluid columns">
        <div class="column is-8">
            <router-view/>
            <footer class="has-background-dark">
                <status-block/>
            </footer>
        </div>
        <information-block class="column"/>
    </div>
</template>

<script>
import InformationBlock from './information/info.vue'
import MainContent from './maincontent.vue'
import StatusBlock from './statusblock.vue'
import {visibilityHandlers} from '@/assets/js/visibility'

console.log('Registering onHide')
visibilityHandlers.onHide = function() {
    console.error('HIDE!')
}
visibilityHandlers.onShow = function() {
    console.error('SHOW!')
}

export default{
	components: {
        InformationBlock,
        StatusBlock,
        MainContent
	},
    methods: {
        
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