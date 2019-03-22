/* jslint browser */
/* global window */

'use strict'

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

export { submitForm, eaterCredentials }
