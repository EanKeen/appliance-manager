<template>
  <div>
    <div v-if="!loggedIn">
      <div v-if="!loggedIn" class="not-logged-in">
        <h1>Hi! You don't seem to be signed in</h1>
        <h3>Please sign in to view personalized content</h3>
        <router-link to="/signin" class="router-link">
        <a class="buttoner button is-primary is-large">
          Sign In
        </a>
      </router-link>
      </div>
    </div>

    <div v-if="loggedIn" class="logged-in">
      <h1>Welcome, User</h1>
    </div>
  </div>
</template>

<script>
import NotSignedIn from '../components/NotSignedIn.vue';

export default {
  name: 'home',
  data() {
    return {
      name: "name",
      loggedIn: false,
      signInScreen: false
    }
  },
  methods: {
    test: function() {
      bus.$on('sign-in-screen', (data) => {
        this.name = data;
      });
    }
  },
  components: {
    NotSignedIn
  }
}
</script>

<style scoped lang="scss">

#mains {
  display: inline;
  height: 100%;

}

// Commented out because in globals
/*
.not-logged-in {
  height: 100%;
  margin-top: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

#button {
  margin-top: 15px;
}*/
</style>
