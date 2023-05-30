# Define Evaluation Criteria and Weights
evaluation_criteria = {
    'Productivity': 0.4,
    'Quality of Work': 0.3,
    'Teamwork': 0.2,
    'Communication Skills': 0.1
}

# Gather Performance Data (Sample Data)
employee_data = {
    'John': {
        'Productivity': 85,
        'Quality of Work': 90,
        'Teamwork': 80,
        'Communication Skills': 75
    },
    'Jane': {
        'Productivity': 95,
        'Quality of Work': 80,
        'Teamwork': 90,
        'Communication Skills': 85
    }
}

# Get Employee Name from User
employee_name = input("Enter the name of the employee: ")

# Check if Employee Exists
if employee_name in employee_data:
    # Calculate Performance Score for the Employee
    employee_scores = employee_data[employee_name]
    performance_score = sum(employee_scores[criteria] * weight for criteria, weight in evaluation_criteria.items())

    # Print Detailed Evaluation for Selected Aspects
    print(f"Detailed Evaluation for {employee_name}:")
    for criteria in ['Productivity', 'Quality of Work', 'Teamwork']:
        print(f"{criteria}: {employee_scores[criteria]}")

    # Set Performance Thresholds (Example: 70-80: Average, 80-90: Good, 90+: Excellent)
    performance_thresholds = {
        'Average': (70, 80),
        'Good': (80, 90),
        'Excellent': (90, float('inf'))
    }

    # Determine Performance Rating
    performance_rating = None
    for rating, (lower, upper) in performance_thresholds.items():
        if lower <= performance_score < upper:
            performance_rating = rating
            break

    # Print Employee Performance Rating
    print(f"Performance Rating for {employee_name}: {performance_rating}")
else:
    print("Invalid employee details. Please enter a valid employee name.")
