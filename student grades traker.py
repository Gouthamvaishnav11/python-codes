def display_menu():
  print("---------STUDENTS GRADES TRACKER------------ ")
  print("1. Add Course and Grade")
  print("2. Edit Course Grade")
  print("3. Remove Course and Grade")
  print("4. View All Courses and Grades")
  print("5. Exit")

def add_course_grade(courses, grades):
  course = input("Enter course name: ")
  grade = float(input("Enter grade for {}: ".format(course)))
  courses.append(course)
  grades[course] = grade
  print("Course '{}' with grade '{}' added successfully.".format(course, grade))

def edit_course_grade(grades):
  course = input("Enter the name of the course you want to edit: ")
  if course in grades:
      new_grade = float(input("Enter new grade for {}: ".format(course)))
      grades[course] = new_grade
      print("Grade for course '{}' updated successfully.".format(course))
  else:
      print("Course '{}' not found.".format(course))

def remove_course_grade(courses, grades):
  course = input("Enter the name of the course you want to remove: ")
  if course in courses:
      courses.remove(course)
      del grades[course]
      print("Course '{}' removed successfully.".format(course)) 
  else:
      print("Course '{}' not found.".format(course))

def view_all_courses_grades(grades):
  if not grades:
      print("No courses and grades added yet.")
  else:
      print("All Courses and Grades:")
      for course, grade in grades.items():
          print("Course: {}, Grade: {}".format(course, grade))

def main():
  courses = []
  grades = {}

  while True:
      display_menu()
      choice = input("Enter your choice: ")

      if choice == '1':
          add_course_grade(courses, grades)
      elif choice == '2':
          edit_course_grade(grades)
      elif choice == '3':
          remove_course_grade(courses, grades)
      elif choice == '4':
          view_all_courses_grades(grades)
      elif choice == '5':
          print("Exiting program.")
          break
      else:
          print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
  main()
