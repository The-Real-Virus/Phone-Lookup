import phonenumbers
from phonenumbers import timezone, geocoder, carrier, number_type
import os

# Function to display banner
def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  Num-Info
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

# Show banner at script startup
show_banner()

# Ask user for input
choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()

if choice == 'n':
    print("\nExiting the script. Goodbye!")
    exit()
elif choice == 'y':
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen on Linux/Mac ('clear') or Windows ('cls')
else:
    print("\nInvalid choice. Exiting the script.")
    exit()

def logo():
    logo = r"""

███╗   ██╗██╗   ██╗███╗   ███╗      ██╗███╗   ██╗███████╗ ██████╗ 
████╗  ██║██║   ██║████╗ ████║      ██║████╗  ██║██╔════╝██╔═══██╗
██╔██╗ ██║██║   ██║██╔████╔██║█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██║██║ ╚████║██║     ╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                                                                                   
"""
    print(logo)

def get_phone_details(number):
    try:
        # Parsing the phone number
        phone_number = phonenumbers.parse(number)

        # Validate if the number is real and possible
        if not phonenumbers.is_valid_number(phone_number):
            print("❌ Invalid phone number. Please check the format.")
            return
        
        # Get details
        time_zones = timezone.time_zones_for_number(phone_number)
        location = geocoder.description_for_number(phone_number, "en")
        service_provider = carrier.name_for_number(phone_number, "en")
        phone_type = number_type(phone_number)  # Get phone type
        country_code = phone_number.country_code
        formatted_international = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_national = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        possible = phonenumbers.is_possible_number(phone_number)

        # Determine type of phone number
        phone_type_dict = {
            phonenumbers.PhoneNumberType.MOBILE: "Mobile",
            phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Toll-Free",
            phonenumbers.PhoneNumberType.UNKNOWN: "Unknown"
        }
        phone_type_str = phone_type_dict.get(phone_type, "Unknown")

        # Display results
        print("\n📞 Phone Number Details")
        print("=" * 40)
        print(f"📌 Entered Number: {number}")
        print(f"📍 Country Code: +{country_code}")
        print(f"🌍 Location: {location}")
        print(f"⏰ Timezone(s): {', '.join(time_zones)}")
        print(f"📡 Service Provider: {service_provider}")
        print(f"📋 Number Type: {phone_type_str}")
        print(f"🔢 International Format: {formatted_international}")
        print(f"🔠 National Format: {formatted_national}")
        print(f"🟢 Valid & Possible: {'Yes' if possible else 'No'}")
        print("=" * 40)

    except phonenumbers.phonenumberutil.NumberParseException:
        print("❌ Error: Invalid phone number format.")

if __name__ == "__main__":
    logo()
    number = input("Enter the phone number with country code: ")
    get_phone_details(number)
