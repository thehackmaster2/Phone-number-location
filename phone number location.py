import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Input phone number
mobileNo = input("Enter phone number")
mobileNo = phonenumbers.parse(mobileNo)  # Parse without a default region

# Get time zones for the number
print("Time zones for number:", timezone.time_zones_for_number(mobileNo))

# Get carrier/provider for the number
print("Carrier/Provider:", carrier.name_for_number(mobileNo, "en"))

# Get geographical location for the number
print("Geographical location:", geocoder.description_for_number(mobileNo, "en"))

# Validate the phone number
print("Valid Mobile Number:", phonenumbers.is_valid_number(mobileNo))

# Check the possibility of the number
print("Checking possibility of number:", phonenumbers.is_possible_number(mobileNo))