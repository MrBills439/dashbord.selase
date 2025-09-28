# Django Admin Dashboard

A comprehensive Django web application with an Admin Dashboard for managing services, blog posts, and users.

## Features

### 🔐 Admin Features
- **Admin Login & Authentication**: Secure login system using Django's built-in User model
- **Service Management**: Create, update, delete, and view services with title, description, and optional icon
- **Blog Post Management**: Create, edit, delete, and publish blog posts with author tracking
- **Member/User Management**: View registered users with basic information (read-only)

### 🧱 Technical Features
- Django 5.2.6 with modern architecture
- Separate apps: `services` and `blog`
- SQLite database (easily configurable for production)
- Beautiful, responsive admin dashboard with Bootstrap 5
- Custom admin views and templates
- AJAX functionality for dynamic interactions

## Project Structure

```
admin_dashboard/
├── admin_dashboard/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── services/                 # Services app
│   ├── models.py            # Service model
│   ├── admin.py             # Service admin configuration
│   └── migrations/
├── blog/                    # Blog app
│   ├── models.py            # BlogPost model
│   ├── admin.py             # BlogPost admin configuration
│   └── migrations/
├── templates/               # Template files
│   ├── base.html           # Base template
│   ├── admin_dashboard/
│   │   └── dashboard.html  # Main dashboard
│   └── registration/
│       └── login.html      # Login page
├── static/                 # Static files (CSS, JS, images)
├── manage.py
├── requirements.txt
└── README.md
```

## Installation & Setup

### 1. Clone and Navigate
```bash
cd "/Users/uglydemon/Documents/Work Station/selase.e"
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Already created)
```bash
# Default credentials: admin / admin123
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

## Usage

### Access the Application
1. Open your browser and go to `http://127.0.0.1:8000/`
2. Login with the default credentials:
   - **Username**: `admin`
   - **Password**: `admin123`

### Dashboard Features
- **Overview**: View statistics and recent activity
- **Services**: Manage your business services
- **Blog Posts**: Create and manage blog content
- **Users**: View registered users (read-only)

### Django Admin
Access the full Django admin interface at `http://127.0.0.1:8000/admin/` for advanced management features.

## Models

### Service Model
- `title`: Service name (CharField, max 200 chars)
- `description`: Service description (TextField)
- `icon`: Optional icon URL (URLField)
- `created_at`: Auto-generated creation timestamp
- `updated_at`: Auto-generated update timestamp

### BlogPost Model
- `title`: Post title (CharField, max 200 chars)
- `content`: Post content (TextField)
- `author`: Foreign key to User model
- `created_date`: Auto-generated creation timestamp
- `updated_date`: Auto-generated update timestamp
- `is_published`: Boolean field for publish status

## Customization

### Adding New Features
1. Create new apps: `python manage.py startapp app_name`
2. Add to `INSTALLED_APPS` in settings.py
3. Create models and register with admin
4. Add views and URL patterns

### Styling
- Templates use Bootstrap 5 for responsive design
- Custom CSS in `templates/base.html`
- Font Awesome icons for enhanced UI

### Database
- Currently using SQLite for development
- For production, update `DATABASES` in settings.py to use PostgreSQL, MySQL, etc.

## Security Notes

- Change default admin credentials in production
- Set `DEBUG = False` for production
- Use environment variables for sensitive settings
- Implement proper HTTPS in production

## API Endpoints

- `/` - Login page
- `/dashboard/` - Main dashboard
- `/admin/` - Django admin interface
- `/services/` - Services management
- `/blog/` - Blog posts management
- `/users/` - Users management
- `/toggle-post/<id>/` - AJAX endpoint to toggle post publish status

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
