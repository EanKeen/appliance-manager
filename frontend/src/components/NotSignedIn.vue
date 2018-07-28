<template>
  <div v-if="!loggedIn" class="not-logged-in">
    <h1>Hi! You don't sem to be signed in</h1>
    <h3>Please sign in to view personalized content</h3>
    <a class="buttoner button is-primary is-large">Sign In</a>
  </div>
</template>

<script>

export default {
  name: 'home',
  data() {
    return {
      name: "name",
      loggedIn: false
    }
  },
  methods: {
    test: function() {
      bus.$on('infoLocationChanged', (data) => {
        this.name = data;
      });
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
.not-logged-in {
  height: 100%;
  margin-top: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.buttoner {
  margin-top: 15px;
}
</style>
