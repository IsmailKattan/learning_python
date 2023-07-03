email = input("enter your email ").strip().lower()

print(f"Your Name Is {email[:email.index('@')].capitalize()}")
print(f"Email Service Provider Is {email[email.index('@')+1:email.index('.')]}")
print(f"Top Level Domain Is {email[email.index('.')+1:]}")


# Inputs

"Osama@Nn.Sa" # Email

# Needed Output

"Your Name Is Osama"
"Email Service Provider Is nn"
"Top Level Domain Is sa"