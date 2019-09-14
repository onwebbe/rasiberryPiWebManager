<template>
  <div class="GPIODetail">
    <div>
      
    </div>
    <div>
      <div v-for="(names, keyName) in pinData.names" v-bind:key="keyName">
        <span style="display: inline-block;width: 100px;">{{keyName}}:</span>
        <span>{{names}}</span>
      </div>
      <div>
        <span style="display: inline-block;width: 100px;">Mode:</span>
        <span>{{pinData.mode}}</span>
      </div>
      <div>
        <span style="display: inline-block;width: 100px;">Value:</span>
        <span>{{valueString}}</span>
      </div>
    </div>
    <div class="functions">
      <Button v-show="functionValue !== ''" @click="setValue">{{functionValue === 1 ? '高 -> 低': '低 -> 高'}}</Button>
      &nbsp;&nbsp;&nbsp;&nbsp;
      <Button v-show="functionValue !== ''" @click="setMode">{{functionMode === 1 ? '设置为输出' : '设置为输入'}}</Button>
    </div>
  </div>
</template>

<script>
import { Button } from 'ant-design-vue';
export default {
  name: 'GPIODetail',
  components: {
    Button
  },
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
    onClickHide: function () {
      this.$emit('hideDetail');
    },
    setValue: function () {
      let value = (this.functionValue === 1) ? 0 : 1;
      this.$emit('setPinValue', {
        id: this.pinData.names.Physical,
        value: value
      });
    },
    setMode: function () {
      let mode = (this.functionMode === 1) ? 'OUT' : 'IN';
      this.$emit('setPinMode', {
        id: this.pinData.names.Physical,
        value: mode
      });
    }
  },
  computed: {
    valueString: function () {
      if (this.pinData.mode != 'IN' && this.pinData.mode != 'OUT') {
        return '';
      }
      if (this.pinData.value === 1) {
        return 'HIGH';
      } else {
        return 'LOW';
      }
    },
    functionValue: function () {
      if (this.pinData.mode != 'IN' && this.pinData.mode != 'OUT') {
        return '';
      }
      return this.pinData.value;
    },
    functionMode: function () {
      if (this.pinData.mode === 'IN') {
        return 1;
      } else if (this.pinData.mode === 'OUT') {
        return 2;
      }
    }
  }
}
</script>

<style scoped lang="less">
.GPIODetail {
}
.functions {
  margin-top: 10px;
}
</style>
