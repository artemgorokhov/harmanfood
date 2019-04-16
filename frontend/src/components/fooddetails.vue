<template>
  <div class="food-details-card">
      <div class="food-details-empty"
        v-if="!title">
        <span class="icon dish-icon">
            <i class="fas fa-utensils"></i>
            <p>Выберите блюдо</p>
        </span>
      </div>
      <div class="food-details-selected"
        v-else>
        <span class="icon dish-icon">
          <i class="fas fa-hamburger"></i>
          <p>{{ title }}</p>
          <p class="dish-description">{{ description }}</p>
        </span>
        <div class="food-details-footer">
          <a class="button add-dish-btn is-success"
            @click.prevent="add">Добавить</a>
        </div>
      </div>
  </div>
</template>

<script>
  export default {
    name: 'food-details',
    props: {
      title: String,
      price: Number,
      description: String,
      amount: Number
    },
    methods: {
      add() {
        this.$emit('add-dish', {
          amount: this.amount,
          title: this.title
        })
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
    display: block
    text-align: center
    padding-top: 6rem

.dish-icon>i
    font-size: 7rem

.dish-icon>p.dish-description
    font-size: 0.7rem
    padding-top: 0.3rem
    font-family: "Gill Sans MT", "Gill Sans", "My Gill Sans", sans-serif;

.dish-icon>p
    font-size: 1.2rem

.food-details-footer
    position: absolute
    bottom: 0
    width: 100%
    margin-bottom: 1rem

</style>