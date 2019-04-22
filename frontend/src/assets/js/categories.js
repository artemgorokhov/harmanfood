function getCategoryClass(category, withIcon) {
  let conformity = {
    'fire-alt': ['Популярное'],
    'sushi': ['Открытые роллы'],
    'hamburger': ['Бургеры'],
    'snacks': ['Закуски'],
    'cupcake': ['Десерты'],
    'baby': ['Детское меню'],
    'sauces': ['Соусы'],
    'wine-glass-alt': ['Напитки'],
    'drumstick-bite': ['Куриные  бургеры'],
    'fish': ['Рыбные бургеры'],
    'bucket': ['Букеты']
  }
  
  let subClass = 'utensils'
  for (let cl in conformity) {
    if (conformity[cl].indexOf(category) >= 0) {
      subClass = cl
      break;
    }
  }

  let catClass = withIcon ? `cat-${subClass} fa-${subClass}` : `cat-${subClass}`
  let result = {}
  result[catClass] = true
  return result
}

function getColorVariable(index, amount) {
  hue = index * 360 / amount
  return hue
}

export { getCategoryClass }
