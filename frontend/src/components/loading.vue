<template>
    <div class="container has-text-centered size-is-4">
    <div class="container is-flex is-horizontal-center">
      <figure class="image is-128x128">
        <img class="loadingAnimation" src="@/assets/img/pizza.svg"/>
      </figure>
    </div>
    <div>Loading...</div>
    </div>
</template>

<style lang="sass">
@keyframes burger-anim
  100%
    transform: rotate(360deg)

img.loadingAnimation
  -webkit-filter: invert(100%)
  filter: invert(100%)
  animation-name: burger-anim
  animation-duration: 3s
  animation-iteration-count: infinite
  animation-timing-function: cubic-bezier(.64,0,.01,1)

.is-horizontal-center
  justify-content: center
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
      console.log('Loading from path: ' + from.path)
      store.dispatch(ACTION_NAMES.GET_USER_INFO)
          .then(response => {
            console.log("LOADED! Go to " + from.path)
            vm.$router.replace(from.path)
          }, error => {
            console.log('Load error :( Go to Error page')
            //  TODO: Create error page
            vm.$router.replace('/error')
          })
    })
  }
}
</script>