<template>
  <div class="columns is-multiline is-mobile is-7">
    <div class="column is-one-quarter"
        v-for="restaurant in restaurants" :key="restaurant.id">
        <restaurant-card v-bind="restaurant"/>
    </div>
  </div>
</template>

<script>
import RestaurantCard from './restaurantcard.vue'
export default {
    data() {
        return {
            restaurants: [ {title: 'Woking', provider: 'Delivery', asset: 'wok__go.jpg'},
                            {title: 'Папас Китчен', provider: 'Yandex', asset: 'papa_kitchen.jpg'},
                            {title: 'Лепи тесто', provider: 'Yandex', asset: 'pelmennaya_lepi_testo.jpg'},
                            {title: 'Burger King', provider: 'Delivery',asset: 'burger_king.jpg'} ]
        }
    },
    components: {
      RestaurantCard
    }
}
</script>