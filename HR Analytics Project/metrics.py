import math
from datetime import datetime
from helper import read_hr_data


def get_unique_departments(data):
    """
    Return a set of all unique department names in the dataset.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        set: Set of department names
        
    Example:
        >>> get_unique_departments(data)
        {'engineering', 'sales', 'hr', 'marketing', 'product'}
    """
    # create an empty set
    departments = set()

    # go through each employee record
    for row in data:
        # get department and add it on the empty set
        dept = row[1]
        departments.add(dept)

    # return the new set with unique department names
    return departments
    pass


def get_gender_distribution(data):
    """
    Return gender distribution (as percentages) for each department.
    
    All percentages should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is a dictionary
              of gender percentages
        
    Example:
        >>> get_gender_distribution(data)
        {
            'engineering': {'Male': 45.5, 'Female': 35.2, 'Non-binary': 19.3},
            'sales': {'Male': 40.0, 'Female': 50.0, 'Non-binary': 10.0},
            ...
        }
    """
    # create an empty dictionary to store what is counted
    dept_gender = {}

    # count the number of employees by gender in each department
    for row in data:
        # get gender and department
        dept = row[1]
        gender = row[2]

        # create department for departments that are not yet in dictionary
        if dept not in dept_gender:
            dept_gender[dept] = {}

        # if gender not yet in department, initialize count
        if gender not in dept_gender[dept]:
            dept_gender[dept][gender] = 0

        # increase count for gender
        dept_gender[dept][gender] += 1

    result = {}

    # convert counts to percentages
    for dept in dept_gender:
        result[dept] = {}

        # calculate total employees in the department
        total = 0

        for gender in dept_gender[dept]:
            total += dept_gender[dept][gender]

        # calculate the percentage for each gender
        for gender in dept_gender[dept]:
            count = dept_gender[dept][gender]

            # calculate percentage
            percentage = (count / total) * 100

            # round off to two decimals
            result[dept][gender] = round(percentage, 2)

    return result
    
            


def get_avg_age_by_department(data):
    """
    Return average age for each department.
    
    All averages should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the average age
        
    Example:
        >>> get_avg_age_by_department(data)
        {'engineering': 38.5, 'sales': 35.2, 'hr': 42.1, 'marketing': 33.8, 'product': 36.9}
    """
    # create a dictionary to store ages by department
    dept_ages = {}

    # collect all ages
    for row in data:
        dept = row[1]
        age = row[3]

        # create a list if department is not seen before
        if dept not in dept_ages:
            dept_ages[dept] = []

        # add the age to the department list
        dept_ages[dept].append(age)

    # create a dictionary for results
    result = {}

    # calculate the average for each department
    for dept in dept_ages:
        ages = dept_ages[dept]

        # average
        avg = sum(ages) / len(ages)

        # round the result
        result[dept] = round(avg, 2)

    return result
    pass
    


def get_retention_rate(data):
    """
    Calculate overall retention rate as a percentage.
    
    Formula: (Active Employees / Total Employees) × 100
    
    Status column (index 8) contains 'Active' or 'Resigned'
    
    Result should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        float: Retention rate as a percentage (0-100)
        
    Example:
        >>> get_retention_rate(data)
        87.5
    """
     # set a counter for active employees
    active = 0

    # calculate total employees
    total = len(data)

    # loop through each employee record in dataset
    for row in data:
        status = row[8].strip()

        # check if employee is active
        if status == "Active":
            active += 1

    # calculate employee retention
    retention = (active / total) * 100

    # return the result rounded off to two decimals
    return round(retention, 2)
    pass


def get_turnover_rate_by_department(data):
    """
    Calculate turnover rate for each department as a percentage.
    
    Formula (per department): (Resigned Employees in Department / Total Employees in Department) × 100
    
    All rates should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the turnover rate
        
    Example:
        >>> get_turnover_rate_by_department(data)
        {'engineering': 15.5, 'sales': 22.3, 'hr': 10.0, 'marketing': 18.5, 'product': 12.0}
    """
    # create dictionaries to track totals and resigned counts
    dept_total = {}
    dept_resigned = {}

    # count employees per department
    for row in data:
        dept = row[1]
        status = row[8].strip()

        # initialize department if needed
        if dept not in dept_total:
            dept_total[dept] = 0
            dept_resigned[dept] = 0

        # count total employees
        dept_total[dept] += 1

        # count resigned employees
        if status == "Resigned":
            dept_resigned[dept] += 1

    # calculate turnover rate
    result = {}

    for dept in dept_total:
        total = dept_total[dept]
        resigned = dept_resigned[dept]

        turnover = (resigned / total) * 100

        # Step 7: round result
        result[dept] = round(turnover, 2)

    return result


