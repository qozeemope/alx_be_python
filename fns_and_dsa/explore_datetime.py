from datetime import datetime, timedelta

def display_current_datetime () :
    current = datetime.now()
    # current_date = current.datetime()

    # year = current.strftime("%Y")
    # month = current.strftime("%m")
    # day = current.strftime("%d")
    # hour = current.strftime("%H")
    # minute = current.strftime("%M")
    # sec = current.strftime("%S")

    # print(day)



    print(f"Current date and time: {current.strftime('%Y-%m-%d %H:%M:%S')}")


display_current_datetime()


number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date (days):
    current = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_date = current.date()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")

calculate_future_date(number_of_days)