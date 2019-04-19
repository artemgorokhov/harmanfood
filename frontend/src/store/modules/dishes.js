import { ACTION_NAMES, MUTATION_NAMES } from '@/store/consts'
import axios from 'axios'
import { createDish } from '@/models/Dish'
import { mockFood } from '@/store/mock/responses'

const state = function () {
  return {
    restaurant_on_view: null,
    chosen_restaurant: null,
    dinner: [],
    menu: []
  }
}

const mutations = {
  [MUTATION_NAMES.SWITCH_RESTAURANT] (state) {
    state.chosen_restaurant = state.restaurant_on_view
    state.dinner = []
  },
  [MUTATION_NAMES.SET_DISHES_FOR_DINNER] (state, dishes) {
    state.dinner = dishes
  },
  [MUTATION_NAMES.CURRENT_RESTAURANT] (state, restaurant) {
    state.restaurant_on_view = restaurant
  },
  [MUTATION_NAMES.SET_MENU_FOR_RESTAURANT] (state, food) {
    state.menu = food
  }
}

const actions = {
  async [ACTION_NAMES.SWITCH_RESTAURANT] ({commit, state}) {
    // Not really async yet
    if (state.chosen_restaurant === null ||
      !state.chosen_restaurant.equal(state.restaurant_on_view)) {
      console.log('Change restaurant of my dinner from ' + state.chosen_restaurant.title + ' to ' + state.restaurant_on_view.title)
      commit(MUTATION_NAMES.SWITCH_RESTAURANT)
    } else {
      console.log('Requested to switch restaurant, but it is the same already')
    }
  },
  async [ACTION_NAMES.ADD_DISH_TO_MY_DINNER] ({commit, state}, payload) {
    if (state.chosen_restaurant == null ||
      !state.chosen_restaurant.equal(state.restaurant_on_view)) {
      commit(MUTATION_NAMES.SWITCH_RESTAURANT)
    }
    let dinner = state.dinner
    dinner.push(createDish(payload))
    commit(MUTATION_NAMES.SET_DISHES_FOR_DINNER, dinner)
  },
  async [ACTION_NAMES.REMOVE_DISH_FROM_MY_DINNER] ({commit, state}, dish) {
    let dinner = state.dinner
    let dishIndex = dinner.map(x => x.unique).indexOf(dish.unique)
    // This check does not take into account dish options yet
    if (dishIndex >= 0) {
      dinner.splice(dishIndex, 1)
      commit(MUTATION_NAMES.SET_DISHES_FOR_DINNER, dinner)
    }
  },
  async [ACTION_NAMES.UPDATE_MENU] ({commit}, payload) {
    try {
      if (!(payload.hasOwnProperty('restaurant') && payload.hasOwnProperty('provider'))) {
        console.error('Wrong payload for menu')
      }
      var foodResp = mockFood
      if (process.env.NODE_ENV !== 'development') {
        foodResp = await axios.post('/api/menu', payload)
        console.log('Food response: ' + Object.keys(foodResp.data))
      }
      console.log('Menu for ' + payload.restaurant + ' has ' + foodResp.data.food.length + ' items')
      commit(MUTATION_NAMES.SET_MENU_FOR_RESTAURANT, foodResp.data.food)
      // commit(MUTATION_NAMES.RESTAURANT_UPTODATE, {
      //   provider: foodResp.data.provider,
      //   title: foodResp.data.restaurant,
      //   updated: true
      // })
    } catch (error) {
      console.error('Menu request error: ' + error)
    }
  }
}

const getters = {
  getByRestaurant: (state) => () => {
    if (state.chosen_restaurant === null) {
      console.log('No restaurant is chosen yet')
      return []
    }
    if (state.chosen_restaurant.equal(state.restaurant_on_view)) {
      console.log('Get selected dishes for this restaurant')
      return state.dishes
    }
    console.log('Getting dishes from another restaurant')
    return []
  }
}

export const dishes = {
  actions,
  mutations,
  state,
  getters
}
