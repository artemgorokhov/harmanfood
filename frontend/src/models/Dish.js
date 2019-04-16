export class Dish {
  constructor ({ title = ``, price = 0, description = ``,
    amount = 0, where = {} }) {
    this.title = title
    this.price = price
    this.description = description
    this.amount = amount
  }

  getPrice () {
    return this.amount * this.price
  }
}
