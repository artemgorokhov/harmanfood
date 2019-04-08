<template>
    <div>
        <nav class="level">
            <div class="level-left participantName">
                <span>{{ name }}</span>
            </div>
            <div class="level-right participantPrice">
                250 р
            </div>
        </nav> 
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
        }
    }
}
</script>

<style lang="sass">
.participantName
    overflow: hidden
    white-space: nowrap
    width: 250px

.level
    width: 300px

.participantName span:after
    content: " . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."

.participantPrice
    overflow: hidden
</style>
