import datetime
# adding date

def add_expense(cat, date, money)
    try:
        date.datetime.striptime(date, '%Y-%m-%d' )
    except ValueError:
        print("Please try again with the format of YYYY-MM-DD")
        return



    