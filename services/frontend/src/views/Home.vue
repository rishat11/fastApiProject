<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Seats msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Seats from "@/components/Seats";

export default {
  name: 'Home',
  components: {
    Seats,
  }
}
</script>
