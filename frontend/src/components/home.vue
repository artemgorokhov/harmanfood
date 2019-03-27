<template>
    <div class="container is-fluid columns is-gapless">
        <div class="mainContent column is-7">
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
    padding: 20px
</style>