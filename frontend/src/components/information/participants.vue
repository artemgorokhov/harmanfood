<template>
    <div>
        <div v-for="user in users" :key="user.id" class="card">
            <div class="card-content">
                {{ user.name }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'participants',
    data: () => ({
        users: [
            { name: 'Артем' },
            { name: 'Дмитрий'}
        ]
    })
}
</script>