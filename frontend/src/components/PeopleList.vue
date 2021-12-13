<template>
  <v-simple-table>
    <template #default>
      <thead>
        <tr>
          <th>Nome</th>
          <th>Idade</th>
          <th>Remover</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(person, idx) in peopleMap"
          :key="idx"
        >
          <td>{{ person.person_name }}</td>
          <td>{{ person.person_age }} {{ person.person_age > 1 ? 'Anos' : 'Anos' }}</td>
          <td>
            <v-icon
              small
              @click="$emit('remove', person.person_id)"
            >
              mdi-delete
            </v-icon>
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>
<script>
import moment from 'moment'
export default {
  name: 'PeopleList',
  props: {
    people: {
      type: Array,
      required: false,
      default: () => []
    }
  },
  computed: {
    headers: () => [
      { text: 'Nome', value: 'person_name' },
      { text: 'Idade', value: 'person_age' },
    ],
    peopleMap () {
      return this.people.map(x => ({
        ...x,
        person_age: moment().diff(x.person_birthdate, 'years')
      }))
    }
  }
  }
</script>
