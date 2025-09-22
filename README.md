# Tirumba 🚀

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python) ![Django](https://img.shields.io/badge/Django-5.0-green?logo=django) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql) ![Redis](https://img.shields.io/badge/Redis-7.0-red?logo=redis) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Tirumba** (ጥሩምባ, Tigrinya and Amharic for "trumpet") is a Django-based RESTful API that modernizes funeral announcements in Tigray, Ethiopia. Drawing inspiration from the traditional practice of announcing funerals via bicycle and microphone, Tirumba delivers timely, reliable notifications through SMS, robocalls, and Telegram. Designed with scalability, reliability, and cultural sensitivity, it uses Tigrinya as the default language and targets specific kebeles (local areas) to ensure communities stay connected during times of loss.

## ✨ Features

- **Create Announcements**: Admins submit funeral details (name, venue, date, audio) via a secure API.
- **Approval Workflow**: Two-step verification ensures only trusted announcements are dispatched.
- **Multi-Channel Delivery**: Supports SMS, robocalls, and Telegram for maximum reach.
- **Recipient Management**: Stores phone numbers by kebele for targeted notifications.
- **Scalable Storage**: Uses MinIO for reliable audio and photo uploads.
- **Asynchronous Processing**: Celery and Redis handle background tasks like message dispatching.

## 💡 Motivation

In Tigray, funeral announcements are a cornerstone of community life, traditionally shared through loudspeakers or word-of-mouth. These methods can be slow and limited in reach. Tirumba digitalizes this process, making it efficient, inclusive, and respectful of cultural practices. As an Ethiopian developer with experience at YBS Software Development, I built Tirumba to leverage technology for community empowerment, ensuring timely and respectful communication.

## 🛠️ Technologies

| Category       | Tools                          |
|----------------|--------------------------------|
| Backend        | Django, Django REST Framework  |
| Database       | PostgreSQL                    |
| Storage        | MinIO                         |
| Task Queue     | Celery, Redis                 |
| Authentication | Token-based (DRF)             |

## 📦 Installation

### Prerequisites
- Python 3.10+
- PostgreSQL 15+
- Redis 7.0+
- MinIO
- Git

### Setup Steps

1. **Clone the Repository**:
   ```bash
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

### Step-by-Step: Apply the README Correctly

**Where You Are**:
- Project folder: `C:\Users\Makda Tsegazeab\Desktop\portfolio_projects\tirumba`.
- Virtual environment activated: `env\Scripts\activate`.
- Project pushed to GitHub (`https://github.com/yourusername/tirumba`).
- Celery running with `--pool=solo`.

**Steps**:

1. **Open or Create README.md**:
   - Check if `README.md` exists: `dir README.md`.
   - Open it:
     - **VS Code** (recommended): `code README.md` (install VS Code if needed: https://code.visualstudio.com).
     - **Notepad**: `notepad README.md`.
   - If it doesn’t exist: `echo. > README.md` then `notepad README.md`.

2. **Copy and Paste the Content**:
   - Copy the content above (starting from `# Tirumba 🚀` to the end, excluding `<xaiArtifact>` tags).
   - Paste into `README.md`, replacing all existing content.
   - **Important**: Ensure you copy from a source that preserves Markdown formatting (e.g., this chat interface’s code block or a raw text editor). Avoid copying from places that strip formatting (e.g., some web browsers).

3. **Save with UTF-8 Encoding**:
   - **VS Code**:
     - Check bottom-right corner for "UTF-8" (click to set if different).
     - Save: Ctrl+S.
   - **Notepad**:
     - File > Save As.
     - File name: `README.md`.
     - Encoding: UTF-8.
     - Save.
   - Why: UTF-8 ensures Tigrinya (ጥሩምባ) and emojis (🚀) render correctly.

4. **Commit and Push to GitHub**:
   - In Command Prompt or PowerShell:
     ```
     git add README.md
     git commit -m "Update README with correct Markdown for GitHub rendering"
     git push
     ```
   - If prompted, use your GitHub username and Personal Access Token (PAT) as password.
   - If push fails:
     ```
     git remote set-url origin https://yourusername:yourPAT@github.com/yourusername/tirumba.git
     git push
     ```
     Replace `yourusername` and `yourPAT` with your actual GitHub username and token.

5. **Verify on GitHub**:
   - Visit `https://github.com/yourusername/tirumba`.
   - The README should render as a polished page with:
     - **Badges**: Colorful tags (Python, Django, PostgreSQL, Redis, MIT License) at the top.
     - **Headers**: Large "Tirumba 🚀", subheadings like "✨ Features".
     - **Tigrinya**: ጥሩምባ displayed correctly.
     - **Tables**: Neatly aligned for Technologies and API Endpoints.
     - **Code Blocks**: Commands like `git clone` in gray boxes.
     - **Emojis**: Visual flair (🚀, ✨, etc.).
   - If it doesn’t look right, check:
     - File is exactly `README.md` (case-sensitive).
     - No extra spaces/tabs (copy exactly as above).
     - Saved in UTF-8 (re-save if Tigrinya is garbled).
     - Repo is public (badges may not render in private repos).

6. **Add a Logo (Optional for Extra Polish)**:
   - Create a logo (e.g., a trumpet image) or use a placeholder: `https://via.placeholder.com/150?text=Tirumba`.
   - Upload to repo:
     - Create `assets` folder: `mkdir assets`.
     - Copy your logo (e.g., `logo.png`) to `assets/`.
     - Update README’s first line after `# Tirumba 🚀`:
       ```markdown
       ![Tirumba Logo](assets/logo.png)
       ```
     - Commit: `git add assets/logo.png`, `git commit -m "Add logo"`, `git push`.
   - Alternatively, use a MinIO URL after we implement the upload endpoint.

### Why This Will Look Pleasant
- **Badges**: Shields.io URLs with logos (e.g., Python, Django) render as colorful tags.
- **Markdown Syntax**: Proper `|`, `-`, and spacing for tables; blank lines between sections.
- **UTF-8**: Ensures Tigrinya (ጥሩምባ) and emojis (🚀) display correctly.
- **GitHub Renderer**: Converts Markdown to a formatted page with no extra code needed.
- **Professional Design**: Clear structure, your YBS experience, and cultural context make it impactful.

### Troubleshooting
- **Not Rendering Correctly**: Share a screenshot or describe the issue (e.g., "badges show as text", "table is misaligned").
- **Tigrinya Garbled**: Verify UTF-8 encoding (re-save in VS Code/Notepad).
- **Push Errors**: Share the error message (e.g., `git push` output).
- **Specific Look Desired**: Describe what’s missing (e.g., colors, images, or an example repo’s style).

### Next Steps
- **Verify**: Check `https://github.com/yourusername/tirumba` and confirm the README looks good.
- **Development**:
  - Add audio/photo upload endpoint (MinIO integration).
  - Implement Telegram dispatch task with Celery.
  - Add CSV import for Recipient phone numbers.
- **Priority**: Let me know what to focus on next or if you need README tweaks (e.g., more Tigrinya, a screenshot).

Replace `yourusername` with your actual GitHub username. If the README still doesn’t look right, share a screenshot or describe the issue, and I’ll help debug!
