<template>
    <nav class="navbar" id="mainMenu">
        <div class="navbar-brand">
            <div class="navbar-item">
                <div>
                <h1 class="title">HarmanFood</h1>
                <h2 class="subtitle has-text-centered">Обед в компании</h2>
                </div>
            </div>
        </div>
        <div class="navbar-start is-size-7" id="navMenu">
            <div class="nav-item">
                Home
            </div>
            <div class="nav-item">
                Help hand
            </div>
            <div class="nav-item">
                Logout
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'main-menu',
    data: () => ({
        show: true
    })
}
</script>

<style lang="sass">
#navMenu
    display: none
</style>