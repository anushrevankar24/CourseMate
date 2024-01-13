# CourseMate - Course Registration System

CourseMate is a web-based course registration system developed using the Django framework. It simplifies the process of course registration for students and facilitates course management for administrators and faculty.

## Demo Video

[Watch CourseMate Demo Video](#) 

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
     


4. **Install Dependencies:**

   - Install required packages using the provided requirements.txt file:
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








