from classes.product import InternetPlan

def save_plans_to_txt(plans: list[InternetPlan], filename="plans.txt"):
    with open(filename, 'a', encoding='utf-8') as file: 
        if file.tell() == 0:
            file.write(f"{'Name':<50} {'Speed':<20} {'Price':<10} {'Company':<10}\n")
            file.write("="*90 + "\n")
        for plan in plans:
            file.write(f"{plan.name:<50} {plan.speed:<20} {plan.price:<10} {plan.company:<10}\n")