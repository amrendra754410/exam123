amount = int(input("Enter the amount: "))

hundred_notes = amount // 100
remaining = amount % 100

fifty_notes = remaining // 50
remaining = remaining % 50

ten_notes = remaining // 10
remaining = remaining % 10

print("100 Rs notes:", hundred_notes)
print("50 Rs notes:", fifty_notes)
print("10 Rs notes:", ten_notes)

if remaining > 0:
    print("Remaining amount:", remaining, "(cannot be dispensed)")


