<template>
  <v-form>
    <v-text-field
      v-model="person.person_name"
      label="Nome"
      prepend-icon="mdi-account-circle"
      trim
    />
    <v-menu
      v-model="menuDate"
      :close-on-content-click="false"
      :nudge-right="40"
      transition="scale-transition"
      offset-y
      min-width="290px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-text-field
          v-model="dateFormatted"
          label="Data de Nascimento"
          prepend-icon="mdi-calendar-blank-outline"
          readonly
          v-bind="attrs"
          v-on="on"
        />
      </template>
      <v-date-picker
        v-model="person.person_birthdate"
        @input="menuDate = false"
        locale="pt-br"
      />
    </v-menu>
    <v-btn
      :disabled="!valid"
      color="primary"
      block
      @click="submit()"
    >
      <v-icon>mdi-account-plus</v-icon> Salvar
    </v-btn>
  </v-form>
</template>
<script>
import moment from 'moment'

export default {
  name: 'PersonForm',
  data: () => ({
    person: {},
    dateFormatted: null,
    menuDate: false
  }),
  computed: {
    valid () {
      return !!this.person.person_name && !!this.person.person_birthdate
    },
    computedDateFormatted () {
      return this.formatDate(this.person.person_birthdate)
    },
  },
  methods: {
    submit() {
      if(moment(this.person.person_birthdate).diff(moment(), 'days') > 0){
        return
      }
      this.$emit('save', { ...this.person })
      this.person.person_name = null
      this.person.person_birthdate = null
    },
    formatDate (date) {
      if (!date) return null
      const [year, month, day] = date.split('-')
      return `${month}/${day}/${year}`
    },
    parseDate (date) {
      if (!date) return null
      const [month, day, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    }
  },
  watch: {
    'person.person_birthdate'() {
      this.dateFormatted = this.formatDate(this.person.person_birthdate)
    }
  }
}
</script>
