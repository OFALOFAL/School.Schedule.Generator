from debug_log import debug_log


class Subject:
    """
    subject from subjects dataframe turned into an object
    """
    def __init__(self, subject_id=0, subject_name_id=0, class_id=0, number_of_groups=0, subject_length=0,
                 lesson_hours_id=0, teachers_id=None, classroom_id=0, is_empty=False,
                 movable=True, group=None, max_stack=0,
                 log_file_name=''):

        if teachers_id is None:
            teachers_id = [-1]
        self.subject_id = subject_id
        self.subject_name_id = subject_name_id
        self.class_id = class_id
        self.number_of_groups = number_of_groups
        self.subject_length = subject_length
        self.lesson_hours_id = lesson_hours_id
        self.teachers_id = teachers_id
        self.classroom_id = classroom_id
        self.is_empty = is_empty
        self.max_stack = max_stack
        self.movable = movable
        self.group = group
