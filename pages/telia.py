from playwright.sync_api import Page
from utils.save_to_file import save_plans_to_txt
from classes.product import InternetPlan

def get_telia_plans(page: Page):
    
    link = "https://www.telia.lt/privatiems/internetas"
    company_name = 'telia'
    products = page.locator(".component__content .row .px-sm-20")
    
    page.goto(link)
    
    plans: list[InternetPlan] = []
    
    for i in range(products.count()):
        name: str = products.nth(i).locator("a").first.text_content()
        speed = products.nth(i).locator("strong").text_content().split('Nuo')[0].split('iki')[1].strip()
        price = products.nth(i).locator(".price").text_content()
        
        plan = InternetPlan(name=name, speed=speed, price=price, company=company_name)
        plans.append(plan)
    
    save_plans_to_txt(plans)
    return plans