import User from './user_info.js'

function install (Vue) {
  // User information
  var user = new User('Artem')

  Vue.getUserName = function () {
    console.log('Get username: ' + user.name)
    return user.name
  }

  Vue.setUserName = function (newname) {
    console.log('set username: ' + newname)
    user.name = newname
  }
}

export default install
