<script>
import axios from "axios";

export default {
  name: "TableList",
  mixins: [],
  data() {
    return {
      days : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
      timeSlots : ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00'],
      events : [],
    };
  },
  methods: {
    async getRooms() {
      const { data } = await axios.get('http://localhost:4000/tables', {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}`
            }
          });
      this.events = data;
    },
  getEvents(day, time) {
      return this.events.filter(event => event.weekday === day && event.time === time);
  } 
  },
  beforeMount() {
    this.getRooms();
  },
};
</script>

<!-- <script setup>
import { onBeforeMount } from "vue";

async function getRooms() {
  const { data } = await axios.get("http://127.0.0.1:4000/tables");
  this.schedule_data = data;
}

onBeforeMount(() => {
  getRooms();
});
</script> -->

<template>
  <div>
    <div class="schedule-grid">
      <!-- Заголовок (дни недели) -->
       <div class="head">
        <div class="header"></div>
        <div class="header" v-for="(day, index) in days" :key="index">{{ day }}</div>
      </div>
      <!-- Дни недели (строки) -->
      <div v-for="time in timeSlots" :key="time" class="time-row">
        <div class="time">{{ time }}</div>
        <div
          class="grid-cell"
          v-for="(day, index) in days"
          :key="index"
        >
          <div v-for="event in getEvents(day, time)" :key="event.id" class="event">
            <strong>{{ event.title }}</strong><br>
            <span>Cabinet: {{ event.cabinet }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.schedule-grid {
  display: grid;
  grid-template-columns: 1fr;
  grid-gap: 1px;
  text-align: center;
  border: none;
}

.head {
  display: grid;
  grid-template-columns: 150px repeat(5, 1fr);
  grid-gap: 1px;
}

.header {
  font-weight: bold;
  background-color: #888888;
  color: #FFF;
  padding: 10px;
}

.time-row {
  display: grid;
  grid-template-columns: 150px repeat(5, 1fr);
  grid-gap: 1px;
}

.time {
  font-weight: bold;
  padding: 10px;
  background-color: #888888;
  color: #FFF;
}

.grid-cell {
  min-width: 100px;
  background-color: #e9e9e9;
  /* padding: 10px; */
}

.event {
  
  padding: 5px;
  /* border-radius: 5px; */
  /* border-style: solid; */
  /* border-radius: 15px; */
  /* border-color: hwb(272 60% 24%); */
}
</style>


  
