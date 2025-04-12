UniFace - University Event & News Portal

UniFace is a centralized Django-based portal that allows all departments of a university to manage and publish their upcoming events and news. Students can follow departments, RSVP to events, and participate in polls and surveys — all from a single platform.


---

Features

For Departments

Department Management

Each department has its own dashboard.

Departments can create and manage their own events and news posts.


Event Management

Add upcoming events with details like date, time, venue, and description.

Enable RSVP for events to track interested attendees.


News Publishing

Post latest announcements and categorized news updates.


Polls & Surveys

Create polls and surveys to engage students.

View live results and statistics.




---

For Students

Follow/Unfollow Departments

Students can follow specific departments to receive updates relevant to them.


Event RSVP System

RSVP to events with a single click.

View list of events you’ve RSVP’d to.


View Departmental News & Events Feed

Personalized dashboard showing content only from followed departments.


Participate in Polls/Surveys

Vote in department-specific polls or fill out surveys.




---

Tech Stack

Backend: Django

Frontend: Django Templates with Bootstrap

Database: SQLite (for development)

Authentication: Django’s built-in authentication system



---

Getting Started

1. Clone the Repository

git clone https://github.com/your-username/uniface.git
cd uniface


2. Install Dependencies

pip install -r requirements.txt


3. Apply Migrations

python manage.py makemigrations
python manage.py migrate


4. Create Superuser

python manage.py createsuperuser


5. Run the Server

python manage.py runserver


6. Access the Portal

Visit http://localhost:8000/ to view the portal.

Visit http://localhost:8000/admin/ for the admin dashboard.





---



Contributing

Contributions are welcome! Please fork the repository and open a pull request with your changes.


