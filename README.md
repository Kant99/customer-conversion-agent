# 🧠 Agentic AI System for Banking CRM

## 🎯 Objective

This project implements an **Agentic AI system** to assist Relationship Managers (RM) in identifying high-value customers likely to convert for a personal loan and generating personalized WhatsApp outreach messages.

---

## 🏦 Use Case

A Relationship Manager asks:

> “Find high-value customers likely to convert for a personal loan this month and generate personalized WhatsApp messages.”

---

## 🧩 System Architecture

```
User Query
   ↓
Agent Orchestrator
   ↓
-----------------------------------------
| Data Tool → Fetch customer data       |
| Scoring Tool → Evaluate customers     |
| Product Tool → Load product configs   |
| Recommendation Tool → Match products  |
| Message Tool → Generate messages (LLM)|
-----------------------------------------
   ↓
Final Output (Top Customers + Messages)
```

---

## ⚙️ Execution Flow

1. **Query Understanding**

   * Agent interprets intent (personal loan targeting)

2. **Data Retrieval**

   * Fetch customer data from JSON (simulating CRM)

3. **Customer Evaluation**

   * Apply heuristic-based scoring using:

     * Income
     * Credit score
     * Account balance
     * Transaction activity
     * Loan history

4. **Product Recommendation**

   * Match customers with products using configuration (`products.json`)

5. **Ranking & Filtering**

   * Sort customers based on conversion score
   * Select top high-potential customers

6. **Message Generation**

   * Use LLM (Gemini) to generate personalized WhatsApp messages

---

## 🧠 Agentic Design

This system follows an **agentic architecture** where:

* The **Agent Orchestrator** controls the workflow
* Each capability is encapsulated as a **tool**
* The system performs:

  * Task decomposition
  * Step-by-step reasoning
  * Tool invocation
  * Context propagation

---

## 🛠️ Tech Stack

* **Python**
* **Google Gemini API** (LLM)
* **JSON** (data storage)
* **python-dotenv** (environment management)

---

## 📁 Project Structure

```
customer-conversion-agent/
│
├── agent/
│   └── orchestrator.py
│
├── tools/
│   ├── data_tool.py
│   ├── scoring_tool.py
│   ├── product_tool.py
│   ├── recommendation_tool.py
│   └── message_tool.py
│
├── data/
│   ├── customers.json
│   └── products.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔍 Key Design Decisions

### 1. Heuristic-Based Scoring

* Used rule-based scoring instead of ML for:

  * Simplicity
  * Explainability
  * Faster implementation

---

### 2. Data-Driven Product Configuration

* Products are stored in `products.json`
* Enables:

  * Easy updates
  * Extensibility
  * Separation of logic and data

---

### 3. Selective LLM Usage

* LLM used **only for message generation**
* Core decision logic remains deterministic

---

### 4. Modular Tool-Based Architecture

* Each component is independent
* Improves:

  * Maintainability
  * Reusability
  * Testing

---

## ⚖️ Trade-offs & Limitations

* No real-time database (used JSON for simplicity)
* Heuristic scoring instead of ML model
* Basic intent parsing (rule-based)
* Limited to personal loan use case (extensible)

---

## 🚀 Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd customer-conversion-agent
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
python main.py
```

---

## 📦 Sample Output

```
Name: Rahul Sharma
Phone: +919812340001
Product: Premium Personal Loan

Message:
Hi Rahul, based on your strong financial profile, we have a tailored personal loan offer that could suit your needs. Let us know a convenient time to discuss further!
```

---

## 🚀 Future Enhancements

* Add ML-based conversion prediction
* Support multiple product types (credit cards, home loans)
* Integrate with real database / CRM
* Add UI dashboard (Streamlit / React)
* Multi-channel communication (Email, SMS)

---

## 🎥 Demo

A demo video is included showing:

* System walkthrough
* End-to-end execution
* Design explanation

---

## ✅ Conclusion

This project demonstrates a **practical implementation of an Agentic AI system** combining:

* Structured reasoning
* Modular tool usage
* LLM-powered personalization
