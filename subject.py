class Subject:
    """
    subject from subjects dataframe turned into an object
    """
    def __init__(self, subject_id=-1, subject_name_id=None, class_id=None, number_of_groups=0,
                 lesson_hour_id=None, teachers_id=None, classroom_id=None, is_empty=False,
                 movable=True, group=None, max_stack=None, classroom_types=[],
                 log_file_name=''):

        if teachers_id is None:
            teachers_id = [-1]
        self.subject_id = subject_id
        self.subject_name_id = subject_name_id
        self.class_id = class_id
        self.number_of_groups = number_of_groups
        self.lesson_hour_id = lesson_hour_id
        self.teachers_id = teachers_id
        self.classroom_id = classroom_id
        self.is_empty = is_empty
        self.max_stack = max_stack
        self.movable = movable
        self.group = group
        self.classroom_types = classroom_types


def split_subjects(subjects_df, teachers, classes_id):
    """
    :param subjects_df: dataframe of all subjects
    :param teachers: list of school_classes
    :param classes_id: list of ids of classes
    :return: split per teacher lists of subjects
    """

    subject_per_teacher_per_class = {}
    for teacher_id in teachers:
        subject_per_teacher_df = subjects_df[subjects_df['teachers_id'].apply(lambda x: teacher_id in x)]

        subject_per_teacher_per_class[teacher_id] = {}
        for class_id in classes_id:
            subject_per_teacher_per_class[teacher_id][class_id] = []

            subject_per_teacher_classes_df = subject_per_teacher_df[subject_per_teacher_df['class_id'] == class_id]

            for index, row in subject_per_teacher_classes_df.iterrows():
                for _ in range(row['subject_count_in_week']):
                    subject_per_teacher_per_class[teacher_id][class_id].append(
                        Subject(
                            subject_id=int(row['subject_id']),
                            subject_name_id=int(row['subject_name_id']),
                            class_id=int(row['class_id']),
                            number_of_groups=int(row['number_of_groups']),
                            teachers_id=[int(x) for x in row['teachers_id']],
                            max_stack=int(row['max_stack']),
                            classroom_types=row['classroom_types']
                        )
                    )

    return subject_per_teacher_per_class
