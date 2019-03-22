<template>
  <section class="section">
    <h1 class="has-text-dark 
               has-text-left-desktop
               has-text-weight-bold
               title">Harman Food</h1>
    <div class="columns">
        <main-content class="column is-half"/>
        <information-block class="column"/>
    </div>
  </section>
    <hero-header/>
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