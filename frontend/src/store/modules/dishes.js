import { ACTION_NAMES, MUTATION_NAMES } from '@/store/consts'
import axios from 'axios'
import createDish from '@/models/Dish'

const state = function () {
  return {
    restaurant_on_view: null,
    chosen_restaurant: null,
    dishes: []
  }
}

const mutations = {
  [MUTATION_NAMES.SWITCH_RESTAURANT] (state) {
    state.chosen_restaurant = state.restaurant_on_view
    state.dishes = []
  },
  [MUTATION_NAMES.SET_DISHES_FOR_DINNER] (state, dishes) {
    state.dishes = dishes
  },
  [MUTATION_NAMES.CURRENT_RESTAURANT] (state, restaurant) {
    state.restaurant_on_view = restaurant
  }
}

const actions = {
  async [ACTION_NAMES.SWITCH_RESTAURANT] ({commit, state}) {
    // Not really async yet
    if (!state.chosen_restaurant.equal(state.restaurant_on_view)) {
      console.log('Change restaurant of my dinner from ' + state.chosen_restaurant.title + ' to ' + state.restaurant_on_view.title)
      commit(MUTATION_NAMES.SWITCH_RESTAURANT)
    } else {
      console.log('Requested to switch restaurant, but it is the same already')
    }
  },
  async [ACTION_NAMES.ADD_DISH_TO_MY_DINNER] ({commit, state}, payload) {
    if (state.chosen_restaurant == null || !state.chosen_restaurant.equal(state.restaurant_on_view)) {
      commit(MUTATION_NAMES.SWITCH_RESTAURANT)
    }
    state.dishes.push(createDish(payload))
    commit(MUTATION_NAMES.SET_DISHES_FOR_DINNER, dishes)
  },
  async [ACTION_NAMES.REMOVE_DISH_FROM_MY_DINNER] ({commit, state}, dish) {
    let dishIndex = state.dishes.map(x => x.unique).indexOf(dish.unique)
    // This check does not take into account dish options yet
    if (dishIndex >= 0) {
      dishes.splice(dishIndex, 1)
      commit(MUTATION_NAMES.SET_DISHES_FOR_DINNER, dishes)
    }
  }
}

const getters = {
  getByRestaurant: (state) => () => {
    if (state.chosen_restaurant.equal(state.restaurant_on_view)) {
      let dishList = []
      for (var dishtitle in state.dishes) {
        if (state.dishes.hasOwnProperty(dishtitle)) {
          dishList.push(state.dishes[dishtitle])
        }
      }
      return dishList
    }
    return []
  }
}

export const dishes = {
  actions,
  mutations,
  state,
  getters
}
