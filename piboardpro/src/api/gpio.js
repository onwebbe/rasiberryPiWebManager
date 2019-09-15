import api from './index'
import { axios } from '@/utils/request'


export function gpioOverview (parameter) {
  return axios({
    url: '/v1/gpio/overall/',
    method: 'get'
  })
}

export function setPinData (parameter) {
  let mode  = parameter.mode;
  let value = parameter.value === 1 ? 'HIGH' : 'LOW';
  let id = parameter.id;
  let url = '/v1/gpio/setPinStatus/?boardID=' + id + '&direction=' + mode + '&value=' + value;
  return axios({
    url: url,
    method: 'get'
  })
}
