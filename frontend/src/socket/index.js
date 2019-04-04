import store from '@/store'
import SocketIO from 'socket.io-client'
import VueSocketIO from 'vue-socket.io'

const options = { path: '' }

export default new VueSocketIO({
  debug: true,
  connection: SocketIO('http://127.0.0.1:5000', options),
  vuex: {
    store,
    actionPrefix: 'SOCKET_',
    mutationPrefix: 'SOCKET_'
  }
})
