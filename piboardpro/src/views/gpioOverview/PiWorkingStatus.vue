<template>
  <div class="page-header-index-wide">
    <a-row :gutter="24">
      <a-col :sm="24" :md="12" :xl="12" :style="{ marginBottom: '24px', backgroundColor: 'white', paddingTop: '24px' }">
        <div :style="{width: '100%', height: '350px'}"  ref="cpuStatusChart"></div>
      </a-col>
      <a-col :sm="24" :md="12" :xl="12" :style="{ marginBottom: '24px', backgroundColor: 'white', paddingTop: '24px'  }">
        <div :style="{width: '100%', height: '350px'}"  ref="memoryStatusChart"></div>
      </a-col>
    </a-row>
    <a-row :gutter="24">
      <a-col :sm="24" :md="24" :xl="24" :style="{ marginBottom: '24px', backgroundColor: 'white', paddingTop: '24px' }">
        <div :style="{width: '100%', height: '350px'}"  ref="diskUsageChart"></div>
      </a-col>
    </a-row>
    <a-row :gutter="24">
      <a-col :sm="24" :md="24" :xl="24" :style="{ marginBottom: '24px', backgroundColor: 'white', paddingTop: '24px' }">
        <PiProcessList></PiProcessList>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import moment from 'moment'
import { ChartCard, MiniArea, MiniBar, MiniProgress, RankList, Bar, Trend, NumberInfo, MiniSmoothArea } from '@/components'
import { mixinDevice } from '@/utils/mixin'
import { setInterval } from 'timers';
import { getPiUsage, getDiskInformation } from '@/api/piWorkingStatus'

