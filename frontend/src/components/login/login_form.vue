<template>
    <form>
    Login <input type="text" 
                 v-model="login" 
                 v-on:input="changeSubmitStatus"
                 placeholder="LOGIN"/>
            <br>
    Password <input 
                 type="text" 
                 v-model="passwd" 
                 v-on:input="changeSubmitStatus"
                 placeholder="PASSWORD"/>
            <br>
    <button v-on:click="submit" 
            type="button" 
            class="btn" 
            ref="submitButton" disabled>Submit</button>
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