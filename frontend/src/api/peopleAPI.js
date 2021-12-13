import axios from 'axios'

const api = axios
  .create({ baseURL: 'http://localhost:3000/people'})

export const list = () =>
  api.get('/list')

export const create = person =>
  api.post('/create', person)

export const remove = id =>
  api.delete(`/remove/${id}`)
