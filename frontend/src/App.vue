<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

@import "@/assets/css/contrast_theme.scss"

<style lang="sass">
#app
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

</style>
