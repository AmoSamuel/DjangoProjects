# Import module 
import sqlite3


# Task 1: Create connection object
 con = sqlite3.connect("hotel_booking.db")

# Task 2: Create cursor object

cur = con.cursor()
# Task 3: View first row of booking_summary

print(cur.execute('''SELECT * FROM booking_summary''').fetchone())
# Task 4: View first ten rows of booking_summary 
print(cur.execute('''SELECT * FROM booking_summary''').fetchmany(10))

# Task 5: Create object bra and print first 5 rows to view data

('''SELECT * FROM booking_summary WHERE country = 'BRA';''')
# Task 6: Create new table called bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
                   num INTEGER,
                   hotel TEXT,
                   is_cancelled INTEGER,
                   lead_time INTEGER,
                   arrival_date_year INTEGER,
                   arrival_date_month,
                   arrival_date_day_of_month INTEGER,
                   adults INTEGER,
                   children INTEGER,
                   country TEXT,
                   adr REAL,
                   special_requests INTEGER)''')

# Task 7: Insert the object bra into the table bra_customers 
'''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# Task 8: View the first 10 rows of bra_customers
print(cur.execute('''SELECT * FROM bra_customers''').fetchmany(10))

# Task 9: Retrieve lead_time rows where the bookings were canceled
'''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;'''

# Task 10: Find average lead time for those who canceled and print results
sum = 0
for num in lead_time_can:  
  sum = sum + num[0]

# Task 13: Retrieve special_requests rows where the bookings were canceled
cur.execute('''SELECT special_requests FROM bra_customers WHERE is_canceled = 1;''').fetchall()

