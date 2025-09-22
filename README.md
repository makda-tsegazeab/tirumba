Tirumba 🚀
    
Tirumba (ጥሩምባ, Tigrinya and Amharic for "trumpet") is a Django-based RESTful API that modernizes funeral announcements in Tigray, Ethiopia. Drawing inspiration from the traditional practice of announcing funerals via bicycle and microphone, Tirumba delivers timely, reliable notifications through SMS, robocalls, and Telegram. Designed with scalability, reliability, and cultural sensitivity, it uses Tigrinya as the default language and targets specific kebeles (local areas) to ensure communities stay connected during times of loss.
✨ Features

Create Announcements: Admins submit funeral details (name, venue, date, audio) via a secure API.
Approval Workflow: Two-step verification ensures only trusted announcements are dispatched.
Multi-Channel Delivery: Supports SMS, robocalls, and Telegram for maximum reach.
Recipient Management: Stores phone numbers by kebele for targeted notifications.
Scalable Storage: Uses MinIO for reliable audio and photo uploads.
Asynchronous Processing: Celery and Redis handle background tasks like message dispatching.

💡 Motivation
In Tigray, funeral announcements are a cornerstone of community life, traditionally shared through loudspeakers or word-of-mouth. These methods can be slow and limited in reach. Tirumba digitalizes this process, making it efficient, inclusive, and respectful of cultural practices. As an Ethiopian developer with experience at YBS Software Development, I built Tirumba to leverage technology for community empowerment, ensuring timely and respectful communication.
🛠️ Technologies



Category
Tools



Backend
Django, Django REST Framework


Database
PostgreSQL


Storage
MinIO


Task Queue
Celery, Redis


Authentication
Token-based (DRF)


📦 Installation
Prerequisites

Python 3.10+
PostgreSQL 15+
Redis 7.0+
MinIO
Git

Setup Steps

Clone the Repository:
git clone https://github.com/yourusername/tirumba.git
cd tirumba


Set Up Virtual Environment:
python -m venv env
env\Scripts\activate  # Windows
# source env/bin/activate  # Linux/Mac


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

Create a database named tirumba_db using pgAdmin or CLI:createdb tirumba_db


Run migrations:python manage.py makemigrations
python manage.py migrate




Start Redis and MinIO:

Redis: Ensure Redis is running:redis-server


MinIO: Start MinIO server:minio.exe server C:\minio-data  # Windows
# minio server /data  # Linux/Mac




Run the Django Server:
python manage.py runserver


Run Celery Worker:
celery -A tirumba worker -l info --pool=solo  # Windows workaround



🔌 API Endpoints



Method
Endpoint
Description



POST
/api/auth/register/
Register a user (phone_number, email, password, confirm_password)


POST
/api/login/
Obtain authentication token


POST
/api/announcements/
Create a funeral announcement


POST
/api/announcements/{id}/approve/
Approve an announcement


POST
/api/announcements/{id}/dispatch/
Queue dispatch to channels (e.g., Telegram)


🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a feature branch:git checkout -b feature/your-feature-name


Commit your changes:git commit -m "Add your feature"


Push to the branch:git push origin feature/your-feature-name


Open a pull request on GitHub.

📞 Contact
For questions, feedback, or collaboration, reach out via:

GitHub Issues
Email: makdatsegazeab93@gmail.com

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

Built with passion to empower communities through technology.© 2025 Makda Tsegazeab – Portfolio Project
