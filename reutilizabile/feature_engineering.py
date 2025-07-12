
from reutilizabile.common_imports import *

def salary_interval(row):
    salary = row['Salary Range']
    separator = "K"
    min_salary = salary[1:].split(separator)[0]
    max_salary = salary.split(separator)[1]
    max_salary = max_salary[2:].split(separator)[0]

    min_salary = int(min_salary)*1000*4.3
    max_salary = int(max_salary)*1000*4.3 #to make it ron
    average_salary = int((min_salary+max_salary)/2)
    return min_salary, max_salary, average_salary

def tercile_label(s,low_33,high_67):
    if s <= low_33:
        return 'Low'
    elif s <= high_67:
        return 'Medium'
    else:
        return 'High'

def parse_benefits_string(benefits_str):
    # Remove outer curly braces and single quotes
    cleaned_str = benefits_str.strip("{}'").replace("'", "")
    # Split by comma and strip whitespace from each benefit
    return [benefit.strip() for benefit in cleaned_str.split(',')]

def applybenefits(benefits_str):
    benefits = parse_benefits_string(benefits_str)

def parse_experience(exp):
    years = exp.replace("Years", "").strip().split("to")
    return int((int(years[0]) + int(years[1])) / 2)

def company_aggregation(c,low_33,high_67):
    if c <= low_33:
        return 'Small'
    elif c <= high_67:
        return 'Medium'
    else:
        return 'Large'
