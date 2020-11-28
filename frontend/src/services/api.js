import axios from 'axios'

const ApiService = {
  init(baseURL) {
    axios.defaults.baseURL = baseURL

    axios.interceptors.response.use(
      response => response.data
    )
  },

  get(resource) {
    return axios.get(resource)
  },

  post(resource, data) {
    return axios.post(resource, data)
  },

  put(resource, data) {
    return axios.put(resource, data)
  },

  patch(resource, data) {
    return axios.patch(resource, data)
  },

  options(resource) {
    return axios.options(resource)
  },

  delete(resource) {
    return axios.delete(resource)
  },

  customRequest(data) {
    return axios(data)
  }
}

export default ApiService
