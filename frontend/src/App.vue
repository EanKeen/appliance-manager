<template>
  <div id="app">
    <div id="nav" v-if="navEnabled">
      <Menu/>
    </div>
    <router-view/>
  </div>
</template>

<script type="text/javascript">
    import Menu from '@/components/Menu.vue'

    export default {
      data() {
        return {
          navEnabled: true
        }
      },
      components: {
        Menu
      }
    }
</script>

<style scoped lang="scss">
#app {


}

</style>
