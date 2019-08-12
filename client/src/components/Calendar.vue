<template>
    <div class="calendar">
      <!-- Month nav -->
      <div class="nav">
        <div class="left">
          <i class="fas fa-angle-left" @click.prevent="nextMonth(-1)"></i>
        </div>
        <div class="month">{{monthName}}</div>
        <div class="right">
          <i class="fas fa-angle-right" @click.prevent="nextMonth(1)"></i>
        </div>
      </div>
      <!-- Days -->
      <div class="days">
        <div class="day">mon</div>
        <div class="day">tue</div>
        <div class="day">wed</div>
        <div class="day">thu</div>
        <div class="day">fri</div>
        <div class="day">sat</div>
        <div class="day">sun</div>
      </div>
      <!-- Cells -->
      <div class="cells">

        <div class="cell-row" v-for="(row, index) in calendar" :key="index">
          <div :class="{'date': true, 'available': col.date_number !== null && col.passed !== true && col.available === true, 'unavailable': col.date_number !== null && col.available === false && col.passed !== true, 'passed': col.passed === true, 'noDate': col.date_number === null}" v-for="(col, index) in row" :key="index">
            <span v-if="col.date_number !== null">{{ col.date_number }}</span>
          </div>
        </div>

      </div>
    </div>
</template>

<script>
export default {
    name: 'Calendar',
    methods: {
      nextMonth(direction) {
        if (direction === -1) {
          // Can't go left
          if (this.$store.state.listings.active_calendar_month === 0) {
            return;
          }
        } else {
          // Can't go right
          if (this.$store.state.listings.active_calendar_month === 5) {
            return;
          }
        }
        this.$store.dispatch('updateCalendarMonth', direction);
      }
    },
    computed: {
      calendar() {
        return this.$store.state.listings.active_calendar;
      },
      monthName() {
        return this.$store.state.listings.active_month;
      }
    },
    beforeMount() {
      this.$store.dispatch('getCalendar');
    }
}
</script>


<style>
* {
  box-sizing: border-box;
}
.calendar {
  width: 80%;
  display: block;
  margin: 10% auto;
  box-shadow: 0 2px 8px #ccc;
  border-radius: 4px;
  overflow: auto;
}
.nav {
  height: 20%;
}
.nav > div {
  float: left;
  height: 100%;
  text-align: center;
  padding-top: 20px;
  font-weight: bold;
}
.left, .right {
  width: 20%;
  font-size: 1.8em;
}
.month {
  width: 60%;
}
.days {
  height: 10%;
}
.day, .date {
  float: left;
  width: 14%;
  text-align: center;
  padding-top: 4px;
}
.cells {
  height: 70%;
}
.cell-row {
  height: 20%;
  width: 100%;
}
.date {
  width: 13%;
  margin: 5px 2px;
  height: 24px;
  border-radius: 4px;
}
.passed {
  background-color: rgba(244, 241, 243, 0.8);
  color: #ccc;
}
.unavailable {
  background-color: rgb(235, 156, 156);
  color: rgb(180, 74, 55);
}
.available {
  background-color: rgba(148, 233, 210, 0.21);
  color: rgba(50, 166, 135, 1);
}
.noDate {
  background-color: white;
  color: white;
}

</style>
