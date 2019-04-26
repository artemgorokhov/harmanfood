import store from '@/store'
import SocketIO from 'socket.io-client'
import VueSocketIO from 'vue-socket.io'

export const SocketInstance = SocketIO('/ws')

export default new VueSocketIO({
  debug: true,
  connection: SocketInstance,
  vuex: {
    store,
    actionPrefix: 'SOCKET_',
    mutationPrefix: 'SOCKET_'
  }
})
