import store from '@/store'
import SocketIO from 'socket.io-client'
import VueSocketIO from 'vue-socket.io'

const options = { path: '/ws/' }

export default new VueSocketIO({
  debug: true,
  connection: SocketIO('', options),
  vuex: {
    store,
    actionPrefix: 'SOCKET_',
    mutationPrefix: 'SOCKET_'
  }
})
