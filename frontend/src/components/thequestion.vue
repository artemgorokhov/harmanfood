<template>
    <div class="container" id="theQuestion">
        <p class="has-text-centered
                   is-size-1">
               Хочешь пообедать?
        </p>
        <nav class="level buttons-level">
            <a class="button 
                    level-left
                    is-success
                    is-large">Да!</a>
            <a class="button 
                    level-right
                    is-danger
                    is-large
                    is-outlined">Не</a>
        </nav>
    </div>
</template>

<style lang="sass">
.buttons-level
    margin-left: 35%
    margin-right: 35%

.buttons-level a
    padding-left: 2em
    padding-right: 2em
#theQuestion
    margin-top: -30%
</style>