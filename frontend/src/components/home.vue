<template>
  <section class="section">
    <h1 class="has-text-dark 
               has-text-left-desktop
               has-text-weight-bold
               title">Harman Food</h1>
    <div class="columns">
        <information-block class="column is-one-third"/>
        <main-content class="column"/>
    </div>
  </section>
</template>

<script>
import InformationBlock from './info.vue'
import MainContent from './maincontent.vue'

export default{
	components: {
    InformationBlock,
    MainContent
	}
}
</script>