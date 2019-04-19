import { ACTION_NAMES, MUTATION_NAMES } from '@/store/consts'
import axios from 'axios'
import { createRestaurant } from '@/models/Restaurant'
import { mockRestaurants } from '@/store/mock/responses'

// TODO: use localStorage to cache food between sessions

const state = function () {
  return {
    'yandex': {},
    'delivery': {},
    'other': {}
  }
}

const mutations = {
  [MUTATION_NAMES.RESTAURANT_UPTODATE] (state, payload) {
    state[payload.provider][payload.title].setUpdated(payload.updated)
  },
  [MUTATION_NAMES.RESTAURANT_LOADED] (state, payload) {
    console.log('Mutating restaurant ' + payload.title)
    state[payload.provider][payload.title] = createRestaurant(payload)
  }
}

const actions = {
  async [ACTION_NAMES.UPDATE_RESTAURANT_LIST] ({commit}) {
    try {
      var restList = mockRestaurants
      if (process.env.NODE_ENV !== 'development') {
        restList = await axios.get('/api/restaurant_list')
      }
      console.log('Rests: ' + Object.keys(restList.data))
      for (var i in restList.data.restaurants) {
        var r = restList.data.restaurants[i]
        commit(MUTATION_NAMES.RESTAURANT_LOADED, r)
      }
    } catch (error) {
      console.error('Error during fetch of restaurant data: ' + error)
      // TODO: Inform user that restaurant data is possibly outdated
    }
  }
}

const getters = {
  getByProvider: (state) => (id) => {
    return state[id]
  }
}

export const restaurants = {
  actions,
  mutations,
  state,
  getters
}
