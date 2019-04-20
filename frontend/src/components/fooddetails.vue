<template>
  <div class="food-details-card">
      <div class="food-details-empty"
        v-if="!title">
        <span class="icon dish-icon">
            <i class="fas fa-utensils"></i>
        </span>
        <div class="food-detail-title">Выберите блюдо</div>
      </div>
      <div class="food-details-basket"
        v-else-if="basket">
        <span class="icon dish-icon">
          <i class="fas"
             :class="categoryClass()"></i>
        </span>
        <div class="food-detail-title">{{ title }}</div>
        <div class="dish-description">{{ description }}</div>
        <div class="food-details-footer">
          <a class="button remove-dish-btn"
            @click.prevent="remove">
            <span class="icon is-small">
              <i class="fas fa-trash-alt"></i>
            </span>
            <span>Удалить</span>
          </a>
        </div>
      </div>
      <div class="food-details-selected"
        v-else>
        <span class="icon dish-icon">
          <i class="fas"
            :class="categoryClass()"></i>
        </span>
        <div class="food-detail-title">{{ title }}</div>
        <div class="dish-description">{{ description }}</div>
        <div class="food-details-footer">
          <a class="button add-dish-btn is-success"
            @click.prevent="add">
            <span class="icon is-small">
              <i class="fas fa-shopping-basket"></i>
            </span>
            <span>Добавить</span>
            </a>
        </div>
      </div>
  </div>
</template>

<script>
  import { getCategoryClass } from '@/assets/js/categories'
  export default {
    name: 'food-details',
    props: {
      title: String,
      price: Number,
      description: String,
      category: String,
      basket: Boolean
    },
    methods: {
      add() {
        this.$emit('add-dish', {
          title: this.title,
          description: this.description,
          price: this.price,
          category: this.category
        })
      },
      remove() {
        this.$emit('remove-dish', {
          title: this.title
        })
      },
      categoryClass() {
        console.log('Details category: ' + this.category + ' title: '+this.title)
        return getCategoryClass(this.category, true)
      }
    }
  }
</script>

<style lang="sass">
@import "@/assets/css/contrast_theme.scss"
.food-details-card
    margin: 1em
    height: 25rem
    border-radius: 30px

.food-details-empty
    border: $light 10px dashed
    border-radius: inherit
    height: 100%
    text-align: center
    position: relative

.food-details-selected
    border: $light 10px solid
    border-radius: inherit
    height: 100%
    text-align: center
    position: relative

.dish-icon
    width: 80%
    height: 8rem
    margin: auto
    margin-top: 3rem
    display: block
    text-align: center
    padding-top: 6rem

.food-detail-title
    margin-top: 1rem

.dish-icon>i.fas
    font-size: 7rem

div.dish-description
    font-size: 0.7rem
    padding-top: 0.3rem
    font-family: "Gill Sans MT", "Gill Sans", "My Gill Sans", sans-serif

.dish-icon>p
    font-size: 1.2rem

.food-details-footer
    position: absolute
    bottom: 0
    width: 100%
    margin-bottom: 1rem

.food-details-basket
    background-color: rgba(130, 250, 128, 0.15)
    border: $light 10px solid
    border-radius: inherit
    height: 100%
    position: relative
    text-align: center

</style>