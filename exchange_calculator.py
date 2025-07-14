budget = 127.5
exchange_rate = 1.2
spread = 10
denomination = 20 # face value of a single bill or banknote

# spread in every euro you get
real_rate = exchange_rate * (1 + spread / 100)

# how much euros you get with US$ 1
conversion = 1 / real_rate

# how many euros you get with your budget
euros_total = budget * conversion

# total amount of euros received after rounding down to the nearest bill denomination
bills_count = int(euros_total / denomination)
euros_received = bills_count * denomination