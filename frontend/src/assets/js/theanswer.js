/* jslint browser */
/* global window */

'use strict'

import axios from 'axios'

var sendAnswer = function (participate) {
  console.log('The answer is ' + (participate ? 'YES!' : 'no...'))
}

export { sendAnswer }
