from frontend import print_menu,project_menu
from authentication import register_login as l
from projects_operations import *

def run():
    while True:
        opt = print_menu()
        if opt ==1:
            l.User_registiration()
        elif opt ==2:
            useremail=l.userLogin()
            if useremail:
                projopt = project_menu()
                if projopt ==1:
                    create_project(useremail)
                elif projopt==2:
                    viewAllProjects()
                elif projopt==3:
                    delete_project(useremail)
                elif projopt==4:
                    break
            
        else:
            print("👋 See You Later......")
            break


if __name__=='__main__':
    run()