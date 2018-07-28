<template lang="html">

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
      <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            <router-link to="/info" class="router-link">
            Info
            </router-link>
          </a>
        <div class="navbar-dropdown is-boxed">
          <a class="navbar-item">
            <router-link to="/about" class="router-link">
            About
            </router-link>
          </a>
          <a class="navbar-item">
            <router-link to="/terms" class="router-link">
            Terms
          </router-link>
          </a>
        </div>
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="field is-grouped">
          <p class="control">

          </p>
          <p class="control">
            <a class="button is-primary">
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


</template>

<script>
export default {
  data() {
    return {
      // Change sign in message to 'Hello User'
      signInMessage: 'Sign in',

      // Boolean for is signed in
      signIn: false
    }
  }
}
</script>

<style scoped lang="scss">
@import '@/styles/variables.scss';

</style>
