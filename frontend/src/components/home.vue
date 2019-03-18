<template>
  <div>
    <p>Home page, man</p>
    <information-block/>
    <main-content/>
  </div>
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