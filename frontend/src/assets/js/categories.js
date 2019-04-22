function getCategoryClass(category) {
  let conformity = {
    'fa-fire-alt': ['Популярное'], //Font awesome
    'fa-sushi': ['Открытые роллы'],
    'fa-hamburger': ['Бургеры'], //Font awesome
    'fa-snacks': ['Закуски'],
    'fa-cupcake': ['Десерты'],
    'fa-baby': ['Детское меню'], //Font awesome
    'fa-sauces': ['Соусы'],
    'fa-wine-glass-alt': ['Напитки'], //Font awesome
    'fa-drumstick-bite': ['Куриные  бургеры'], //Font awesome
    'fa-fish': ['Рыбные бургеры'], //Font awesome
    'fa-bucket': ['Букеты']
  }
  
  let iconClass = 'fa-utensils' //Font awesome
  for (let cl in conformity) {
    if (conformity[cl].indexOf(category) >= 0) {
      iconClass = cl
      break;
    }
  }
  let result = {}
  result[iconClass] = true
  return result
}

function getColorVariable(index, amount) {
  hue = index * 360 / amount
  return hue
}

export { getCategoryClass }
