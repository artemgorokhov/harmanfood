<template>
    <div class="infoBlock has-text-dark">
        <patron/>
        <div v-for="user in users" :key="user.id" class="participantsList">
            <participant-item v-bind="user"/>
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
            users: [ {name: 'Артем'},
                    {name: 'Алексей'} ]
        }
    }
}
</script>

<style lang="sass">
.infoBlock
    padding: 20px
    background-color: rgba(250, 250, 250, 0.9)
</style>


