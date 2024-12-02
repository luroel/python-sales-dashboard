import csv # Read and write CSV files
import random # Generate random data
from faker import Faker # Library to generate fake data (names, adress, date, etc)
from datetime import datetime # To work with date and time

# Initializacing vars 
fake = Faker()

#Random data for CSV file Instance
data = []
# Gerate a random number in between A,B
rows = random.randint(10000, 15000)

for _ in range(rows):
    # Int value between min=A, max=B
    invoice_id = fake.random_int(min=10000, max=15000)
    start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2024-12-31', '%Y-%m-%d')
    purchase_date = fake.date_between(start_date=start_date, end_date=end_date)
    time = fake.time(pattern='%H:%M')
    while not(time >= '09:00' and time <= '21:00'):
        time = fake.time(pattern='%H:%M')
    gender = random.choice(['Male', 'Female'])
    invoice_amount = round(random.uniform(10, 1000), 2)
    payment_method = random.choice(['Credit Card', 'Cash', 'PayPal'])
    city = random.choice(['Guanajuato', 'León', 'Moroleón', 'Morelia', 'Monterrey'])
    
    data.append([invoice_id, purchase_date, time, gender, city, payment_method, invoice_amount])
    
# Write data in CSV
filename = 'data_2024.csv'
with open(filename, 'w', newline= '') as file:
    write = csv.writer(file)
    write.writerow(['Invoice ID', 'Purchase Date', 'Time', 'Gender', 'City', 'Payment Method', 'Invoice Amount'])
    write.writerows(data)

print(f"Archivo CSV '{filename} creado exitosamente.")
    