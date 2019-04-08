import { MUTATION_NAMES, ACTION_NAMES } from '@/store/consts.js'
import axios from 'axios'
import { createUser } from '@/models/User'
import { mockInitialResp } from '@/store/mock/responses'

const state = function () {
  return {
    user: createUser(),
    currentStage: null,
    order: {
      patron: createUser(),
      phase: null
    },
    loaded: false
  }
}

const mutations = {
  [MUTATION_NAMES.SET_USER] (state, payload) {
    state.user = createUser(payload)
    console.log('Now user is ' + state.user.firstName)
  },
  [MUTATION_NAMES.SET_CURRENT_STAGE] (state, stage) {
    state.currentStage = stage
    console.log('Current stage is ' + state.currentStage)
  },
  [MUTATION_NAMES.FLAG_DATA_LOADED] (state) {
    console.log('MUTATION ' + state.user.firstName + ' loaded: ' + state.user.isLoaded)
    state.loaded = state.user.isLoaded
  },
  [MUTATION_NAMES.PATRON] (state, payload) {
    state.order.patron = createUser(payload)
  },
  'SOCKET_TEST' (msg) {
    console.log('Received message from socket: ' + msg)
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
  async [ACTION_NAMES.LOAD_DATA] ({commit, dispatch}) {
    try {
      await dispatch(ACTION_NAMES.LOAD_MAIN_INFO)
      console.log('User info is loaded successfully. Loading restaurants.')
      await dispatch(ACTION_NAMES.UPDATE_RESTAURANT_LIST)
      console.log('Restaurants are loaded. Flagging app is loaded')
      commit(MUTATION_NAMES.FLAG_DATA_LOADED)
    } catch (error) {
      console.error('Initial chain failed! ' + error)
      throw new Error(error)
    }
  },
  async [ACTION_NAMES.I_AM_PATRON] ({commit, state}) {
    try {
      console.log('I want to be a patron')
      if (process.env.NODE_ENV !== 'development') {
        await axios.post('/api/iampatron')
      } else {
        commit(MUTATION_NAMES.PATRON, state.user)
      }
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
