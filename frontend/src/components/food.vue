<template>
    <div class="columns is-mobile food-view">
        <div class="column is-half is-paddingless dishes-list">
            <ul class="with-border">
                <li v-for="dish in menu"
                    :key="dish.id">
                    <food-item v-bind="dish"
                        :class="{ selected: dish == current_dish }"
                        v-bind:amount="0"
                        @click.native="foodItemSelect(dish)"/>
                </li>
            </ul>
        </div>
        <div class="column is-paddingless">
            <food-details
                v-bind="current_dish"
                v-on:add-dish="addToBasket"/>
            <ul class="my-dishes-list">
                <li v-for="mydish in selectedFood"
                    :key="mydish.id">
                    <food-item v-bind="mydish"
                        @click.native="myDishSelect(mydish)"/>
                </li>    
            </ul>
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
            selectedFood: [],
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
                },
                {
                    category: 'Популярное', 
                    title: 'Ролл с лососем 130 г', 
                    price: 129, 
                    description: '8 кусочков. Рис, нори, лосось'
                },
                {
                    category: 'Популярное', 
                    title: 'Сет 1 400 г', 
                    price: 299, 
                    description: '16 кусочков.Филадельфия 2, ролл лосось'
                },
                {
                    category: 'Популярное',
                    title: 'Сет 3 800 г',
                    price: 579,
                    description: '28 кусочков. Филадельфия 2, цезарь ролл, горячая филадельфия'
                },
                {
                    category: 'Популярное',
                    title: 'Лапша с курицей 360 г',
                    price: 229, 
                    description: 'Курица, лапша, перец болгарский, морковь, лук репчатый, лук зеленый, кунжут, соус соево-чесночный'
                },
                {
                    category: 'Открытые роллы',
                    title: 'Филафорния 280 г',
                    price: 359,
                    description: '8 кусочков.Рис, нори, лосось, сыр творожный, огурец, тигровая креветка в панировке, икра тобико(красная)'
                },
                {
                    category: 'Открытые роллы', 
                    title: 'Ночная москва 240 г', 
                    price: 269,
                    description: '8 кусочков. Рис, нори, икра тобико(черная), сыр творожный, жареный лосось, огурец'
                }, 
                {
                    category: 'Открытые роллы',
                    title: 'Сливочный лосось 220 г',
                    price: 199, 
                    description: '8 кусочков. Рис, нори, сыр творожный, лосось, кунжут'
                },
                {
                    category: 'Открытые роллы', 
                    title: 'Сливочный угорь 235 г', 
                    price: 199, 
                    description: '8 кусочков. Рис, нори, сыр творожный, угорь, соус терияки, кунжут'
                },
                {
                    category: 'Открытые роллы',
                    title: 'Сливочная креветка 230 г',
                    price: 199,
                    description: '8 кусочков. Рис, нори, сыр творожный, тигровая креветка в панировке, кунжут'
                }, 
                {
                    category: 'Открытые роллы',
                    title: 'Брутал 250 г',
                    price: 199,
                    description: '8 кусочков. Рис, нори, бекон опаленный, перец болгарский, сыр творожный, китайстакая капуста'
                }, 
                {
                    category: 'Открытые роллы',
                    title: 'Динамит 300 г',
                    price: 349,
                    description: '8 кусочков. Рис, нори, сыр творожный, огурец, тигровая креветка, соус спайс, кунжут'
                },
                {
                    category: 'Открытые роллы',
                    title: 'Кани сарадо 240 г',
                    price: 229, 
                    description: '8 кусочков. Рис, нори, краб (имит.), огурец, сыр творожный, кунжут'
                }, 
                {
                    category: 'Открытые роллы',
                    title: 'Дракон 360 г', 
                    price: 559, 
                    description: '10 кусочков. Рис, нори, угорь, сыр творожный, такуан, соус терияки, кунжут, украшение(морковь, перец болгарский, огурец)'
                }, 
                {
                    category: 'Открытые роллы',
                    title: 'Канада 300 г',
                    price: 379,
                    description: '8 кусочков. Рис, нори, сыр творожный, угорь, огурец, краб(имит.), соус терияки, кунжут'
                },
                {
                    category: 'Открытые роллы',
                    title: 'Нью йорк 280 г', 
                    price: 439, 
                    description: '8 кусочков. Рис, нори, угорь, жаренный лосось, икра тобико(черная), огурец, сыр творожный, соус терияки, кунжут'
                }
            ]
        }
    },
    methods: {
        foodItemSelect(dish) {
            console.log('Clicked: ' + dish.title)
            this.current_dish = dish
        },
        myDishSelect(mydish) {
            console.log('Selected my dish ' + mydish.title)
            this.current_dish = mydish
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
    height: 12rem
    border-top: $light 1px solid

</style>