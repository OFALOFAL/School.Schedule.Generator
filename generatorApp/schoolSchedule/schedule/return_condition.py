def are_teachers_taken(self, teachers_id, day, lesson_index):
    same_time_teachers = self.get_same_time_teacher(
        day_to=day,
        lesson_index=lesson_index,
    )

    for teacher in teachers_id:
        for same_time_teacher in same_time_teachers:
            if same_time_teacher == teacher:
                return True
    return False


def check_teacher_conditions(teachers_id, day, days, lesson_index, teachers):
    if type(teachers_id) is not list:
        teachers_id = [teachers_id]

    day_index = days.index(day)
    for teacher_id in teachers_id:
        teacher = teachers[teacher_id]
        start_index = teacher.start_hour_index[day_index]
        end_index = teacher.end_hour_index[day_index]
        if end_index == -1:
            end_index = lesson_index

        if not ((start_index <= lesson_index <= end_index) and teachers[teacher_id].days[day_index]):
            return False

    return True
