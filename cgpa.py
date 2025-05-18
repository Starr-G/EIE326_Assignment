def grade_point(grade):
    grade = grade.upper()
    if grade == 'A':
        return 5.0
    elif grade == 'B':
        return 4.0
    elif grade == 'C':
        return 3.0
    elif grade == 'D':
        return 2.0
    elif grade == 'F':
        return 0.0
    else:
        return -1.0

def main():
    try:
        n = int(input("How many courses do you want to enter? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    grades = []
    credits = []

    for i in range(n):
        grade = input(f"Enter grade for course {i + 1} (A-F): ").strip()
        if grade_point(grade) < 0:
            print(f"Oops! '{grade}' is not a valid grade. Try again.")
            return

        try:
            credit = int(input(f"Enter credit hours for course {i + 1}: "))
            if credit <= 0:
                print("Credit hours should be a positive integer.")
                return
        except ValueError:
            print("Please enter a valid number for credit hours.")
            return

        grades.append(grade)
        credits.append(credit)

    total_points = 0
    total_credits = 0

    for i in range(len(grades)):
        point = grade_point(grades[i])
        total_points += point * credits[i]
        total_credits += credits[i]

    cgpa = total_points / total_credits
    print(f"\nYour CGPA is: {cgpa:.2f}")

if __name__ == "__main__":
    main()
