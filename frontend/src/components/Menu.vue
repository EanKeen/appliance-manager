<template lang="html">
  <div v-if="!signInScreen">
  <nav class="navbar is-transparent">
    <div class="navbar-brand">
      <a class="navbar-item">
        <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
      </a>
      <div class="navbar-burger burger" data-target="navbarExampleTransparentExample">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>


    <div id="navbarExampleTransparentExample" class="navbar-menu">
    <div class="navbar-start">
        <a class="navbar-item">
          <router-link to="/" class="router-link">
          Home
        </router-link>
        </a>
        <a class="navbar-item">
          <router-link to="/items" class="router-link">
          My Products
        </router-link>
        </a>
      <a class="navbar-item">
        <router-link to="/information" class="router-link">
        Info
        </router-link>
      </a>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="field is-grouped">
          <p class="control">

          </p>
          <p class="control">
            <a @click="signInClick" class="button is-primary">
              <router-link to="/signin" class="router-link router-link-button">
              <!-- <span class="icon">
                <i class="fas fa-download"></i>
              </span> -->
              <span>
                Sign In
              </span>
              </router-link>
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</nav>
</div>


</template>

<script>
import bus from '../bus.js'

export default {
  data() {
    return {
      // Change sign in message to 'Hello User'
      signInMessage: 'Sign in',

      // Boolean for if sign in screen is active
      signInScreen: false,

      // Boolean for if user is signed in
      signIn: false
    }
  },
  methods: {
    signInClick: function() {
      this.signInScreen = !this.signInScreen;
    }
  }
}
</script>

<style scoped lang="scss">
@import '@/styles/variables.scss';

</style>
