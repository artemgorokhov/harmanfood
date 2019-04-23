function getCategoryClass (category) {
  let conformity = {
    'fa-fire-alt': ['Популярное'], // Font awesome
    'ic-sushi': ['Открытые роллы', 'Суши и гунканы', 'Сладкие роллы',
      'Филадельфии', 'Вегетарианские роллы', 'Жареные роллы', 'Закрытые роллы',
      'Классические роллы', 'Сеты(ассорти)'],
    'fa-hamburger': ['Бургеры', 'Бургеры с говядиной'], // Font awesome
    'ic-french-fries': ['Закуски'],
    'ic-cupcake': ['Десерты'],
    'fa-baby': ['Джуниор меню'], // Font awesome
    'ic-sauces': ['Соусы', 'Дополнительно к заказу'],
    'ic-wok': ['Лапша'],
    'fa-wine-glass-alt': [], // Font awesome
    'ic-juice': ['Напитки'],
    'fa-drumstick-bite': ['Бургеры с курицей'], // Font awesome
    'fa-fish': ['Бургеры с рыбой'], // Font awesome
    'ic-bucket': ['Букеты']
  }

  let iconClass = 'fa-utensils' // Font awesome
  for (let cl in conformity) {
    if (conformity[cl].indexOf(category) >= 0) {
      iconClass = cl
      break
    }
  }
  let result = {}
  result[iconClass] = true
  return result
}

export { getCategoryClass }
