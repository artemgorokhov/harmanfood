<template>
<div>
    <div class="tabs is-centered is-boxed">
        <ul class="with-border">
            <li v-for="tab in tabs" 
                @click.prevent="activeTab = tab.id" 
                :class="{ 'is-active': tab.id === activeTab }"
                :key="tab.id">
                <a>{{ tab.name }}</a>
            </li>
        </ul>
    </div>
    <div class="columns is-multiline is-mobile is-7">
        <div class="column is-one-quarter"
            v-for="restaurant in restaurants(activeTab)" :key="restaurant.id">
            <restaurant-card v-bind="restaurant"/>
        </div>
    </div> 
</div>
</template>

<script>
import RestaurantCard from './restaurantcard.vue'
export default {
    data: function () {
      return {
            tabs: [
                { name: 'ЯндексЕда', id: 'yandex' },
                { name: 'DeliveryClub', id: 'delivery' },
                { name: 'Другое', id: 'other' }
            ],
            activeTab: 'yandex'
      }
    },
    methods: {
        restaurants(provider) {
            return this.$store.getters.getByProvider(provider)
        }
    },
    components: {
      RestaurantCard
    }
}
</script>

<style lang="sass">

ul.with-border
  border-bottom: 1px solid #f9f8ec !important

</style>
