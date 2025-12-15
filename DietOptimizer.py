import streamlit as st
import pandas as pd
import math
from datetime import date

st.set_page_config(page_title="Diet Planner Pro", page_icon="🍽️", layout="wide")


# -----------------------------
# Food database (same as your JS)
# NOTE: costs are per given unit
# -----------------------------
FOODS = [
    # Poultry & Meat
    {"name": "Chicken Breast", "calories": 165, "protein": 31, "carbs": 0, "fat": 3.6, "fiber": 0, "cost": 3.99, "unit": "100g", "category": "Poultry"},
    {"name": "Chicken Thigh", "calories": 209, "protein": 26, "carbs": 0, "fat": 10.9, "fiber": 0, "cost": 3.49, "unit": "100g", "category": "Poultry"},
    {"name": "Ground Beef (lean)", "calories": 250, "protein": 26, "carbs": 0, "fat": 15, "fiber": 0, "cost": 4.99, "unit": "100g", "category": "Meat"},
    {"name": "Beef Steak", "calories": 271, "protein": 25, "carbs": 0, "fat": 19, "fiber": 0, "cost": 6.99, "unit": "100g", "category": "Meat"},
    {"name": "Pork Loin", "calories": 242, "protein": 27, "carbs": 0, "fat": 14, "fiber": 0, "cost": 4.49, "unit": "100g", "category": "Meat"},
    {"name": "Lamb", "calories": 294, "protein": 25, "carbs": 0, "fat": 21, "fiber": 0, "cost": 7.99, "unit": "100g", "category": "Meat"},

    # Fish & Seafood
    {"name": "Salmon", "calories": 208, "protein": 20, "carbs": 0, "fat": 13, "fiber": 0, "cost": 5.99, "unit": "100g", "category": "Fish"},
    {"name": "Tuna", "calories": 132, "protein": 28, "carbs": 0, "fat": 1.3, "fiber": 0, "cost": 4.99, "unit": "100g", "category": "Fish"},
    {"name": "Tilapia", "calories": 128, "protein": 26, "carbs": 0, "fat": 2.7, "fiber": 0, "cost": 3.99, "unit": "100g", "category": "Fish"},
    {"name": "Cod", "calories": 82, "protein": 18, "carbs": 0, "fat": 0.7, "fiber": 0, "cost": 4.49, "unit": "100g", "category": "Fish"},
    {"name": "Shrimp", "calories": 99, "protein": 24, "carbs": 0.2, "fat": 0.3, "fiber": 0, "cost": 6.99, "unit": "100g", "category": "Seafood"},

    # Vegetarian Protein
    {"name": "Tofu (firm)", "calories": 144, "protein": 17, "carbs": 3, "fat": 9, "fiber": 2, "cost": 1.99, "unit": "100g", "category": "Veg Protein"},
    {"name": "Paneer", "calories": 265, "protein": 18, "carbs": 3.5, "fat": 20, "fiber": 0, "cost": 2.99, "unit": "100g", "category": "Veg Protein"},
    {"name": "Soya Chunks", "calories": 345, "protein": 52, "carbs": 33, "fat": 0.5, "fiber": 13, "cost": 1.49, "unit": "100g", "category": "Veg Protein"},
    {"name": "Hung Curd", "calories": 98, "protein": 11, "carbs": 4.7, "fat": 4.3, "fiber": 0, "cost": 1.29, "unit": "100g", "category": "Veg Protein"},
    {"name": "Tempeh", "calories": 193, "protein": 20, "carbs": 9, "fat": 11, "fiber": 9, "cost": 2.49, "unit": "100g", "category": "Veg Protein"},
    {"name": "Chickpeas", "calories": 164, "protein": 9, "carbs": 27, "fat": 2.6, "fiber": 7.6, "cost": 0.60, "unit": "100g", "category": "Veg Protein"},
    {"name": "Lentils", "calories": 116, "protein": 9, "carbs": 20, "fat": 0.4, "fiber": 7.9, "cost": 0.40, "unit": "100g", "category": "Veg Protein"},
    {"name": "Black Beans", "calories": 132, "protein": 8.9, "carbs": 24, "fat": 0.5, "fiber": 8.7, "cost": 0.55, "unit": "100g", "category": "Veg Protein"},
    {"name": "Kidney Beans", "calories": 127, "protein": 8.7, "carbs": 23, "fat": 0.5, "fiber": 6.4, "cost": 0.50, "unit": "100g", "category": "Veg Protein"},

    # Eggs & Dairy
    {"name": "Eggs", "calories": 155, "protein": 13, "carbs": 1.1, "fat": 11, "fiber": 0, "cost": 0.30, "unit": "egg", "category": "Dairy"},
    {"name": "Greek Yogurt", "calories": 59, "protein": 10, "carbs": 3.6, "fat": 0.4, "fiber": 0, "cost": 1.20, "unit": "100g", "category": "Dairy"},
    {"name": "Milk", "calories": 42, "protein": 3.4, "carbs": 5, "fat": 1, "fiber": 0, "cost": 0.15, "unit": "100ml", "category": "Dairy"},
    {"name": "Cottage Cheese", "calories": 98, "protein": 11, "carbs": 3.4, "fat": 4.3, "fiber": 0, "cost": 1.49, "unit": "100g", "category": "Dairy"},

    # Grains & Carbs
    {"name": "Brown Rice", "calories": 112, "protein": 2.6, "carbs": 24, "fat": 0.9, "fiber": 1.8, "cost": 0.50, "unit": "100g", "category": "Grains"},
    {"name": "Quinoa", "calories": 120, "protein": 4.4, "carbs": 21, "fat": 1.9, "fiber": 2.8, "cost": 1.20, "unit": "100g", "category": "Grains"},
    {"name": "Oatmeal", "calories": 389, "protein": 17, "carbs": 66, "fat": 7, "fiber": 11, "cost": 0.25, "unit": "100g", "category": "Grains"},
    {"name": "Whole Wheat Bread", "calories": 247, "protein": 13, "carbs": 41, "fat": 3.4, "fiber": 7, "cost": 0.30, "unit": "slice", "category": "Grains"},
    {"name": "White Rice", "calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3, "fiber": 0.4, "cost": 0.40, "unit": "100g", "category": "Grains"},
    {"name": "Pasta (whole wheat)", "calories": 124, "protein": 5.3, "carbs": 26, "fat": 0.5, "fiber": 3.9, "cost": 0.45, "unit": "100g", "category": "Grains"},

    # Vegetables
    {"name": "Broccoli", "calories": 34, "protein": 2.8, "carbs": 7, "fat": 0.4, "fiber": 2.6, "cost": 0.80, "unit": "100g", "category": "Vegetables"},
    {"name": "Spinach", "calories": 23, "protein": 2.9, "carbs": 3.6, "fat": 0.4, "fiber": 2.2, "cost": 0.70, "unit": "100g", "category": "Vegetables"},
    {"name": "Sweet Potato", "calories": 86, "protein": 1.6, "carbs": 20, "fat": 0.1, "fiber": 3, "cost": 0.60, "unit": "100g", "category": "Vegetables"},
    {"name": "Cauliflower", "calories": 25, "protein": 1.9, "carbs": 5, "fat": 0.3, "fiber": 2, "cost": 0.75, "unit": "100g", "category": "Vegetables"},
    {"name": "Bell Peppers", "calories": 31, "protein": 1, "carbs": 6, "fat": 0.3, "fiber": 2.1, "cost": 0.90, "unit": "100g", "category": "Vegetables"},
    {"name": "Carrots", "calories": 41, "protein": 0.9, "carbs": 10, "fat": 0.2, "fiber": 2.8, "cost": 0.50, "unit": "100g", "category": "Vegetables"},
    {"name": "Tomatoes", "calories": 18, "protein": 0.9, "carbs": 3.9, "fat": 0.2, "fiber": 1.2, "cost": 0.65, "unit": "100g", "category": "Vegetables"},

    # Fruits & Nuts
    {"name": "Banana", "calories": 89, "protein": 1.1, "carbs": 23, "fat": 0.3, "fiber": 2.6, "cost": 0.20, "unit": "piece", "category": "Fruits"},
    {"name": "Apple", "calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2, "fiber": 2.4, "cost": 0.25, "unit": "piece", "category": "Fruits"},
    {"name": "Orange", "calories": 47, "protein": 0.9, "carbs": 12, "fat": 0.1, "fiber": 2.4, "cost": 0.30, "unit": "piece", "category": "Fruits"},
    {"name": "Almonds", "calories": 579, "protein": 21, "carbs": 22, "fat": 50, "fiber": 12.5, "cost": 2.50, "unit": "100g", "category": "Nuts"},
    {"name": "Peanuts", "calories": 567, "protein": 26, "carbs": 16, "fat": 49, "fiber": 8.5, "cost": 1.80, "unit": "100g", "category": "Nuts"},
    {"name": "Walnuts", "calories": 654, "protein": 15, "carbs": 14, "fat": 65, "fiber": 6.7, "cost": 3.20, "unit": "100g", "category": "Nuts"},
]


def optimize_meal_plan(goals: dict, budget: float):
    # score foods similar to your JS (avoid divide-by-zero)
    def safe_div(a, b):
        return a / b if b and b != 0 else 0.0

    scored = []
    for f in FOODS:
        protein_score = safe_div(safe_div(f["protein"], goals["protein"]), f["cost"])
        carb_score = safe_div(safe_div(f["carbs"], goals["carbs"]), f["cost"])
        fiber_score = safe_div(safe_div(f["fiber"], goals["fiber"]), f["cost"])
        calorie_score = safe_div(safe_div(f["calories"], goals["calories"]), f["cost"])

        eff = protein_score * 0.30 + carb_score * 0.25 + fiber_score * 0.20 + calorie_score * 0.25
        scored.append({**f, "efficiency": eff})

    scored.sort(key=lambda x: x["efficiency"], reverse=True)

    selected = []
    totals = {"calories": 0.0, "protein": 0.0, "carbs": 0.0, "fat": 0.0, "fiber": 0.0, "cost": 0.0}

    iterations = 0
    max_iterations = 50

    while iterations < max_iterations and totals["cost"] < budget * 0.9:
        best_food = None
        best_amount = 0.0
        best_score = -1e18

        calorie_deficit = max(0.0, goals["calories"] - totals["calories"])
        protein_deficit = max(0.0, goals["protein"] - totals["protein"])
        carb_deficit = max(0.0, goals["carbs"] - totals["carbs"])
        fiber_deficit = max(0.0, goals["fiber"] - totals["fiber"])

        for food in scored:
            for amount in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
                added_cost = food["cost"] * amount
                if totals["cost"] + added_cost > budget:
                    continue

                added_cals = food["calories"] * amount
                added_protein = food["protein"] * amount
                added_carbs = food["carbs"] * amount
                added_fiber = food["fiber"] * amount

                score = (
                    (min(added_cals, calorie_deficit) / goals["calories"]) * 0.25 +
                    (min(added_protein, protein_deficit) / goals["protein"]) * 0.35 +
                    (min(added_carbs, carb_deficit) / goals["carbs"]) * 0.25 +
                    (min(added_fiber, fiber_deficit) / goals["fiber"]) * 0.15 -
                    (added_cost / budget) * 0.10
                )

                if score > best_score:
                    best_score = score
                    best_food = food
                    best_amount = amount

        if best_food is None or best_score <= 0:
            break

        # merge if already selected
        existing = next((s for s in selected if s["name"] == best_food["name"]), None)
        if existing:
            existing["amount"] += best_amount
        else:
            selected.append({**best_food, "amount": best_amount})

        totals["calories"] += best_food["calories"] * best_amount
        totals["protein"] += best_food["protein"] * best_amount
        totals["carbs"] += best_food["carbs"] * best_amount
        totals["fat"] += best_food["fat"] * best_amount
        totals["fiber"] += best_food["fiber"] * best_amount
        totals["cost"] += best_food["cost"] * best_amount

        iterations += 1

    # format outputs
    foods_out = []
    for f in selected:
        foods_out.append({
            "Food": f["name"],
            "Category": f["category"],
            "Amount": round(f["amount"], 1),
            "Unit": f["unit"],
            "Cost ($)": round(f["cost"] * f["amount"], 2),
            "Calories": int(round(f["calories"] * f["amount"])),
            "Protein (g)": round(f["protein"] * f["amount"], 1),
            "Carbs (g)": round(f["carbs"] * f["amount"], 1),
            "Fat (g)": round(f["fat"] * f["amount"], 1),
            "Fiber (g)": round(f["fiber"] * f["amount"], 1),
        })

    totals_out = {
        "cost": round(totals["cost"], 2),
        "calories": int(round(totals["calories"])),
        "protein": round(totals["protein"], 1),
        "carbs": round(totals["carbs"], 1),
        "fat": round(totals["fat"], 1),
        "fiber": round(totals["fiber"], 1),
    }

    completion = {
        "Calories": int(round((totals["calories"] / goals["calories"]) * 100)) if goals["calories"] else 0,
        "Protein": int(round((totals["protein"] / goals["protein"]) * 100)) if goals["protein"] else 0,
        "Carbs": int(round((totals["carbs"] / goals["carbs"]) * 100)) if goals["carbs"] else 0,
        "Fiber": int(round((totals["fiber"] / goals["fiber"]) * 100)) if goals["fiber"] else 0,
    }

    return foods_out, totals_out, completion


def build_export_text(goals, budget, foods_out, totals_out, completion):
    lines = []
    lines.append("OPTIMIZED MEAL PLAN")
    lines.append(f"Budget: ${budget}")
    lines.append(f"Generated: {date.today().isoformat()}")
    lines.append("")
    lines.append("NUTRITIONAL GOALS:")
    lines.append(f"- Calories: {goals['calories']} kcal")
    lines.append(f"- Protein: {goals['protein']} g")
    lines.append(f"- Carbs: {goals['carbs']} g")
    lines.append(f"- Fat: {goals['fat']} g")
    lines.append(f"- Fiber: {goals['fiber']} g")
    lines.append("")
    lines.append("MEAL PLAN:")
    for f in foods_out:
        lines.append(f"- {f['Amount']} {f['Unit']} {f['Food']} — ${f['Cost ($)']}")
    lines.append("")
    lines.append("TOTALS:")
    lines.append(f"- Total Cost: ${totals_out['cost']}")
    lines.append(f"- Calories: {totals_out['calories']} ({completion['Calories']}%)")
    lines.append(f"- Protein: {totals_out['protein']} g ({completion['Protein']}%)")
    lines.append(f"- Carbs: {totals_out['carbs']} g ({completion['Carbs']}%)")
    lines.append(f"- Fat: {totals_out['fat']} g")
    lines.append(f"- Fiber: {totals_out['fiber']} g ({completion['Fiber']}%)")
    return "\n".join(lines)


# -----------------------------
# UI
# -----------------------------
st.title("🍽️ Diet Planner Pro")
st.caption("Cost-minimized meal planning using a greedy optimization heuristic (Streamlit version of your React app).")

with st.sidebar:
    st.header("Set Goals")
    calories = st.number_input("Daily Calories (kcal)", min_value=0, value=2000, step=50)
    protein = st.number_input("Protein (g)", min_value=0, value=150, step=5)
    carbs = st.number_input("Carbohydrates (g)", min_value=0, value=250, step=5)
    fat = st.number_input("Fat (g)", min_value=0, value=65, step=5)
    fiber = st.number_input("Fiber (g)", min_value=0, value=30, step=1)

    st.divider()
    st.header("Budget")
    budget = st.number_input("Daily Budget ($)", min_value=0.0, value=50.0, step=1.0)

    optimize_btn = st.button("🧮 Optimize Meal Plan", use_container_width=True)

goals = {"calories": float(calories), "protein": float(protein), "carbs": float(carbs), "fat": float(fat), "fiber": float(fiber)}

if "result" not in st.session_state:
    st.session_state.result = None

if optimize_btn:
    with st.spinner("Optimizing..."):
        foods_out, totals_out, completion = optimize_meal_plan(goals, float(budget))
        st.session_state.result = (foods_out, totals_out, completion)

result = st.session_state.result

if not result:
    st.info("Set your nutritional goals + budget on the left, then click **Optimize Meal Plan**.")
    st.stop()

foods_out, totals_out, completion = result
df = pd.DataFrame(foods_out)

# Metrics row
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Cost", f"${totals_out['cost']}", f"{int(round((totals_out['cost']/budget)*100)) if budget else 0}% of budget")
c2.metric("Calories", f"{totals_out['calories']}", f"{completion['Calories']}% of goal")
c3.metric("Protein", f"{totals_out['protein']} g", f"{completion['Protein']}% of goal")
c4.metric("Food Items", f"{len(df)}")

st.divider()

# Table + download
top_left, top_right = st.columns([2, 1])

with top_left:
    st.subheader("Optimized Meal Plan")
    if df.empty:
        st.warning("No feasible plan found for this budget/goals. Try increasing budget or lowering targets.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)

with top_right:
    st.subheader("Export")
    export_text = build_export_text(goals, budget, foods_out, totals_out, completion)
    st.download_button(
        label="⬇️ Download meal-plan.txt",
        data=export_text,
        file_name="meal-plan.txt",
        mime="text/plain",
        use_container_width=True
    )

st.divider()

# Charts
chart1, chart2 = st.columns(2)

with chart1:
    st.subheader("Goal Completion (%)")
    completion_df = pd.DataFrame(
        [{"Metric": k, "Completion (%)": v} for k, v in completion.items()]
    )
    st.bar_chart(completion_df.set_index("Metric"))

with chart2:
    st.subheader("Macronutrient Distribution (Calories)")
    macro_cals = pd.DataFrame([
        {"Macro": "Protein", "Calories": totals_out["protein"] * 4},
        {"Macro": "Carbs", "Calories": totals_out["carbs"] * 4},
        {"Macro": "Fat", "Calories": totals_out["fat"] * 9},
    ])
    st.dataframe(macro_cals, use_container_width=True, hide_index=True)
    st.caption("Streamlit's native pie is limited; use the table above or swap to Plotly if you want a pie chart.")
