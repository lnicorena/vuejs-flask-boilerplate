import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

Vue.config.productionTip = false;

Vue.use({
  install(Vue) {
    Vue.prototype.$http = axios.create({
      baseURL: process.env.VUE_APP_API_URL
    });
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
