<template>
  <login-form/>
</template>

<script>
import LoginForm from '@/components/login/login_form.vue'

export default {
    name: 'LoginApp',
    components: {
        LoginForm
    }
}
</script>

<style lang="sass">

@import "@/assets/css/main.scss"

#loginApp
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

</style>
