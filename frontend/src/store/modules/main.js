import { MUTATION_NAMES, ACTION_NAMES } from '@/store/consts.js'
import axios from 'axios'
import { createUser } from '@/models/User'
import { mockInitialResp, mockOrderResp } from '@/store/mock/responses'

const state = function () {
  return {
    user: createUser(),
    order: {
      patron: createUser(),
      participants: [],
      phase: null,
      total: 0
    },
    loaded: false
  }
}

const mutations = {
  [MUTATION_NAMES.SET_USER] (state, payload) {
    state.user = createUser(payload)
    console.log('Now user is ' + state.user.firstName)
  },
  [MUTATION_NAMES.FLAG_DATA_LOADED] (state) {
    console.log('MUTATION ' + state.user.firstName + ' loaded: ' + state.user.isLoaded)
    state.loaded = state.user.isLoaded
  },
  [MUTATION_NAMES.ORDER] (state, payload) {
    state.order.patron = createUser(payload.patron)
    state.order.participants = [...payload.participants]
    state.order.total = payload.total
    state.order.phase = payload.phase
  },
  [MUTATION_NAMES.PATRON] (state, payload) {
    state.order.patron = createUser(payload)
  },
  'SOCKET_TEST' (msg) {
    console.log('Received message from socket: ' + msg)
  },
  'SOCKET_ORDER' (state, msg) {
    console.log('Order is ' + state.order)
    state.order.patron = createUser(msg.patron)
    state.order.participants = [...msg.participants]
    state.order.total = msg.total
    state.order.phase = msg.phase
  }
}

const actions = {
  async [ACTION_NAMES.LOAD_MAIN_INFO] ({commit}) {
    try {
      console.log('Getting main data for ' + process.env.NODE_ENV)
      var initialResp = mockInitialResp
      if (process.env.NODE_ENV !== 'development') {
        initialResp = await axios.get('/api/initial_data')
      }
      console.log('Initial data is: ' + Object.keys(initialResp.data))
      commit(MUTATION_NAMES.SET_USER, initialResp.data.user)
      commit(MUTATION_NAMES.SET_CURRENT_STAGE, initialResp.data.curre)
    } catch (error) {
      console.error('Error during loading initial data: ' + error)
      throw new Error(error)
    }
  },
  async [ACTION_NAMES.LOAD_ORDER_DATA] ({commit}) {
    try {
      console.log('Loading data for info block')
      var infoResp = mockOrderResp
      if (process.env.NODE_ENV !== 'development') {
        infoResp = await axios.get('/api/order')
      }
      console.log('Order data is: ' + Object.keys(infoResp.data))
      commit(MUTATION_NAMES.ORDER, infoResp.data)
    } catch (e) {
      console.error(e)
      console.error("Can't load data for info block")
    }
  },
  async [ACTION_NAMES.LOAD_DATA] ({commit, dispatch}) {
    try {
      await dispatch(ACTION_NAMES.LOAD_MAIN_INFO)
      await dispatch(ACTION_NAMES.UPDATE_RESTAURANT_LIST)
      await dispatch(ACTION_NAMES.LOAD_ORDER_DATA)
      commit(MUTATION_NAMES.FLAG_DATA_LOADED)
    } catch (error) {
      console.error('Initial chain failed! ' + error)
      throw new Error(error)
    }
  },
  async [ACTION_NAMES.I_AM_PATRON] ({commit, state}) {
    try {
      console.log('I want to be a patron')
      let newpatron = createUser(state.user)
      if (process.env.NODE_ENV !== 'development') {
        newpatron = await axios.post('/api/iampatron')
      }
      commit(MUTATION_NAMES.PATRON, newpatron)
    } catch (error) {
      console.error('Patron request failed: ' + error)
      throw new Error(error)
    }
  }
}

export const mainModule = {
  state,
  mutations,
  actions
}
