import csv

header = ['customer_name', 'program_end_date']
data = [
    ['nationwide', '31.12.2023'],
    ['evergy', '31.12.2025']
]


with open('customers.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)