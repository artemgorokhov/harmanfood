import store from '@/store'
import SocketIO from 'socket.io-client'
import VueSocketIO from 'vue-socket.io'

export default new VueSocketIO({
  debug: true,
  connection: SocketIO('http://127.0.0.1:5000/ws'),
  vuex: {
    store,
    actionPrefix: 'SOCKET_',
    mutationPrefix: 'SOCKET_'
  }
})
