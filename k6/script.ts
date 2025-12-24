import http from 'k6/http';
import {check} from 'k6';

export const options = {
    vus: 1000,
    duration: '1m'
}

export default function() {
    const url = "http://api:8000"
    const res = http.get(`${url}/requests/`)
    check(res, {
        'is_status_200': (r) => r.status === 200,
    })
}