# British Airways Lounge Demand Forecasting

## 📌 Project Overview

Lounge access is a key part of the premium travel experience, and forecasting demand helps airlines plan capacity and investments. In this project, I built a **scalable data model** to estimate passenger eligibility for British Airways lounges at Heathrow Terminal 3. The model is designed to work without relying on specific aircraft or flight numbers, making it adaptable to future schedules.

## 🎯 Objectives

* Analyze flight schedules to understand passenger mix.
* Define logical **groupings** (haul type, region) to capture differences in lounge demand.
* Estimate **eligibility percentages** for three lounge tiers:

  * Tier 1: Concorde Room (hypothetical)
  * Tier 2: First Lounge
  * Tier 3: Club Lounge
* Deliver a reusable **lookup table + justifications** for business planning.

## 🛠️ Tech Stack

* **Python**: pandas, numpy, matplotlib
* **Excel**: Output tables and justifications
* **Jupyter Notebook**: Workflow, analysis, and visualization

## 📂 Repository Structure

```
ba-lounge-demand-forecasting/
│── data/
│   └── sample_schedule.xlsx       # Mock dataset (replace with real data if available)
│
│── notebooks/
│   └── lounge_demand_model.ipynb  # Main notebook with analysis
│
│── outputs/
│   └── Completed_Lookup.xlsx      # Final lookup table + justifications
│
│── README.md                      # Project overview
│── requirements.txt               # Python dependencies
```

## 📊 Key Steps

1. **Data Exploration**: Reviewed flight schedule dataset by haul type, destination region, and cabin mix.
2. **Grouping**: Grouped flights into categories (short/long haul, Europe, North America, Asia, Middle East).
3. **Eligibility Modeling**: Calculated lounge eligibility ratios from observed data and applied assumptions.
4. **Visualization**: Bar charts showing lounge demand by haul and region.
5. **Deliverable**: Exported results into an Excel file with lookup table + justifications.

## 📈 Example Output

* **Lookup Table**: Estimated % of passengers eligible for each lounge tier per haul/region.
* **Visuals**: Charts comparing lounge demand across categories.
* **Excel Deliverable**: Business-ready file with justifications.

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ba-lounge-demand-forecasting.git
   cd ba-lounge-demand-forecasting
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:

   ```bash
   jupyter notebook notebooks/lounge_demand_model.ipynb
   ```

## 💡 Impact

* Supports BA’s **strategic planning** for lounge capacity at Terminal 3.
* Helps identify potential demand for a future Tier 1 lounge.
* Provides a **scalable forecasting framework** adaptable to new routes and schedules.

---

👤 Author: \[Your Name]
📧 Contact: \[Your Email / LinkedIn]
