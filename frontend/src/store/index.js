import Vue from 'vue'
import Vuex from 'vuex'
import { restaurants } from '@/store/modules/restaurants'
import { dishes } from '@/store/modules/dishes'
import { stage } from '@/store/modules/status'
import { mainModule } from '@/store/modules/main'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    main: mainModule,
    restaurants: restaurants,
    dishes: dishes,
    stage: stage
  }
})

export default store
