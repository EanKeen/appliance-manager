<template>
  <div id="mains">


  <div class="not-logged-in">
          <!-- <section>
            <b-field label="Name">
                <b-input value="Kevin Garvey"></b-input>
            </b-field>

            <b-field label="Email"
                type="is-danger"
                message="This email is invalid">
                <b-input type="email"
                    value="john@"
                    maxlength="30">
                </b-input>
            </b-field>

            <b-field label="Username"
                type="is-success"
                message="This username is available">
                <b-input value="johnsilver" maxlength="30"></b-input>
            </b-field>

            <b-field label="Password"
                type="is-warning"
                :message="['Password is too short', 'Password must have at least 8 characters']">
                <b-input value="123" type="password" maxlength="30"></b-input>
            </b-field>

            <b-field label="Subject">
                <b-select placeholder="Select a subject">
                    <option value="1">Option 1</option>
                    <option value="2">Option 2</option>
                </b-select>
            </b-field>
        </section> -->



    <div class="card">
      <div class="card-content">
        <p class="title">
          Sign In
        </p>
        <div class="man-flex">

          <!-- <div class="user flex">
            <h3>Username</h3>
            <input id="top" type="text"></input>
          </div>
          <div class="pass flex">
            <h3>Password</h3>
            <input type="text"></input>
          </div> -->

          <b-field label="Username"
              type="is-success"
              message="Choose a Username">
              <b-input v-model="username" maxlength="30"></b-input>
          </b-field>

          <b-field label="Password"
              type="is-warning"
              :message="['Choose a Strong Password']">
              <b-input v-model="password" value="123" type="password" maxlength="30"></b-input>
          </b-field>

        </div>
      </div>
      <footer class="card-footer">
        <div class="back">
          <!-- <a @click="showNavBar" id="left-button" class="button is-primary router-link">
            <router-link to="/" class="router-link">
            Back
          </router-link>
          </a> -->
          <a class="button is-primary router-link" id="left-button">
            <router-link to="/" class="router-link router-link-button">
              Back
            </router-link>
          </a>

          <a class="button is-primary router-link">
            <div @click="signIn" class="">

              Sign In
            </div>
          </a>





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
      username: '',
      password: '',
      url: 'http://localhost:5000'
    }
  },
  methods: {
    test: function() {

    },
    showNavBar: function() {
      // Variable recieved will be "isSignInScreenActive" or along those lines
      bus.$emit('show-nav-bar', false);
    },
    signIn: function() {
      console.log(this.username);
      console.log(this.password);

      axios.post(this.url + '/login', {
        username: this.username,
        password: this.passowrd
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
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
