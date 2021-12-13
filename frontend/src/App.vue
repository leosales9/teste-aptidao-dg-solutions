<template>
  <v-app>
    <v-container>
      <v-row align="center">
        <v-col align-self="start" xs="6">
          <person-form @save="createPerson"/>
        </v-col>
        <v-col xs="6">
          <people-list
            :people="people"
            @remove="removePerson"
          />
        </v-col>
      </v-row>
      <v-snackbar
        v-model="snackbar.visible"
        :timeout="snackbar.timeout"
        :color="snackbar.type"
        absolute
        bottom
      >
        {{ snackbar.message }}
        <template #actions="{ attrs }">
          <v-btn
            v-bind="attrs"
            @click="snackbar.visible = false"
          >
            Fechar <v-icon>mdi-close</v-icon>
          </v-btn>
        </template>
      </v-snackbar>
    </v-container>
  </v-app>
</template>
<script>
import PeopleList from './components/PeopleList.vue'
import {
  list,
  create,
  remove
} from './api/peopleAPI'
import PersonForm from './components/PersonForm.vue'
export default {
  name: 'App',
  components: { PeopleList, PersonForm },
  data: () => ({
    people: [],
    person: {},
    snackbar: {
      visible: false,
      type: null,
      message: null,
      timeout: 1500
    }
  }),
  created () {
    this.listPeople()
  },
  methods: {
    listPeople () {
      list()
        .then(res => this.people = [...res.data.people])
    },
    createPerson (person) {
      create(person)
        .then(() => this.popSnackbar('success', 'Salvo com sucesso'))
        .then(() => this.listPeople())
        .catch(err => {
          this.popSnackbar('error', 'Não foi possível salvar')
          console.error(err)
        })
    },
    removePerson (person_id) {
      remove(person_id)
        .then(() => this.popSnackbar('success', 'Removido com sucesso'))
        .then(() => this.listPeople())
        .catch(err => {
          this.popSnackbar('error', 'Não foi possível remover')
          console.error(err)
        })
    },
    popSnackbar (type = 'success', message = 'Sucesso') {
      this.snackbar = {
        ...this.snackbar,
        visible: true,
        type,
        message
      }
    }
  }
}
</script>
