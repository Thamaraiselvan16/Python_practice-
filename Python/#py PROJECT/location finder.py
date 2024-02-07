import phonenumbers
from phonenumbers import geocoder

phone_num1 = phonenumbers.parse("+919952206342")
phone_num2 = phonenumbers.parse("+917538844612")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_num1, "en"))
print(geocoder.description_for_number(phone_num2, "en"))
