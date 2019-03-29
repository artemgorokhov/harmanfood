/* jslint browser */
/* global window */

'use strict'

import axios from 'axios'

var formIsInvalid = function (login, passwd) {
  return !(login.length && passwd.length)
}

var submitForm = function (login, passwd, successCb, errorCb) {
  if (!formIsInvalid(login, passwd)) {
    // instance - only for development
    // const instance = axios.create({baseURL: 'http://localhost:5000'})
    // instance.post('/api/login', {
    axios.post('/api/login', {
      username: login,
      password: passwd
    })
      .then(successCb)
      .catch(errorCb)
  }
}

export { submitForm }
