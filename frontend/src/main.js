import Vue from 'vue'
import Material from 'material-icons'

// Import fonts and other global styles
//import '@/assets/fonts/fonts.scss'
import '@/styles/globals.scss'

// BUEFY
import Buefy from 'buefy'
import 'buefy/lib/buefy.css'
Vue.use(Buefy)

// AT UIKIT
import AtComponents from 'at-ui'
import 'at-ui-style'
Vue.use(AtComponents)


import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
