<template>
    <div class="columns is-mobile food-view">
        <div class="column is-half is-paddingless dishes-list">
            <ul class="with-border">
                <li v-for="dish in menu"
                    :key="dish.id">
                    <food-item v-bind="dish"
                        :class="{ selected: dish == current_dish }"
                        @click.native="foodItemSelect(dish)"/>
                </li>
            </ul>
        </div>
        <div class="column is-paddingless">
            <food-details
                v-bind="current_dish"
                v-on:add-dish="addToBasket"
                v-on:remove-dish="removeFromBasket"/>
            <div class="my-dishes-list">
                <dinner-item
                    v-for="mydish in selectedDishes()"
                    :key="mydish.id"
                    :class="{ selected: mydish == current_dish }"
                    v-bind:dish="mydish"
                    @click.native="myDishSelect(mydish)"/>
            </div>
        </div>
    </div>
</template>

<script>
import FoodItem from './fooditem.vue'
import DinnerItem from './dinneritem.vue'
import FoodDetails from './fooddetails.vue'
import { ACTION_NAMES } from '@/store/consts'
export default {
    data: function() {
        return {
            current_dish: null,
            menu: 
        }
    },
    methods: {
        selectedDishes() {
            console.log("Getting selected dishes")
            let sd = this.$store.getters.getByRestaurant()
            sd.forEach((s)=>{
                console.log(s)
            })
            return sd
        },
        foodItemSelect(dish) {
            console.log('Clicked: ' + dish.title)
            this.current_dish = dish
            this.current_dish.basket = false
        },
        myDishSelect(mydish) {
            console.log('Selected my dish ' + mydish.title)
            this.current_dish = mydish
            this.current_dish.basket = true
        },
        addToBasket(payload) {
            console.log("Adding to basket " + payload.title)
            this.current_dish = null
            this.$store.dispatch(ACTION_NAMES.ADD_DISH_TO_MY_DINNER, payload)
            .then(response => {
                console.log("Action 'add dish' was dispatched")
            })
        },
        removeFromBasket(payload) {
            console.log('Removing ' + payload.title + ' from basket')
            this.current_dish = null
            this.$store.dispatch(ACTION_NAMES.REMOVE_DISH_FROM_MY_DINNER, {
                unique: payload.title
            })
            .then(response => {
                console.log("Actions 'remove dish' was dispatched")
            })
        }
    },
    components: {
        FoodItem,
        DinnerItem,
        FoodDetails
    }
}
</script>

<style lang="sass">
@import "@/assets/css/contrast_theme.scss"
.food-view
    height: calc(100% + 1.5rem - 6rem)

.dishes-list
    overflow-y: auto
    -ms-overflow-style: none
    scrollbar-width: none

.dishes-list::-webkit-scrollbar
    display: none

.my-dishes-list
    height: calc(100% - 27rem)
    border-top: $light 1px solid

</style>