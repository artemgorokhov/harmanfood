import Vue from 'vue'
import Vuex from 'vuex'
import { MUTATION_NAMES, ACTION_NAMES } from './consts.js'
import { restaurants } from '@/store/modules/restaurants'
import axios from 'axios'

Vue.use(Vuex)

const state = {
  user: 'Anonymous',
  loaded: false,
  patron: {name: 'Артём Горохов',
    phone: '+7 951 902 00 46'}
}

const mutations = {
  [MUTATION_NAMES.SET_USERNAME] (state, username) {
    state.user = username
  },
  [MUTATION_NAMES.FLAG_DATA_LOADED] (state) {
    state.loaded = true
  },
  [MUTATION_NAMES.PATRON] (state, patron) {
    state.patron = patron
  }
}

const actions = {
  async [ACTION_NAMES.GET_USER_INFO] ({commit}) {
    try {
      console.log('Getting initial data')
      const initialResp = await axios.post('/api/initial_data')
      console.log('Initial data is: ' + Object.keys(initialResp.data))
      commit(MUTATION_NAMES.SET_USERNAME, initialResp.data.user.firstName)
      commit(MUTATION_NAMES.FLAG_DATA_LOADED)
    } catch (error) {
      console.log('Error during loading initial data: ' + error)
    }
  },
  async [ACTION_NAMES.INITIAL_DATA] ({commit, dispatch}) {
    try {
      await dispatch(ACTION_NAMES.GET_USER_INFO)
      console.log('User info is loaded successfully')
      await dispatch(ACTION_NAMES.UPDATE_RESTAURANT_LIST)
      console.log('Loaded restaurants')
    } catch (error) {
      console.log('Initial chain failed! ' + error)
    }
  }
}

const mainModule = {
  state,
  mutations,
  actions
}

const store = new Vuex.Store({
  modules: {
    main: mainModule,
    restaurants: restaurants
  }
})

export default store
