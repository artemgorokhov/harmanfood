<template>
    <div id="mainMenu">
        MENU!! {{ show }}
    </div>
</template>

<script>
export default {
    name: 'main-menu',
    data: () => ({
        show: true
    })
}
</script>

<style>
    #mainMenu {
        font-family: sans-serif;
        background-color: #abc;
        max-width: 500px;
    }
</style>