import Vue from 'vue'
import Vuex from 'vuex'
import { MUTATION_NAMES, ACTION_NAMES } from './consts.js'
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
  [ACTION_NAMES.GET_USER_INFO] ({commit}) {
    return new Promise((resolve, reject) => {
      // const instance = axios.create({baseURL: 'http://localhost:5000'})
      // instance.post('/api/initial_data')
        axios.post('/api/initial_data')
              .then((response) => {
                console.log('Response is: ' + response.data)
                if (!(response.data.user &&response.data.restaurants)) {
                  throw new Error('Wrong payload')
                }
                user = response.data.user
                restaurants = response.data.restaurants
                commit(MUTATION_NAMES.SET_USERNAME, response.data.firstName)
                
                commit(MUTATION_NAMES.FLAG_DATA_LOADED)
                resolve()
              })
              .catch((error) => {
                console.log("error response: " + error)
                reject()
              })
    })
  }
}

const store = new Vuex.Store({
  state,
  mutations,
  actions
})

export default store
