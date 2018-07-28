<template>
  <div id="mains">


  <div class="not-logged-in">

    <div class="card">
      <div class="card-content">
        <p class="title">
          Sign In
        </p>
        <div class="man-flex">

          <div class="user flex">
            <h3>Username</h3>
            <input id="top" type="text"></input>
          </div>
          <div class="pass flex">
            <h3>Password</h3>
            <input type="text"></input>
          </div>

        </div>
      </div>
      <footer class="card-footer">
        <div class="back">
          <a id="left-button" class="button is-primary is-info">
            <router-link to="/" class="router-link">
            Back
          </router-link>
          </a>
          <a class="button is-primary is-normal">Submit</a>

        </div>
      </footer>
    </div>
  </div>
</div>
</template>

<script>
import bus from '../bus.js'
import axios from 'axios'

export default {
  data() {
    return {
      name: ''
    }
  },
  methods: {
    test: function() {
      bus.$emit('name', this.name);
    }
  }
}
</script>

<style scoped lang="scss">
.back {
  margin-top: 8px;
}
#left-button {
  margin-right: 20px;
}
.man-flex {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pass {
  margin-left: 4px;
}

.flex {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

#mains {
  display: inline;
  height: 100%;

}

.card {
  width: 400px;
  margin-top: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.button {
  margin-bottom: 10px;
}
#top {
  margin-bottom: 10px;
}
.not-logged-in {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

#button {
  margin-top: 15px;
}
input {
  margin-left: 8px;
}
</style>
