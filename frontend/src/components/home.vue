<template>
    <div class="container is-fluid columns is-gapless">
        <main-content class="column is-7"/>
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

</style>