class MetaRobot(type):
    def __new__(meta, name, base_classes, dictionary):
        if (name != 'Robot'):
            raise NameError('A class other than Robot is attempting to '
                            'be created')

        creator = 'my_user_name'
        start_ip = '190.102.62.283'

        def check_creator(self):
            if self.creator in self.creators:
                print('The creator of the robot is in the list of '
                      'programmers!')
                return True
            print('Danger!! The creator of the robot is trying to blame'
                  'someone else! Stop him!!')
            return False

        def change_node(self, node):
            print('Moving from conection {} to conection {}!'
                  .format(self.actual.ide, node.ide))
            self.actual = node

        def disconnect(self):

            if self.Verify():
                print('Congratulations! You have found a hacker and ',
                      end='')
                print('you kicked him out of the network!')

                # disconnect the hacker from the actual port
                self.actual.hacker = 0
                return True

            print('Hey! There is no hacker here!')

        dictionary['creator'] = creator
        dictionary['start_ip'] = start_ip
        dictionary['check_creator'] = check_creator
        dictionary['change_node'] = change_node
        dictionary['disconnect'] = disconnect
        return super().__new__(meta, name, base_classes, dictionary)
