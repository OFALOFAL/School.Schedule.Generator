class Settings:
    def __init__(self):
        # Describe mode to run the program on
        self.DEBUG = True

        # Take screenshots - True
        self.TKCAPTURE = False
        self.SAVELOG = False

        # if debug create default names
        self.TEST_DATA_PATH = '../../testdata'
        self.BASE_DATA_PATH = '../static/data'
        self.DATABASE_NAME = 'db'
        self.DF_NAMES = ['SSG_LESSON_HOURS', 'SSG_SUBJECT_NAMES', 'SSG_SUBJECTS', 'SSG_TEACHERS', 'SSG_CLASSES',
                         'SSG_CLASSROOMS', 'SSG_CLASSROOM_TYPES']

        self.COLUMN_NAMES = {
            'SSG_LESSON_HOURS': ['lesson_id', 'start_hour', 'duration'],
            'SSG_SUBJECT_NAMES': ['subject_name_id', 'name'],
            'SSG_SUBJECTS': ['subject_id', 'subject_name_id', 'class_id', 'subject_count_in_week',
                             'number_of_groups', 'subject_length', 'lesson_hours_id', 'teachers_id',
                             'classroom_id', 'max_stack', 'classroom_types'],
            'SSG_TEACHERS': ['teacher_id', 'name', 'surname', 'possible_subjects', 'start_hour_index',
                             'end_hour_index', 'days', 'main_classroom'],
            'SSG_CLASSES': ['Class_id', 'grade', 'class_signature',
                            'supervising_teacher', 'starting_lesson_hour_id'],
            'SSG_CLASSROOMS': ['classroom_id', 'classroom_name', 'type_id'],
            'SSG_CLASSROOM_TYPES': ['type_id', 'description']
        }

        self.SQLTABLES = {
            'SSG_LESSON_HOURS': {
                'Name': 'LessonHours',
                'Columns': self.COLUMN_NAMES['SSG_LESSON_HOURS']
            },
            'SSG_SUBJECT_NAMES': {
                'Name': 'SubjectNames',
                'Columns': self.COLUMN_NAMES['SSG_SUBJECT_NAMES']
            },
            'SSG_SUBJECTS': {
                'Name': 'Subject',
                'Columns': self.COLUMN_NAMES['SSG_SUBJECTS']
            },
            'SSG_TEACHERS': {
                'Name': 'Teachers',
                'Columns': self.COLUMN_NAMES['SSG_TEACHERS']
            },
            'SSG_CLASSES': {
                'Name': 'Classes',
                'Columns': self.COLUMN_NAMES['SSG_CLASSES']
            },
            'SSG_CLASSROOMS': {
                'Name': 'Classrooms',
                'Columns': self.COLUMN_NAMES['SSG_CLASSROOMS']
            },
            'SSG_CLASSROOM_TYPES': {
                'Name': 'ClassroomTypes',
                'Columns': self.COLUMN_NAMES['SSG_CLASSROOM_TYPES']
            }
        }


settings = Settings()
