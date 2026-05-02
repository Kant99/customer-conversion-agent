class AgentOrchestrator:
    def __init__(
        self,
        data_tool,
        scoring_tool,
        recommendation_tool,
        product_tool,
        message_tool
    ):
        self.data_tool = data_tool
        self.scoring_tool = scoring_tool
        self.recommendation_tool = recommendation_tool
        self.product_tool = product_tool
        self.message_tool = message_tool

    def run(self, query):
        print("\n[Agent] Understanding user request...")

        # Step 1: Basic intent check
        if "loan" not in query.lower():
            return "Unsupported query"

        print("[Agent] Identified task: Personal Loan Targeting")

        # Step 2: Fetch customer data
        print("[Agent] Fetching customer data...")
        customers = self.data_tool.fetch_customers()

        # Step 3: Evaluate customers (scoring)
        print("[Agent] Evaluating customers (scoring)...")
        evaluated_customers = self.scoring_tool.evaluate_customers(customers)

        # Step 4: Fetch product configurations
        print("[Agent] Fetching product configurations...")
        products = self.product_tool.fetch_products()

        # Step 5: Generate recommendations
        print("[Agent] Generating product recommendations...")
        recommendations = self.recommendation_tool.generate_recommendations(
            evaluated_customers,
            products
        )

        # Step 6: Rank customers
        print("[Agent] Ranking customers...")
        ranked = sorted(
            recommendations,
            key=lambda x: x["score"],
            reverse=True
        )

        # Step 7: Select top customers
        final_targets = ranked[:2]

        print(f"[Agent] Selected {len(final_targets)} customers for outreach")

        # Step 8: Generate personalized messages
        print("[Agent] Generating personalized WhatsApp messages...")
        messages = self.message_tool.generate_messages_for_customers(final_targets)

        print("[Agent] Process completed successfully")

        return messages