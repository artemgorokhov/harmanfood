<template>
    <div class="has-background-light has-text-gray-dark">
    <div class="info-block">
        <patron/>
        <participants/>
    </div>
    </div>
</template>

<script>
import Patron from './patron.vue'
import Participants from './participants.vue'

export default{
    name: 'information-block',
    components: {
        Patron,
        Participants
    }
}
</script>

<style lang="sass">
.info-block
    padding: 20px;
</style>


