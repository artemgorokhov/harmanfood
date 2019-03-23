<template>
    <form class="has-background-light
                 has-text-dark"
          id="loginForm">
        <table class="table is-fullwidth">
            <thead>
                <tr><td><div class="centered">
                    <i class="far fa-user"></i>
                </div></td></tr>
            </thead>
            <tfoot>
                <tr><td>
                    <button v-on:click="submit" 
                        type="button" 
                        class="btn centered" 
                        ref="submitButton" disabled>Submit</button>
                </td></tr>
            </tfoot>
            <tbody>
                <tr><td>
                    <input type="text" 
                         class="centered"
                         v-model="login" 
                         v-on:input="changeSubmitStatus"
                         placeholder="LOGIN"/>
                </td></tr>
                <tr><td>
                    <input type="text" 
                         class="centered"
                         v-model="passwd" 
                         v-on:input="changeSubmitStatus"
                         placeholder="PASSWORD"/>
                    
                </td></tr>
            </tbody>
        </table>
  </form>
</template>

<script>
import { submitForm, formIsInvalid } from '@/assets/js/login_form.js'

export default {
  name: 'login-form',
  data: () => ({
    login: '',
    passwd: ''
  }),
  methods: {
    submit: function() {
        submitForm(this.$data.login, this.$data.passwd);
    },
    changeSubmitStatus: function() {
        this.$refs.submitButton.disabled = formIsInvalid(this.$data.login, this.$data.passwd);
    }
  }
}

</script>

<style lang="sass">
#loginForm
    border: 1px solid gray;
    max-width: 50%;

#loginForm table
    background-color: rgba(0, 0, 0, 0);
#loginForm table tr td
    border: none;

#loginForm input
    font-size: 1em;
    width: 75%;

.centered
    margin: auto
    display: block

</style>