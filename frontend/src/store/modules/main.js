import { MUTATION_NAMES, ACTION_NAMES } from '@/store/consts.js'
import axios from 'axios'
import { createUser } from '@/models/User'

const state = function () {
  return {
    user: createUser(),
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
  [MUTATION_NAMES.FLAG_DATA_LOADED] (state) {
    console.log('MUTATION ' + state.user.firstName + ' loaded: ' + state.user.isLoaded)
    state.loaded = state.user.isLoaded
  },
  [MUTATION_NAMES.PATRON] (state, payload) {
    state.order.patron = createUser(payload)
  }
}

const actions = {
  async [ACTION_NAMES.LOAD_MAIN_INFO] ({commit}) {
    try {
      console.log('Getting main data')
      const initialResp = await axios.post('/api/initial_data')
      console.log('Initial data is: ' + Object.keys(initialResp.data))
      commit(MUTATION_NAMES.SET_USER, initialResp.data.user)
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
  }
}

export const mainModule = {
  state,
  mutations,
  actions
}
