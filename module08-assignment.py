# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "AI Specialist": 200,
    "Customer Service": 120,
    "Marketing": 190
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "Rocket Money",
    "contact_person": "Tyler Johnson",
    "email": "tylerj@gmail.com",
    "phone": "738-846-9876"
}

customer2 = {
    "company_name": "Microsoft",
    "contact_person": "Johnson Jackson",
    "email": "johnj@yahoo.com",
    "phone": "647-948-5637"
}

customer3 = {
    "company_name": "Apple",
    "contact_person": "Sara Popper",
    "email": "spopper@gmail.com",
    "phone": "836-989-0987"
}

customer4 = {
    "company_name": "NVIDIA",
    "contact_person": "Smith Rocket",
    "email": "srocket@gmail.com",
    "phone": "234-843-7694"
}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {"C001": customer1, "C002": customer2, "C003": customer3, "C004": customer4}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for customer_id, customer in customers.items():
    print(f"Customer ID: {customer_id}")
    for key, value in customer.items():
        print(f"{key}: {value}")

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
c002_info = customers["C002"]
print("C002 Information:", c002_info)

c003_contact = customers["C003"]["contact_person"]
print("C003 Contact Person:", c003_contact)

c999_info = customers.get("C999", "Customer not found")
print("C999 Information:", c999_info)


# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
customers["C001"]["phone"] = "123-456-7890"
customers["C002"]["industry"] = "Engineering"

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])


# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here
project1 = {"name": "Website Redesign", "service": "Marketing", "hours": 120, "budget": 18000}
project2 = {"name": "Security Audit", "service": "AI Specialist", "hours": 40, "budget": 9000}
project3 = {"name": "Data Dashboard", "service": "Data Analysis", "hours": 60, "budget": 10500}
project4 = {"name": "Cloud Migration", "service": "Web Development", "hours": 80, "budget": 16000}
project5 = {"name": "System Maintenance", "service": "Customer Service", "hours": 30, "budget": 2700}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

for customer_id, project_list in projects.items():
    print("Customer:", customer_id)
    for project in project_list:
        print(project)
    print()
# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    for project in project_list:
        
        service_type = project["service"]
        hours = project["hours"]
        
        hourly_rate = services[service_type]
        cost = hourly_rate * hours
        
        print("Customer:", customer_id)
        print("Project:", project["name"])
        print("Service:", service_type)
        print("Hours:", hours)
        print("Cost:", cost)
        print()

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print("Customer IDs:", list(customers.keys()))
print("\nCustomer Companies:")
for customer in customers.values():
    print(customer["company_name"])

total_customers = len(customers)
print("\nTotal Customers:", total_customers)
# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
service_counts = {}

for project_list in projects.values():
    for project in project_list:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("Service Usage Counts:")
for service, count in service_counts.items():
    print(service, ":", count)
# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
total_hours = 0
total_budget = 0
budgets = []

for project_list in projects.values():
    for project in project_list:
        total_hours += project["hours"]
        total_budget += project["budget"]
        budgets.append(project["budget"])

avg_budget = total_budget / len(budgets)

max_budget = max(budgets)
min_budget = min(budgets)

print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Highest Budget:", max_budget)
print("Lowest Budget:", min_budget)

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for customer_id, customer in customers.items():

    project_list = projects.get(customer_id, [])

    num_projects = len(project_list)

    total_hours = sum(project["hours"] for project in project_list)
    total_budget = sum(project["budget"] for project in project_list)

    print("Customer:", customer["company_name"])
    print("Projects:", num_projects)
    print("Total Hours:", total_hours)
    print("Total Budget:", total_budget)
    print("-" * 30)

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("Adjusted Rates:")
for service, rate in adjusted_rates.items():
    print(service, ":", rate)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
active_customers = {cid: customers[cid] for cid in projects if len(projects[cid]) > 0}

for cid, customer in active_customers.items():
    print(cid, ":", customer["company_name"])

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
customer_budgets = {
    cid: sum(project["budget"] for project in project_list)
    for cid, project_list in projects.items()
}

print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}

for service, tier in service_tiers.items():
    print(service, ":", tier)

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
def validate_customer(customer_dict):

    required_fields = ["company_name", "contact_person", "email", "phone"]

    for field in required_fields:
        if field not in customer_dict:
            return False

    return True


for cid, customer in customers.items():
    print(cid, "Valid:", validate_customer(customer))

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
status_counts = {"active": 0, "completed": 0, "pending": 0}

statuses = ["active", "completed", "pending"]
i = 0

for project_list in projects.values():
    for project in project_list:

        status = statuses[i % 3]
        project["status"] = status

        status_counts[status] += 1
        i += 1

print("Project Status Counts:")
print(status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
def analyze_customer_budgets(projects_dict):

    results = {}

    for cid, project_list in projects_dict.items():

        total = sum(project["budget"] for project in project_list)
        count = len(project_list)

        average = total / count if count > 0 else 0

        results[cid] = {
            "total": total,
            "average": average,
            "count": count
        }

    return results


budget_analysis = analyze_customer_budgets(projects)

print(budget_analysis)

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
def recommend_services(customer_id, customers, projects, services):

    used_services = []

    for project in projects.get(customer_id, []):
        used_services.append(project["service"])

    recommendations = []

    for service in services:
        if service not in used_services:
            recommendations.append(service)

    return recommendations


for cid in customers:
    rec = recommend_services(cid, customers, projects, services)
    print("Customer", cid, "recommended services:", rec)