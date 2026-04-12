
def largest_of_3(nums=None,display=True):
    """Returns the largest of a list of three numbers input either as 
    arg or via input prompt."""
    if nums == None:
        a = float(input("Enter first number..."))
        b = float(input("Enter second number..."))
        c = float(input("Enter third number..."))
    else:
        a, b, c = nums
    biggest = max(a, b, c)
    if display:
        print("The largest number is: ", biggest)
    return biggest


def para_parallelogram(width=8, height=5, display=True):
    """Print a parallelogram with the given width and height.
    Height includes top and bottom lines."""
    end_line = "-" * width
    mid_line = "/" + " " * (width - 2) + "/"

    for i in range(height): 
        if i == 0:
            print(" " * (height - 1 - i) + end_line)
        elif i == height - 1:
            print(end_line)
        else:
            print(" " * (height - 1 - i) + mid_line)


def pay_calc(day_type=None, hours=None, display=True):
    """Calculate pay for one day based on given hours and day type. 
    Pay rates hardcoded to $15 base and $21 OT or weekend."""
    if day_type == None:
        day_type = str(input("Input day type (weekday/weekend)..."))
        while day_type not in ("weekday", "weekend"):
            day_type = input("Invalid day type. Enter \"weekday\" or \"weekend\": ")
    if hours == None:
        hours = float(input("Enter number of hours..."))

    if day_type == "weekday":
        # 15 for all hours plus additional 6 for OT hours
        pay = hours * 15 + max(0, hours - 8) * 6 
        if display:
            print(f"Pay for given day: {pay:.2f}")
        return pay
    else:
        pay = hours * 21
        if display:
            print(f"Pay for given day: {pay:.2f}")
        return pay
    
def income_tax(income=None, year=2026, display=True):
    if income == None:
        income = float(input("Enter total annual income..."))
    while year != 2026:
        year = int(input("Please enter the year 2026...")) # lol
    tax = 0
    brackets = [
        (58523, 0.14),
        (117045, 0.205),
        (181440, 0.26),
        (258482, 0.29),
        (float('inf'), 0.33) # just in case!
    ]

    prev = 0
    for limit, rate in brackets:
        if income <= prev:
            break
        taxable = min(income, limit) - prev
        tax += taxable * rate
        prev = limit
    if display:
        print(f"Total federal income tax: ${tax:.2f}")
    return tax


def perc_to_GPA(perc=None, display=True):
    """Convert a percentage grade to GPA using U of C standard. Returns GPA only."""
    if perc == None:
        perc = float(input("Enter your percentage grade: "))

    if perc >= 90:
        letter, gpa = "A+", 4.0
    elif perc >= 85:
        letter, gpa = "A", 4.0
    elif perc >= 80:
        letter, gpa = "A-", 3.7
    elif perc >= 77:
        letter, gpa = "B+", 3.3
    elif perc >= 73:
        letter, gpa = "B", 3.0
    elif perc >= 70:
        letter, gpa = "B-", 2.7
    elif perc >= 67:
        letter, gpa = "C+", 2.3
    elif perc >= 63:
        letter, gpa = "C", 2.0
    elif perc >= 60:
        letter, gpa = "C-", 1.7
    elif perc >= 55:
        letter, gpa = "D+", 1.3
    elif perc >= 50:
        letter, gpa = "D", 1.0
    else:
        letter, gpa = "F", 0.0

    if display:
        print(f"Percentage: {perc}% | Letter Grade: {letter} | GPA: {gpa}")
    return gpa