class StaticArray:
    def __init__(self, data_num):
        self.data = [None] * data_num
        self.contain = 0

    def set_at(self, i, x):
        if not (0 <= i < len(self.data)):
            print('invalid set index')
        else:
            self.data[i] = x
            self.contain += 1

    def get_at(self, i):
        if not (0 <= i < len(self.data)):
            print('invalid get index')
        else:
            return self.data[i]


def birthday_match(students):
    '''
    find a pair of student with the same birthday or all students with tht same birthday
    :param students: all students
    :return: a dict, the key is the birthday and item is the name
    '''
    n = len(students)
    student_record = StaticArray(n)
    lucky_guys = {}  # record all student in the same birthday
    for i in range(n):
        found = False
        name1, birthday1 = students[i]
        for k in range(student_record.contain):
            name2, birthday2 = student_record.get_at(k)
            if birthday1 == birthday2:
                '''
                find all student in the same birthday, may be many student have different same birthday
                it need to look through all students
                '''
                found = True
                if lucky_guys.get(birthday2) == None:
                    lucky_guys.setdefault(birthday2, [name1, name2])
                else:
                    lucky_guys[birthday2].append(name1)
                break

                # this method only find a pair of student in the same birthday
                # return name1, name2, birthday2
        if not found:
            student_record.set_at(student_record.contain, students[i])
    return lucky_guys


if __name__ == '__main__':
    students = [('jason', '6.23'), ('how', '6.23'), ('why', '9.4'), ('maomao', '2.5'), ('what', '9.4')]
    match = birthday_match(students)
    print(match)