import PiProcessList from '@/components/gpioOverview/PiProcessList'
export default {
  name: 'PiWorkingStatus',
  mixins: [mixinDevice],
  components: {
    ChartCard,
    MiniArea,
    MiniBar,
    MiniProgress,
    RankList,
    Bar,
    Trend,
    NumberInfo,
    MiniSmoothArea,
    PiProcessList
  },
  data () {
    return {
      piUsageDataTimerLooping: true,
      diskUsageChart: {
        diskUsageChartObj: null,
        diskUsageChart: {
          tooltip : {
            formatter: "{a} <br/>{b} : {c}%"
          },
          series: [{
            name: '磁盘使用情况',
            type: 'gauge',
            detail: {formatter:'{value}%'},
            data: [{value: 0, name: '使用率'}]
          }]
        }
      },
      cpuChart: {
        cpuUsageChartObj: null,
        cpuCurrentPerc: 0,
        cpuUsageChart: {
          title: { text: 'CPU 使用率' },
          tooltip: {},
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: []
          },
          yAxis: {
            boundaryGap: [0, '50%'],
            type: 'value'
          },
          series: [{
            name: 'CPU使用率',
            type: 'line',
            smooth: true,
            symbol: 'none',
            areaStyle: {
              normal: {}
            },
            data: []
          }]
        }
      },
      memoryChart: {
        memoryUsageChartObj: null,
        memoryCurrentPerc: 0,
        memoryUsageChart: {
          title: { text: '内存 使用率' },
          tooltip: {},
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: []
          },
          yAxis: {
            type: 'value'
          },
          series: [{
            name: '内存使用率',
            type: 'line',
            smooth: true,
            symbol: 'none',
            areaStyle: {
              normal: {}
            },
            data: []
          }]
        }
      },
      loading: true
    }
  },
  created () {
    setTimeout(() => {
      this.loading = !this.loading
    }, 100)
    this.piUsageDataTimerLooping = true;
  },
  mounted () {
    this.drawCPUStatusChart();
    this.drawDiskUsageChart();
    this.addPIWorkingStatusData();

    this.getDiskStorageData();
  },
  beforeDestroy () {
    this.piUsageDataTimerLooping = false;
  },
  methods: {
    drawCPUStatusChart: function () {
      let cpuStatusChartDiv = this.$refs['cpuStatusChart'];
      this.cpuChart.cpuUsageChartObj = this.$echarts.init(cpuStatusChartDiv);
      this.cpuChart.cpuUsageChartObj.setOption(this.cpuChart.cpuUsageChart);

      let memoryStatusChartDiv = this.$refs['memoryStatusChart'];
      this.memoryChart.memoryUsageChartObj = this.$echarts.init(memoryStatusChartDiv);
      this.memoryChart.memoryUsageChartObj.setOption(this.memoryChart.memoryUsageChart);
    },
    drawDiskUsageChart () {
      let diskUsageChartDiv = this.$refs['diskUsageChart'];
      this.diskUsageChart.diskUsageChartObj = this.$echarts.init(diskUsageChartDiv);
      this.diskUsageChart.diskUsageChartObj.setOption(this.diskUsageChart.diskUsageChart);
    },
    addCPUData: function (res) {
      var cpuPercent = res.CPUUsage.percent;
      this.cpuChart.cpuCurrentPerc = cpuPercent;
      this.cpuChart.cpuUsageChart.title.text = 'CPU 使用率 ' + cpuPercent + '%';
      this.cpuChart.cpuUsageChart.xAxis.data.push('');
      this.cpuChart.cpuUsageChart.series[0].data.push(cpuPercent);
      if (this.cpuChart.cpuUsageChart.xAxis.data.length >= 20) {
        this.cpuChart.cpuUsageChart.xAxis.data.shift();
        this.cpuChart.cpuUsageChart.series[0].data.shift();
      }
      this.cpuChart.cpuUsageChartObj.setOption(this.cpuChart.cpuUsageChart);
    },
    addMemoryData: function (res) {
      var memorySize = res.MemoryUsage.usage / res.MemoryUsage.total;
      memorySize = Math.floor(memorySize * 100);
      this.memoryChart.memoryCurrentPerc = memorySize;
      this.memoryChart.memoryUsageChart.title.text = '内存 使用率 ' + memorySize + '% - ' + res.MemoryUsage.usage + 'M/' + res.MemoryUsage.total + 'M';
      this.memoryChart.memoryUsageChart.xAxis.data.push('');
      this.memoryChart.memoryUsageChart.series[0].data.push(memorySize);
      if (this.memoryChart.memoryUsageChart.xAxis.data.length >= 20) {
        this.memoryChart.memoryUsageChart.xAxis.data.shift();
        this.memoryChart.memoryUsageChart.series[0].data.shift();
      }
      this.memoryChart.memoryUsageChartObj.setOption(this.memoryChart.memoryUsageChart);
    },

    addPIWorkingStatusData: function () {
      getPiUsage({})
      .then(res => {
        // this.$set('pinList', res);
        // update CPU Status
        this.addCPUData(res.result);
        this.addMemoryData(res.result);
        if (this.piUsageDataTimerLooping === true) {
          this.piUsageDataTimer = setTimeout(() => {
            this.addPIWorkingStatusData();
          }, 200);
        }
      })
      .catch(() => {
      });
    },
    getDiskStorageData() {
      getDiskInformation({})
      .then(res => {
        this.updateDiskStorageChart(res.result);
      })
    },
    updateDiskStorageChart(data) {
      let usedPercent = data.percent;
      this.diskUsageChart.diskUsageChart.series[0].data[0].value = usedPercent;
      this.diskUsageChart.diskUsageChartObj.setOption(this.diskUsageChart.diskUsageChart);
    }
  }
}
</script>

<style lang="less" scoped>
  .extra-wrapper {
    line-height: 55px;
    padding-right: 24px;

    .extra-item {
      display: inline-block;
      margin-right: 24px;

      a {
        margin-left: 24px;
      }
    }
  }

  .antd-pro-pages-dashboard-analysis-twoColLayout {
    position: relative;
    display: flex;
    display: block;
    flex-flow: row wrap;
  }

  .antd-pro-pages-dashboard-analysis-salesCard {
    height: calc(100% - 24px);
    /deep/ .ant-card-head {
      position: relative;
    }
  }

  .dashboard-analysis-iconGroup {
    i {
      margin-left: 16px;
      color: rgba(0,0,0,.45);
      cursor: pointer;
      transition: color .32s;
      color: black;
    }
  }
  .analysis-salesTypeRadio {
    position: absolute;
    right: 54px;
    bottom: 12px;
  }
</style>
