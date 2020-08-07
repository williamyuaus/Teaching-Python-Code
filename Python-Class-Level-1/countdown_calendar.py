from tkinter import Tk, Canvas
from datetime import date, datetime

root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(100, 50, anchor='w', fill='orange',
              font='Arial 28 bold underline', text='My Countdown Calendar')

def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d%m%Y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    #number_of_days = time_between.split(' ')
    return time_between
#number_of_days[0]

events = get_events()
today = date.today()


vertical_space = 100
for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = 'It is %s days until %s' % (days_until, event_name)
    c.create_text(100, vertical_space, anchor='w', fill='lightblue',
                  font='Arial 28 bold', text = display)
    vertical_space = vertical_space + 30

