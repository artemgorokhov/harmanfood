<template>
  <div class="card card-equal-height has-text-centered">
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
export default {
  name: 'restaurant-card',
  props: {
    title: String,
    provider: String,
    asset: String
  },
  computed: {
    asset_path: function () {
      console.log('Asset: ' + this.$props.asset)
      console.log('title: ' + this.$props.title)
      console.log('provider: ' + this.$props.provider)
      return "@/assets/img/places/" + this.$props.asset
    }
  }
}
</script>

<style lang="sass">
.card-equal-height
  display: flex
  flex-direction: column
  height: 100%
  margin: auto

.card-equal-height .card-footer
  margin-top: auto

.provider
  text-transform: uppercase
  font-size: 0.5em
</style>
