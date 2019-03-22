/* jslint browser */
/* global window */

'use strict'

import axios from 'axios'


var formIsInvalid = function (login, passwd) {
  console.log("Checking form with" + login + " and " + passwd)
  return !(login.length && passwd.length)
}

var submitForm = function (login, passwd) {
  console.log('Submit button clicked')
  if (!formIsInvalid(login, passwd)) {
    axios.post('/api/login', {
      username: login,
      password: passwd
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

export { submitForm, formIsInvalid }
