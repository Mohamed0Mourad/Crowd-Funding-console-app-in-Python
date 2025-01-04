
from validations import *
#Main menu
def print_menu():
    print("\n🛠️ **Main Menu** 🛠️")
    print("=" * 30)
    options = [
        '1) 📝 User Register',
        '2) 🔑 User Login',
        '3) 🚪 Exit Program'
    ]
    
    for option in options:
            print(option)
    print("=" * 35)
    
    optionselected = f'👉 Enter Your Choice (From 1 to {len(options)}:): '
    return input_validation(optionselected,1,len(options))

def project_menu():
    while True:
        print("\n📊 **Project Menu** 📊")
        print("=" * 35)
        options = [
            '1) 🛠️ Create Project',
            '2) 📚 View Projects',
            '3) 🗑️ Delete Project',
            '4) 🚪 Exit to Main Menu'
        ]
        
        for option in options:
            print(option)
        
        print("=" * 35)
        
        optionselected = f'👉 Enter Your Choice (From 1 to {len(options)}:): '
        return input_validation(optionselected,1,len(options))
        