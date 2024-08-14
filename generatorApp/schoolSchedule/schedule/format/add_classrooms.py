import numpy as np


def add_classrooms(self, classrooms, teachers, days):
    """
    :param self:
    :param classrooms: list of classrooms
    :param teachers: list of all teachers in schedule
    :param days: list of days
    :description: adding classrooms to subjects
    """
    for class_id in self.data:
        class_schedule = self.data[class_id]
        for day in days:
            class_schedule_at_day = class_schedule[day]

            for subjects_list in class_schedule_at_day:
                for subject in subjects_list:

                    if subject.classroom_id is not None or subject.is_empty:
                        continue

                    print("*" * 10)

                    stacked_subjects, _ = self.get_stacked_lessons(
                        class_id=class_id,
                        day=day,
                        group=subject.group,
                        lesson_index=subject.lesson_hour_id
                    )

                    for classroom in classrooms:
                        valid = True
                        for stacked_subject in stacked_subjects:
                            teacher_id = stacked_subject.teachers_id[0]
                            teacher = teachers[teacher_id]
                            try:
                                main_classroom = str(int(teacher.main_classroom))
                            except ValueError:
                                main_classroom = None

                            if (main_classroom is not None and main_classroom != classroom) \
                               or classroom in self.get_same_time_classrooms(
                                day,
                                stacked_subject.lesson_hour_id
                            ):
                                valid = False
                                break

                            elif classrooms[classroom].type_id not in stacked_subject.classroom_types   \
                                or classroom in self.get_same_time_classrooms(
                                day,
                                stacked_subject.lesson_hour_id
                            ):
                                valid = False
                                break

                        if valid:
                            for stacked_subject in stacked_subjects:
                                stacked_subject.classroom_id = classroom
                            break
    return self
