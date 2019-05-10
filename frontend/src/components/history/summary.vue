<template>
    <div class="box orderSummaryItem">
    	<div class="order-name">
    		{{ ordername }}
    	</div>
    </div>
</template>

<script>
	import { getNow } from '@/assets/js/date_representation'
    export default {
        name: 'order-summary-item',
        data() {
            return {}
        },
        computed: {
        	ordername() {
        		return getNow()
        	}
        }
    }
</script>

<style lang="sass">
.orderSummaryItem
	background-color: rgba(230, 230, 235, 1)
	max-width: 50em
	margin-left: auto
	margin-right: auto
	margin-top: 5em

</style>