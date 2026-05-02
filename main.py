from tools import (
    data_tool,
    scoring_tool,
    recommendation_tool,
    product_tool,
    message_tool
)
from agent.orchestrator import AgentOrchestrator


def main():
    print("🚀 Starting Customer Conversion Agent...\n")

    # Initialize agent
    agent = AgentOrchestrator(
        data_tool=data_tool,
        scoring_tool=scoring_tool,
        recommendation_tool=recommendation_tool,
        product_tool=product_tool,
        message_tool=message_tool
    )

    # Input query
    query = "Find high-value customers likely to convert for a personal loan this month and generate personalized WhatsApp messages"

    # Run agent
    results = agent.run(query)

    # Display results
    print("\n================ FINAL OUTPUT ================\n")

    if isinstance(results, str):
        print(results)
        return

    for i, r in enumerate(results, start=1):
        print(f"\n----- Customer {i} -----")
        print("Name:", r["customer"]["name"])
        print("Phone:", r["phone"])
        print("Product:", r["product"])
        print("Message:\n", r["message"])
        print("-----------------------------------")

    print("\n✅ All messages generated successfully!")


if __name__ == "__main__":
    main()