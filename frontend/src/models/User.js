export class User {
  constructor ({ firstName = ``, lastName = ``, phone = `` } = {}) {
    this.firstName = firstName
    this.lastName = lastName
    this.phone = phone
  }

  get fullName () {
    return this.firstName + ' ' + this.lastName
  }

  get isLoaded () {
    return !!this.firstName
  }
}

export function createUser (data) {
  return new User(data)
}
