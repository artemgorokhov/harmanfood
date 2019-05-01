<template>
    <div class="participant">
        <div class="participant-total">
            <span class="participant-name">{{ fullName }}</span>
            <span class="participant-price ">
                {{ total }} &#x20bd;
            </span>
        </div> 
        <ul class="food-list">
        <li v-for="foodItem in foodList" :key="foodItem.title">
            <span class="food-item-name">{{ foodItem.title }}</span>
            <span class="food-item-price">{{ foodItem.price }}  &#x20bd;</span>
        </li>
        </ul>
        <div class="participant-stage">Choosing restaurant</div>
    </div>
</template>

<script>
export default {
    name: 'participant-item',
    props: {
        fullName: String,
        food: Array,
        total: Number
    },
    computed: {
        name: function() {
            console.log('this keys: ' + Object.keys(this.participant))
            return this.participant.firstName + ' ' + this.participant.lastName
        },
        foodList: function() {
            return this.food
        }
    }
}
</script>

<style lang="sass">
.participant
    border-bottom: 1px solid LightSlateGrey
    overflow-x: hidden
    margin-left: 0
    margin-right: 0

.participant-total
    font-size: 1.2em

.participant-total:before
    float: left
    width: 0
    content: " . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
    white-space: nowrap

.participant-name
    background-color: rgba(230, 230, 235, 1)

.participant-price
    background-color: rgba(230, 230, 235, 1)
    float: right

.food-list
    font: 0.8em Gill Sans MT, Gill Sans, My Gill Sans, sans-serif
    padding-left: 0.5em

.food-item-price
    float: right

.participant-stage
    float: right
    font: 0.7em Gill Sans MT, Gill Sans, My Gill Sans, sans-serif
    color: LightSlateGrey
    font-style: italic
    padding-top: 0.5em

</style>
