<template>
    <div class="patronInfo has-text-right">
        <p class="is-size-7 has-text-grey">Кормилец</p>
        <p class="is-size-3" id="patronName">{{ patron.fullName }}</p>
        <p class="is-size-7">{{ patron.phone }}</p>
        <a v-if="$store.getters.isImmutable()"
            class="button is-text is-small"
            @click.prevent="iWannaBePatron">Хочу заказать</a>
    </div>
</template>

<script>
import { ACTION_NAMES } from '@/store/consts'
export default {
    name: "patron",
    computed: {
        patron() {
            return this.$store.state.main.order.patron
        }
    },
    methods: {
        iWannaBePatron: function () {
            this.$store.dispatch(ACTION_NAMES.I_AM_PATRON)
        }
    }
}
</script>

<style lang="sass">
.patronInfo p:nth-child(1)
    margin-bottom: -0.75rem

.patronInfo p:nth-child(3)
    margin-top: -0.2rem

</style>