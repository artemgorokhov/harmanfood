<template>
    <div class="informationBlock">
        Information
    </div>
</template>

<script>
export default{
    name: 'information-block',
    data: () => ({
        patron: 'Artem'
    })
}
</script>

<style>
.informationBlock {
    min-width: 100px;
    min-height: 300px;
    background-color: rgb(189, 147, 228)
}
</style>
