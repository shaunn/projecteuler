# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
#
# Thirty days has September,
#
# April, June and November.
#
# All the rest have thirty-one,
#
# Saving February alone,
#
# Which has twenty-eight, rain or shine.
#
# And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# -----
#
# Strategy
#
# - Remember: The day of the week is always a 7-day cycle, regardless of year or month. Track separately
# - If a century year is not divisible by 400, no leap year. Like 1900
# - Loop through every year, then month, then day starting 01JAN1900 and index every day to 31DEC2000
# - Map the first of each month with an index value
# - Identify the index representing every Sunday
# - Find every Sunday that is also the first of the month
# - Forget patterns, brute force it

# Tuple is (month, day, year, day of week) where day of week of 0 is Sunday
start = (1, 1, 1900)
start_day_of_week = 1
end = (12, 31, 2000)

# Other limits/rules
months_in_year = 12
days_in_week = 7
days_in_month = {1: 31,
                 2: 28,
                 3: 31,
                 4: 30,
                 5: 31,
                 6: 30,
                 7: 31,
                 8: 31,
                 9: 30,
                 10: 31,
                 11: 30,
                 12: 31
                 }

year_to_start_count = 1901


def main():
    day_count = 0
    sunday_on_the_first_of_the_month_count = 0

    total_years = end[2] - start[2]
    day_of_week = start_day_of_week
    print("total_years", total_years)
    for year in range(start[2], end[2] + 1):
        print("===================")
        print("year", year)
        leap_year = check_leap_year(year)

        # I wish there was an alternative range that includes the last element for readability
        for month in range(1, months_in_year + 1):
            print("-------")
            if month == 2 and leap_year:
                days_in_month_adjustment = 1
            else:
                days_in_month_adjustment = 0

            for day_of_month in range(1, days_in_month[month] + 1 + days_in_month_adjustment):
                print("year", year, "month", month, "day", day_of_month, "day_count", day_count, "dow", day_of_week)

                if year > start[2] and day_of_month == 1 and day_of_week == 0:
                    sunday_on_the_first_of_the_month_count += 1

                if day_of_week == 6:
                    day_of_week = 0
                else:
                    day_of_week += 1

                day_count += 1

    print("sunday_on_the_first_of_the_month_count", sunday_on_the_first_of_the_month_count)


def check_leap_year(_year):
    if _year % 4 == 0:
        if _year % 100 != 0:
            return True
    if _year % 400 == 0:
        return True
    return False


if __name__ == "__main__":
    main()
