<template lang="html">
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

  <h1>Welcome, {{ name }}</h1>
  <h3>Here are your household appliances.</h3>
  <div id="card-holder">

    <!-- SAMPLE CARDS -->
    <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        Component
      </p>
      <a href="#" class="card-header-icon" aria-label="more options">
        <span class="icon">
          <i class="fas fa-angle-down" aria-hidden="true"></i>
        </span>
      </a>
    </header>
    <div class="card-content">
      <div class="content">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.
        <a href="#">@bulmaio</a>. <a href="#">#css</a> <a href="#">#responsive</a>
        <br>
        <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
      </div>
    </div>
    <footer class="card-footer">
      <a href="#" class="card-footer-item">Save</a>
      <a href="#" class="card-footer-item">Edit</a>
      <a href="#" class="card-footer-item">Delete</a>
    </footer>
  </div>
</div>

</div>
</div>
</template>

<script>
export default {
  data() {
    return {
      name: 'Edwin',
      loggedIn: false,
      signInScreen: false
    }
  }
}
</script>

<style lang="scss">
#card-holder {
  width: 500px;
}
.card {
  margin-top: 10px;
}
</style>
