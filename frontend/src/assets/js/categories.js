function getCategoryClass(category, withIcon) {
	let popular = withIcon ? 'cat-popular fa-fire-alt' : 'cat-popular'
    let sushi = withIcon ? 'cat-sushi fa-sushi' : 'cat-sushi'
    let burger = withIcon ? 'cat-burger fa-hamburger' : 'cat-burger'
    const cObj = {}
    cObj[popular] = category === 'Популярное'
    cObj[sushi] = category === 'Открытые роллы'
    cObj[burger] = category === 'Бургеры'
    return cObj
}

export { getCategoryClass }
