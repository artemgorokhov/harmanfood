<template>
    <nav class="tabs is-right">
		<div class="container">
		<ul>
			<li class="is-active"><a>Мой заказ</a></li>
			<li><a>Помочь с заказом</a></li>
			<li><a href="/login">Logout</a></li>
		</ul>
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
