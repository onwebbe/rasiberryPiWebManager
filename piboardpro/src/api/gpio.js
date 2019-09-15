import api from './index'
import { axios } from '@/utils/request'

/**
 * login func
 * parameter: {
 *     username: '',
 *     password: '',
 *     remember_me: true,
 *     captcha: '12345'
 * }
 * @param parameter
 * @returns {*}
 */
export function gpioOverview (parameter) {
  return axios({
    url: '/v1/gpio/overall/',
    method: 'post',
    data: parameter
  })
}
