from model.people_model import PeopleModel


class PeopleController:

    def __init__(self, database):
        self.__model = PeopleModel(database)

    def get_people(self):
        return self.__model.list_all()

    def create_person(self, person):
        return self.__model.create(person)

    def remove_person(self, person_id):
        return self.__model.remove(person_id)
