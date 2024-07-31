from playwright.sync_api import sync_playwright, Page
from pages.cgate import get_penki_plans
from pages.telia import get_telia_plans

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plans_to_dataframe(plans):
    data = {
        "Name": [plan.name for plan in plans],
        "Speed": [plan.speed for plan in plans],
        "Price": [plan.price for plan in plans],
        "Company": [plan.company for plan in plans]
    }
    return pd.DataFrame(data)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page: Page = browser.new_page()
    telia_plans = get_telia_plans(page)
    penki_plans = get_penki_plans(page)
    
    all_plans = telia_plans + penki_plans
    df = plans_to_dataframe(all_plans)
    browser.close()


# Plotting the data
plt.figure(figsize=(12, 8))
sns.barplot(data=df, y='Speed', x='Price', hue='Company', ci=None, orient='h')

plt.title('Palyginimas')
plt.xlabel('Kaina (€)')
plt.ylabel('Greitis')
plt.legend(title='Tiekėjas')
plt.grid(True)
plt.show()


count_data = df['Company'].value_counts()

# Create a bar plot
plt.figure(figsize=(6, 4))
count_data.plot(kind='bar', color=['blue', 'orange'])  # You can customize colors as needed

plt.title('Count of Internet Plans by Company')
plt.xlabel('Company')
plt.ylabel('Number of Plans')
plt.xticks(rotation=0)  # Rotate x labels if needed
plt.grid(axis='y')
plt.show()