budget = 127.5
exchange_rate = 1.2
spread = 10
denomination = 20  # face value of bills available at exchange booth

# Calculate real exchange rate including spread fee
real_rate = exchange_rate * (1 + spread / 100)
conversion = 1 / real_rate

# Display exchange rates
print(f"Exchange rate: US$ {real_rate:.2f} per euro")
print(f"US$ 1 = EUR {conversion:.2f}")

# Calculate euros received and bills dispensed
euros_total = budget * conversion
bills_count = int(euros_total / denomination)
euros_received = bills_count * denomination

print(f"Total euros: EUR {euros_total:.2f}")
print(f"Bills received: {bills_count} x EUR {denomination} = EUR {euros_received}")