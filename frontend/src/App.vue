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
      <transition name="fade" mode="out-in">
        <router-view/>
      </transition>
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

.flexBody
    flex-flow: column

.fade-enter-active
  transition: opacity 2s

.fade-leave-active
  transition: opacity 0.4s
  
.fade-enter, .fade-leave-to
  opacity: 0

</style>
