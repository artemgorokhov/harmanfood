<template>
    <div class="box has-background-light
                has-text-dark"
          id="loginForm">
        <table class="table is-fullwidth">
            <thead>
                <tr><td><span class="centered">
                    <img src="@/assets/img/chef.svg" class="centered"/>
                </span></td></tr>
            </thead>
            <tfoot>
                <tr><td>
                    <a v-on:click="submit"
                       class="button is-success centered" 
                       :disabled="!(login && passwd)">Join in</a>
                </td></tr>
            </tfoot>
            <tbody>
                <tr><td><div class="control has-icons-left">
                    <input type="text" 
                         class="input"
                         v-model="login"
                         v-on:keyup.enter="submit"
                         placeholder="LOGIN"/>
                    <span class="icon is-left">
                        <i class="fas fa-user"></i>
                    </span>
                </div></td></tr>
                <tr><td><div class="control has-icons-left">
                    <input type="password" 
                         class="input"
                         :class="{'is-danger':wrongPasswd}"
                         v-on:keyup.enter="submit"
                         v-on:focus="(wrongPasswd = false)"
                         v-model="passwd" 
                         placeholder="PASSWORD"/>
                    <span class="icon is-left">
                        <i class="fas fa-lock"></i>
                    </span>
                </div></td></tr>
            </tbody>
        </table>
  </div>
</template>

<script>
import { submitForm } from '@/assets/js/login_form.js'

export default {
  name: 'login-form',
  data: () => ({
    login: '',
    passwd: '',
    wrongPasswd: false
  }),
  methods: {
    login_success: function (response) {
        console.log('All right, redirecting to home page')
        window.location.href = '/'
    },
    login_failure: function (error) {
        this.$data.wrongPasswd = true
    },
    submit: function() {
        if (!(this.$data.login && this.$data.passwd)) {
            return false;
        }
        submitForm(this.$data.login, this.$data.passwd,
                this.login_success, this.login_failure);
        this.$data.passwd = ''
    }
  }
}

</script>

<style lang="sass">
#loginForm
    border: 1px solid gray
    min-width: 50%
    max-width: 60%

#loginForm img
    height: 2.5em

#loginForm table
    background-color: rgba(0, 0, 0, 0)
#loginForm table tr td
    border: none

.centered
    margin: auto
    display: block

</style>