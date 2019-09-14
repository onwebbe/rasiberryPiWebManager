import React, { Component } from 'react';
import styles from  './index.module.scss';
const pinOverall = [ { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "3.3v", "Physical": "1" } }, { "value": "", "mode": "", "names": { "Physical": "2", "Name": "5v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "2", "wPi": "8", "Name": "SDA.1", "Physical": "3" } }, { "value": "", "mode": "", "names": { "Physical": "4", "Name": "5v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "3", "wPi": "9", "Name": "SCL.1", "Physical": "5" } }, { "value": "", "mode": "", "names": { "Physical": "6", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "4", "wPi": "7", "Name": "GPIO. 7", "Physical": "7" } }, { "value": "0", "mode": "OUT", "names": { "Physical": "8", "Name": "TxD", "wPi": "15", "BCM": "14" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "9" } }, { "value": "1", "mode": "IN", "names": { "Physical": "10", "Name": "RxD", "wPi": "16", "BCM": "15" } }, { "value": "0", "mode": "IN", "names": { "BCM": "17", "wPi": "0", "Name": "GPIO. 0", "Physical": "11" } }, { "value": "0", "mode": "IN", "names": { "Physical": "12", "Name": "GPIO. 1", "wPi": "1", "BCM": "18" } }, { "value": "0", "mode": "IN", "names": { "BCM": "27", "wPi": "2", "Name": "GPIO. 2", "Physical": "13" } }, { "value": "", "mode": "", "names": { "Physical": "14", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "22", "wPi": "3", "Name": "GPIO. 3", "Physical": "15" } }, { "value": "0", "mode": "IN", "names": { "Physical": "16", "Name": "GPIO. 4", "wPi": "4", "BCM": "23" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "3.3v", "Physical": "17" } }, { "value": "0", "mode": "IN", "names": { "Physical": "18", "Name": "GPIO. 5", "wPi": "5", "BCM": "24" } }, { "value": "0", "mode": "IN", "names": { "BCM": "10", "wPi": "12", "Name": "MOSI", "Physical": "19" } }, { "value": "", "mode": "", "names": { "Physical": "20", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "9", "wPi": "13", "Name": "MISO", "Physical": "21" } }, { "value": "0", "mode": "IN", "names": { "Physical": "22", "Name": "GPIO. 6", "wPi": "6", "BCM": "25" } }, { "value": "0", "mode": "IN", "names": { "BCM": "11", "wPi": "14", "Name": "SCLK", "Physical": "23" } }, { "value": "1", "mode": "IN", "names": { "Physical": "24", "Name": "CE0", "wPi": "10", "BCM": "8" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "25" } }, { "value": "1", "mode": "IN", "names": { "Physical": "26", "Name": "CE1", "wPi": "11", "BCM": "7" } }, { "value": "1", "mode": "IN", "names": { "BCM": "0", "wPi": "30", "Name": "SDA.0", "Physical": "27" } }, { "value": "1", "mode": "IN", "names": { "Physical": "28", "Name": "SCL.0", "wPi": "31", "BCM": "1" } }, { "value": "1", "mode": "IN", "names": { "BCM": "5", "wPi": "21", "Name": "GPIO.21", "Physical": "29" } }, { "value": "", "mode": "", "names": { "Physical": "30", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "6", "wPi": "22", "Name": "GPIO.22", "Physical": "31" } }, { "value": "0", "mode": "IN", "names": { "Physical": "32", "Name": "GPIO.26", "wPi": "26", "BCM": "12" } }, { "value": "0", "mode": "IN", "names": { "BCM": "13", "wPi": "23", "Name": "GPIO.23", "Physical": "33" } }, { "value": "", "mode": "", "names": { "Physical": "34", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "19", "wPi": "24", "Name": "GPIO.24", "Physical": "35" } }, { "value": "0", "mode": "IN", "names": { "Physical": "36", "Name": "GPIO.27", "wPi": "27", "BCM": "16" } }, { "value": "0", "mode": "IN", "names": { "BCM": "26", "wPi": "25", "Name": "GPIO.25", "Physical": "37" } }, { "value": "0", "mode": "IN", "names": { "Physical": "38", "Name": "GPIO.28", "wPi": "28", "BCM": "20" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "39" } }, { "value": "0", "mode": "IN", "names": { "Physical": "40", "Name": "GPIO.29", "wPi": "29", "BCM": "21" } } ];
import axios from 'axios';
import { thisTypeAnnotation } from '@babel/types';

