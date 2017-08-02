import csv


class Student:
    def __init__(self, name, middle_name, last_name):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name


class RescueERP:
    def __init__(self, file_name='students.csv'):
        self.students = [student for student in self.reader(file_name)]

    def reader(self, file_name='students.csv'):
        with open(file_name) as file:
            reader = csv.DictReader(file)
            self.headers = reader.fieldnames
            for row in reader:
                name = self.prepare_string(row['name'])
                middle_name = self.prepare_string(row['middle_name'])
                last_name = self.prepare_string(row['last_name'])
                yield (Student(name, middle_name, last_name))

    @classmethod
    def prepare_string(cls, string):
        result = cls.to_upper_case(string)
        result = cls.correct_number_of_ns(result)
        result = cls.remove_number_if_present(result)
        return result

    @classmethod
    def remove_number_if_present(cls, string):
        aux_name = string.split(' ')
        if aux_name[0].isnumeric():
            aux_name = ' '.join(aux_name[1:])
        else:
            aux_name = ' '.join(aux_name[:])
        return aux_name

    @classmethod
    def correct_number_of_ns(cls, string):
        aux_text = string.replace('rrr', '##')
        aux_text = aux_text.replace('rr', 'r')
        aux_text = aux_text.replace('##', 'rr')
        return aux_text

    @classmethod
    def to_upper_case(cls, string):
        return string.upper()

    def to_latex(self, file_name='students.tex'):
        out = open(file_name, 'w')
        # Header file
        out_t = '\\begin{table}[h]\n\\begin{tabular}{|l|l|l|}\n\\hline\n'

        for h in self.headers:
            if h == 'name':
                out_t += h + '\\\\ \\hline\n'
            else:
                out_t += h + ' & '

        out.write(out_t)

        for register in self.students:
            out_t = '{0} & {1} & {2} \\\\ \\hline\n' \
                .format(register.middle_name, register.last_name,
                        register.name)
            out.write(out_t)

        out_t = '\end{tabular}\n \end{table}\n'
        out.write(out_t)
        out.close()

    def to_html(self, file_name='students.html'):
        out = open(file_name, 'w')
        # Header archivo
        out_t = '<table>\n<tr>'

        for h in self.headers:
            out_t += '<th>{0}</th>'.format(h)
        out_t += '</tr>'
        out.write(out_t)
        for register in self.students:
            out_t = '<tr>\n<td>{0}</td>\n<td>{1}</td>\n<td>{2}</td>\n</tr>\n' \
                .format(register.middle_name, register.last_name, register.name)
            out.write(out_t)

        out_t = '</table>'
        out.write(out_t)
        out.close()

    def to_markdown(self, file_name='students.md'):
        out = open(file_name, 'w')
        # Header archivo
        out_t = '|'

        for h in self.headers:
            out_t += h + '|'
        out_t += '\n|------------|--------|---------|\n'
        out.write(out_t)
        out_t = ''
        for register in self.students:
            out_t = '|{0}|{1}|{2}|\n' \
                .format(register.middle_name, register.last_name, register.name)
            out.write(out_t)
        out.close()


if __name__ == '__main__':
    rescue_siding = RescueERP()
    rescue_siding.to_latex()
    rescue_siding.to_html()
    rescue_siding.to_markdown()
