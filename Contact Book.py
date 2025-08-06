
contacts = {
    "Ali" : "01258684266",
    "Ahmed" : "01259425226",
    "Amir" : "01567532842"
}
print("Contact names in the contact book:")
for name in contacts:
    print(name)
Name = input("\nEnter a name to search for: ")
if Name in contacts :
    print(f"{Name}'s phone number is: {contacts[Name]}")
else :
    print(f"No contact found with the name '{Name}'.")