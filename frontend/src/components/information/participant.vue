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
    props: {
        name: String
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
    content: ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."

.participantPrice
    overflow: hidden
</style>
