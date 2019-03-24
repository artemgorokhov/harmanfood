<template>
    <section id="app" 
             class="hero 
                  is-fullheight 
                  has-background-dark
                  has-text-light">
    <div class="hero-head">
        <main-menu/>
    </div>
    <div class="hero-body is-paddingless">
        <router-view/>
    </div>
    </section>
</template>

<script>
import MainMenu from '@/components/mainmenu.vue'

export default {
  name: 'App',
  components: {
    MainMenu
  }
}
</script>

<style lang="sass">
@import "@/assets/css/contrast_theme.scss"

#app
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale

</style>
