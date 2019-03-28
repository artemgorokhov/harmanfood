<template>
    <div class="patron has-text-centered">
        <p class="is-size-7 has-text-grey-light">Кормилец</p>
        <p class="is-size-2">{{ patron_name }}</p>
    </div>
</template>

<script>
export default {
    name: "patron",
    computed: {
        patron_name() {
            return this.$store.state.patron
        }
    }
}
</script>

<style lang="sass">
.patron
    border-bottom: 1px solid
</style>