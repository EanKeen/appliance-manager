<template>
  <div id="app">
    <div id="nav">
      <Menu/>
    </div>
    <div id="router-view">
      <router-view/>
    </div>
  </div>
</template>

<script type="text/javascript">
import bus from './bus.js'
import Menu from '@/components/Menu.vue'

    export default {
      data() {
        return {

        }
      },
      components: {
        Menu
      }
    }
</script>

<style scoped lang="scss">
#router-view {
  height: 100%;
  margin-left: 20px;
  margin-right: 20px;
}

</style>
