import tkinter as tk
import tkcap
import os
from .settings import settings


def tkinter_schedule_vis(schedule, days, capture_name='tkCapture', dir_name='log_0', capture=True):

    if not (settings.TKCAPTURE and capture and settings.DEBUG):
        return False

    def get_invalid_data(day_to, lesson_index, class_id, group):
        same_time_teachers = []
        same_time_classrooms = []
        for class_schedule_id in schedule.data:
            try:
                subjects_list = schedule.data[class_schedule_id][day_to][lesson_index]
                for subject in subjects_list:
                    if subject.group is None and class_schedule_id == class_id:
                        continue
                    if subject.group is not None and class_schedule_id == class_id and subject.group == group:
                        continue
                    same_time_teachers.append(subject.teachers_id[0])

                    if subject.classroom_id is not None:
                        same_time_classrooms.append(subject.classroom_id)
            except IndexError:
                pass
        return same_time_teachers, same_time_classrooms

    def rgb(red, green, blue):
        return f'#{red:02x}{green:02x}{blue:02x}'

    def get_digits(number):
        return [int(d) for d in str(number)]

    root = tk.Tk()
    data = schedule.data

    for i, day in enumerate(days):  # i -> day id
        week_day = tk.Label(root, text=day, font=("Arial", 14))
        week_day.grid(row=0, column=i * len(data), columnspan=len(data))

        # loop through classes and subjects
        for j, class_schedule_id in enumerate(data):  # j -> class id
            class_schedule = data[class_schedule_id]
            for k in range(len(class_schedule[day])):  # k -> subject id
                subjects_list = class_schedule[day][k]

                if subjects_list[0].is_empty:
                    label = tk.Label(
                        root,
                        text="empty",
                        font=("Arial", 8),
                        bg=rgb(173, 217, 230)
                    )
                else:
                    color = [27, 58, 19]
                    last_digit = 1

                    for subject in subjects_list:
                        taken_teachers, taken_classrooms = get_invalid_data(day, subject.lesson_hour_id,
                                                                            class_schedule_id, subject.group)
                        if subject.teachers_id[0] in taken_teachers or subject.classroom_id in taken_classrooms:
                            color = [255, 0, 0]
                            break

                        for teacher_id in subject.teachers_id:
                            for digit in get_digits(teacher_id):
                                color[1] *= digit + 1
                            color[1] = color[1] % 255

                            for digit in reversed(get_digits(teacher_id)):
                                color[2] *= digit + 1
                                last_digit = digit
                            color[2] = color[2] % 255

                        color[0] *= last_digit + 1
                        color[0] = color[0] % 255
                        color[0] = min(color[0], 200)

                    teachers = []
                    classrooms = []

                    for subject in subjects_list:
                        if subject.classroom_id is not None:
                            classrooms.append(subject.classroom_id)

                        teachers.append(subject.teachers_id[0])

                    color = rgb(*color)

                    subjects_ids = [x.subject_id for x in subjects_list]

                    label = tk.Label(
                        root,
                        text=f"subjects id {subjects_ids}\n"
                        f"teacher: {teachers}\n"
                        f"lesson_hour_id: {subjects_list[0].lesson_hour_id}\n"
                        f"classrooms_id: {classrooms}",
                        font=("Arial", 8),
                        bg=color
                    )

                label.grid(row=k + 1, column=i * len(data) + j)

    if not os.path.exists('logs'):
        os.mkdir('logs')

    if not os.path.exists(f'logs/{dir_name}'):
        os.mkdir(f'logs/{dir_name}')

    if not os.path.exists(f'logs/{dir_name}/{schedule.version}'):
        os.mkdir(f'logs/{dir_name}/{schedule.version}')

    if capture:
        cap = tkcap.CAP(root)
        cap.capture(f'logs/{dir_name}/{schedule.version}/{capture_name}.jpg')

        root.after(0, lambda: root.destroy())
        root.mainloop()

    return True
