import Vue from 'vue'
import Vuex from 'vuex'
import { MUTATION_NAMES } from './consts.js'

Vue.use(Vuex)

const state = {
  user: 'Artem'
}

const mutations = {
  [MUTATION_NAMES.SET_USERNAME] (state, username) {
    state.user = username
  }
}

const store = new Vuex.Store({
  state,
  mutations
})

export default store
