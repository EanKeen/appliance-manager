<template lang="html">

<div class="rg" id="top">

  <div class="card">
  <header class="card-header">
    <p class="card-header-title">
      Coffee Machine
    </p>
    <a href="#" class="card-header-icon" aria-label="more options">
      <span class="icon">
        <i class="fas fa-angle-down" aria-hidden="true"></i>
      </span>
    </a>
  </header>
  <div class="card-content">
    <div class="content">
      View info about your coffee machine.

      <br>
    </div>
  </div>
  <footer class="card-footer">
    <a href="#" class="card-footer-item">Open</a>
    <a href="#" class="card-footer-item">Edit</a>
    <a href="#" class="card-footer-item">Get Info</a>
  </footer>
</div>
<div class="rg" id="top">

  <div class="card">
  <header class="card-header">
    <p class="card-header-title">
      Refrigerator
    </p>
    <a href="#" class="card-header-icon" aria-label="more options">
      <span class="icon">
        <i class="fas fa-angle-down" aria-hidden="true"></i>
      </span>
    </a>
  </header>
  <div class="card-content">
    <div class="content">
      View info about your refrigerator.

      <br>
    </div>
  </div>
  <footer class="card-footer">
    <a href="#" class="card-footer-item">Open</a>
    <a href="#" class="card-footer-item">Edit</a>
    <a href="#" class="card-footer-item">Get Info</a>
  </footer>
</div>
</div>
<div class="rg" id="top">

  <div class="card">
  <header class="card-header">
    <p class="card-header-title">
      Laundry Machine
    </p>
    <a href="#" class="card-header-icon" aria-label="more options">
      <span class="icon">
        <i class="fas fa-angle-down" aria-hidden="true"></i>
      </span>
    </a>
  </header>
  <div class="card-content">
    <div class="content">
      View info about your laundry Machine.

      <br>
    </div>
  </div>
  <footer class="card-footer">
    <a href="#" class="card-footer-item">Open</a>
    <a href="#" class="card-footer-item">Edit</a>
    <a href="#" class="card-footer-item">Get Info</a>
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

<style scoped lang="scss">
.rg {
  width: 400px;
  margin-top: 10px;

}


</style>
