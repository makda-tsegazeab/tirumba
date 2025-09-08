Tirumba
 
Tirumba (ጥሩምባ, Tigrinya and Amharic for "trumpet") is a Django-based API that modernizes funeral announcements in Tigray, Ethiopia. Inspired by the traditional practice of announcing funerals via bicycle and microphone, Tirumba delivers timely, reliable notifications through SMS, robocalls, and Telegram, ensuring communities stay connected during times of loss. Built with scalability and cultural sensitivity in mind, it supports Tigrinya as the default language and targets specific kebeles (local areas).
Features

Create Announcements: Admins can submit funeral details (name, venue, date, audio) via a RESTful API.
Approval Workflow: Two-step verification ensures only trusted announcements are sent.
Multi-Channel Dispatch: Supports SMS, robocalls, and Telegram for broad reach.
Recipient Management: Stores phone numbers by kebele for targeted notifications.
Scalable Storage: Uses MinIO for audio/photo uploads, ensuring reliability.
Async Processing: Celery and Redis handle background tasks like sending messages.

Motivation
In Tigray, funeral announcements are a vital community tradition, often limited by manual methods like loudspeakers. Tirumba digitalizes this process, making it more efficient, inclusive, and respectful of cultural practices. As a developer from Ethiopia, I aim to leverage technology to strengthen community bonds, drawing from my experience building impactful solutions at YBS Software Development.
Installation
Prerequisites

Python 3.10+
PostgreSQL
Redis
MinIO
Git

Setup

Clone the Repository:
git clone https://github.com/yourusername/tirumba.git
cd tirumba


Set Up Virtual Environment:
python -m venv env
env\Scripts\activate  # Windows


Install Dependencies:
pip install -r requirements.txt


Configure Environment Variables:Create a .env file in the project root:
DJANGO_SECRET_KEY=your-secret-key
DB_NAME=tirumba_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_USE_HTTPS=False
MINIO_MEDIA_BUCKET_NAME=tirumba-media


Set Up PostgreSQL:

Create a database: createdb tirumba_db (use pgAdmin or CLI).
Run migrations:python manage.py makemigrations
python manage.py migrate




Start Redis and MinIO:

Redis: redis-server (ensure installed).
MinIO: minio.exe server C:\minio-data.


Run the Server:
python manage.py runserver


Run Celery Worker:
celery -A tirumba worker -l info --pool=solo



API Endpoints

POST /api/auth/register/: Register a user (phone_number, email, password, confirm_password).
POST /api/login/: Obtain authentication token.
POST /api/announcements/: Create a funeral announcement.
POST /api/announcements/{id}/approve/: Approve an announcement.
POST /api/announcements/{id}/dispatch/: Queue dispatch to channels (e.g., Telegram).

Technologies

Backend: Django, Django REST Framework
Database: PostgreSQL
Storage: MinIO
Task Queue: Celery, Redis
Authentication: Token-based (DRF)

Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit changes: git commit -m "Add feature".
Push: git push origin feature-name.
Open a pull request.

Contact
For questions or collaboration, reach out via GitHub Issues or email (makdatsegazeab93@gmail.com).

Built with passion to empower communities through technology.