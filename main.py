from bs4 import BeautifulSoup
import requests
import calc

grade_list = []
class_list = []

#Asks for the StudentID number, and LogIn details

Username = input("Username/Email: ")
Password = input("Password: ")
StudentID_Num = input("What is your student ID number?(ex: 162527): ")

#The auth url and the url you want to go to

login_url = ('https://parents.sparta.org/sparta/sis/j_security_check')
secure_url = ('https://parents.sparta.org/sparta/parents?tab1=studentdata&tab2=gradebook&tab3=weeklysummary&action=form&studentid=' + StudentID_Num)

#Where you have the username and password for the user you want the data extracted from

payload = {
    'j_username': Username,
    'j_password': Password
}

#Sends the user and pass through the websites post and sends us the authorized url in return

with requests.session() as s:
    s.post(login_url, data=payload)
    r = s.get(secure_url)
    soup = BeautifulSoup(r.content, 'html.parser')

#Gets the "Table where all the grades, classes, and teachers are located"

table = soup.find('table', class_='list')
rows = table.find_all('tr')

#Shifts through every line that has the "grade cell" and "class cell"
#Gets value and adds it to the Grades and Classes List

for row in rows:
    gradecell = row.find_all('td', class_='cellRight', style=lambda value: value and 'cursor:pointer;' in value)
    classcell = row.find_all('td', class_='cellLeft')

    for grades in gradecell:
        grade = grades.find(width=lambda value: value and '70%' in value)

        if grade == None:
            grade_list.append("No Grade")
            continue
        else:
            grade_list.append(grade.get_text().strip())

    for classes in classcell:
        class_list.append(classes.get_text().strip())

classes = class_list[::2]
classes_final = classes[1::]
grades_final = grade_list

#Use grades_final and classes_final
#Type: Grades_Final = String List; Classes_Final = String List;

print(calc.AverageGrade(grades_final))
print(calc.Grade_Class_Organizer(grades_final, classes_final))