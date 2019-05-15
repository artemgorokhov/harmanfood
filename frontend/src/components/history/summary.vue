<template>
    <div class="box orderSummaryItem">
    	<div class="order-name">
    		{{ ordername }}
    	</div>
		<div class="columns">
			<div class="column is-half">
				<patron/>
			</div>
			<div class="column">
				right
			</div>
		</div>
    </div>
</template>

<script>
	import { getNow } from '@/assets/js/date_representation'
	import Patron from '@/components/information/patron.vue'
    export default {
		name: 'order-summary-item',
		components: {
			Patron
		},
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

.order-name
	font-size: 2em
	text-align: center
</style>