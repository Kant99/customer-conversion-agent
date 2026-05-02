def calculate_conversion_score(customer):
    score = 0
    reasons = []

    # Income
    if customer["income"] > 80000:
        score += 2
        reasons.append("High income")
    elif customer["income"] > 50000:
        score += 1
        reasons.append("Moderate income")

    # Credit Score
    if customer["credit_score"] > 750:
        score += 2
        reasons.append("Excellent credit score")
    elif customer["credit_score"] > 700:
        score += 1
        reasons.append("Good credit score")

    # Account Balance
    if customer["account_balance"] > 200000:
        score += 2
        reasons.append("Strong account balance")

    # Activity
    if customer["monthly_transactions"] > 25:
        score += 1
        reasons.append("Highly active account")

    # Loan History
    if not customer["loan_history"]:
        score += 1
        reasons.append("No existing loan (higher likelihood to take new loan)")

    return score, reasons

def classify_conversion(score):
    if score >= 6:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"

def evaluate_customers(customers):
    evaluated = []

    for customer in customers:
        score, reasons = calculate_conversion_score(customer)
        category = classify_conversion(score)

        evaluated.append({
            "customer": customer,
            "score": score,
            "category": category,
            "reasons": reasons
        })

    return evaluated

def get_top_customers(customers, top_n=1):
    evaluated = evaluate_customers(customers)

    # Sort by score (descending)
    sorted_customers = sorted(
        evaluated,
        key=lambda x: x["score"],
        reverse=True
    )

    return sorted_customers[:top_n]    