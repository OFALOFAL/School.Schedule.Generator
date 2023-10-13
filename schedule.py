import random

class Schedule:
    def __init__(self):
        self.school_schedule = []

    def add_class_schedule(self, class_schedule):
        self.school_schedule.append(class_schedule)

    def create(self, classes_id, conditions, days, subject_per_class):
        for class_id in classes_id:
            new_class_schedule = self.create_class_schedule(days)
            for subject in subject_per_class[class_id]:
                for i in range(subject.subject_count_in_week):
                    day = random.choice(days)
                    while len(new_class_schedule[day]) >= conditions.general['max_lessons_per_day']:
                        day = random.choice(days)

                    subject.lesson_hours_id = len(new_class_schedule[day])
                    new_class_schedule[day].append(subject)
            self.add_class_schedule(new_class_schedule)

        return self

    @staticmethod
    def create_class_schedule(days):
        """
        :param days: list of days that the lessons can be in
        :return: empty schedule of passed in days
        """
        new_class_schedule = {}
        for day in days:
            new_class_schedule[day] = []
        return new_class_schedule

    def move_from_bottom(self, class_id, day_from, day_to):
        pass

    def move_from_top(self, class_id, day_from, day_to):
        pass

    def print(self, classes_id, days, print_subjects=False):
        for i, class_schedule in enumerate(self.school_schedule):
            print(f'class {classes_id[i]}')
            for j in range(len(class_schedule)):
                print(f'\t{days[j]}\n\t\tlen={len(class_schedule[days[j]])}')
                if print_subjects:
                    for subject in class_schedule[days[j]]:
                        print(f'\t\t{subject.subject_name_id}')
                print('\n')
            print('-' * 10)

    def swap(self):
        pass
