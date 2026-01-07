class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    location_offices = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def location(self):
        print("Our offices are offices are located in", self.location_offices)


# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()

class OOPCourse(Course):

    description = ""
    trainer = ""

    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"This course is about {self.description} and the name of the trainer is {self.trainer}")

    id_number = "#12345"

    def show_course_id(self):
        print("The ID number of the course is: ", self.id_number)

course_1 = OOPCourse()

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

print(course_1)