# 💀Phone-Lookup💀

## 📜Description
This script allows users to input a phone number with a country code and get useful details such as:  

Country and region of the number  
Timezone(s) where the number is active  
Carrier (service provider)  
Phone number type (mobile, VoIP, toll-free, etc.)  
International & national formats  
Ideal for security researchers, OSINT enthusiasts, or anyone who wants to verify phone number details.  

## 🔑Features
- ✅ Parses and validates phone numbers  
- ✅ Identifies the country and carrier of the number  
- ✅ Displays timezones and number type (Mobile, VoIP, etc.)  
- ✅ Formats the number in international and national styles  
- ✅ Error handling for incorrect number formats  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  

>sudo apt upgrade  

Step 2: install Dependencies  
>sudo apt install python3-phonenumbers  

Step 3: Clone the repository  
>git clone https://github.com/The-Real-Virus/Phone-Lookup.git  

Step 4: Go to the Tool Directory where u clone it  
>cd Phone-Lookup  

Step 5: After Completing the process now u can run script  
>python3 lookup.py  

## 💡Tips !
🌐 Always enter the phone number with the country code (e.g., +1 for USA, +44 for UK).  
⚡ Ensure you have Python installed and install dependencies using  
📊 This script does not track live locations—it only provides static information from a public database.  

## 🤝Follow the Prompts !
1) Run the script:  
2) Enter the phone number with country code:  
3) View the results:   

## ⚙️Troubleshooting

1) `Issue: ModuleNotFoundError?:`  
- install the requirements (step 2 above).  

2) `Issue: Invalid phone number. Please check the format?:`  
- Ensure the number includes the country code (e.g., +91 for India, +1 for USA).  

3) `Issue: Permission Denied?:`  
- try running with sudo  

4) `Issue: Python3 or pip not found?:`  
- read the requirements.txt file, (cat requirements.txt) or (gedit requirements.txt).  

5) `Issue: No service provider found?:`  
- Some numbers (landlines, VoIP) may not have an assigned carrier.    

## 🛠️MODIFICATION 

IF U WANT TO MODIFY OR USE THE SCRIPT IN UR PROJECTs , CONSIDER GIVING CREDITS !  

## 📂Example OutPut

	📞 Phone Number Details
	========================================
	📌 Entered Number: +14155552671
	📍 Country Code: +1
	🌍 Location: California, United States
	⏰ Timezone(s): America/Los_Angeles
	📡 Service Provider: AT&T Wireless
	📋 Number Type: Mobile
	🔢 International Format: +1 415-555-2671
	🔠 National Format: (415) 555-2671
	🟢 Valid & Possible: Yes
	========================================


# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  