def get_avg_salary_by_age_range(data, min_age, max_age):
    """
    Return average salary for employees within an age range (inclusive).
    
    Result should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        min_age (int): Minimum age (inclusive)
        max_age (int): Maximum age (inclusive)
        
    Returns:
        float: Average salary for employees in the age range
        
    Example:
        >>> get_avg_salary_by_age_range(data, 25, 35)
        68500.75
    """
    
    total_salary = 0
    count = 0

    # iterate through employees
    for row in data:
        age = row[3]
        salary = row[4]

        # check if age is in range
        if min_age <= age <= max_age:
            total_salary += salary
            count += 1

    # when no employee match retun 0.0
    if count == 0:
        return 0.0

    # calculate average
    avg = total_salary / count

    return round(avg, 2)
   

def get_avg_dept_performance_by_training_range(data, min_hours, max_hours):
    """
    Return average performance rating for each department within a training hours range (inclusive).
    
    Calculates the average performance rating for employees within the specified training hours range,
    grouped by department.
    
    All ratings should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        min_hours (int): Minimum training hours (inclusive)
        max_hours (int): Maximum training hours (inclusive)
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the average performance rating
              for employees in that department within the training hours range
        
    Example:
        >>> get_avg_dept_performance_by_training_range(data, 20, 40)
        {
            'engineering': 4.2,
            'sales': 3.9,
            'hr': 4.0,
            'marketing': 3.6,
            'product': 4.3
        }
    """
    # create a dictionary to store ratings per department
    dept_perf = {}

    # collect ratings
    for row in data:
        dept = row[1]
        hours = row[5]
        rating = row[6]

        # check if training hours are in range
        if min_hours <= hours <= max_hours:

            # initialize department 
            if dept not in dept_perf:
                dept_perf[dept] = []

            # add rating
            dept_perf[dept].append(rating)

    # calculate average
    result = {}

    for dept in dept_perf:
        ratings = dept_perf[dept]

        # handle empty case
        if len(ratings) == 0:
            result[dept] = 0.0
        else:
            avg = sum(ratings) / len(ratings)
            result[dept] = round(avg, 2)

    return result
    pass


if __name__ == "__main__":
    # Load cleaned data from CSV file
    data = read_hr_data('cleaned_dataset.csv')
    print(f"Loaded {len(data)} employee records\n")
    
    print("=" * 70)
    print("METRICS CALCULATION")
    print("=" * 70)
    
    # Test metrics functions
    # Uncomment the lines below to test each metrics function
    # You can modify the function arguments to test different inputs
    
    # 1. Get unique departments
    # depts = get_unique_departments(data)
    # print(f"\nUnique departments: {depts}")
    
    # 2. Get gender distribution per department
    # gender_dist = get_gender_distribution(data)
    # print(f"\nGender distribution by department:")
    # for dept, dist in gender_dist.items():
    #     print(f"  {dept}: {dist}")
    
    # 3. Get average age per department
    # avg_age = get_avg_age_by_department(data)
    # print(f"\nAverage age by department:")
    # for dept, age in avg_age.items():
    #     print(f"  {dept}: {age}")
    
    # 4. Get retention rate
    # retention = get_retention_rate(data)
    # print(f"\nOverall retention rate: {retention}%")
    
    # 5. Get turnover rate per department
    # turnover = get_turnover_rate_by_department(data)
    # print(f"\nTurnover rate by department:")
    # for dept, rate in turnover.items():
    #     print(f"  {dept}: {rate}%")
    
    # 6. Get average salary for age range
    # avg_sal_age = get_avg_salary_by_age_range(data, 25, 35)
    # print(f"\nAverage salary for employees aged 25-35: ${avg_sal_age}")
    
    # 7. Get average department performance by training hours range
    # avg_perf_training = get_avg_dept_performance_by_training_range(data, 20, 40)
    # print(f"\nAverage performance rating by department for employees with 20-40 training hours:")
    # for dept, rating in avg_perf_training.items():
    #     print(f"  {dept}: {rating}")
