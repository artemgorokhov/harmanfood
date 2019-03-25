<template>
    <section class="hero is-info">
        <div class="hero-body">
            <div class="container">
                <h1 class="title">
                    Harman Food
                </h1>
                <h2 class="subtitle has-text-centered">
                    Обед в тесном кругу
                </h2>
            </div>
        </div>
        <div class="hero-footer is-pulled-right">
            <main-menu/>
        </div>
    </section>
</template>

<script>
import MainMenu from './mainmenu.vue'

export default {
    name: 'hero-header',
    components: {
        MainMenu
    }
}
</script>
