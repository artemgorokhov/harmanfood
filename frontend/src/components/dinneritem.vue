<template>
    <div class="is-unselectable dish-item has-text-dark">
        <article class="media">
            <div class="media-left dish-picture">
                <figure class="image is-48x48">
                    <i class="fas"
                        :class="categoryClass(dish.category)"></i>
                </figure>
            </div>
            <div class="media-content">
                <div class="content">
                    <span>
                        <div class="strong-title">{{dish.title}}</div>
                        <p class="d-description">{{dish.description}}</p>
                    </span>
                </div>
            </div>
            <div class="media-right dish-price">
                <figure class="image is-32x32">
                    <strong>{{ dish.price }}&#x20bd;</strong>
                </figure>
            </div>
        </article>
    </div>
</template>

<script>
    import { getCategoryClass } from '@/assets/js/categories'
    export default {
        name: 'dinner-item',
        props: {
            dish: Object
        },
        methods: {
            categoryClass() {
                console.log("DINNER item category: "+this.dish.category)
                return getCategoryClass(this.dish.category)
            }
        }
    }
</script>

<style lang="sass">
.dish-item
    background-color: rgba(250, 250, 250, 0.7)
    margin: 0.2rem
    padding: 0.5rem
    cursor: pointer

.dish-item .strong-title
    font-weight: bold

.dish-item .image
    font-size: 2rem

.dish-item .d-description
    font-size: 0.7rem
    font-family: "Gill Sans MT", "Gill Sans", "My Gill Sans", sans-serif

.dish-price strong
    font-size: 1rem

.dish-item.selected
    background-color: rgba(200, 250, 200, 0.7)

</style>