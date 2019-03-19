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

<style lang="sass">

@import "@/assets/css/main.scss"

#app
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

</style>
