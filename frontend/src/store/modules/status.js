import { ACTION_NAMES, MUTATION_NAMES} from '@/store/consts'

const Stage = {
	'Initial': {
		description: 'Пока не присоединился',
		page: '/'
	},
	'Declined': {
		description: 'Отказывается есть',
		page: '/info'
	},
	'ChoosingPlace': {
		description: 'Выбирает ресторан',
		page: '/home/restaurants'
	},
	'ComposingDinner': {
		description: 'Выбирает еду',
		page: '/home/food'
	},
	'Ready': {
		description: 'Определился',
		page: '/info'
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
		userstage: Stage.Initial
	}
}

const mutations = {
	[MUTATION_NAMES.SET_CURRENT_STAGE] (state, stagename) {
	    state.userstage = Stage[stagename]
	    console.log('Current stage is ' + stagename)
	}
}

const getters = {
	isChoosingFood: (state) => () => {
		return state.userstage === Stage.ComposingDinner
	}
}

export const stage = {
	state,
	mutations,
	getters
}
