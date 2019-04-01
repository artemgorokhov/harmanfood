<template>
    <div class="patronInfo has-text-centered">
        <p class="is-size-7 has-text-grey">Кормилец</p>
        <p class="is-size-2" id="patronName">{{ patron.name }}</p>
        <p class="is-size-7">{{ patron.phone }}</p>
    </div>
</template>

<script>
export default {
    name: "patron",
    computed: {
        patron() {
            return this.$store.state.main.patron
        }
    }
}
</script>

<style lang="sass">
.patronInfo
    border-bottom: 1px solid

.patronInfo p:nth-child(1)
    margin-bottom: -0.75rem

.patronInfo p:nth-child(3)
    margin-top: -0.5rem

</style>