<template>
    <div class="card">
        <div class="card-content is-unselectable">
            <span class="has-text-dark is-size-5">{{ title }}</span>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'food-item',
        props: {
            title: String,
            price: Number
        },
        methods: {
            select() {
                console.log('Food: ' + this.$props.title)
            }
        }
    }
</script>