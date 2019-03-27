import Vue from 'vue'
import Vuex from 'vuex'
import { MUTATION_NAMES, ACTION_NAMES } from './consts.js'

Vue.use(Vuex)

const state = {
  user: 'Anonymous',
  loaded: false
}

const mutations = {
  [MUTATION_NAMES.SET_USERNAME] (state, username) {
    state.user = username
  },
  [MUTATION_NAMES.FLAG_DATA_LOADED] (state) {
    state.loaded = true
  }
}

const actions = {
  [ACTION_NAMES.GET_USER_INFO] ({commit}) {
    // Here we will need to make async call to server to get data
    // For now there is a async-like mock
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        commit(MUTATION_NAMES.SET_USERNAME, 'Артём')
        commit(MUTATION_NAMES.FLAG_DATA_LOADED)
        resolve()
      }, 2000)
    })
  }
}

const store = new Vuex.Store({
  state,
  mutations,
  actions
})

export default store
