<template>
  <div class="mainContent">
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

<style>
.mainContent {
    min-width: 300px;
    min-height: 300px;
    background-color: crimson
}
</style>
