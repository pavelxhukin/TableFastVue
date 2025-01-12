<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      tables: {},
      days_of_week : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
      time_slots : ['09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00'],
      schedule_data : {},
    };
  },
  methods: {
    async getAnswer() {
      const { data } = await axios.get("http://localhost:4000/table");
      this.tables = data;
    },
    async getRooms() {
      const { data } = await axios.get("http://127.0.0.1:8000/tables");
      this.schedule_data = data;
    },
  },
  beforeMount() {
    this.getAnswer();
    this.getRooms();
  },
};
</script>

<template>
    <header>
    <div class="title">ScHeDule</div>
    </header>

    <section>
    <div class="schedule-container">
        <div class="schedule-header">
        <!-- Итерация по временным слотам -->
        <div v-for="time in time_slots" :key="time">{{ time }}</div>
      </div>
      <div class="schedule-body">
        <!-- Итерация по дням недели -->
        <div v-for="(day, index) in days_of_week" :key="index">
            <div class="day-header">{{ day }}</div>
            <div class="event-cell" v-for="time in time_slots" :key="time">
              <!-- Проверка на наличие данных для текущего дня -->
                <div v-if="schedule_data[day]">
                  <div v-for="event in schedule_data[day]" :key="event.time">
                    <!-- Проверка на соответствие времени события и текущего времени -->
                      <div v-if="event.time === time">
                        <div class="event" v-bind:class="{ now: event.now }">
                          {{ event.title }} ({{ event.cabinet }})
                        </div>
                      </div>
                  </div>
                </div>
            </div>
        </div>
      </div>
    </div> 
  </section>
</template>

<style>
body {
    font-family: Arial, sans-serif;
    height: 100vh;
    width: 100vw;
    padding: 0px;
    margin: 0px;
    background-color: black;
}

header {
    background: black;
    height: 15%;
    padding: 0px;
    margin: 0px;
    position: relative;
}

.schedule-container {
    display: grid;
    grid-template-columns: 100px repeat(6, minmax(100px, 1fr));
    width: 80%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: linear-gradient(340deg, #0c0716, #4c2099);
    color: white;
    font-weight: bold;
    border: 2px solid black;
    border-radius: 20px;
    min-height: 500px;
}

.schedule-header {
    display: grid;
    grid-column: 2 / -1;
    grid-template-columns: repeat(6, minmax(100px, 1fr));
    align-content: center;
}

.schedule-header div {
    padding: 10px;
    text-align: center;
}

.schedule-body {
    display: grid;
    grid-column: 1 / -1;
    grid-template-columns: inherit;
}

.schedule-body .day-header {
    padding: 10px;
    text-align: center;
    align-self: center;
}

.schedule-body .event-cell {
    padding: 10px;
    min-height: 60px;
    text-align: center;
    word-wrap: break-word;
    background-color: white;
    color: black;
    border-radius: 20px;
    position: relative;
    margin: 2px;
}

.title {
    color: white;
    font-size: 60px;
    padding: 0px;
    margin: 0px;
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-weight: bold;
}

section {
    position: relative;
    height: 85%;
    background: linear-gradient(360deg, #673AB7, #000000);
}

.event {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    margin: 0px;
}
.event-cell:hover {
    background: grey;
}

.now {
    background: #673ab796;
    border-radius: 20px;
    padding: 15px;
}
</style>



  
