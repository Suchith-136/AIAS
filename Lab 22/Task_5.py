"""
Loan Approval System

This script simulates a simple loan approval system. The decision process is rule-based and fully explainable to users.
"""

def explain_decision(applicant, approved, reasons):
    print("\nLoan Approval Result")
    print("--------------------")
    print(f"Applicant Name: {applicant.get('name', 'N/A')}")
    print(f"Requested Amount: ${applicant.get('amount', 0):,.2f}")
    print(f"Annual Income: ${applicant.get('income', 0):,.2f}")
    print(f"Credit Score: {applicant.get('credit_score', 'N/A')}")
    print(f"Employment Years: {applicant.get('employment_years', 'N/A')}")
    print()
    if approved:
        print("Decision: APPROVED")
        print("Reason(s):")
        for r in reasons:
            print(" -", r)
    else:
        print("Decision: NOT APPROVED")
        print("Reason(s) for denial:")
        for r in reasons:
            print(" -", r)
    print("--------------------\n")
    print("This decision is based on simple threshold rules and can be adjusted for more sophistication.")


def approve_loan(applicant):
    """
    Determines whether an applicant qualifies for a loan.

    Args:
        applicant (dict): Information about the applicant.

    Returns:
        (bool, list): Tuple of approval result and explanation reasons.
    """
    reasons = []
    approved = True

    # Criteria thresholds
    min_income = 25000
    min_credit_score = 650
    max_debt_to_income = 0.4
    min_employment_years = 2

    # Extract applicant data (simple field names)
    income = applicant.get("income", 0)
    credit_score = applicant.get("credit_score", 0)
    employment_years = applicant.get("employment_years", 0)
    current_debt = applicant.get("current_debt", 0)
    loan_amount = applicant.get("amount", 0)

    # Decision rules
    # 1. Minimum income
    if income < min_income:
        reasons.append(f"Annual income (${income:,.2f}) is below the minimum required (${min_income:,.2f}).")
        approved = False
    else:
        reasons.append(f"Income meets or exceeds minimum requirement (${min_income:,.2f}).")

    # 2. Credit Score
    if credit_score < min_credit_score:
        reasons.append(f"Credit score ({credit_score}) is below the minimum required ({min_credit_score}).")
        approved = False
    else:
        reasons.append(f"Credit score meets or exceeds minimum ({min_credit_score}).")

    # 3. Employment History
    if employment_years < min_employment_years:
        reasons.append(f"Employment history ({employment_years} years) is less than required ({min_employment_years} years).")
        approved = False
    else:
        reasons.append(f"Employment years meet or exceed minimum ({min_employment_years}).")

    # 4. Debt-to-Income Ratio
    total_debt = current_debt + loan_amount
    dti = total_debt / income if income > 0 else 1
    if dti > max_debt_to_income:
        reasons.append(f"Debt-to-income ratio ({dti:.2%}) exceeds maximum allowed ({max_debt_to_income:.0%}).")
        approved = False
    else:
        reasons.append(f"Debt-to-income ratio ({dti:.2%}) is within acceptable range ({max_debt_to_income:.0%}).")

    return approved, reasons

if __name__ == "__main__":
    # Simple CLI for user input
    print("=== Loan Approval System ===\n")
    name = input("Applicant name: ").strip()
    try:
        amount = float(input("Loan amount requested ($): "))
        income = float(input("Annual income ($): "))
        credit_score = int(input("Credit score (300-850): "))
        employment_years = int(input("Years at current job: "))
        current_debt = float(input("Current total debt ($): "))
    except Exception as e:
        print("Invalid input. Please enter numeric values where required.")
        exit(1)

    applicant = {
        "name": name,
        "amount": amount,
        "income": income,
        "credit_score": credit_score,
        "employment_years": employment_years,
        "current_debt": current_debt
    }

    is_approved, explanation = approve_loan(applicant)
    explain_decision(applicant, is_approved, explanation)
    print("The decision process is rule-based and explainable: each criterion is assessed and the decision reasons are given to the user.")

