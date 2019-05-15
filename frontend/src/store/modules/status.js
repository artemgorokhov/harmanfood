import { MUTATION_NAMES } from '@/store/consts'

const Stage = {
  'NotStarted': {
    description: 'Пока не присоединился',
    page: '/'
  },
  'Declined': {
    description: 'Отказывается есть',
    page: '/summary'
  },
  'ChoosingPlace': {
    description: 'Выбирает ресторан',
    page: '/home/restaurants'
  },
  'ComposingDinner': {
    description: 'Выбирает еду',
    page: '/home/food'
  },
  'Delivery': {
    description: 'Определился',
    page: '/summary'
  },
  'Error': {
    description: 'Зашел в тупик',
    page: '/error'
  },
  'Loading': {
    description: 'Загрузка данных',
    page: '/loading'
  }
}

const state = function () {
  return {
    userstage: Stage.NotStarted
  }
}

const mutations = {
  [MUTATION_NAMES.SET_USER_STAGE] (state, stagename) {
    stagename = stagename || 'NotStarted'
    state.userstage = Stage[stagename]
    console.log('Current stage is ' + stagename)
  }
}

const getters = {
  isImmutable: (state) => () => {
    return [Stage.Error, Stage.Declined, Stage.Delivery].includes(state.userstage)
  }
}

export const stage = {
  state,
  mutations,
  getters
}
