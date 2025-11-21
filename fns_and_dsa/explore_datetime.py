import datetime


def display_current_datetime () :
    current = datetime.datetime.now()
    current_date = current.date()

    year = current.strftime("%Y")
    month = current.strftime("%m")
    day = current.strftime("%d")
    hour = current.strftime("%H")
    minute = current.strftime("%M")
    sec = current.strftime("%S")

    # print(day)

    print(f"Current date and time: {year}-{month}-{day} {hour}:{minute}:{sec}")

display_current_datetime()


number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date (days):
    current = datetime.datetime.now()
    current_date = current.date()
    future_date = current_date + datetime.timedelta(days=days)
    print(f"Future date: {future_date}")

calculate_future_date(number_of_days)