<template>
  <div>
    <div v-if="isValidPlace">
      <div id="order-place" class="has-text-right">
        <p class="is-size-5">{{ restaurant }} ({{ provider }})</p>
      </div>
      <ul class="food-list-summary has-text-right">
        <li v-for="(amount, title) in dishList" :key="title">
          <span>{{ title }}</span>
          <span> x {{ amount }}</span>
        </li>
      </ul>
    </div>
    <div v-else class="place-not-chosen">
      Место не выбрано
    </div>
  </div>
</template>

<script>

export default {
  name: 'dishes-summary',
  props: {
    participants: Array,
    restaurant: String,
    provider: String
  },
  computed: {
    dishList: function() {
      if (!this.isValidPlace) {
        return []
      }
      let dishes = {}
      this.participants.forEach(participant => {
        console.log('each participant')
        if (participant.restaurant === this.restaurant &&
            participant.provider === this.provider) {
              console.log('inside his if')
              participant.food.forEach(dish => {
                console.log('each dish')
                if (dish.title in dishes) {
                  dishes[dish.title] += 1
                }
                else {
                  dishes[dish.title] = 1
                }
              })
            }
      })
      return dishes
    },
    isValidPlace: function() {
      return this.restaurant && this.provider
    }
  }
}
</script>

<style lang="sass">
.place-not-chosen
  font-size: 2em
  font-family: 'Roboto', sans-serif
  text-align: center
  padding: 1.5em

.food-list-summary
  font-size: 0.8em
  font-family: 'Roboto', sans-serif

#order-place
  padding-bottom: 0.5em

</style>