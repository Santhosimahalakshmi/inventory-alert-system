import csv
from datetime import datetime

body = f"""Subject:  Restock Alert

Hello Team,

Items requiring attention:

"""

critical_count = 0
low_count = 0

with open('stock.csv', 'r') as file:
    data = csv.DictReader(file)

    for row in data:
        name = row['item_name'].strip()
        qty = int(row['quantity'])
        th = int(row['threshold'])

        print("DEBUG:", name, qty, th)  

        if qty < th:
            if qty < 0.25 * th:
                status = "CRITICAL"
                critical_count += 1
            else:
                status = "LOW"
                low_count += 1

            print("ADDING:", name)  
            body += f"- {name} (Qty: {qty}) → {status}\n"

if critical_count == 0 and low_count == 0:
    body += "All items are sufficiently stocked.\n"

body += f"""

Summary:
Critical items: {critical_count}
Low stock items: {low_count}
"""

print("\n\nFINAL OUTPUT:\n")
print(body)