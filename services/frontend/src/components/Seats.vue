<template>
  <div>
    <ul>
      <li v-for="seat in seats" :key="seat.number">
        {{ seat }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Seats",
  data() {
    return {
      seats: [],
    };
  },
  methods: {
    getSeats() {
      axios.get('/seats')
        .then((res) => {
          this.seats = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getSeats();
  },
}
</script>

<style scoped>

</style>