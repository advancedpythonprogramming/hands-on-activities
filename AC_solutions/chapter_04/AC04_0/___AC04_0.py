class CompanyMeta(type):
    first = True

    def __new__(meta, clsname, bases, clsdict):
        if not (clsname == 'Company'):
            raise NameError('Cannot use {} as class name'.format(clsname))

        def raise_salary(self, employee_id, password):
            if self.boss.password == password:
                self.employees[employee_id].salary *= 2

        def new_employee(self, employee):
            if employee.__class__.__name__ == 'Employee':
                self.employees[employee.employee_id] = employee

        clsdict['new_employee'] = new_employee
        clsdict['raise_salary'] = raise_salary

        print('Creating company...\n')

        return super().__new__(meta, clsname, bases, clsdict)

    def __call__(cls, *args, **kwargs):
        if kwargs == {}:
            CompanyMeta.first = not CompanyMeta.first
            return super().__call__(*args, **kwargs)
        elif 'company' in kwargs and kwargs[
            'company'].__class__.__name__ == 'Company':
            s = 0
            for ID in kwargs['company'].employee:
                s += kwargs['company'].employees[ID].salary
            s += kwargs['company'].boss.salary
            return 'The company will spend ${} in its employees'.format(s)
        else:
            raise AttributeError('Not a company')


class PersonMeta(type):
    def __new__(meta, clsname, bases, clsdict):
        if clsname not in ['Person', 'Employee', 'Boss']:
            raise NameError('Not a valid class name')

        def do_task(self, task):
            print('{} has to {}'.format(self.name, task))
            print('Doing task...')
            print('Finished {}'.format(task), '\n')

        clsdict['__call__'] = do_task
        return super().__new__(meta, clsname, bases, clsdict)
