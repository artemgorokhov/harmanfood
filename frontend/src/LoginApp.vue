<template>
  <form>
    Login <input type="text" name="login" placeholder="LOGIN" v-model="login"/><br>
    Password <input type="text" name="pwd" placeholder="PASSWORD" v-model="passwd"/><br>
    <button v-on:click="submit" type="button" class="btn" ref="submitButton" disabled>Submit</button>
  </form>
</template>

<script>

// import { submitForm, eaterCredentials } from '@/assets/js/login_form.js'
import axios from 'axios'

var eaterCredentials = {
  login: '',
  passwd: ''
}

var formIsInvalid = function () {
  return !(eaterCredentials.login.length && eaterCredentials.passwd.length)
}

var submitForm = function () {
  console.log('Submit button clicked')
  if (!formIsInvalid()) {
    axios.post('/api/login', {
      username: eaterCredentials.login,
      password: eaterCredentials.passwd
    })
      .then(function (response) {
        if (!response.data.hasOwnProperty('result')) {
          console.log('Response without result...')
        }
        if (response.data.result === 'success') {
          console.log('All right, redirecting to home page')
          window.location.href = '/'
        } else {
          console.log('Wrong credentials!')
        }
      })
      .catch(function (error) {
        console.log('Error: ' + error)
      })
  }
}

var enableSubmitBtn = function () {
    this.$refs.submitButton.disabled = formIsInvalid();
};

export default {
  name: 'LoginApp',
  data: () => (
    eaterCredentials
  ),
  methods: {
    submit: submitForm
  },
  watch: {
    login: enableSubmitBtn,
    passwd: enableSubmitBtn
  }
}

</script>

<style lang="sass">

@import "@/assets/css/main.scss"

#loginApp
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

</style>
