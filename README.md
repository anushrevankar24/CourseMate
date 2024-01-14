# CourseMate - Course Registration System

CourseMate is a web-based course registration system developed using the Django framework. It simplifies the process of course registration for students and facilitates course management for administrators and faculty.

## Watch CourseMate Demo Video

[Video Link](https://drive.google.com/file/d/1sAD3tZ0ymyPJFBUfmHMeEksKjeaCTGm_/view?usp=drive_link) 

## Installation

Follow these steps to set up the project from scratch.

### Technologies used

- Python 3.11.4
- Django - MVC architecture
- SMTP
- HTML/CSS/JavaScript/Bootstrap
- sqlite3 database


## Installation Steps

### Local Setup Instructions
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
 ### Running the Application:     
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
  3. **Start the development server**
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
- Check course details and download schedule
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
-  Accept / Reject student enrollment requests
- View enrollment statistics.


### Enrollment & Validation:

- Students submit course selections.
- System checks prerequisites like CGPA criteria for enrolling a particular course.
- Faculty/admin manage student enrollments.

### Exceptions and edge cases handled:
- Students cannot add the same course to cart more then once
- Students cannot submit same course more then once
- Two courses with same course code cannot be added by faculty/admin


### Notifications & Reminders:

**Automated emails notifications to the students on enrollment and submission updates.**

![CourseMate_notification_1](https://github.com/anushrevankar24/IRIS_Rec23_221AI009_Django/assets/129506519/5c408ee8-e579-4258-bd0e-242aafb65597)
- 
![CourseMate_notification_3](https://github.com/anushrevankar24/IRIS_Rec23_221AI009_Django/assets/129506519/37285c70-612f-48de-b5b4-808170b37f28)
-
![CourseMate_notification_2](https://github.com/anushrevankar24/IRIS_Rec23_221AI009_Django/assets/129506519/221d9f8f-d6c9-43c3-9055-48675032221e)


### Features/Improvements that can be made
- a back button for all the pages
- grades section
- course feedback forms

 ## Problems/Solutions
 **During the development of the CourseMate project, I encountered and successfully addressed two significant challenges:**

 ### Problem No 1: Sending Notification Emails to Users
 The recent modifications in Google's guidelines for Gmail accounts removed the option of access for lesser-known apps, creating issues for developers in providing access to their Gmail accounts for project-related emails. Consequently, the conventional SMTP server for sending emails was no longer feasible. To overcome this hurdle, I implemented the concept of an app password for the Gmail account. By utilizing this app password, third-party servers and applications could successfully log in to the accounts and send emails, resolving the problem effectively.

### Problem No 2: Approve/Reject student enrollment requests options for the faculty
Issue:
Managing and categorizing enrollment requests into approved, rejected, and requested posed a challenge. Additionally, providing options for faculty to approve or reject enrollment requests required a structured solution.

Solution:
I introduced a new model called Enrollment, which stores details of the course and student. The model includes a field called status, which is initially set to 'Request' but can be changed to 'Accepted', 'Rejected', or 'Requested'.
When a student submits a course, the status of the enrollment changes from 'Request' to 'Requested'. If the faculty accepts the student enrollment request, the status changes to 'Accepted'; otherwise, it changes to 'Rejected'


## References

- [Django Documentation](https://docs.djangoproject.com/en/5.0/)
-  https://docs.djangoproject.com/en/4.0/topics/auth/
- [Sending email in Django](https://docs.djangoproject.com/en/5.0/topics/email/)
- https://youtube.com/playlist?list=PLVBKjEIdL9bvCdI4l1Emvbezv10GjUaLk&si=3fw54c4hNZnKNntf
- https://youtube.com/playlist?list=PLjVLYmrlmjGcyt3m6rt21nfjhYSWP_Ue_&si=M_keMoDalE1-4J85

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

## Contact :
 **Email : anushrevenkar07@gmail.com**

Feel free to reach out for any issues or improvements! Happy coding with CourseMate!





