<template>
    <div class="participant">
        <div class="participant-total">
            <span class="participant-name">{{ name }}</span>
            <span class="participant-price ">
                250 р
            </span>
        </div> 
            <ul class="food-list">
            <li v-for="foodItem in foodList" :key="foodItem.id">
                {{ foodItem.name }}
            </li>
            </ul>
    </div>
</template>

<script>
export default {
    name: 'participant-item',
    props: [
        'participant'
    ],
    computed: {
        name: function() {
            console.log('this keys: ' + Object.keys(this.participant))
            return this.participant.firstName + ' ' + this.participant.lastName
        },
        foodList: function() {

            return this.participant.food
        }
    }
}
</script>

<style lang="sass">
.participant
    border-bottom: 1px solid gray
    padding-bottom: 1em
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
    font: 0.8em Gill Sans MT, Gill Sans, My Gill Sans, sans-serif;
    padding-left: 0.33em

</style>
