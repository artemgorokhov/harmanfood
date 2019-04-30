export class Restaurant {
  constructor ({ title = ``, provider = ``, hash = ``, asset = ``, categories = [] } = {}) {
    this.title = title
    this.provider = provider
    this.hash = hash
    this.asset = asset
    this.categories = [...categories]
    this.updated = false
  }

  update () {
    // TODO: update menu and restaurant cache
    this.updated = true
  }

  outdated () {
    return !this.updated
  }

  setUpdated (updated) {
    this.udpated = updated
  }

  equal (b) {
    if (!b.hasOwnProperty('hash')) {
      return false
    }
    const thesame = (b.title === this.title && b.provider === this.provider)
    if (!thesame) {
      return false
    }
    this.updated = (this.hash === b.hash)
    return true
  }
}

export function createRestaurant (data) {
  return new Restaurant(data)
}
