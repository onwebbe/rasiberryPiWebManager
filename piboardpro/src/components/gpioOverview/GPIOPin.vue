<template>
  <div class="GPIOPin">
      <div class="pinTitle">( {{pinData.names.Physical}} ) {{pinData.names.Name}}</div>
      <div class="pinIconOuter">
        <div class="pinIcon" :class="pinBackgroundColor">{{pinData.names.Physical}}</div>
        <div class="light" :class="lightBackgroundColor"></div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'GPIOPin',
  props: {
    pinData: {
      type: Object,
      default: {}
    }
  },
  data () {
    return {
    }
  },
  created () {
  },
  methods: {
  },
  computed: {
    pinBackgroundColor: function () {
      if (this.pinData.mode === 'IN') {
        return {
          'in': true
        };
      } else if (this.pinData.mode === 'OUT') {
        return {
          'out': true
        };
      } else {
        return {
          'other': true
        };
      }
    },
    lightBackgroundColor: function () {
      if (this.pinData.mode !== 'IN' && this.pinData.mode !== 'OUT') {
        return '';
      }
      if (this.pinData.value === 0) {
          return {
            'low': true
          };
        } else {
          return {
            'high': true
          };
        }
    }
  }
}
</script>

<style scoped lang="less">
.GPIOPin {
  .pinIconOuter {
    margin: auto;
    width: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .pinIcon {
    width: 25px;
    height: 25px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid black;
    background-color: rgba(0, 0, 0, 0.25);
    color: white;
    font-weight: bold;
    &.in {
      background-color: #52c41a;
      color: white;
    }
    &.out {
      background-color: #f5222d;
      color: white;
    }
  }
  .light {
    height: 10px;
    width: 10px;
    border-radius: 5px;
    margin-left: 5px;
    &.high {
      background-color: #52c41a;
    }
    &.low {
      background-color: transparent;
    }
  }
  .pinTitle {
    text-align: center;
    margin-bottom: 2px;
  }
}

</style>
