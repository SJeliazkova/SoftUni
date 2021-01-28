data = input()

company_users = {}

while not data == "End":
    company, empl_id = data.split(" -> ")

    if company not in company_users:
        company_users[company] = []
    if empl_id not in company_users[company]:
        company_users[company].append(empl_id)

    data = input()

company_users = dict(sorted(company_users.items(), key=lambda x: x[0]))

for company, empl_id in company_users.items():
    print(company)

    for e_id in empl_id:
        print(f"-- {e_id}")