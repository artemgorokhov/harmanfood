<template>
    <div class="columns is-mobile food-view">
        <div class="column is-1 categories-list">
            <ul class="menu-category"
                v-scroll-spy-active="{selector: 'figure.cat-item'}"
                v-scroll-spy-link="{selector: 'figure.cat-item'}">
                <li v-for="menu_cat in categories"
                    :key="menu_cat"
                    class="is-unselectable">
                    <figure class="image is-32x32 cat-item">
                        <i class="fas"
                            :class="categoryClass(menu_cat, true)"></i>
                    </figure>
                </li>
            </ul>
        </div>
        <div class="column is-5 is-paddingless dishes-list"
            v-scroll-spy="{sectionSelector: 'ul.cat-group'}">
            <ul v-for="category in categories"
                :key="category"
                class="cat-group">
                <li v-for="dish in menu[category]"
                    :key="dish.id">
                    <food-item 
                        v-bind:dish="dish"
                        v-bind:categoryClass="categoryClass(category, false)"
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
import { getCategoryClass } from '@/assets/js/categories'
export default {
    data: function() {
        return {
            current_dish: null,
            categories: [
                'Популярное',
                'Открытые роллы',
                'Бургеры'
            ],
            menu: {
                'Популярное': [
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
                        title: 'Ролл с лососем 130 г', 
                        price: 129,
                        category: 'Популярное', 
                        description: '8 кусочков. Рис, нори, лосось'
                    },
                    {
                        title: 'Сет 1 400 г', 
                        price: 299,
                        category: 'Популярное',
                        description: '16 кусочков.Филадельфия 2, ролл лосось'
                    },
                    {
                        title: 'Сет 3 800 г',
                        price: 579,
                        category: 'Популярное',
                        description: '28 кусочков. Филадельфия 2, цезарь ролл, горячая филадельфия'
                    },
                    {
                        title: 'Лапша с курицей 360 г',
                        price: 229,
                        category: 'Популярное',
                        description: 'Курица, лапша, перец болгарский, морковь, лук репчатый, лук зеленый, кунжут, соус соево-чесночный'
                    }
                ],
                'Открытые роллы': [
                    {
                        title: 'Филафорния 280 г',
                        price: 359,
                        category: 'Открытые роллы',
                        description: '8 кусочков.Рис, нори, лосось, сыр творожный, огурец, тигровая креветка в панировке, икра тобико(красная)'
                    },
                    {
                        title: 'Ночная москва 240 г', 
                        price: 269,
                        category: 'Открытые роллы',
                        description: '8 кусочков. Рис, нори, икра тобико(черная), сыр творожный, жареный лосось, огурец'
                    }, 
                    {
                        title: 'Сливочный лосось 220 г',
                        price: 199,
                        category: 'Открытые роллы',
                        description: '8 кусочков. Рис, нори, сыр творожный, лосось, кунжут'
                    },
                    {
                        title: 'Сливочный угорь 235 г', 
                        price: 199,
                        category: 'Открытые роллы',
                        description: '8 кусочков. Рис, нори, сыр творожный, угорь, соус терияки, кунжут'
                    },
                    {
                        title: 'Сливочная креветка 230 г',
                        price: 199,
                        category: 'Открытые роллы',
                        description: '8 кусочков. Рис, нори, сыр творожный, тигровая креветка в панировке, кунжут'
                    }, 
                    {
                        title: 'Брутал 250 г',
                        price: 199,
                        category: 'Открытые роллы',
                        description: '8 кусочков. Рис, нори, бекон опаленный, перец болгарский, сыр творожный, китайстакая капуста'
                    }, 
                    {
                        title: 'Динамит 300 г',
                        price: 349,
                        category: 'Открытые роллы',
                        description: '8 кусочков. Рис, нори, сыр творожный, огурец, тигровая креветка, соус спайс, кунжут'
                    }
                ],
                'Бургеры': [
                    {
                        title: 'Кани сарадо 240 г',
                        price: 229,
                        category: 'Бургеры',
                        description: '8 кусочков. Рис, нори, краб (имит.), огурец, сыр творожный, кунжут'
                    }, 
                    {
                        title: 'Дракон 360 г', 
                        price: 559,
                        category: 'Бургеры',
                        description: '10 кусочков. Рис, нори, угорь, сыр творожный, такуан, соус терияки, кунжут, украшение(морковь, перец болгарский, огурец)'
                    }, 
                    {
                        title: 'Канада 300 г',
                        price: 379,
                        category: 'Бургеры',
                        description: '8 кусочков. Рис, нори, сыр творожный, угорь, огурец, краб(имит.), соус терияки, кунжут'
                    },
                    {
                        title: 'Нью йорк 280 г', 
                        price: 439,
                        category: 'Бургеры',
                        description: '8 кусочков. Рис, нори, угорь, жаренный лосось, икра тобико(черная), огурец, сыр творожный, соус терияки, кунжут'
                    }
                ]
            }
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
            if (this.current_dish === dish) {
                this.current_dish = null
            } else {
                console.log('Selected dish from '+dish.category)
                this.current_dish = dish
                this.current_dish.basket = false
            }
        },
        myDishSelect(mydish) {
            if (this.current_dish === mydish) {
                console.log("Deselect my dish")
                this.current_dish = null
            } else {
                console.log('Selected my dish ' + mydish.title)
                this.current_dish = mydish
                this.current_dish.basket = true
            }
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
        },
        categoryClass: getCategoryClass
    },
    components: {
        FoodItem,
        DinnerItem,
        FoodDetails
    }
}
</script>

<style lang="sass">
@import "./../assets/css/custom_icons.css"
.food-view
    height: calc(100% + 1.5rem - 6rem)

// Category colors
.cat-popular
    --rgb: 255, 246, 198
.cat-sushi
    --rgb: 224, 254, 255
.cat-burger
    --rgb: 204, 139, 183


.dishes-list
    overflow-y: auto
    -ms-overflow-style: none
    scrollbar-width: none
    position: relative

.dishes-list::-webkit-scrollbar
    display: none

.my-dishes-list
    height: calc(100% - 27rem)
    border-top: white 1px solid

.categories-list li
    margin-bottom: 1.5rem
    // border: 1px white solid

.categories-list i.fas
    font-size: 2rem

.categories-list figure.cat-item
    cursor: pointer

.categories-list figure.cat-item>i
    color: rgba(var(--rgb), 0.2)

.categories-list figure.cat-item>i:hover
    color: rgba(var(--rgb), 0.3)

.categories-list figure.cat-item.active>i
    color: rgba(var(--rgb), 0.7)

</style>