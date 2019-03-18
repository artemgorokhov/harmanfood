<template>
  <div class="mainContent has-background-light">
    <p>Main content</p>
  </div>
</template>

<script>
import MainMenu from './mainmenu.vue'

export default {
    components: {
        MainMenu
    }
}
</script>

<style lang="sass">

.mainContent
    min-width: 300px;
    min-height: 300px;

</style>
