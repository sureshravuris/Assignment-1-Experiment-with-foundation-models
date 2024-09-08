# Code Simplification

# Old Version: A complex function with multiple nested loops and conditions

def process_student_grades(students):
    results = []
    for student in students:
        total_score = 0
        weighted_score = 0
        for subject in student['subjects']:
            if subject['type'] == 'major':
                for assignment in subject['assignments']:
                    if assignment['type'] == 'exam':
                        score = assignment['score']
                        if score > 90:
                            total_score += score * 1.1
                        elif score > 80:
                            total_score += score * 1.05
                        else:
                            total_score += score
                    elif assignment['type'] == 'project':
                        total_score += assignment['score'] * 1.2
                    else:
                        total_score += assignment['score']
                weighted_score += total_score * 0.6
            else:
                for assignment in subject['assignments']:
                    total_score += assignment['score']
                weighted_score += total_score * 0.4
        final_grade = weighted_score / len(student['subjects'])
        if final_grade >= 90:
            letter_grade = 'A'
        elif final_grade >= 80:
            letter_grade = 'B'
        elif final_grade >= 70:
            letter_grade = 'C'
        elif final_grade >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        results.append({
            'name': student['name'],
            'final_grade': final_grade,
            'letter_grade': letter_grade
        })
    return results

# New Version: Simplified function broken into smaller, reusable functions

def calculate_assignment_score(assignment):
    score = assignment['score']
    if assignment['type'] == 'exam':
        if score > 90:
            return score * 1.1
        elif score > 80:
            return score * 1.05
        return score
    elif assignment['type'] == 'project':
        return score * 1.2
    return score

def calculate_subject_score(subject):
    return sum(calculate_assignment_score(assignment) for assignment in subject['assignments'])

def calculate_weighted_score(subjects):
    major_score = sum(calculate_subject_score(subject) for subject in subjects if subject['type'] == 'major')
    minor_score = sum(calculate_subject_score(subject) for subject in subjects if subject['type'] != 'major')
    return (major_score * 0.6) + (minor_score * 0.4)

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    return 'F'

def process_student_grades_simplified(students):
    results = []
    for student in students:
        weighted_score = calculate_weighted_score(student['subjects'])
        final_grade = weighted_score / len(student['subjects'])
        results.append({
            'name': student['name'],
            'final_grade': final_grade,
            'letter_grade': get_letter_grade(final_grade)
        })
    return results

# Example usage
students = [
    {
        'name': 'Alice',
        'subjects': [
            {
                'type': 'major',
                'assignments': [
                    {'type': 'exam', 'score': 85},
                    {'type': 'project', 'score': 92},
                    {'type': 'homework', 'score': 88}
                ]
            },
            {
                'type': 'minor',
                'assignments': [
                    {'type': 'exam', 'score': 78},
                    {'type': 'project', 'score': 85}
                ]
            }
        ]
    }
]

print("Old Version Results:")
print(process_student_grades(students))

print("\nNew Version Results:")
print(process_student_grades_simplified(students))