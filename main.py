from playwright.sync_api import sync_playwright, Locator
from dataclasses.product import InternetPlan

def save_plans_to_txt(plans:list[InternetPlan], filename="plans.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        # Write headers
        file.write(f"{'Name':<50} {'Speed':<20} {'Price':<10} {'Company':<10}\n")
        file.write("="*90 + "\n")
        # Write plan details
        for plan in plans:
            file.write(f"{plan.name:<50} {plan.speed:<20} {plan.price:<10} {plan.company:<10}\n")

            
            
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.telia.lt/privatiems/internetas")
    products = page.locator(".component__content .row .px-sm-20")
    
    plans:list[InternetPlan] = []
    
    for i in range(products.count()):
        name = products.nth(i).locator("a").first.text_content()
        speed = products.nth(i).locator("strong").text_content().split('Nuo')[0].split('iki')[1]
        price = products.nth(i).locator(".price").text_content()
        
        plan = InternetPlan(name=name, speed=speed, price=price, company="talia")
        plans.append(plan)
    
    
    save_plans_to_txt(plans)