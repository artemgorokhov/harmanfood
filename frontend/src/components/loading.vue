<template>
    <div class="container has-text-centered size-is-4">
    <div class="container is-flex is-horizontal-center">
      <figure class="image is-128x128">
        <img src="@/assets/img/hamburger_empty.svg"/>
      </figure>
    </div>
    <div>Loading...</div>
    </div>
</template>

<style lang="sass">
img
  -webkit-filter: invert(100%)
  filter: invert(100%)

.is-horizontal-center
  justify-content: center;
</style>

<script>
import store from '@/store'
import { ACTION_NAMES } from '@/store/consts'

var fromRoute = {path: '/'}

export default {
  name: 'loading',
  beforeRouteEnter (to, from, next) {
    console.log('Before loaded')
    if (store.state.loaded) {
      console.log('Data alredy loaded')
      next(false)
    }
    fromRoute = from
    next(vm => {
      console.log('Loading from path: ' + fromRoute.path)
      store.dispatch(ACTION_NAMES.GET_USER_INFO)
          .then(response => {
            console.log("LOADED! Go to " + fromRoute.path)
            vm.$router.replace('/')
          }, error => {
            console.log('Load error :( Go to Error page')
            //  TODO: Create error page
            vm.$router.replace('/')
          })
    })
  }
}
</script>