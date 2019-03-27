<template>
  <div class="columns is-multiline is-mobile">
    <div class="card column"
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