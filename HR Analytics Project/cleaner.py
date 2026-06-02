import math
from datetime import datetime
from helper import read_hr_data


def remove_null_salaries(data):
    """
    Remove all records where Salary (index 4) is NaN or missing.
    
    Returns the list without the removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """

    # create an empty list to store cleaned data
    data_clean = []

    # loop through each employee record
    for employee in data:

        # get salary from column 4
        salary = employee[4]

        # keep only records with valid salary values
        if math.isnan(salary) == False:
            data_clean.append(employee)

    return data_clean

def standardize_departments(data):
    """
    Convert all Department names (index 1) to lowercase.
    
    Modifies the data list in place. Returns nothing.
    
    Args:
        data (list): 2D list of employee records
    """
    for employee in data:

        # get department and convert to lower case
        department = employee[1].lower()

        # update the original values
        employee[1] = department
    pass    


def remove_invalid_performance_ratings(data):
    """
    Remove records with Performance_Rating (index 6) outside range [0, 5].
    
    Returns the list without the removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """
    # create a new empty list to store updated records
    data_clean = []

    # loop through each employee
    for employee in data:

        # get performance rating 
        rating = employee[6]

        # check if rating is valid
        if 0 <= rating <= 5:
            data_clean.append(employee)
    return data_clean
    


def fix_format_dates(data):
    """
    Fix the formatting of hire dates that are not in YYYY-MM-DD format.
    
    Some dates may be in DD/MM/YYYY format; convert these to YYYY-MM-DD.
    Expected format: YYYY-MM-DD
    
    Modifies the data list in place. Returns nothing.
    
    Args:
        data (list): 2D list of employee records
    """
    # loop through each employee record
    for employee in data:

        # get the date, remove any whitespace 
        date = employee[9].strip()

        if "/" in date:
            # split the date using "/" to create a list
            split_date = date.split("/")

            day = split_date[0]
            month = split_date[1]
            year = split_date[2]

            # create date with new format
            new_date = year + "-" + month + "-" + day

            # replace old date with new date
            employee[9] = new_date
        else:
            # for date that is already in correct format
            employee[9] = date
    pass


def remove_invalid_dates(data):
    """
    Remove records with invalid hire dates.
    
    Removes entries where:
    - The year is before 2015 (company was founded in 2015)
    - The year is after 2025 (future dates beyond company scope)
    - The date is logically invalid:
      - Days less than 1 or greater than 30
      - For February: check leap year (29 days in leap years, 28 otherwise)
      - Months less than 1 or greater than 12
    
    Returns the list without the removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """
    # create a new empty list to store updated records
    cleaned_data = []

    for employee in data:
        # get the date, remove any whitespace 
        date = employee[9].strip()

        # split the date using "/" to create a list
        split_date = date.split("-")

        # assign date elements to variables
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])

        # check if year is outside range
        if year < 2015 or year>2025:
            continue

        # check if month is outside range
        if month < 1 or month > 12:
            continue

        # check if year is leap year using Feb
        if month == 2:

            # correct leap year check
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

            if is_leap:
                if day < 1 or day > 29:
                    continue
            else:
                if day < 1 or day > 28:
                    continue

        else:
            # check if days are valid for other months
            if day < 1 or day > 30:
                continue

        # add dates that meet our criteria to empty list
        cleaned_data.append(employee)

    return cleaned_data
    pass

if __name__ == "__main__":
    # Load uncleaned data from CSV file
    data = read_hr_data('uncleaned_dataset.csv')
    print(f"Loaded {len(data)} employee records\n")
    
    print("=" * 70)
    print("DATA CLEANING")
    print("=" * 70)
    
    # Test data cleaning functions
    # Uncomment the lines below to test each cleaning function
    # You can modify the function arguments to test different inputs
    
    # 1. Remove null salaries
    # removed_salaries = remove_null_salaries(data)
    # print(f"Removed {len(removed_salaries)} records with null salaries")
    # print(f"Remaining records: {len(data)}\n")
    
    # 2. Standardize departments
    # standardize_departments(data)
    # print("Standardized department names to lowercase\n")
    
    # 3. Remove invalid performance ratings
    # removed_ratings = remove_invalid_performance_ratings(data)
    # print(f"Removed {len(removed_ratings)} records with invalid performance ratings")
    # print(f"Remaining records: {len(data)}\n")
    
    # 4. Fix hire date formatting
    # fix_format_dates(data)
    # print("Fixed hire date formatting\n")
    
    # 5. Remove invalid dates
    # removed_dates = remove_invalid_dates(data)
    # print(f"Removed {len(removed_dates)} records with invalid dates")
    # print(f"Remaining records: {len(data)}\n")
