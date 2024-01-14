# CourseMate - Course Registration System

CourseMate is a web-based course registration system developed using the Django framework. It simplifies the process of course registration for students and facilitates course management for administrators and faculty.

## Watch CourseMate Demo Video

[Video Link](https://drive.google.com/file/d/1SXEztR2rfXsj0CFK44OlWZoXUXs6pazI/view?usp=drive_link) 

## Installation

Follow these steps to set up the project from scratch.

### Prerequisites

- Python 3.11.4
- Django


### Installation Steps

## Local Setup Instructions
1. **Clone this repository**.

2. **Environment Setup:**
   - Ensure Python is installed on your system.
   - Create a virtual environment using:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - For Windows:
       ```
       venv\Scripts\activate
       ```
     - For macOS/Linux:
       ```
       source venv/bin/activate
       ```
3. **Navigate to the project directory**
     ```bash
     cd CourseMate
     ```
     


4. ** Install required packages using the provided requirements.txt file:**
     ```
     pip install -r requirements.txt
     ```
 ## Running the Application:     
  1. **Perform database migrations**
      ```
      python manage.py makemigrations
      ```
      ```
       python manage.py migrate
      ```
 2. **Create a superuser**  
   ```
     python manage.py createsuperuser  
   ``` 
3.**Start the development server**
  ```
   python manage.py runserver
  ```
Open the application in your web browser: http://127.0.0.1:8000/  

To access the admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials created during installation.  

Note: Ensure that all the prerequisites are installed and the virtual environment (if used) is activated before running the project.   


# Features

### Student Functions:
- Sign Up / Login
- Log in and view available courses based on the program/major.
- Search for courses by code, title, or department.
- Check course schedules.
- Add courses to the course cart.
- Remove courses from cart.
- Submit enrollment request for the courses in the course cart to the instructors  .
- View their submission status

### Faculty Functions:
- Faculty/Admin can add new courses.
- Set available slots for each course.
- Specify prerequisites and additional course details.
- Access courses they're teaching.
- Accept / Reject student enrollment requests
- View enrolled students.
- Modify course details.


### Admin Functions:
- View all courses, student enrollments, and available slots.
- Add/Remove courses.
- View enrollment statistics.

### Enrollment & Validation:

- Students submit course selections.
- System checks prerequisites.
- Instructors manage student enrollments.

### Notifications & Reminders:

- Automated emails notifications to the students on enrollment and submission updates.


## Contributing

We welcome contributions from the community to enhance the CourseMate project. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-contribution`).
3. Make your changes and ensure the code follows the project's coding conventions.
4. Test your changes thoroughly.
5. Commit your changes (`git commit -am 'Add some feature'`).
6. Push to the branch (`git push origin feature/awesome-contribution`).
7. Create a new Pull Request.

Please ensure your Pull Request description clearly describes the changes made and any associated issues.


## Known Bugs

- [Bug 1]
- [Bug 2]

## References

- Django Documentation
- [Any other references used]

## Screenshots

- [Include relevant screenshots if available]

Feel free to reach out for any issues or improvements! Happy coding with CourseMate!