class GPIOPin extends React.Component {
  constructor(props) {
    super(props);
    let pinData = props.pinData;
    this.state = {
      pinData: pinData
    };
  }
  render() {
    return <div className={styles.pinDiagram.pin}>
    <div className={styles.pinTitle}>({this.state.pinData.names.Physical}) - {this.state.pinData.names.Name}</div>
    <div onClick={(e) => this.props.handleClick(e, this.state.pinData)} className={[styles.pinIcon, this.state.pinData.mode === 'IN'?styles.in:this.state.pinData.mode === 'OUT'?styles.out:styles.vt].join(' ')}></div>
  </div>;
  }
}
class PinDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isShow: props.isShow
    }
  }
  componentWillReceiveProps(nextProps) {
    if (nextProps. isShow!== this.props.isShow) {
     this.setState({
      isShow: nextProps.isShow
     });
    }
   }
  render() {
    if (this.state.isShow === false) {
      return null;
    }
    return <div onClick={this.props.handleClick} style={{color:'white'}}>
      data {this.state.isShow}
      </div>
  }
}
// function PinDetail(props) {
//   this.state = {
//     isShow: false
//   }
//   this.setState({
//     isShow: props.isShow
//   });

//   if (props.isShow === false) {
//     return null;
//   }
//   return <div style={{color:'white'}}>
//     data {this.state.isShow}
//     </div>
// }
class PinList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      pinOverall: [],
      isShowDetail: false,
      detailDisplayPinData: null
    };
    var self = this;
    // axios.get('/gpio/overall/')
    //     .then( (response)=> {
    //       var theData = response.data.data;
    //       console.log(theData);
    //     })
    //     .catch(function (error) {
    //         console.log(error);
    // })
    this.handlePinClick = this.handlePinClick.bind(this);
    this.handleDetailClick = this.handleDetailClick.bind(this);
    setTimeout(function () {
      self.setState({
        pinOverall: mockGPIOData
      })
    }, 1000);
  }
  handlePinClick(e, pinData) {
    this.setState({
      isShowDetail: true,
      detailDisplayPinData: pinData
    })
  }
  handleDetailClick(e) {
    this.setState({
      isShowDetail: false
    })
  }
  render() {
    const pinList = this.state.pinOverall.map((pinData, index) =>
      // Only do this if items have no stable IDs
      <GPIOPin key={index} pinData={pinData} handleClick={this.handlePinClick}></GPIOPin>
    );
    return (
      <div style={{'margin':'auto', 'display':'flex', 'justifyContent': 'center'}}>
        <div className={styles.pinDiagram}>
          {pinList}
        </div>
        <PinDetail handleClick={this.handleDetailClick} isShow={this.state.isShowDetail} pinData={this.state.detailDisplayPinData}></PinDetail>
      </div>
    );
  }
}

export default function() {
  return <div className="GpioPinOverall-page">
    <div className="functions"></div>
    <div className="title"></div>
    <div className="summary"></div>
    <PinList></PinList>
  </div>;
}


