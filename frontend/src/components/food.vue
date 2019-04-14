<template>
    <div class="columns is-mobile">
        <div class="column is-one-third">
            <ul class="with-border">
                <li v-for="dish in menu"
                    :key="dish.id">
                    <food-item v-bind="dish"/>
                </li>
            </ul>
        </div>   
        <div class="column">
            <div class="food-details-card">
                <span class="icon">
                    <i class="fas fa-utensils"></i>
                </span>
            </div>
        </div>     
    </div>
</template>

<script>
import FoodItem from './fooditem.vue'
export default {
    data: function() {
        return {
            menu: [
                {
                    title: 'Филадельфия 2 260 г',
                    price: 199,
                    category: 'Популярное'
                },
                {
                    title: 'Горячая филадельфия 330 г',
                    price: 249,
                    category: 'Популярное'
                }
            ]
        }
    },
    components: {
        FoodItem
    }
}
</script>

<style lang="sass">
.food-details-card
    border: #f9f8ec 10px solid
    margin: 1em
    min-height: 400px
    border-radius: 30px
</style>