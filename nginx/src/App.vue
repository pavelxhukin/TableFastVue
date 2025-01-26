<template>
  <Navigation/>
  <div>
    <router-view/>
  </div>
</template>

<script>
import TableList from "./components/TableList.vue";
import Navigation from "./components/Navigation.vue";

export default {
  name: "App",
  components: {
    TableList,
    Navigation
  }
};
</script>

