import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = 'csrftoken';

axios.interceptors.request.use(function (config) {
    const token = localStorage.getItem('sessionid');
    if (token) {
        config.headers.Cookie = `sessionid=${token}`;
    }
    return config;
});


export default axios;
