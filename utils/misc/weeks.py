from datetime import datetime

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
para_time_alldays = ['8:30', '10:15', '12:00', '14:15', '16:00', '17:55', '19:40', '']
para_time_saturday = ['8:30', '10:15', '12:00', '13:45', '15:30', '17:15', '19:00', '']
weeks = [datetime.strptime('09 01 2020', '%m %d %Y'), datetime.strptime('09 07 2020', '%m %d %Y'),
         datetime.strptime('09 14 2020', '%m %d %Y'), datetime.strptime('09 21 2020', '%m %d %Y'),
         datetime.strptime('09 28 2020', '%m %d %Y'), datetime.strptime('10 05 2020', '%m %d %Y'),
         datetime.strptime('10 12 2020', '%m %d %Y'), datetime.strptime('10 19 2020', '%m %d %Y'),
         datetime.strptime('10 26 2020', '%m %d %Y'), datetime.strptime('11 02 2020', '%m %d %Y'),
         datetime.strptime('11 09 2020', '%m %d %Y'), datetime.strptime('11 16 2020', '%m %d %Y'),
         datetime.strptime('11 23 2020', '%m %d %Y'), datetime.strptime('11 30 2020', '%m %d %Y'),
         datetime.strptime('12 07 2020', '%m %d %Y'), datetime.strptime('12 14 2020', '%m %d %Y'),
         datetime.strptime('12 21 2020', '%m %d %Y'), datetime.strptime('12 28 2020', '%m %d %Y'),
         datetime.strptime('01 04 2021', '%m %d %Y'), datetime.strptime('01 11 2021', '%m %d %Y'),
         datetime.strptime('01 18 2021', '%m %d %Y'), datetime.strptime('01 25 2021', '%m %d %Y'),
         datetime.strptime('02 01 2021', '%m %d %Y'), datetime.strptime('02 08 2021', '%m %d %Y'),
         datetime.strptime('02 15 2021', '%m %d %Y'), datetime.strptime('02 22 2021', '%m %d %Y'),
         datetime.strptime('03 01 2021', '%m %d %Y'), datetime.strptime('03 08 2021', '%m %d %Y'),
         datetime.strptime('03 15 2021', '%m %d %Y'), datetime.strptime('03 22 2021', '%m %d %Y'),
         datetime.strptime('03 29 2021', '%m %d %Y'), datetime.strptime('04 05 2021', '%m %d %Y'),
         datetime.strptime('04 12 2021', '%m %d %Y'), datetime.strptime('04 19 2021', '%m %d %Y'),
         datetime.strptime('04 26 2021', '%m %d %Y'), datetime.strptime('05 03 2021', '%m %d %Y'),
         datetime.strptime('05 10 2021', '%m %d %Y'), datetime.strptime('05 17 2021', '%m %d %Y'),
         datetime.strptime('05 24 2021', '%m %d %Y'), datetime.strptime('05 31 2021', '%m %d %Y'),
         datetime.strptime('06 07 2021', '%m %d %Y'), datetime.strptime('06 14 2021', '%m %d %Y'),
         datetime.strptime('06 21 2021', '%m %d %Y'), datetime.strptime('06 28 2021', '%m %d %Y')]


def get_week():
    today = datetime.now()
    for i, day in enumerate(weeks):
        if today < day:
            return (i - 1) % 2
