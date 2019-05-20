'use strict'

import dateFormat from 'dateformat';

dateFormat.i18n = {
  dayNames: [
	  'Вскр', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб',
	  'Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'
  ],
  monthNames: [
    'Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек',
    'Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря'
  ],
  timeNames: []
};

let getNow = function() {
  var now = new Date()
  return dateFormat(now, "dddd, d mmmm")
}

export { getNow };
