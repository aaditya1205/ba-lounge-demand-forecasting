# British Airways Lounge Demand Forecasting Project

# --- Step 1: Import libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Step 2: Load sample dataset ---
# NOTE: Replace 'data/sample_schedule.xlsx' with the actual dataset if available.
file_path = "data/sample_schedule.xlsx"
try:
    df = pd.read_excel(file_path)
except FileNotFoundError:
    # Create a mock dataset if not present
    df = pd.DataFrame({
        "HAUL": ["LONG", "LONG", "SHORT", "SHORT"],
        "ARRIVAL_REGION": ["North America", "Asia", "Europe", "Middle East"],
        "FIRST_CLASS_SEATS": [8, 6, 0, 0],
        "BUSINESS_CLASS_SEATS": [49, 42, 17, 8],
        "ECONOMY_SEATS": [178, 200, 160, 170],
        "TIER1_ELIGIBLE_PAX": [5, 3, 0, 0],
        "TIER2_ELIGIBLE_PAX": [20, 18, 11, 16],
        "TIER3_ELIGIBLE_PAX": [60, 55, 40, 54],
    })

# --- Step 3: Grouping and calculating eligibility percentages ---
grouped = df.groupby(["HAUL", "ARRIVAL_REGION"])
lookup = grouped[["TIER1_ELIGIBLE_PAX", "TIER2_ELIGIBLE_PAX", "TIER3_ELIGIBLE_PAX",
                  "FIRST_CLASS_SEATS", "BUSINESS_CLASS_SEATS", "ECONOMY_SEATS"]].sum()

lookup["TOTAL_PAX"] = lookup["FIRST_CLASS_SEATS"] + lookup["BUSINESS_CLASS_SEATS"] + lookup["ECONOMY_SEATS"]
lookup["Tier1_%"] = (lookup["TIER1_ELIGIBLE_PAX"] / lookup["TOTAL_PAX"] * 100).round(2)
lookup["Tier2_%"] = (lookup["TIER2_ELIGIBLE_PAX"] / lookup["TOTAL_PAX"] * 100).round(2)
lookup["Tier3_%"] = (lookup["TIER3_ELIGIBLE_PAX"] / lookup["TOTAL_PAX"] * 100).round(2)

lookup_table = lookup[["Tier1_%", "Tier2_%", "Tier3_%"]].reset_index()
print("Lounge Eligibility Lookup Table:")
print(lookup_table)

# --- Step 4: Visualization ---
lookup_table.set_index(["HAUL", "Region" if "Region" in lookup_table.columns else "ARRIVAL_REGION"])[["Tier1_%", "Tier2_%", "Tier3_%"]].plot(kind="bar", figsize=(10,6))
plt.title("Lounge Eligibility by Haul and Region")
plt.ylabel("Percentage of Eligible Passengers")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# --- Step 5: Export results to Excel ---
output_path = "outputs/Completed_Lookup.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    lookup_table.to_excel(writer, sheet_name="Lounge Eligibility Lookup Table", index=False)

    justification_answers = pd.DataFrame({
        "Question": [
            "How did you choose to group the flights?",
            "Why do your groupings make sense for this type of modeling?",
            "What assumptions did you make and why?",
            "How can your model scale to future or unknown schedules?"
        ],
        "Answer": [
            "Grouped flights by haul (short/long) and region to capture passenger mix and cabin differences.",
            "These dimensions affect lounge demand: long-haul attracts more premium flyers, short-haul less so.",
            "Assumed eligibility percentages are stable within each group and based on observed patterns.",
            "Model scales by applying percentages to categories, making it flexible for new routes and schedules."
        ]
    })
    justification_answers.to_excel(writer, sheet_name="Justification", index=False)

print(f"Results exported to {output_path}")
