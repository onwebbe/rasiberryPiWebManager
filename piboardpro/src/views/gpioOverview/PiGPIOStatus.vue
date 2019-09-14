<template>
  <div class="page-header-index-wide PIGPIOStatus">
    <div class="thumlist">
      <span class="thumtitle">图示：输入信号:&nbsp;</span>
      <span class="thumIcon in"></span> 输出信号:&nbsp;<span class="thumIcon out"></span></div>
    <div class="PIGPIOStatusInner">
      <div class="pinContainer"> 
        <div v-for="(pinData, idx) in pinList" v-bind:key="idx" class="pinOuter" @click="onClickPin(pinData)">
          <GPIOPin :pinData="pinData"></GPIOPin>
        </div>
      </div>
      <div>
        <a-modal :visible="isShowDetail" :closable="false">
          <GPIODetail :pinData="selectedGPIOPin" @setPinValue="setPinValue" @setPinMode="setPinMode"></GPIODetail>
          <template slot="footer">
            <a-button type="primary" @click.stop="hideGPIODetail">关闭</a-button>
          </template>
        </a-modal>
      </div>
    </div>
  </div>
</template>

<script>
import { mixinDevice } from '@/utils/mixin'
import { GPIOPin, GPIODetail } from '@/components'
import { Modal } from 'ant-design-vue';

export default {
  name: 'PIGPIOStatus',
  mixins: [mixinDevice],
  components: {
    GPIOPin,
    GPIODetail
  },
  data () {
    return {
      loading: true,
      isShowDetail: false,
      selectedGPIOPin: {},
      pinList: [ { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "3.3v", "Physical": "1" } }, { "value": "", "mode": "", "names": { "Physical": "2", "Name": "5v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "2", "wPi": "8", "Name": "SDA.1", "Physical": "3" } }, { "value": "", "mode": "", "names": { "Physical": "4", "Name": "5v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "3", "wPi": "9", "Name": "SCL.1", "Physical": "5" } }, { "value": "", "mode": "", "names": { "Physical": "6", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "4", "wPi": "7", "Name": "GPIO. 7", "Physical": "7" } }, { "value": "0", "mode": "OUT", "names": { "Physical": "8", "Name": "TxD", "wPi": "15", "BCM": "14" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "9" } }, { "value": "1", "mode": "IN", "names": { "Physical": "10", "Name": "RxD", "wPi": "16", "BCM": "15" } }, { "value": "0", "mode": "IN", "names": { "BCM": "17", "wPi": "0", "Name": "GPIO. 0", "Physical": "11" } }, { "value": "0", "mode": "IN", "names": { "Physical": "12", "Name": "GPIO. 1", "wPi": "1", "BCM": "18" } }, { "value": "0", "mode": "IN", "names": { "BCM": "27", "wPi": "2", "Name": "GPIO. 2", "Physical": "13" } }, { "value": "", "mode": "", "names": { "Physical": "14", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "22", "wPi": "3", "Name": "GPIO. 3", "Physical": "15" } }, { "value": "0", "mode": "IN", "names": { "Physical": "16", "Name": "GPIO. 4", "wPi": "4", "BCM": "23" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "3.3v", "Physical": "17" } }, { "value": "0", "mode": "IN", "names": { "Physical": "18", "Name": "GPIO. 5", "wPi": "5", "BCM": "24" } }, { "value": "0", "mode": "IN", "names": { "BCM": "10", "wPi": "12", "Name": "MOSI", "Physical": "19" } }, { "value": "", "mode": "", "names": { "Physical": "20", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "9", "wPi": "13", "Name": "MISO", "Physical": "21" } }, { "value": "0", "mode": "IN", "names": { "Physical": "22", "Name": "GPIO. 6", "wPi": "6", "BCM": "25" } }, { "value": "0", "mode": "IN", "names": { "BCM": "11", "wPi": "14", "Name": "SCLK", "Physical": "23" } }, { "value": "1", "mode": "IN", "names": { "Physical": "24", "Name": "CE0", "wPi": "10", "BCM": "8" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "25" } }, { "value": "1", "mode": "IN", "names": { "Physical": "26", "Name": "CE1", "wPi": "11", "BCM": "7" } }, { "value": "1", "mode": "IN", "names": { "BCM": "0", "wPi": "30", "Name": "SDA.0", "Physical": "27" } }, { "value": "1", "mode": "IN", "names": { "Physical": "28", "Name": "SCL.0", "wPi": "31", "BCM": "1" } }, { "value": "1", "mode": "IN", "names": { "BCM": "5", "wPi": "21", "Name": "GPIO.21", "Physical": "29" } }, { "value": "", "mode": "", "names": { "Physical": "30", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "6", "wPi": "22", "Name": "GPIO.22", "Physical": "31" } }, { "value": "0", "mode": "IN", "names": { "Physical": "32", "Name": "GPIO.26", "wPi": "26", "BCM": "12" } }, { "value": "0", "mode": "IN", "names": { "BCM": "13", "wPi": "23", "Name": "GPIO.23", "Physical": "33" } }, { "value": "", "mode": "", "names": { "Physical": "34", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "19", "wPi": "24", "Name": "GPIO.24", "Physical": "35" } }, { "value": "0", "mode": "IN", "names": { "Physical": "36", "Name": "GPIO.27", "wPi": "27", "BCM": "16" } }, { "value": "0", "mode": "IN", "names": { "BCM": "26", "wPi": "25", "Name": "GPIO.25", "Physical": "37" } }, { "value": "0", "mode": "IN", "names": { "Physical": "38", "Name": "GPIO.28", "wPi": "28", "BCM": "20" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "39" } }, { "value": "0", "mode": "IN", "names": { "Physical": "40", "Name": "GPIO.29", "wPi": "29", "BCM": "21" } } ]
    }
  },
  created () {
    setTimeout(() => {
      this.loading = !this.loading
    }, 1000)
  },
  methods: {
     onClickPin: function (pinData) {
       this.isShowDetail = true;
       this.selectedGPIOPin = pinData;
     },
     hideGPIODetail: function () {
       this.isShowDetail = false;
     },
     setPinValue: function (params) {
       let pin = this._findPinById(params.id);
       pin.value = params.value;
       this.selectedGPIOPin = pin;
     },
     setPinMode: function (params) {
       let pin = this._findPinById(params.id);
       pin.mode = params.value;
       this.selectedGPIOPin = pin;
     },
     _findPinById: function (pinid) {
       for(let i = 0; i < this.pinList.length; i++) {
         let pin = this.pinList[i];
         if (pinid === pin.names.Physical) {
           return pin;
         }
       }
       return null;
     }
  }
}
</script>

<style scoped lang="less">
.PIGPIOStatusInner {
  display: flex;
  flex-flow: row nowrap;
}
.pinContainer {
  display: flex;
  flex-flow: row wrap;
  width: 250px;
  flex-grow: 0;
  flex-shrink: 0;
  .pinOuter {
    width: 50%;
    margin-top: 5px;
  }
}
.thumlist {
  height: 25px;
  line-height: 25px;
  display: flex;
  .thumtitle {
    height: 25px;
    display: inline-block;
  }
}
.thumIcon {
  height: 25px;
  width: 25px;
  margin-right: 20px;
  display: inline-block;
  &.in {
    background-color: #52c41a;
    color: white;
  }
  &.out {
    background-color: #f5222d;
    color: white;
  }
}

</style>
