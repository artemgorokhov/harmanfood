<template>
  <div class="columns is-multiline is-mobile is-7">
    <div class="card column is-one-quarter"
        v-for="restaurant in restaurants">
        {{ restaurant.name }}
    </div>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                restaurants: [ {name: 'Woking'},
                               {name: 'Lepitesto'},
                               {name: 'Burger King'} ]
            }
        }
    }
</script>