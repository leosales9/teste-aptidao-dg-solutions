from flask import jsonify
from psycopg2.extras import RealDictCursor


class PeopleModel:
    def __init__(self, database):
        self.__database = database
        self.__cursor = None

    def list_all(self):
        try:
            sql = "SELECT person_id, person_name, person_birthdate FROM people"

            self.__cursor = self.__database.cursor(cursor_factory=RealDictCursor)
            self.__cursor.execute(sql)

            people = self.__cursor.fetchall()
            return jsonify({'people': people}), 200

        except Exception as e:
            return jsonify({'msg': 'Erro', 'err': e}), 500

        finally:
            self.__cursor.close()

    def create(self, person):
        try:
            sql = "INSERT INTO people(" \
                  "person_name," \
                  "person_birthdate" \
                  ") VALUES ('{0}','{1}')".format(person['person_name'], person['person_birthdate'])

            self.__cursor = self.__database.cursor()
            self.__cursor.execute(sql)
            self.__database.commit()

            return jsonify({'msg': 'Success'}), 200

        except Exception as e:
            return jsonify({'msg': 'Erro', 'err': e}), 500

        finally:
            self.__cursor.close()

    def remove(self, person_id):
        try:
            sql = "DELETE FROM people " \
                  "WHERE person_id = {0}".format(person_id)

            self.__cursor = self.__database.cursor()
            self.__cursor.execute(sql)
            self.__database.commit()

            return jsonify({'msg': 'Success'}), 200

        except Exception as e:
            return jsonify({'msg': 'Erro', 'err': e}), 500

        finally:
            self.__cursor.close()
