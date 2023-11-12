import tkinter as tk
import tkcap
import os


# TODO: change to handle lists of subjects and multiple teachers in same time
def tkinter_schedule_vis(schedule, days, subjects_num=1000, capture_name='tkCapture', dir_name='log_0', capture=True):
    def rgb(red, green, blue):
        return f'#{red:02x}{green:02x}{blue:02x}'

    root = tk.Tk()
    colors = []
    for i in range(subjects_num):
        colors.append(rgb(
            min(max(100, (i * 10) % 255), 200),
            max(100, (i * 20) % 255),
            max(100, (i * 30) % 255))
        )

    grid = {}
    for i, day in enumerate(days):  # i -> day id
        week_day = tk.Label(root, text=day, font=("Arial", 14))
        week_day.grid(row=0, column=i * len(schedule), columnspan=len(schedule))
        for j, class_schedule_id in enumerate(schedule):  # j -> class id
            class_schedule = schedule[class_schedule_id]
            for k in range(len(class_schedule[day])):  # k -> subject id
                subjects = class_schedule[day][k]

                same_time_subjects = []
                for x, other_class_schedule_id in enumerate(schedule):
                    other_class_schedule = schedule[other_class_schedule_id]
                    if other_class_schedule != class_schedule:
                        try:
                            same_time_subjects.append(other_class_schedule[day][k])
                        except IndexError:
                            pass

                color = colors[subject.subject_id - 1]
                for other_subject in same_time_subjects:
                    if other_subject.teacher_id == subject.teacher_id:
                        color = rgb(255, 0, 0)

                if subjects[0].is_empty:
                    label = tk.Label(
                        root,
                        text="empty",
                        font=("Arial", 8),
                        bg=rgb(173, 217, 230)
                    )
                else:
                    label = tk.Label(
                        root,
                        text=f"teacher: {teachers}\n"
                        f"lesson_hours_id: {subjects[0].lesson_hours_id}",
                        font=("Arial", 8),
                        bg=color
                    )

                label.grid(row=k + 1, column=i * len(schedule) + j)

    if not os.path.exists('logs'):
        os.mkdir('logs')

    if not os.path.exists(f'logs/{dir_name}'):
        os.mkdir(f'logs/{dir_name}')

    if capture:
        cap = tkcap.CAP(root)
        cap.capture(f'logs/{dir_name}/{capture_name}.jpg')

        root.after(0, lambda: root.destroy())
        root.mainloop()
