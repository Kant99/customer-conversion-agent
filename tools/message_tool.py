import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-3-flash-preview")


def generate_message(customer, recommendation, score, reasons):
    """
    Generate personalized WhatsApp message using LLM
    """

    prompt = f"""
    You are a banking assistant helping a Relationship Manager.

    Generate a personalized WhatsApp message for the following customer:

    Customer Name: {customer['name']}
    Income: {customer['income']}
    Credit Score: {customer['credit_score']}
    Account Balance: {customer['account_balance']}

    Conversion Score: {score}
    Key Reasons: {', '.join(reasons)}

    Recommended Product: {recommendation['product']}
    Recommendation Reason: {recommendation['reason']}

    Instructions:
    - Keep message concise (3-4 lines)
    - Professional but friendly tone
    - Personalized using customer context
    - Mention benefit of product
    - End with a soft call-to-action

    Output only the message.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating message: {str(e)}"


def generate_messages_for_customers(customers):
    """
    Generate messages for multiple customers
    """

    results = []

    for entry in customers:
        customer = entry["customer"]
        recommendation = entry["recommendation"]
        score = entry["score"]
        reasons = entry["reasons"]

        if recommendation["product"] is None:
            continue

        message = generate_message(
            customer,
            recommendation,
            score,
            reasons
        )

        results.append({
            "customer": customer,
            "phone": customer["phone"],
            "product": recommendation["product"],
            "message": message
        })

    return results