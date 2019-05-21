<template>
    <div class="box orderSummaryItem">
    	<div class="order-name">
    		{{ ordername }}
    	</div>
		<div class="columns">
			<div class="column is-half">
				<div id="patronSummary" class="has-text-right">
					<p class="is-size-3">{{ patron.fullName }}</p>
					<p class="is-size-7">{{ patron.phone }}</p>
				</div>
				<dishes-summary v-bind="order"/>
			</div>
			<div class="column">
				<participant-item v-for="p in participants" :key="p.id" v-bind="p"/>
			</div>
		</div>
        <div id="orderTotal" class="is-size-3 has-text-info has-text-centered">
            <div class="has-text-dark">Итого: {{ order.total }} &#x20bd; </div><div id="fullPrice">2345  &#x20bd;</div>
        </div>
    </div>
</template>

<script>
	import { getNow } from '@/assets/js/date_representation'
	import ParticipantItem from '@/components/information/participant'
	import DishesSummary from './dishessummary'

    export default {
		name: 'order-summary-item',
		components: {
			ParticipantItem,
			DishesSummary
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
			    return this.$store.state.main.order
			},
            participants() {
                return this.$store.state.main.order.participants
            }
        }
    }
</script>

<style lang="sass">
.order-name
    padding-bottom: 0.7em
    font-size: 3em
    font-family: 'Roboto', sans-serif
    text-align: center

.orderSummaryItem
	background-color: rgba(230, 230, 235, 1)
	max-width: 50em
	margin-left: auto
	margin-right: auto

#patronSummary
    border-bottom: 1px solid grey

#fullPrice
    text-decoration: line-through
    font-size: 0.5em
    color: grey
</style>