export class User {
  constructor ({ firstName = ``, lastName = ``, phone = `` } = {}) {
    console.log('User constructor ' + firstName)
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
  if (!data) {
    return new User()
  }
  return new User(data)
}
