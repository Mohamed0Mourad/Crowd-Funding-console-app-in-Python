import json
from datetime import datetime


projectsFile = 'projects.json'
#load any projects from json file if found, if not create empty one with{}
def Load_all_projects():
    try:
        with open(projectsFile,'r') as pf:
            data=json.load(pf)
            return data if isinstance(data,dict)else{}
    except (FileNotFoundError,json.JSONDecodeError):
        return {}

###########
def Saveprojects(projects):
    with open(projectsFile,'w') as pf:
        json.dump(projects,pf,indent=4)
        
###########
def create_project(usermail):
    allProjects = Load_all_projects()
    
    print("\n🛠️ **Create a New Project** 🛠️")
    print("=" * 40)
    
    #title
    title = input("📌 Enter Project Title: ").strip()
    if not title:
        print("❌ Title cannot be empty!")
        return
    
    #details
    details = input("📝 Enter Project Details: ").strip()
    if not details:
        print("❌ Details cannot be empty!")
        return
    
    #target
    target = input("💰 Enter Project Target (EGP): ").strip()
    if not target.isdigit() or int(target) <= 0:
        print("❌ Invalid target amount! Please enter a positive number.")
        return
    
    #date
    try:
        start_date = input("📅 Enter Start Date (YYYY-MM-DD): ").strip()
        end_date = input("📅 Enter End Date (YYYY-MM-DD): ").strip()
        
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    
        if start >= end:
            print("❌ Invalid date range! Start date must be before the end date.")
            return
    except ValueError:
        print("❌ Invalid date format! Please use YYYY-MM-DD.")
        return
    
    project_id = len(allProjects) + 1 if isinstance(allProjects, dict) else 1
    
    # Add the project to the dictionary
    allProjects[str(project_id)]={
        "owner":usermail,
        "title":title,
        "details":details,
        "target":int(target),
        "start_date":start_date,
        "end_date":end_date
        
    }
    Saveprojects(allProjects)
    print("✅ Project is created successfully....")
    print("=" * 40)
    
###########
def viewAllProjects():
    allProjects = Load_all_projects()
    
    if not allProjects:
        print("\n❌ There is no projects to show!!!")
        return
    print("\n📚-------All Projects-------📚")
    print(f"{'ID':<5} {'Title':<20} {'Target (EGP)':<15} {'Details':<35}{'Start Date':<12} {'End Date':<12} {'Owner':<20}")
    print("-" * 130)
    
    for project_id, project in allProjects.items():
        print(f"{project_id:<5} {project['title']:<20} {project['details']:<35}{project['target']:<15} {project['start_date']:<12} {project['end_date']:<12} {project['owner']:<20}")
    
    print("-" * 130)
    print("✅ End of Projects List")
    

####################
def delete_project(useremail):
    allProjects = Load_all_projects()
    if not allProjects:
        print("\n❌ No Projects available to delete!!!!!!")
        return
    print("\n📚 -----------Your Projects---------- 📚")
    user_projects = {k:v for k,v in allProjects.items() if v["owner"]==useremail}
    
    if not user_projects:
        print("⚠️ You have no permission to delete this project!!!")
        return
    
    #show him projects he owns
    print(f"{'ID':<5} {'Title':<20} {'Target (EGP)':<15} {'Start Date':<12} {'End Date':<12}")
    print("-" * 70)
    
    for project_id, project in user_projects.items():
        print(f"{project_id:<5}.{project['title']:<20} - {project['details']}{project['target']:<15} {project['start_date']:<12} {project['end_date']:<12}")
    print("-" * 70)
    
    #select pid
    project_id = input("Enter the project id you want to delete: ").strip()
    
    if project_id in user_projects:
        confirmation = input(f"⚠️ Are you sure you want to delete the project '{user_projects[project_id]['title']}'? (yes/no): ").strip().lower()
        if confirmation=='yes':
            del allProjects[project_id]
            Saveprojects(allProjects)
            print(f"\n✅ Project ID {project_id} ({user_projects[project_id]['title']}) has been successfully deleted.")
        else:
            print("\n❌ Deletion cancelled.")
    else:
        print("\n❌Invalid project id or you don't own this project")