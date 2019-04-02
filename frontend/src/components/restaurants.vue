<template>
<div>
  <p class="title has-text-centered">
      Шаг 1. Выбираем ресторан
  </p>
  <!-- <div class="tabs"> -->
    <div class="columns is-multiline is-mobile is-7">
        <div class="column is-one-quarter"
            v-for="restaurant in restaurants" :key="restaurant.id">
            <restaurant-card v-bind="restaurant"/>
        </div>
    </div>
    <footer class="footer has-background-dark">
        <div class="content has-text-centered">
            <p>STATUS</p>
        </div>
    </footer>
    </div>
<!-- </div> -->
</template>

<script>
import RestaurantCard from './restaurantcard.vue'
export default {
    data() {

    },
    computed: {
        restaurants() {
            console.log('Rest0: ' + Object.keys(this.$store.state.restaurants.yandex))
            return this.$store.state.restaurants.yandex
        }
    },
    components: {
      RestaurantCard
    }
}
</script>
