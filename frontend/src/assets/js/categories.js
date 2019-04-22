function getCategoryClass (category, withIcon) {
  let popular = withIcon ? 'cat-popular fa-fire-alt' : 'cat-popular' // Font awesome
  let sushi = withIcon ? 'cat-sushi fa-sushi' : 'cat-sushi'
  let hamburger = withIcon ? 'cat-hamburger fa-hamburger' : 'cat-hamburger' // Font awesome
  let snacks = withIcon ? 'cat-snacks fa-snacks' : 'cat-snacks'
  let dessert = withIcon ? 'cat-cupcake fa-cupcake' : 'cat-cupcake'
  let junior = withIcon ? 'cat-baby fa-baby' : 'cat-baby' // Font awesome
  let sauces = withIcon ? 'cat-sauces fa-sauces' : 'cat-sauces'
  let beverages = withIcon ? 'cat-beverages fa-wine-glass-alt' : 'cat-beverages' // Font awesome
  let pigburger = withIcon ? 'cat-pigburger fa-pigburger' : 'cat-pigburger'
  let chicken = withIcon ? 'cat-chicken fa-drumstick-bite' : 'cat-chicken'
  let fish = withIcon ? 'cat-fish fa-fish' : 'cat-fish'
  let bucket = withIcon ? 'cat-bucket fa-bucket' : 'cat-bucket'
  const cObj = {}
  cObj[popular] = category === 'Популярное'
  cObj[sushi] = category === 'Открытые роллы'
  cObj[hamburger] = category === 'Бургеры'
  return cObj
}

export { getCategoryClass }
