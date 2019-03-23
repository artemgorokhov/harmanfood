<template>
  <section class="section">
    <hero-header/>
    <div class="columns">
        <main-content class="column is-half"/>
        <information-block class="column"/>
    </div>
  </section>
</template>

<script>
import InformationBlock from './info.vue'
import MainContent from './maincontent.vue'
import HeroHeader from './header.vue'
export default{

	components: {
        HeroHeader,
        InformationBlock,
        MainContent
	}
}
</script>