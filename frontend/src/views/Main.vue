<template lang="html">
  <h1>Main</h1>
</template>

<script>
import bus from '../bus.js'
import axios from 'axios'

export default {
  data() {
    return {
      username: ''
    }
  },
  mounted() {
    bus.$on('register-success', (data) => {
      this.user = data;
    });

    var myuser = this.username;
    axios.post(this.url + '/getappliances', myuser)
    .then(function (response) {
      console.log(response);


    })
    .catch(function (error) {
      console.log(error);
    });
  }
}
</script>

<style lang="scss">
</style>
