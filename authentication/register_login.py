
from validations import phoneNumberValidation,load_users,save_users,emailvalidate
"""
function for user registeration:
    if user found ----> told him that he already registered
    if not ---> register him
"""
def User_registiration():
    registeredUsers = load_users()
    if not isinstance(registeredUsers, dict):
        print("\n❌ Error: User data is not in the correct format. Resetting to an empty dictionary.")
        registeredUsers = {}
        
    print("\n📝 **User Registration** 📝")
    print("=" * 35)    
    #Email validate
    userEmail = input("📧 Enter your email: ").strip()
    if not emailvalidate(userEmail):
        print("❌ Invalid email format. Please try again with a valid email!")
        return

    if userEmail in registeredUsers:
        print("⚠️ Email already exists. Please login instead!")
        return
    
    fname = input("👤 Enter your first name: ").strip()
    lname = input("👤 Enter your last name: ").strip()
    if not fname or not lname:
        print("❌ First and Last names cannot be empty!")
        return
    
    
    #phone number and it's validation
    phoneNumber = input("📱 Enter your mobile phone: ").strip()
    if not phoneNumberValidation(phoneNumber):
        print("❌ Invalid Egyptian phone number! Please use a valid format (e.g., 01012345678).")
        return
    
    
    #password and it's confirmation
    passwd = input("🔑 Enter your password: ").strip()
    passwdConfirmation = input("🔑 Confirm your password: ").strip()
    if passwd != passwdConfirmation:
        print("❌ Passwords do not match. Please try again!")
        return
    
    registeredUsers[userEmail]={
        "First_Name":fname,
        "Last_Name":lname,
        "Phone Number":phoneNumber,
        "Password":passwd
    }
    
    save_users(registeredUsers)
    print("\n✅ Registration Completed Successfully!")
    print("=" * 35)
    
    
    
#user login
def userLogin():
    registerdusers = load_users()
    
    print("\n🔑 **User Login** 🔑")
    print("=" * 35)
    
    userEmail = input("📧 Enter your email: ").strip()
    passwd = input("🔑 Enter your password: ").strip()
    
    #check email and passwd for the user
    if userEmail in registerdusers and registerdusers[userEmail]["Password"] == passwd:
        print(f"\n✅ Welcome, {registerdusers[userEmail]['First_Name']} {registerdusers[userEmail]['Last_Name']}!")
        print("=" * 35)
        return userEmail
    else:
        print("❌ Invalid email or password. Please try again!")
        return None