import { ACTION_NAMES, MUTATION_NAMES} from '@/store/consts'

const Stage = {
	'Initial': 'Пока не присоединился',
	'Declined': 'Отказывается есть',
	'ChoosingPlace': 'Выбирает ресторан',
	'ComposingDinner': 'Выбирает еду',
	'Ready': 'Определился'
}


const state = function () {
	return {
		page: '/',
		userstage: Stage.Initial
	}
}