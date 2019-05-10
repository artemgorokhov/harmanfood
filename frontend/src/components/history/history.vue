<template>
    <div class="container history-view">
        <order-summary-item/>
    </div>
</template>

<script>
    export default {
        name: 'order-history',
        components: {
            OrderSummaryItem: () => import('./summary.vue')
        }
    }
</script>