// axiosInstance.js
import axios from 'axios'

const axiosInstance = axios.create({
   baseURL: 'http://localhost:8000', // Change this to your backend URL
   headers: {
      'Content-Type': 'application/json',
   },
})

axiosInstance.interceptors.request.use(
   (config) => {
      const token = localStorage.getItem('access_token')
      if (token) {
         config.headers.Authorization = `Bearer ${token}`
      }
      return config
   },
   (error) => Promise.reject(error),
)

axiosInstance.interceptors.response.use(
   (response) => response,
   async (error) => {
      const originalRequest = error.config

      if (error.response.status === 401 && !originalRequest._retry) {
         originalRequest._retry = true
         const refreshToken = localStorage.getItem('refresh_token')

         if (refreshToken) {
            try {
               const response = await axiosInstance.post('/token/refresh/', {
                  refresh: refreshToken,
               })
               localStorage.setItem('access_token', response.data.access)
               axiosInstance.defaults.headers['Authorization'] =
                  'Bearer ' + response.data.access
               originalRequest.headers['Authorization'] =
                  'Bearer ' + response.data.access
               return axiosInstance(originalRequest)
            } catch (err) {
               console.error(err)
            }
         }
      }
      return Promise.reject(error)
   },
)

export default axiosInstance
