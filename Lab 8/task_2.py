def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Test suite
def test_assign_grade():
    assert assign_grade(95) == 'A'
    assert assign_grade(85) == 'B'
    assert assign_grade(75) == 'C'
    assert assign_grade(65) == 'D'
    assert assign_grade(55) == 'F'
    assert assign_grade(90) == 'A'
    assert assign_grade(80) == 'B'
    assert assign_grade(70) == 'C'
    assert assign_grade(60) == 'D'
    print("All tests passed.")

if __name__ == "__main__":
    score = int(input("Enter the score: "))
    grade = assign_grade(score)
    print(f"Grade: {grade}")