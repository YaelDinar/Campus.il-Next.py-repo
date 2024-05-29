def gen_secs():
    """
    Generator that yields all seconds in a minute (0-59).
    :yield: int - second
    :rtype: generator
    """
    for sec in range(60):
        yield sec


def gen_minutes():
    """
    Generator that yields all minutes in an hour (0-59).
    :yield: int - minute
    :rtype: generator
    """
    for minute in range(60):
        yield minute

def gen_hours():
    """
    Generator that yields all hours in a day (0-23).
    :yield: int - hour
    :rtype: generator
    """
    for hour in range(24):
        yield hour

def gen_time():
    """
    Generator that yields all possible times in a day in the format HH:MM:SS.
    Uses gen_hours, gen_minutes, and gen_secs generators.
    :yield: str - time in the format "HH:MM:SS"
    :rtype: generator
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)

def gen_years(start=2024):
    """
    Generator that yields years starting from a given year.
    :param start: int - starting year (default is 2024)
    :yield: int - year
    :rtype: generator
    """
    year = start
    while True:
        yield year
        year += 1

def gen_months():
    """
    Generator that yields all months in a year (1-12).
    :yield: int - month
    :rtype: generator
    """
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    """
    Generator that yields all days in a given month.
    Accounts for leap years if the month is February.
    :param month: int - the month number (1-12)
    :param leap_year: bool - whether it's a leap year (default is True)
    :yield: int - day
    :rtype: generator
    """
    #the function is using a dictionary of days of each month. leap year affects the second month only.
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    }
    for day in range(1, days_in_month[month] + 1):
        yield day

def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    :param year: int - the year to check
    :return: bool - True if the year is a leap year, False otherwise
    """
    #it's a leap year if it can be divided by 4 and not by 100 or it can be divided by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def gen_date():
    """
    Generator that yields complete datetime stamps in the format dd/mm/yyyy HH:MM:SS.
    Combines gen_years, gen_months, gen_days, and gen_time generators.
    :yield: str - datetime stamp in the format "dd/mm/yyyy HH:MM:SS"
    :rtype: generator
    """
    for year in gen_years():
        leap_year = is_leap_year(year)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)

def main():
    """
    Main function to test the gen_date generator.
    Prints the datetime stamp every 1,000,000 iterations.
    """
    #create a new genretor and count it iterations
    date_generator = gen_date()
    iteration_count = 0

    #infinate loop that will print the next valid dates after 1000000 iterations
    #get the next date and if it's after 1000000 and it's not the first one iterations print it and add 1 to the iteration count
    while True:
        date = next(date_generator)

        if iteration_count % 1000000 == 0 and iteration_count != 0:
            print(date)

        iteration_count += 1

if __name__ == '__main__':
    main()
