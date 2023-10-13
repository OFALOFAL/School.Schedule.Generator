import tkinter as tk


def tkinter_schedule_vis(schedule, days, subjects_num):
    def rgb(red, green, blue):
        return f'#{red:02x}{green:02x}{blue:02x}'

    root = tk.Tk()
    colors = []
    for i in range(subjects_num):
        colors.append(rgb(
            min(max(100, (i*10) % 255), 200),
            max(100, (i*20) % 255),
            max(100, (i*30) % 255))
        )

    grid = {}
    for i, day in enumerate(days):  # i -> day id
        week_day = tk.Label(root, text=day, font=("Arial", 16))
        week_day.grid(row=0, column=i * len(schedule), columnspan=len(schedule))

        for j, class_schedule in enumerate(schedule):   # j -> class id
            for k in range(len(class_schedule[day])):    # k -> subject id
                subject = class_schedule[day][k]
                b = tk.Label(
                    root,
                    text=f"subject_name_id:{subject.subject_name_id}\nteacher: {subject.teacher_id}",
                    bg=colors[subject.subject_id-1]
                )
                b.grid(row=k+1, column=i * len(schedule) + j)

    root.mainloop()
