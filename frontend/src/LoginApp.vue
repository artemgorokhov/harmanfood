<template>
    <section class="hero is-fullheight 
                    has-background-dark">
        <div class="hero-body is-paddingless">
        <div class="container 
                    columns
                    is-fluid
                    welcomeContainer">
            <div class="column is-half 
                        has-text-light">
                <div class="welcomeTitle">
                <h1 class="is-size-3"> {{ welcome_message }} </h1>
                <h2 class="is-size-6"> 
                    {{ welcome_description }} 
                </h2>
            </div>
            </div>
            <div class="column
                        has-text-dark">
                <login-form/>
            </div>
        </div>
        </div>
    </section>
</template>

<script>
import LoginForm from '@/components/login/login_form.vue'

export default {
    name: 'LoginApp',
    data: () => ({
        welcome_message: "Добро пожаловать, едок!",
        welcome_description: "Пожалуйста, представься. Так ты сможешь присоединиться к нашему скромному обеду."
    }),
    components: {
        LoginForm
    }
}
</script>

<style lang="sass">

@import "@/assets/css/contrast_theme.scss"

#loginApp
    -webkit-font-smoothing: antialiased
    -moz-osx-font-smoothing: grayscale

.welcomeContainer .column
    padding: 2em

.welcomeTitle
    margin-right: 0
    margin-left: auto
    max-width: 80%
    text-align: center

.welcomeTitle h1
    text-decoration: underline

</style>
