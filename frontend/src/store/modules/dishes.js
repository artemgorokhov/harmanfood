import { ACTION_NAMES, MUTATION_NAMES } from '@/store/consts'
import axios from 'axios'
import { createDish } from '@/models/Dish'
import { mockFood } from '@/store/mock/responses'
import { createRestaurant } from '@/models/Restaurant'

const state = function () {
  return {
    restaurant_on_view: null,
    chosen_restaurant: null,
    dinner: [],
    menu: {}
  }
}

const mutations = {
  [MUTATION_NAMES.SWITCH_RESTAURANT] (state) {
    state.chosen_restaurant = createRestaurant(state.restaurant_on_view)
    state.dinner = []
    state.menu = {}
  },
  [MUTATION_NAMES.SET_DISHES_FOR_DINNER] (state, dishes) {
    state.dinner = [...dishes]
  },
  [MUTATION_NAMES.RESTAURANT_ON_VIEW] (state, restaurant) {
    state.restaurant_on_view = Object.assign({}, restaurant)
  },
  [MUTATION_NAMES.SET_MENU_FOR_RESTAURANT] (state, food) {
    state.menu = Object.assign({}, food)
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
    let newdinner = [...state.dinner]
    let olddinner = [...state.dinner]
    newdinner.push(createDish(payload))
    commit(MUTATION_NAMES.SET_DISHES_FOR_DINNER, newdinner)
    let dinnerTitles = []
    newdinner.forEach(function (element) {
      console.log('NEWDINNERTITLE: ' + Object.keys(element.title))
      dinnerTitles.push({
        title: element.title,
        category: element.category
      })
    })
    if (process.env.NODE_ENV !== 'development') {
      try {
        await axios.post('/api/menu', {
          food_list: dinnerTitles,
          restaurant: state.chosen_restaurant.title,
          provider: state.chosen_restaurant.provider
        })
      } catch (e) {
        console.error("Can't update dinner. Rolling back.")
        commit(MUTATION_NAMES.SET_DISHES_FOR_DINNER, olddinner)
      }
    }
  },
  async [ACTION_NAMES.REMOVE_DISH_FROM_MY_DINNER] ({commit, state}, dish) {
    let newdinner = [...state.dinner]
    let olddinner = [...state.dinner]
    newdinner.forEach(function(item){
      console.log("THEDINNER: " + item)  
    })
    console.log("DISH: " + dish.unique)
    let dishIndex = newdinner.map(x => x.unique).indexOf(dish.unique)
    // This check does not take into account dish options yet
    if (dishIndex === -1) {
      console.error('The dish ' + dish.unique + ' was not found in dinner')
      return
    }
    newdinner.splice(dishIndex, 1)
    commit(MUTATION_NAMES.SET_DISHES_FOR_DINNER, newdinner)
    let dinnerTitles = []
    newdinner.forEach(function (element) {
      console.log('SPLICEDDINNER: ' + Object.keys(element.title))
      dinnerTitles.push({
        title: element.title,
        category: element.category
      })
    })
    if (process.env.NODE_ENV !== 'development') {
      try {
        await axios.post('/api/menu', {
          food_list: dinnerTitles,
          provider: state.chosen_restaurant.provider,
          restaurant: state.chosen_restaurant.title
        })
      } catch (e) {
        console.error("Can't update dinner. Rolling back.")
        commit(MUTATION_NAMES.SET_DISHES_FOR_DINNER, olddinner)
      }
    }
  },
  async [ACTION_NAMES.UPDATE_MENU] ({commit}, payload) {
    try {
      if (!(payload.hasOwnProperty('title') && payload.hasOwnProperty('provider'))) {
        console.error('Wrong payload for menu')
      }
      var foodResp = mockFood
      if (process.env.NODE_ENV !== 'development') {
        foodResp = await axios.get('/api/menu', {params: payload})
        console.log('Food response: ' + Object.keys(foodResp.data))
      }
      console.log('Menu for ' + payload.title + ' has ' + foodResp.data.food.length + ' items')
      let foodByCategories = {}
      foodResp.data.food.forEach(foodItem => {
        if (!foodByCategories.hasOwnProperty(foodItem.category)) {
          foodByCategories[foodItem.category] = []
        }
        foodByCategories[foodItem.category].push(foodItem)
      })
      commit(MUTATION_NAMES.SET_MENU_FOR_RESTAURANT, foodByCategories)
      // commit(MUTATION_NAMES.RESTAURANT_UPTODATE, {
      //   provider: foodResp.data.provider,
      //   title: foodResp.data.restaurant,
      //   updated: true
      // })
    } catch (error) {
      console.error('Menu request error: ' + error)
    }
  },
  async [ACTION_NAMES.SET_VIEW_RESTAURANT] ({commit, state, rootState}, payload) {
    let rest = rootState.restaurants[payload.provider][payload.title]
    commit(MUTATION_NAMES.RESTAURANT_ON_VIEW, rest)
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
      return state.dinner
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
