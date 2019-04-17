<template>
    <div class="is-unselectable dish-item">
        <article class="media">
            <div class="media-left dish-picture has-text-dark">
                <figure class="image is-32x32">
                    <i class="fas fa-pizza-slice"></i>
                </figure>
            </div>
            <div class="media-content">
                <div class="content">
                    <span>
                        <strong>{{dish.title}}</strong>
                        <br>
                        <p class="d-description">{{dish.description}}</p>
                    </span>
                </div>
            </div>
        </article>
    </div>
</template>

<script>
    export default {
        name: 'dinner-item',
        props: {
            dish: Object
        }
    }
</script>

<style lang="sass">
.dish-item
    background-color: rgba(250, 250, 250, 0.4)
    margin: 0.2rem

.dish-item .image
    font-size: 2rem

.dish-item .d-description
    font-size: 0.7rem
</style>