const mockGPIOData = [ { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "3.3v", "Physical": "1" } }, { "value": "", "mode": "", "names": { "Physical": "2", "Name": "5v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "2", "wPi": "8", "Name": "SDA.1", "Physical": "3" } }, { "value": "", "mode": "", "names": { "Physical": "4", "Name": "5v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "3", "wPi": "9", "Name": "SCL.1", "Physical": "5" } }, { "value": "", "mode": "", "names": { "Physical": "6", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "4", "wPi": "7", "Name": "GPIO. 7", "Physical": "7" } }, { "value": "0", "mode": "OUT", "names": { "Physical": "8", "Name": "TxD", "wPi": "15", "BCM": "14" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "9" } }, { "value": "1", "mode": "IN", "names": { "Physical": "10", "Name": "RxD", "wPi": "16", "BCM": "15" } }, { "value": "0", "mode": "IN", "names": { "BCM": "17", "wPi": "0", "Name": "GPIO. 0", "Physical": "11" } }, { "value": "0", "mode": "IN", "names": { "Physical": "12", "Name": "GPIO. 1", "wPi": "1", "BCM": "18" } }, { "value": "0", "mode": "IN", "names": { "BCM": "27", "wPi": "2", "Name": "GPIO. 2", "Physical": "13" } }, { "value": "", "mode": "", "names": { "Physical": "14", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "22", "wPi": "3", "Name": "GPIO. 3", "Physical": "15" } }, { "value": "0", "mode": "IN", "names": { "Physical": "16", "Name": "GPIO. 4", "wPi": "4", "BCM": "23" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "3.3v", "Physical": "17" } }, { "value": "0", "mode": "IN", "names": { "Physical": "18", "Name": "GPIO. 5", "wPi": "5", "BCM": "24" } }, { "value": "0", "mode": "IN", "names": { "BCM": "10", "wPi": "12", "Name": "MOSI", "Physical": "19" } }, { "value": "", "mode": "", "names": { "Physical": "20", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "9", "wPi": "13", "Name": "MISO", "Physical": "21" } }, { "value": "0", "mode": "IN", "names": { "Physical": "22", "Name": "GPIO. 6", "wPi": "6", "BCM": "25" } }, { "value": "0", "mode": "IN", "names": { "BCM": "11", "wPi": "14", "Name": "SCLK", "Physical": "23" } }, { "value": "1", "mode": "IN", "names": { "Physical": "24", "Name": "CE0", "wPi": "10", "BCM": "8" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "25" } }, { "value": "1", "mode": "IN", "names": { "Physical": "26", "Name": "CE1", "wPi": "11", "BCM": "7" } }, { "value": "1", "mode": "IN", "names": { "BCM": "0", "wPi": "30", "Name": "SDA.0", "Physical": "27" } }, { "value": "1", "mode": "IN", "names": { "Physical": "28", "Name": "SCL.0", "wPi": "31", "BCM": "1" } }, { "value": "1", "mode": "IN", "names": { "BCM": "5", "wPi": "21", "Name": "GPIO.21", "Physical": "29" } }, { "value": "", "mode": "", "names": { "Physical": "30", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "1", "mode": "IN", "names": { "BCM": "6", "wPi": "22", "Name": "GPIO.22", "Physical": "31" } }, { "value": "0", "mode": "IN", "names": { "Physical": "32", "Name": "GPIO.26", "wPi": "26", "BCM": "12" } }, { "value": "0", "mode": "IN", "names": { "BCM": "13", "wPi": "23", "Name": "GPIO.23", "Physical": "33" } }, { "value": "", "mode": "", "names": { "Physical": "34", "Name": "0v", "wPi": "", "BCM": "" } }, { "value": "0", "mode": "IN", "names": { "BCM": "19", "wPi": "24", "Name": "GPIO.24", "Physical": "35" } }, { "value": "0", "mode": "IN", "names": { "Physical": "36", "Name": "GPIO.27", "wPi": "27", "BCM": "16" } }, { "value": "0", "mode": "IN", "names": { "BCM": "26", "wPi": "25", "Name": "GPIO.25", "Physical": "37" } }, { "value": "0", "mode": "IN", "names": { "Physical": "38", "Name": "GPIO.28", "wPi": "28", "BCM": "20" } }, { "value": "", "mode": "", "names": { "BCM": "", "wPi": "", "Name": "0v", "Physical": "39" } }, { "value": "0", "mode": "IN", "names": { "Physical": "40", "Name": "GPIO.29", "wPi": "29", "BCM": "21" } } ];