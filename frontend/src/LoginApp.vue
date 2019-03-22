<template>
  <form>
    Login <input type="text" name="login" placeholder="LOGIN" v-model="login"/><br>
    Password <input type="text" name="pwd" placeholder="PASSWORD" v-model="passwd"/><br>
    <button v-on:click="submit" type="button" class="btn" ref="submitButton" disabled>Submit</button>
  </form>
</template>

<script>
export default {
  name: 'LoginApp'
}
</script>

<style lang="sass">

@import "@/assets/css/main.scss"

#loginApp
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

</style>
