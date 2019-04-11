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
    </div>
</template>

<script>
import FoodItem from './fooditem.vue'
console.log('Dish ' + (FoodItem.name))
export default {
    data: function() {
        return {
            menu: [
                {
                    title: 'Филадельфия 2 260г',
                    price: 199,
                    category: 'Роллы'
                },
                {
                    title: 'Сливочный лосось 220г',
                    price: 249,
                    category: 'Роллы'
                },
                {
                    title: 'Сливочный лосось 220г',
                    price: 199,
                    category: 'Роллы'
                }
            ]
        }
    },
    components: {
        FoodItem
    }
}
</script>
