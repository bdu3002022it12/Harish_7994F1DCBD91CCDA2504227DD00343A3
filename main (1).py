def is_leap_year(year):
  """Checks if a year is a leap year.

  Args:
    year: The year to check.

  Returns:
    True if the year is a leap year, False otherwise.
  """

  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False


# Example usage:

year = 2024

if is_leap_year(year):
  print("The year {} is a leap year.".format(year))
else:
  print("The year {} is not a  leap year .". format (year))