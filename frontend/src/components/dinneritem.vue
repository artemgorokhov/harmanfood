<template>
    <div class="card dinner-item-card is-unselectable">
        {{ dishtitle }}
    </div>
</template>

<script>
    export default {
        name: 'dinner-item',
        props: {
            dishtitle: String
        }
    }
</script>