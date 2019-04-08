/* jslint browser */
/* global window */

'use strict'

import axios from 'axios'

var formIsInvalid = function (login, passwd) {
  return !(login.length && passwd.length)
}

var submitForm = function (login, passwd, successCb, errorCb) {
  if (!formIsInvalid(login, passwd)) {
    axios.post('/login', {
      username: login,
      password: passwd
    })
      .then(successCb)
      .catch(errorCb)
  }
}

export { submitForm }
