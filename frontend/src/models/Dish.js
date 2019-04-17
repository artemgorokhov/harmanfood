export class Dish {
  constructor ({ title = ``, price = 0, category = ``,
    description = ``, selectedOptions = `` }) {
    this.title = title
    this._price = price
    this.category = category
    this.description = description
    this.selectedOptions = selectedOptions
  }

  get price () {
    return this._price
  }

  get isInBasket () {
    return true
  }

  // Unique field to differentiate a dish from other
  // when options will be ready for use
  get unique () {
    return this.title + this.selectedOptions
  }

  equal (b) {
    // This check does not take into account dish options yet
    const thesame = (this.title === b.title &&
      this.price === b.price &&
      this.description === b.description)
    return thesame
  }

  toString () {
    return this.title + ' (' + this.price + ')'
  }
}

export function createDish (payload) {
  return new Dish(payload)
}
