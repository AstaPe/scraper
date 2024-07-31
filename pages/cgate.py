from playwright.sync_api import sync_playwright, Locator, Page
from utils.save_to_file import save_plans_to_txt
from classes.product import InternetPlan

def get_penki_plans(page: Page):
    
    link = "https://www.cgates.lt/internetas/sviesolaidinis-internetas"
    company_name = 'cgate'
    products = page.locator("//div/p/span[contains(text(),'INTERNETAS')]/ancestor::div[@class='vc_column-inner']")
    
    page.goto(link)
    plans: list[InternetPlan] = []
    
    for i in range(products.count()):
        name: str = products.nth(i).locator("//div/p/span[contains(text(),'INTERNETAS')]").first.text_content().strip()
        speed = products.nth(i).locator("//strong").nth(0).text_content()
        speed = speed.replace('iki', '').replace("Mb/s", "Mbps").replace("Gb/s","Gbps").strip()
        
        price = products.nth(i).locator("//strong").nth(2).text_content().replace('€/mėn.', '').strip()
        
        plan = InternetPlan(name=name, speed=speed, price=price, company=company_name)
        plans.append(plan)
    
    save_plans_to_txt(plans)
    return plans