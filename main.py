
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import jdatetime
# jdatetime is a Python library for working with Jalali (Persian) dates


def count():
    try:
        year = int(year_entry.get())
    except ValueError:
        messagebox.showerror('خطا', 'سال را به عدد وارد کنید')
        return
    month = month_map[month_combo.get()]
    day = day_combo.get()

    try:
        birth_date = jdatetime.date(
            int(year),
            month,
            int(day),
        )

    except ValueError:
        messagebox.showerror('خطا', 'ماه انتخاب شده کمتر از 31 روز دارد')
        return

    today = jdatetime.date.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        days += 30
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    if birth_date > todaydate:
        messagebox.showerror('خطا', 'تاریخ وارد شده هنوز نرسیده است')
        return

    result = Label(
        window, text=(f'سن شما  {years} سال  و {months} ماه  و {days} روز میباشد'), font=('', 17))
    result.place(width=370, height=50, x=65, y=470)


def click():
    answer = messagebox.askyesno('خروج', 'آیا میخواهید از برنامه خارج شوید؟')
    if answer == True:
        window.destroy()


window = Tk()
window.geometry('580x580+1250+140')
window.resizable(False, False)
window.title('Age calculate')

todaydate = jdatetime.date.today()

label0 = Label(window, text='تاریخ امروز  :  ' + str(todaydate), font=('', 16))
label0.place(width=220, height=40, x=50, y=10)


label1 = Label(window, text='محاسبه سن دقیق',
               font=('', 23), bg='#111855', fg="#41f1fe")
label1.place(width=180, height=40, x=310, y=10)

line1 = Label(bg="#644076").place(width=600, height=4, y=60)
line2 = Label(bg="#644076").place(width=4, height=600, x=30)
line3 = Label(bg="#644076").place(width=4, height=600, x=550)

natije = Label(window, text=' : نتیجه', font=('', 23))
natije.place(width=85, height=50, x=430, y=470)

year_label = Label(window, text=':  سال تولد', font=('', 22))
year_label.place(width=120, height=40, x=320, y=90)

year_entry = Entry(window, font=('', 18))
year_entry.place(width=100, height=40, x=190, y=92)
year_entry.focus()

month_label = Label(window, text=':  ماه تولد', font=('', 22))
month_label.place(width=120, height=40, x=320, y=160)


month_combo = ttk.Combobox(window, font=('', 18))
month_combo.place(width=100, height=40, x=190, y=162)
month_combo['values'] = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر',
                         'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
month_combo.current(0)


# ----Dictionary mapping----
month_map = {

    'فروردین': 1,
    'اردیبهشت': 2,
    'خرداد': 3,
    'تیر': 4,
    'مرداد': 5,
    'شهریور': 6,
    'مهر': 7,
    'آبان': 8,
    'آذر': 9,
    'دی': 10,
    'بهمن': 11,
    'اسفند': 12,
}

day_label = Label(window, text=':  روز تولد', font=('', 22))
day_label.place(width=120, height=40, x=320, y=230)

day_combo = ttk.Combobox(window, font=('', 18))
day_combo.place(width=100, height=40, x=190, y=232)
day_combo['values'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                       '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
day_combo.current(0)

countbutton = Button(window, text='محاسبه', font=('', 22),
                     bg="#3db213", fg='black', command=count)
countbutton.place(width=90, height=50, x=115, y=330)

exitbutton = Button(window, text='خروج از برنامه', font=('', 20),
                    bg="#b21313", fg='white', command=click)
exitbutton.place(width=180, height=50, x=280, y=330)

exit_button = (window.protocol('WM_DELETE_WINDOW', click))

mainloop()
