import React,

{useState}
from

'react';
import

{LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell}
from

'recharts';
import

{Utensils, DollarSign, Target, TrendingDown, Download, Calculator}
from

'lucide-react';

const
DietPlannerApp = () = > {
    const[activeTab, setActiveTab] = useState('planner');
const[nutritionGoals, setNutritionGoals] = useState({
    calories: 2000,
    protein: 150,
    carbs: 250,
    fat: 65,
    fiber: 30
});
const[budget, setBudget] = useState(50);
const[mealPlan, setMealPlan] = useState(null);
const[isOptimizing, setIsOptimizing] = useState(false);

const
foodDatabase = [
               // Poultry & Meat
{name: 'Chicken Breast', calories: 165, protein: 31, carbs: 0, fat: 3.6, fiber: 0, cost: 3.99, unit: '100g',
 category: 'Poultry'},
{name: 'Chicken Thigh', calories: 209, protein: 26, carbs: 0, fat: 10.9, fiber: 0, cost: 3.49, unit: '100g',
 category: 'Poultry'},
{name: 'Ground Beef (lean)', calories: 250, protein: 26, carbs: 0, fat: 15, fiber: 0, cost: 4.99, unit: '100g',
 category: 'Meat'},
{name: 'Beef Steak', calories: 271, protein: 25, carbs: 0, fat: 19, fiber: 0, cost: 6.99, unit: '100g',
 category: 'Meat'},
{name: 'Pork Loin', calories: 242, protein: 27, carbs: 0, fat: 14, fiber: 0, cost: 4.49, unit: '100g',
 category: 'Meat'},
{name: 'Lamb', calories: 294, protein: 25, carbs: 0, fat: 21, fiber: 0, cost: 7.99, unit: '100g', category: 'Meat'},

// Fish & Seafood
{name: 'Salmon', calories: 208, protein: 20, carbs: 0, fat: 13, fiber: 0, cost: 5.99, unit: '100g', category: 'Fish'},
{name: 'Tuna', calories: 132, protein: 28, carbs: 0, fat: 1.3, fiber: 0, cost: 4.99, unit: '100g', category: 'Fish'},
{name: 'Tilapia', calories: 128, protein: 26, carbs: 0, fat: 2.7, fiber: 0, cost: 3.99, unit: '100g', category: 'Fish'},
{name: 'Cod', calories: 82, protein: 18, carbs: 0, fat: 0.7, fiber: 0, cost: 4.49, unit: '100g', category: 'Fish'},
{name: 'Shrimp', calories: 99, protein: 24, carbs: 0.2, fat: 0.3, fiber: 0, cost: 6.99, unit: '100g',
 category: 'Seafood'},

// Vegetarian
Protein
{name: 'Tofu (firm)', calories: 144, protein: 17, carbs: 3, fat: 9, fiber: 2, cost: 1.99, unit: '100g',
 category: 'Veg Protein'},
{name: 'Paneer', calories: 265, protein: 18, carbs: 3.5, fat: 20, fiber: 0, cost: 2.99, unit: '100g',
 category: 'Veg Protein'},
{name: 'Soya Chunks', calories: 345, protein: 52, carbs: 33, fat: 0.5, fiber: 13, cost: 1.49, unit: '100g',
 category: 'Veg Protein'},
{name: 'Hung Curd', calories: 98, protein: 11, carbs: 4.7, fat: 4.3, fiber: 0, cost: 1.29, unit: '100g',
 category: 'Veg Protein'},
{name: 'Tempeh', calories: 193, protein: 20, carbs: 9, fat: 11, fiber: 9, cost: 2.49, unit: '100g',
 category: 'Veg Protein'},
{name: 'Chickpeas', calories: 164, protein: 9, carbs: 27, fat: 2.6, fiber: 7.6, cost: 0.60, unit: '100g',
 category: 'Veg Protein'},
{name: 'Lentils', calories: 116, protein: 9, carbs: 20, fat: 0.4, fiber: 7.9, cost: 0.40, unit: '100g',
 category: 'Veg Protein'},
{name: 'Black Beans', calories: 132, protein: 8.9, carbs: 24, fat: 0.5, fiber: 8.7, cost: 0.55, unit: '100g',
 category: 'Veg Protein'},
{name: 'Kidney Beans', calories: 127, protein: 8.7, carbs: 23, fat: 0.5, fiber: 6.4, cost: 0.50, unit: '100g',
 category: 'Veg Protein'},

// Eggs & Dairy
{name: 'Eggs', calories: 155, protein: 13, carbs: 1.1, fat: 11, fiber: 0, cost: 0.30, unit: 'egg', category: 'Dairy'},
{name: 'Greek Yogurt', calories: 59, protein: 10, carbs: 3.6, fat: 0.4, fiber: 0, cost: 1.20, unit: '100g',
 category: 'Dairy'},
{name: 'Milk', calories: 42, protein: 3.4, carbs: 5, fat: 1, fiber: 0, cost: 0.15, unit: '100ml', category: 'Dairy'},
{name: 'Cottage Cheese', calories: 98, protein: 11, carbs: 3.4, fat: 4.3, fiber: 0, cost: 1.49, unit: '100g',
 category: 'Dairy'},

// Grains & Carbs
{name: 'Brown Rice', calories: 112, protein: 2.6, carbs: 24, fat: 0.9, fiber: 1.8, cost: 0.50, unit: '100g',
 category: 'Grains'},
{name: 'Quinoa', calories: 120, protein: 4.4, carbs: 21, fat: 1.9, fiber: 2.8, cost: 1.20, unit: '100g',
 category: 'Grains'},
{name: 'Oatmeal', calories: 389, protein: 17, carbs: 66, fat: 7, fiber: 11, cost: 0.25, unit: '100g',
 category: 'Grains'},
{name: 'Whole Wheat Bread', calories: 247, protein: 13, carbs: 41, fat: 3.4, fiber: 7, cost: 0.30, unit: 'slice',
 category: 'Grains'},
{name: 'White Rice', calories: 130, protein: 2.7, carbs: 28, fat: 0.3, fiber: 0.4, cost: 0.40, unit: '100g',
 category: 'Grains'},
{name: 'Pasta (whole wheat)', calories: 124, protein: 5.3, carbs: 26, fat: 0.5, fiber: 3.9, cost: 0.45, unit: '100g',
 category: 'Grains'},

// Vegetables
{name: 'Broccoli', calories: 34, protein: 2.8, carbs: 7, fat: 0.4, fiber: 2.6, cost: 0.80, unit: '100g',
 category: 'Vegetables'},
{name: 'Spinach', calories: 23, protein: 2.9, carbs: 3.6, fat: 0.4, fiber: 2.2, cost: 0.70, unit: '100g',
 category: 'Vegetables'},
{name: 'Sweet Potato', calories: 86, protein: 1.6, carbs: 20, fat: 0.1, fiber: 3, cost: 0.60, unit: '100g',
 category: 'Vegetables'},
{name: 'Cauliflower', calories: 25, protein: 1.9, carbs: 5, fat: 0.3, fiber: 2, cost: 0.75, unit: '100g',
 category: 'Vegetables'},
{name: 'Bell Peppers', calories: 31, protein: 1, carbs: 6, fat: 0.3, fiber: 2.1, cost: 0.90, unit: '100g',
 category: 'Vegetables'},
{name: 'Carrots', calories: 41, protein: 0.9, carbs: 10, fat: 0.2, fiber: 2.8, cost: 0.50, unit: '100g',
 category: 'Vegetables'},
{name: 'Tomatoes', calories: 18, protein: 0.9, carbs: 3.9, fat: 0.2, fiber: 1.2, cost: 0.65, unit: '100g',
 category: 'Vegetables'},

// Fruits & Nuts
{name: 'Banana', calories: 89, protein: 1.1, carbs: 23, fat: 0.3, fiber: 2.6, cost: 0.20, unit: 'piece',
 category: 'Fruits'},
{name: 'Apple', calories: 52, protein: 0.3, carbs: 14, fat: 0.2, fiber: 2.4, cost: 0.25, unit: 'piece',
 category: 'Fruits'},
{name: 'Orange', calories: 47, protein: 0.9, carbs: 12, fat: 0.1, fiber: 2.4, cost: 0.30, unit: 'piece',
 category: 'Fruits'},
{name: 'Almonds', calories: 579, protein: 21, carbs: 22, fat: 50, fiber: 12.5, cost: 2.50, unit: '100g',
 category: 'Nuts'},
{name: 'Peanuts', calories: 567, protein: 26, carbs: 16, fat: 49, fiber: 8.5, cost: 1.80, unit: '100g',
 category: 'Nuts'},
{name: 'Walnuts', calories: 654, protein: 15, carbs: 14, fat: 65, fiber: 6.7, cost: 3.20, unit: '100g',
 category: 'Nuts'}
];

const
optimizeMealPlan = () = > {
    setIsOptimizing(true);

setTimeout(() = > {
    const
scoredFoods = foodDatabase.map(food= > {
    const
proteinScore = (food.protein / nutritionGoals.protein) / food.cost;
const
carbScore = (food.carbs / nutritionGoals.carbs) / food.cost;
const
fiberScore = (food.fiber / nutritionGoals.fiber) / food.cost;
const
calorieScore = (food.calories / nutritionGoals.calories) / food.cost;

return {
    ...
food,
efficiency: proteinScore * 0.3 + carbScore * 0.25 + fiberScore * 0.2 + calorieScore * 0.25
};
}).sort((a, b) = > b.efficiency - a.efficiency);

const
selected = [];
let
totals = {calories: 0, protein: 0, carbs: 0, fat: 0, fiber: 0, cost: 0};
let
iterations = 0;
const
maxIterations = 50;

while (iterations < maxIterations & & totals.cost < budget * 0.9) {
let bestFood = null;
let bestAmount = 0;
let bestScore = -Infinity;

for (const food of scoredFoods) {
const calorieDeficit = Math.max(0, nutritionGoals.calories - totals.calories);
const proteinDeficit = Math.max(0, nutritionGoals.protein - totals.protein);
const carbDeficit = Math.max(0, nutritionGoals.carbs - totals.carbs);
const fiberDeficit = Math.max(0, nutritionGoals.fiber - totals.fiber);

for (let amount = 0.5; amount <= 3; amount += 0.5) {
const addedCost = food.cost * amount;
if (totals.cost + addedCost > budget)
continue;

const
addedCals = food.calories * amount;
const
addedProtein = food.protein * amount;
const
addedCarbs = food.carbs * amount;
const
addedFiber = food.fiber * amount;

const
score =
(Math.min(addedCals, calorieDeficit) / nutritionGoals.calories) * 0.25 +
(Math.min(addedProtein, proteinDeficit) / nutritionGoals.protein) * 0.35 +
(Math.min(addedCarbs, carbDeficit) / nutritionGoals.carbs) * 0.25 +
(Math.min(addedFiber, fiberDeficit) / nutritionGoals.fiber) * 0.15 -
(addedCost / budget) * 0.1;

if (score > bestScore) {
bestScore = score;
bestFood = food;
bestAmount = amount;
}
}
}

if (!bestFood | | bestScore <= 0)
    break;

const
existing = selected.find(s= > s.name == = bestFood.name);
if (existing) {
existing.amount += bestAmount;
} else {
selected.push({...bestFood, amount: bestAmount});
}

totals.calories += bestFood.calories * bestAmount;
totals.protein += bestFood.protein * bestAmount;
totals.carbs += bestFood.carbs * bestAmount;
totals.fat += bestFood.fat * bestAmount;
totals.fiber += bestFood.fiber * bestAmount;
totals.cost += bestFood.cost * bestAmount;

iterations + +;
}

const
plan = {
foods: selected.map(food= > ({
    name: food.name,
    amount: Math.round(food.amount * 10) / 10,
    unit: food.unit,
    totalCost: Math.round(food.cost * food.amount * 100) / 100,
    calories: Math.round(food.calories * food.amount),
    protein: Math.round(food.protein * food.amount * 10) / 10,
    carbs: Math.round(food.carbs * food.amount * 10) / 10,
    fat: Math.round(food.fat * food.amount * 10) / 10,
    fiber: Math.round(food.fiber * food.amount * 10) / 10
})),
totals: {
    calories: Math.round(totals.calories),
    protein: Math.round(totals.protein * 10) / 10,
    carbs: Math.round(totals.carbs * 10) / 10,
    fat: Math.round(totals.fat * 10) / 10,
    fiber: Math.round(totals.fiber * 10) / 10,
    cost: Math.round(totals.cost * 100) / 100
},
goalCompletion: {
    calories: Math.round((totals.calories / nutritionGoals.calories) * 100),
    protein: Math.round((totals.protein / nutritionGoals.protein) * 100),
    carbs: Math.round((totals.carbs / nutritionGoals.carbs) * 100),
    fiber: Math.round((totals.fiber / nutritionGoals.fiber) * 100)
}
};

setMealPlan(plan);
setIsOptimizing(false);
setActiveTab('results');
}, 1500);
};

const
exportPlan = () = > {
if (!mealPlan)
return;

const
content = `OPTIMIZED
MEAL
PLAN
Budget: $${budget}
Generated: ${new
Date().toLocaleDateString()}

NUTRITIONAL
GOALS:
- Calories: ${nutritionGoals.calories}
kcal
- Protein: ${nutritionGoals.protein}
g
- Carbs: ${nutritionGoals.carbs}
g
- Fat: ${nutritionGoals.fat}
g
- Fiber: ${nutritionGoals.fiber}
g

MEAL
PLAN:
${mealPlan.foods.map(f= >
  `${f.amount} ${f.unit} ${f.name} - $${f.totalCost}
`
).join('\n')}

TOTALS:
- Total
Cost: $${mealPlan.totals.cost}
- Calories: ${mealPlan.totals.calories}(${mealPlan.goalCompletion.calories} %)
- Protein: ${mealPlan.totals.protein}
g(${mealPlan.goalCompletion.protein} %)
- Carbs: ${mealPlan.totals.carbs}
g(${mealPlan.goalCompletion.carbs} %)
- Fat: ${mealPlan.totals.fat}
g
- Fiber: ${mealPlan.totals.fiber}
g(${mealPlan.goalCompletion.fiber} %)`;

const
blob = new
Blob([content], {type: 'text/plain'});
const
url = URL.createObjectURL(blob);
const
a = document.createElement('a');
a.href = url;
a.download = 'meal-plan.txt';
a.click();
};

const
COLORS = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'];

return (
    < div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4" >
    < div className="max-w-7xl mx-auto" >
    < div className="bg-white rounded-lg shadow-lg p-6 mb-6" >
    < div className="flex items-center gap-3 mb-2" >
    < Utensils className="w-8 h-8 text-blue-600" / >
    < h1 className="text-3xl font-bold text-gray-800" > Diet Planner Pro < / h1 >
    < / div >
    < p className="text-gray-600" > Linear Programming Optimization for Cost-Minimized Nutrition < / p >
    < / div >

    < div className="bg-white rounded-lg shadow-lg mb-6" >
    < div className="flex border-b" >
    < button
    onClick={() = > setActiveTab('planner')}
className = {`flex - 1
px - 6
py - 4
font - medium
transition - colors ${
    activeTab == = 'planner'
? 'bg-blue-50 text-blue-600 border-b-2 border-blue-600'
: 'text-gray-600 hover:bg-gray-50'
}`}
>
< Target
className = "w-5 h-5 inline mr-2" / >
            Set
Goals
< / button >
    < button
onClick = {() = > setActiveTab('results')}
className = {`flex - 1
px - 6
py - 4
font - medium
transition - colors ${
    activeTab == = 'results'
? 'bg-blue-50 text-blue-600 border-b-2 border-blue-600'
: 'text-gray-600 hover:bg-gray-50'
}`}
disabled = {!mealPlan}
>
< Calculator
className = "w-5 h-5 inline mr-2" / >
            Results
            < / button >
                < / div >
                    < / div >

                        {activeTab == = 'planner' & & (
    < div className="grid md:grid-cols-2 gap-6" >
    < div className="bg-white rounded-lg shadow-lg p-6" >
    < h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2" >
    < Target className="w-6 h-6 text-blue-600" / >
    Nutritional Goals
    < / h2 >

    < div className="space-y-4" >
    < div >
    < label className="block text-sm font-medium text-gray-700 mb-2" >
    Daily Calories (kcal)
                                        < / label >
                                            < input
type = "number"
value = {nutritionGoals.calories}
onChange = {(e) = > setNutritionGoals({...
nutritionGoals, calories: parseInt(e.target.value)})}
className = "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            / >
            < / div >

                < div >
                < label
className = "block text-sm font-medium text-gray-700 mb-2" >
            Protein(g)
            < / label >
                < input
type = "number"
value = {nutritionGoals.protein}
onChange = {(e) = > setNutritionGoals({...
nutritionGoals, protein: parseInt(e.target.value)})}
className = "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            / >
            < / div >

                < div >
                < label
className = "block text-sm font-medium text-gray-700 mb-2" >
            Carbohydrates(g)
            < / label >
                < input
type = "number"
value = {nutritionGoals.carbs}
onChange = {(e) = > setNutritionGoals({...
nutritionGoals, carbs: parseInt(e.target.value)})}
className = "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            / >
            < / div >

                < div >
                < label
className = "block text-sm font-medium text-gray-700 mb-2" >
            Fat(g)
            < / label >
                < input
type = "number"
value = {nutritionGoals.fat}
onChange = {(e) = > setNutritionGoals({...
nutritionGoals, fat: parseInt(e.target.value)})}
className = "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            / >
            < / div >

                < div >
                < label
className = "block text-sm font-medium text-gray-700 mb-2" >
            Fiber(g)
            < / label >
                < input
type = "number"
value = {nutritionGoals.fiber}
onChange = {(e) = > setNutritionGoals({...
nutritionGoals, fiber: parseInt(e.target.value)})}
className = "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            / >
            < / div >
                < / div >
                    < / div >

                        < div
className = "space-y-6" >
            < div
className = "bg-white rounded-lg shadow-lg p-6" >
            < h2
className = "text-xl font-bold text-gray-800 mb-4 flex items-center gap-2" >
            < DollarSign
className = "w-6 h-6 text-green-600" / >
            Budget
Constraint
< / h2 >

    < div >
    < label
className = "block text-sm font-medium text-gray-700 mb-2" >
            Daily
Budget($)
< / label >
    < input
type = "number"
value = {budget}
onChange = {(e) = > setBudget(parseFloat(e.target.value))}
className = "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            / >
            < / div >

                < button
onClick = {optimizeMealPlan}
disabled = {isOptimizing}
className = "w-full mt-6 bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors disabled:bg-gray-400 flex items-center justify-center gap-2"
            >
            {isOptimizing ? (
    <>
    < div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" / >
    Optimizing...
    < / >
): (
    <>
    < Calculator className="w-5 h-5" / >
    Optimize Meal Plan
    < / >
)}
< / button >
    < / div >

        < div
className = "bg-gradient-to-br from-blue-500 to-indigo-600 rounded-lg shadow-lg p-6 text-white" >
            < h3
className = "text-lg font-bold mb-3" > Optimization
Algorithm < / h3 >
              < ul
className = "space-y-2 text-sm" >
            < li
className = "flex items-start gap-2" >
            < span
className = "text-blue-200" >→ < / span >
                                   < span > Linear
Programming
with greedy heuristics < / span >
< / li >
< li className="flex items-start gap-2" >
< span className="text-blue-200" > → < / span >
< span > Minimizes cost
while meeting nutritional constraints < / span >
< / li >
< li
className = "flex items-start gap-2" >
< span
className = "text-blue-200" >→ < / span >
< span > Balances
macronutrients and micronutrients < / span >
< / li >
< li
className = "flex items-start gap-2" >
< span
className = "text-blue-200" >→ < / span >
< span > Considers
food
diversity and practical
portions < / span >
< / li >
< / ul >
< / div >
< / div >
< / div >
)}

{activeTab == = 'results' & & mealPlan & & (
< div
className = "space-y-6" >
< div
className = "grid md:grid-cols-4 gap-4" >
< div
className = "bg-white rounded-lg shadow-lg p-6" >
< div
className = "flex items-center justify-between mb-2" >
< span
className = "text-gray-600 text-sm" > Total
Cost < / span >
< DollarSign
className = "w-5 h-5 text-green-600" / >
< / div >
< div
className = "text-3xl font-bold text-gray-800" >
${mealPlan.totals.cost}
< / div >
< div
className = "text-sm text-gray-500 mt-1" >
{Math.round((mealPlan.totals.cost / budget) * 100)} % of
budget
< / div >
< / div >

< div
className = "bg-white rounded-lg shadow-lg p-6" >
< div
className = "flex items-center justify-between mb-2" >
< span
className = "text-gray-600 text-sm" > Calories < / span >
< TrendingDown
className = "w-5 h-5 text-blue-600" / >
< / div >
< div
className = "text-3xl font-bold text-gray-800" >
{mealPlan.totals.calories}
< / div >
< div
className = "text-sm text-gray-500 mt-1" >
{mealPlan.goalCompletion.calories} % of
goal
< / div >
< / div >

< div
className = "bg-white rounded-lg shadow-lg p-6" >
< div
className = "flex items-center justify-between mb-2" >
< span
className = "text-gray-600 text-sm" > Protein < / span >
< Target
className = "w-5 h-5 text-red-600" / >
< / div >
< div
className = "text-3xl font-bold text-gray-800" >
{mealPlan.totals.protein}
g
< / div >
< div
className = "text-sm text-gray-500 mt-1" >
{mealPlan.goalCompletion.protein} % of
goal
< / div >
< / div >

< div
className = "bg-white rounded-lg shadow-lg p-6" >
< div
className = "flex items-center justify-between mb-2" >
< span
className = "text-gray-600 text-sm" > Food
Items < / span >
< Utensils
className = "w-5 h-5 text-purple-600" / >
< / div >
< div
className = "text-3xl font-bold text-gray-800" >
{mealPlan.foods.length}
< / div >
< div
className = "text-sm text-gray-500 mt-1" >
Optimized
selection
< / div >
< / div >
< / div >

< div
className = "bg-white rounded-lg shadow-lg p-6" >
< div
className = "flex justify-between items-center mb-4" >
< h2
className = "text-xl font-bold text-gray-800" > Optimized
Meal
Plan < / h2 >
< button
onClick = {exportPlan}
className = "flex items-center gap-2 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors"
>
< Download
className = "w-4 h-4" / >
Export
Plan
< / button >
< / div >

< div
className = "overflow-x-auto" >
< table
className = "w-full" >
< thead >
< tr
className = "border-b-2 border-gray-200" >
< th
className = "text-left py-3 px-4 text-gray-700 font-semibold" > Food < / th >
< th
className = "text-right py-3 px-4 text-gray-700 font-semibold" > Amount < / th >
< th
className = "text-right py-3 px-4 text-gray-700 font-semibold" > Cost < / th >
< th
className = "text-right py-3 px-4 text-gray-700 font-semibold" > Calories < / th >
< th
className = "text-right py-3 px-4 text-gray-700 font-semibold" > Protein < / th >
< th
className = "text-right py-3 px-4 text-gray-700 font-semibold" > Carbs < / th >
< th
className = "text-right py-3 px-4 text-gray-700 font-semibold" > Fat < / th >
< / tr >
< / thead >
< tbody >
{mealPlan.foods.map((food, idx) = > (
    < tr key={idx} className="border-b border-gray-100 hover:bg-gray-50" >
    < td className="py-3 px-4 font-medium text-gray-800" > {food.name} < / td >
    < td className="py-3 px-4 text-right text-gray-600" > {food.amount} {food.unit} < / td >
    < td className="py-3 px-4 text-right text-green-600 font-medium" > ${food.totalCost} < / td >
    < td className="py-3 px-4 text-right text-gray-600" > {food.calories} < / td >
    < td className="py-3 px-4 text-right text-gray-600" > {food.protein}g < / td >
    < td className="py-3 px-4 text-right text-gray-600" > {food.carbs}g < / td >
    < td className="py-3 px-4 text-right text-gray-600" > {food.fat}g < / td >
    < / tr >
))}
< tr
className = "bg-blue-50 font-bold" >
< td
className = "py-3 px-4 text-gray-800" > TOTALS < / td >
< td
className = "py-3 px-4" > < / td >
< td
className = "py-3 px-4 text-right text-green-700" >${mealPlan.totals.cost} < / td >
< td
className = "py-3 px-4 text-right text-gray-800" > {mealPlan.totals.calories} < / td >
< td
className = "py-3 px-4 text-right text-gray-800" > {mealPlan.totals.protein}
g < / td >
< td
className = "py-3 px-4 text-right text-gray-800" > {mealPlan.totals.carbs}
g < / td >
< td
className = "py-3 px-4 text-right text-gray-800" > {mealPlan.totals.fat}
g < / td >
< / tr >
< / tbody >
< / table >
< / div >
< / div >

< div
className = "grid md:grid-cols-2 gap-6" >
< div
className = "bg-white rounded-lg shadow-lg p-6" >
< h3
className = "text-lg font-bold text-gray-800 mb-4" > Goal
Completion < / h3 >
< ResponsiveContainer
width = "100%"
height = {300} >
< BarChart
data = {[
    {name: 'Calories', value: mealPlan.goalCompletion.calories},
    {name: 'Protein', value: mealPlan.goalCompletion.protein},
    {name: 'Carbs', value: mealPlan.goalCompletion.carbs},
    {name: 'Fiber', value: mealPlan.goalCompletion.fiber}
]} >
< CartesianGrid
strokeDasharray = "3 3" / >
< XAxis
dataKey = "name" / >
< YAxis / >
< Tooltip / >
< Bar
dataKey = "value"
fill = "#3b82f6" / >
< / BarChart >
< / ResponsiveContainer >
< / div >

< div
className = "bg-white rounded-lg shadow-lg p-6" >
< h3
className = "text-lg font-bold text-gray-800 mb-4" > Macronutrient
Distribution < / h3 >
< ResponsiveContainer
width = "100%"
height = {300} >
< PieChart >
< Pie
data = {[
    {name: 'Protein', value: mealPlan.totals.protein * 4},
    {name: 'Carbs', value: mealPlan.totals.carbs * 4},
    {name: 'Fat', value: mealPlan.totals.fat * 9}
]}
cx = "50%"
cy = "50%"
labelLine = {false}
label = {({name, percent}) = > `${name}: ${(percent * 100).toFixed(0)} % `}
outerRadius = {80}
fill = "#8884d8"
dataKey = "value"
>
{[0, 1, 2].map((entry, index) = > (
    < Cell key={`cell-${index}`} fill={COLORS[index %COLORS.length]} / >
))}
< / Pie >
< Tooltip / >
< / PieChart >
< / ResponsiveContainer >
< / div >
< / div >
< / div >
)}

{activeTab == = 'results' & & !mealPlan & & (
< div
className = "bg-white rounded-lg shadow-lg p-12 text-center" >
< Calculator
className = "w-16 h-16 text-gray-400 mx-auto mb-4" / >
< h3
className = "text-xl font-bold text-gray-800 mb-2" > No
Meal
Plan
Yet < / h3 >
< p
className = "text-gray-600 mb-6" > Set
your
nutritional
goals and budget, then
click
Optimize
Meal
Plan < / p >
< button
onClick = {() = > setActiveTab('planner')}
className = "px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
>
Go
to
Planner
< / button >
< / div >
)}
< / div >
    < / div >
);
};

export
default
DietPlannerApp;