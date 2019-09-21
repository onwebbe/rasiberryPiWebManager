import api from './index'
import { axios } from '@/utils/request'

export function getPiUsage (parameter) {
  let url = '/v1/piWorkingStatus/getPiUsage';
  return axios({
    url: url,
    method: 'get'
  })
}

export function getPiRunningStatus (parameter) {
  let query = '';
  if (parameter.pagination) {
    query += '&pageSize=' + parameter.pagination.pageSize;
    query += '&pageNo=' + parameter.pagination.pageNo
  }
  let url = '/v1/piWorkingStatus/getPiRunningStatus?' + query;
  return axios({
    url: url,
    method: 'get'
  })
}

export function killProcess (parameter) {
  let url = '/v1/piWorkingStatus/killProcess?PID=' + parameter.pid;
  return axios({
    url: url,
    method: 'get'
  })
}

export function getDiskInformation (parameter) {
  let url = '/v1/piWorkingStatus/getDiskInformation';
  return axios({
    url: url,
    method: 'get'
  })
}
