<template>
  <div class="card card-equal-height has-text-centered"
       v-on:click="select">
    <div class="card-image">
      <figure class="image is-4by3">
        <img :src="asset_path" alt="Placeholder image"/>
      </figure>
    </div>
    <div class="card-content is-unselectable">
      <span class="title has-text-dark is-size-4">{{ title }}</span>
      <p class="provider has-text-grey">{{ provider }}</p>
    </div>
  </div>
</template>

<script>
import { createRestaurant } from '@/models/Restaurant'
import { MUTATION_NAMES } from '@/store/consts'

export default {
  name: 'restaurant-card',
  props: {
    title: String,
    provider: String,
    asset: String
  },
  computed: {
    asset_path: function () {
      return require("@/assets/img/places/" + this.$props.asset)
    }
  },
  methods: {
    select() {
        console.log("Restaurant is chosen")
        let current_restaurant = createRestaurant({title: title, provider: provider})
        this.$store.commit(MUTATION_NAMES.CURRENT_RESTAURANT, restaurant)
        this.$router.replace( {path: '/home/food'} )
    }
  }
}
</script>

<style lang="sass">
.card-equal-height
  display: flex
  flex-direction: column
  height: 100%
  cursor: pointer
  margin: auto
  transition: filter 0.3s ease
  filter: opacity(90%)

.card-equal-height img
  filter: grayscale(70%)

.card-equal-height:hover
  filter: opacity(100%)

.card-equal-height:hover img
  filter: grayscale(40%)

.card-equal-height .card-footer
  margin-top: auto

.provider
  text-transform: uppercase
  font-size: 0.5em
</style>
