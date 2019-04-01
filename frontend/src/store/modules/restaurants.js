import { ACTION_NAMES, MUTATION_NAMES } from '@/store/consts'
import axios from 'axios'
import { createRestaurant } from '@/models/restaurant'

// TODO: use localStorage to cache food between sessions

const state = function () {
  return {
    restaurants: {
      'yandex': [],
      'delivery': [],
      'other': []
    }
  }
}

const mutations = {
  [MUTATION_NAMES.RESTAURANT_UPTODATE] (state, payload) {
    state.restaurants[payload.provider][payload.title].setUpdated(payload.updated)
  },
  [MUTATION_NAMES.RESTAURANT_LOADED] (state, payload) {
		console.log('Mutation restaurant ' + payload.title)
    state.restaurants[payload.provider][payload.title] = createRestaurant(payload)
  }
}

const actions = {
  async [ACTION_NAMES.UPDATE_MENU] ({commit}, payload) {
    try {
      if (!(payload.hasOwnProperty('title') && payload.hasOwnProperty('provider'))) {
        console.log('Wrong payload for menu')
      }
      const foodResp = await axios.post('/api/menu', payload)
      commit(MUTATION_NAMES.RESTAURANT_UPTODATE, {
        provider: foodResp.provider,
        title: foodResp.title,
        updated: true
      })
    } catch (error) {
      console.log('Menu request error: ' + error)
    }
  },
  async [ACTION_NAMES.UPDATE_RESTAURANT_LIST] ({commit}) {
    try {
      const restList = await axios.post('/api/restaurant_list')
      for (var i in restList.data.restaurants) {
        var r = restList.data.restaurants[i]
        commit(MUTATION_NAMES.RESTAURANT_LOADED, r)
      }
    } catch (error) {
      console.log('Error during fetch of restaurant data: ' + error)
      // TODO: Inform user that restaurant data is possibly outdated
    }
  }
}

export const restaurants = {
  actions,
  mutations,
  state
}
