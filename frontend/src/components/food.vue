<template>
    <div class="columns is-mobile">
        <div class="column is-half is-paddingless">
            <ul class="with-border">
                <li v-for="dish in menu"
                    :key="dish.id">
                    <food-item v-bind="dish"
                        @click.native="foodItemSelect(dish)"/>
                </li>
            </ul>
        </div>
        <div class="column is-paddingless">
            <food-details
                v-bind="current_dish"
                v-on:add-dish="addToBasket"/>
        </div>
    </div>
</template>

<script>
import FoodItem from './fooditem.vue'
import FoodDetails from './fooddetails.vue'
export default {
    data: function() {
        return {
            current_dish: null,
            menu: [
                {
                    title: 'Филадельфия 2 260 г',
                    price: 199,
                    category: 'Популярное',
                    description: '8 кусочков. Рис, нори, сыр творожный, лосось, огурец'
                },
                {
                    title: 'Горячая филадельфия 330 г',
                    price: 249,
                    category: 'Популярное',
                    description: '10 кусочков! рис, нори, сыр творожный, огурец, лосось, соус терияки, кунжут'
                }
            ]
        }
    },
    methods: {
        foodItemSelect(dish) {
            console.log('Clicked: ' + dish.title)
            this.current_dish = dish
        },
        addToBasket(payload) {
            console.log("Adding to basket " + payload.title)
            this.current_dish = null
        }
    },
    components: {
        FoodItem,
        FoodDetails
    }
}
</script>
