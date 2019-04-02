<template>
    <div class="container mainContent is-fluid columns">
        <div class="column is-8">
            <router-view/>
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
	}
}
</script>

<style lang="sass">
.mainContent
    padding: 1em
    margin: 0

.flexHome
    flex: 1 1 100%
</style>