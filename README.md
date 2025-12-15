Diet Planner Pro – Cost-Optimized Nutrition Planning

APP Preview- 
https://dietoptimizer-njk7hud7yut4d7g5ggjlde.streamlit.app/


🎯 The Problem

Planning a nutritionally balanced diet is harder than it looks—especially when cost is a constraint.

Individuals, students, and working professionals often have specific calorie and macronutrient goals (calories, protein, carbs, fiber), but translating those goals into an affordable, actionable meal plan is non-trivial. Most diet apps focus on tracking or generic recommendations, not on optimizing decisions under constraints.

From an analytics perspective, this is a classic resource allocation problem:
Multiple food choices
Competing nutritional objectives
A fixed budget
Trade-offs between cost, calories, and macronutrients

This problem matters because poor optimization leads to:

Overspending on food
Nutrient imbalance
Inconsistent adherence to health goals

💡 The Solution

Diet Planner Pro is a prescriptive analytics application that computes an optimized daily meal plan tailored to a user’s nutritional targets and budget.
Instead of telling users what they ate, the app answers:
“Given my goals and budget, what should I eat today?”
Prescriptive Analytics Approach
The system models diet planning as an optimization problem:
Decision variables: Quantity of each food item

Objective: Maximize nutritional goal satisfaction while minimizing cost

Constraints:
Budget limit
Calorie target
Macronutrient targets (protein, carbs, fiber)
Practical portion sizes

A greedy heuristic optimization algorithm scores foods based on nutritional efficiency (nutrition per dollar) and iteratively selects optimal portions until constraints are met.

This makes the solution:
Transparent
Fast
Interpretable
Easy to extend into formal linear programming

🚀 Live Demo

👉 Try the app here: (https://dietoptimizer-njk7hud7yut4d7g5ggjlde.streamlit.app/)

Users can input nutrition goals and a daily budget, then instantly generate an optimized meal plan.


⚙️ How It Works

User inputs goals
Daily calories
Protein, carbohydrates, fat, fiber
Daily food budget
System optimizes

Scores foods based on nutritional efficiency per dollar
Iteratively selects food portions that close nutrient gaps
Respects budget and portion constraints
User receives recommendations
Optimized meal plan

Cost breakdown
Nutritional totals vs goals
Visual analytics (charts)
📈 The Analytics Behind It

Data
Nutritional values and costs for common foods (protein, grains, vegetables, dairy, fruits)
Optimization Logic
Greedy heuristic with weighted scoring:
Protein coverage
Calorie coverage
Fiber coverage
Cost penalty


Output

Optimized food selection

Goal completion percentages

Macronutrient distribution

This approach demonstrates prescriptive decision-making, not just descriptive analysis.

📊 Example Output

The app produces:

A tabular meal plan with quantities, costs, and nutrients

Goal completion metrics (e.g., “92% of protein target achieved”)

Visual summaries:

Bar chart for goal completion

Macronutrient calorie distribution

These outputs directly support actionable decisions.

🛠️ Technology Stack

Frontend / App Framework: Streamlit

Optimization Logic: Custom greedy heuristic (prescriptive analytics)

Data Processing: Pandas

Visualization: Streamlit native charts

Language: Python

🎓 About This Project

This project was built as part of ISOM 839 – Prescriptive Analytics
at Suffolk University, with a focus on designing analytics products, not just models.

Author: Sankalp Patel
LinkedIn: (https://www.linkedin.com/in/sankalp-patel98/)
Email: (Sankalp2898@gmail.com)

🔮 Future Possibilities

With more time, this product could evolve into:

Formal linear programming (SciPy / Gurobi)

Weekly meal planning

Dietary filters (vegetarian, halal, allergies)

Dynamic pricing by location

Grocery list optimization

Integration with fitness trackers

From a business perspective, this could support:

Health & wellness platforms

Student meal planning

Corporate wellness programs

Budget-conscious consumers



The value of this project is not the code alone—it’s the ability to identify a real decision problem and design an intelligent solution.
