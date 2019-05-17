<template>
    <div class="box orderSummaryItem">
    	<div class="order-name">
    		{{ ordername }}
    	</div>
		<div class="columns">
			<div class="column is-half">
				<div class="patronSummary">
					<p class="is-size-7 has-text-grey">Кормилец</p>
					<p class="is-size-3 has-text-right">{{ patron.fullName }}</p>
					<p class="is-size-7 has-text-right">{{ patron.phone }}</p>
				</div>
				<div id="orderPlace">
					<p class="is-size-7">Ресторан</p>
					<p class="has-text-right">{{ order.restaurantTitle }}</p>
					<p class="is-size-7 has-text-right">{{ order.provider }}</p>
				</div>
				<div id="dishesSummary">

				</div>
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
			},
			patron() {
				return this.$store.state.main.order.patron
			},
			order() {
			    return {
					restaurantTitle: "Sova",
					provider: "delivery"
				}
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