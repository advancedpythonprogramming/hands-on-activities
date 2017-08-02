import requests
import json
from classes import Student, ConsoleApp


class SpyKiller:
    def __init__(self, my_name, my_username, url):
        self.my_username = my_username
        self.my_name = my_name
        self.url = url

    def mark_absent(self, victim):
        '''
        Mark student (victim) as absent.
        '''
        request = None

        ############
        # COMPLETE #
        ############

        if request and request.status_code == 202:
            return 'return JSON if success'
        return 'return error message'

    def register_me(self):
        '''
        Register your username
        '''
        username = self.my_username
        name = self.my_name
        assistance = True

        request = None

        ############
        # COMPLETE #
        ############

        if request and request.status_code == 201:
            return 'return JSON if success'
        return 'return error message'

    def download_list(self):
        '''
        Return a list of all available students
        '''

        students = []

        ############
        # COMPLETE #
        ############

        return students


if __name__ == '__main__':
    spykiller = SpyKiller(
        my_name='FIRSTNAME_LASTNAME',
        my_username='GITHUB_USERNAME',
        url='http://assistance-py.herokuapp.com'
    )

    ConsoleApp(spykiller).run()
