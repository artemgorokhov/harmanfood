<template>
    <div class="infoBlock has-text-dark">
        <div class="columns info-head">
            <div class="column is-3 current-restaurant"></div>
            <patron class="column"/>
        </div>
        <div class="participantsList">
            <participant-item v-for="p in participants" :key="p.id" v-bind:participant="p"/>
        </div>
    </div>
</template>

<script>
import Patron from './patron.vue'
import ParticipantItem from './participant.vue'

export default{
    name: 'information-block',
    components: {
        Patron,
        ParticipantItem
    },
    data() {
        return {
            
        }
    }
}
</script>

<style lang="sass">
.infoBlock
    padding: 20px
    background-color: rgba(230, 230, 235, 1)

.info-head
    border-bottom: 1px solid 
</style>


