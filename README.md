# updating the readme file  
# Online Event Management System Using Django

## 📋 Project Overview

**EventHub** is a comprehensive online platform for event management that allows users to discover, register, and manage events. It provides a seamless experience for event organizers to create and manage events, and for participants to find and book tickets.

## ✨ Key Features

### 🔐 For Users (Participants)
- ✅ Register and Login with secure authentication
- ✅ Browse all available events with filters
- ✅ Search events by category, date, and price
- ✅ View detailed event information
- ✅ Book event tickets easily
- ✅ Cancel bookings when needed
- ✅ Download digital tickets
- ✅ View booking history
- ✅ Manage profile and preferences

### 📅 For Event Organizers
- ✅ Create new events with detailed information
- ✅ Upload event posters and images
- ✅ Set pricing and seat capacity
- ✅ Edit event details
- ✅ Delete events
- ✅ View all event bookings
- ✅ Monitor participant list
- ✅ Track available seats

### 👨‍💼 For Admin
- ✅ Full system access and control
- ✅ Approve/reject event listings
- ✅ Manage users and roles
- ✅ Delete inappropriate content
- ✅ View system statistics
- ✅ Generate reports
- ✅ Manage event categories

## 🛠️ Technologies Used

| Component | Technology |
|-----------|-----------|
| **Backend** | Python, Django 6.0+ |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Database** | SQLite3 (default) / MySQL |
| **UI Framework** | Bootstrap 5 |
| **Icons** | Font Awesome 6 |
| **Image Handling** | Pillow |
| **Forms** | Django Crispy Forms |

## 📁 Project Structure

```
event_project/
├── event_project/              # Main project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py
├── accounts/                  # User management app
│   ├── models.py              # UserProfile model
│   ├── views.py               # Authentication views
│   ├── forms.py               # User forms
│   ├── urls.py                # Auth URLs
│   └── admin.py               # Admin configuration
├── events/                    # Event management app
│   ├── models.py              # Event model
│   ├── views.py               # Event views
│   ├── forms.py               # Event forms
│   ├── urls.py                # Event URLs
│   └── admin.py               # Admin configuration
├── bookings/                  # Booking management app
│   ├── models.py              # Booking model
│   ├── views.py               # Booking views
│   ├── forms.py               # Booking forms
│   ├── urls.py                # Booking URLs
│   └── admin.py               # Admin configuration
├── templates/                 # HTML templates
│   ├── base.html              # Base template
│   ├── accounts/              # Auth templates
│   ├── events/                # Event templates
│   └── bookings/              # Booking templates
├── static/                    # Static files
│   ├── css/                   # Stylesheets
│   ├── js/                    # JavaScript files
│   └── images/                # Images
├── media/                     # User uploads
├── manage.py                  # Django management
└── db.sqlite3                 # Database file
```

## 🗄️ Database Models

### UserProfile
```
- user (OneToOne with Django User)
- role (user/organizer/admin)
- phone
- company
- bio
- profile_picture
- created_at, updated_at
```

### Event
```
- id (Primary Key)
- title
- description
- category (conference/workshop/seminar/etc)
- date, time
- location
- price
- seats, available_seats
- image
- organizer (FK to User)
- status (pending/approved/cancelled)
- created_at, updated_at
```

### Booking
```
- id (Primary Key)
- user (FK to User)
- event (FK to Event)
- booking_date
- quantity
- total_price
- status (pending/confirmed/cancelled/completed)
- ticket_number (unique)
- payment_status
- notes
- created_at, updated_at
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Virtual Environment (recommended)

### Step-by-Step Installation

1. **Clone/Navigate to Project**
   ```bash
   cd "c:\Users\chakr\OneDrive\Desktop\Event"
   ```

2. **Activate Virtual Environment**
   ```bash
   .\.venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files** (for production)
   ```bash
   python manage.py collectstatic
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access Application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 🚀 Deployment

### ⚠️ Important: Netlify Cannot Host This Django App

**Netlify's static hosting does NOT support Django** because it's a Python server-side framework. Every request returns a 404 because there's no Python runtime.

### ✅ Recommended Hosting Platforms

**Best Options for Django:**
1. **Railway** (Recommended) - https://railway.app
2. **Render** - https://render.com
3. **Heroku** - https://www.heroku.com
4. **PythonAnywhere** - https://www.pythonanywhere.com
5. **AWS/DigitalOcean** - Self-managed

### 🚀 Quick Deploy to Railway

```bash
# 1. Create Railway account and link GitHub
# 2. Create new service from GitHub repo
# 3. Set environment variables in Railway dashboard:
#    - SECRET_KEY=your-secure-key
#    - DEBUG=False
#    - ALLOWED_HOSTS=*.railway.app

# 4. Push to GitHub (Railway auto-deploys)
git add .
git commit -m "Ready for production"
git push origin main
```

**For detailed deployment instructions, see [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md)**

## 📄 Main Pages & Features

### Public Pages
- **Home** (`/`) - Landing page with featured events
- **Events List** (`/events/`) - Browse all events with filters
- **Event Detail** (`/events/<id>/`) - Full event information
- **Register** (`/accounts/register/`) - New user registration
- **Login** (`/accounts/login/`) - User authentication

### Authenticated User Pages
- **Dashboard** (`/accounts/dashboard/`) - User overview
- **Profile** (`/accounts/profile/`) - Edit profile & view bookings
- **My Bookings** (`/bookings/my-bookings/`) - Booking history
- **Booking Detail** (`/bookings/booking/<id>/`) - Full booking info
- **Create Booking** (`/bookings/book/<event_id>/`) - Book tickets

### Organizer Pages
- **Create Event** (`/events/create/`) - Create new event
- **Edit Event** (`/events/<id>/edit/`) - Modify event details
- **My Events** (`/organizer/events/`) - Manage created events

### Admin Features
- Admin Dashboard (`/admin/`)
- User Management
- Event Approval System
- Booking Management
- Statistics & Reports

## 🔑 Key Views & Functions

### Authentication
- `register()` - User registration
- `login_view()` - User login
- `logout_view()` - User logout
- `profile()` - User profile management

### Events
- `home()` - Homepage with featured events
- `event_list()` - Browse and filter events
- `event_detail()` - View event information
- `create_event()` - Create new event (organizer only)
- `edit_event()` - Edit event details
- `delete_event()` - Delete event

### Bookings
- `create_booking()` - Book event tickets
- `booking_detail()` - View booking information
- `user_bookings()` - List user's bookings
- `cancel_booking()` - Cancel booking
- `download_ticket()` - Download ticket as HTML

## 🎨 User Interface

### Design Features
- **Modern Gradient Header** - Purple gradient navbar
- **Responsive Layout** - Bootstrap 5 grid system
- **Card-based Design** - Clean component layout
- **Interactive Elements** - Hover effects and animations
- **Color Scheme** - Purple (#667eea) and dark accents
- **Icon Integration** - Font Awesome icons throughout

### Pages Design
1. **Home Page** - Hero section, stats cards, featured events
2. **Event Listing** - Grid layout, filter panel, event cards
3. **Event Details** - Large image, description, booking section
4. **Booking Form** - Event summary, dynamic price calculation
5. **Dashboard** - Stats cards, recent bookings, quick actions
6. **Admin Panel** - Full Django admin interface

## 📊 Forms & Validation

### User Forms
- `UserRegisterForm` - Registration with validation
- `UserUpdateForm` - Profile information
- `UserProfileForm` - Extended profile details
- `LoginForm` - Custom login form

### Event Forms
- `EventForm` - Create/edit events
- `EventSearchForm` - Advanced search filters

### Booking Forms
- `BookingForm` - Ticket quantity & notes

## 🔒 Security Features

- Django CSRF protection
- Password hashing & validation
- User authentication required for bookings
- Role-based access control (user/organizer/admin)
- Data validation on forms
- SQL injection prevention with ORM

## 🧪 Testing

### Test Accounts
```
Admin:
- Username: admin
- Email: admin@eventmgmt.com
- Password: (set during setup)

Demo User:
- Create via registration page
- Different roles available
```

### Test Scenarios
1. Register new account
2. Create event (as organizer)
3. Browse and book events
4. Manage bookings
5. Admin approvals

## 📝 Usage Instructions

### For Users
1. Register an account on `/register/`
2. Browse events on `/events/`
3. Click "View & Book" on any event
4. Select quantity and complete booking
5. Download ticket or manage booking

### For Organizers
1. Set profile role to "Organizer"
2. Click "Create Event" in navbar
3. Fill event details and upload poster
4. Submit for admin approval
5. Manage events on "My Events" page

### For Admin
1. Login as superuser
2. Go to `/admin/`
3. Approve/reject events
4. Manage users and bookings
5. View system statistics

## 📱 Responsive Design

- Mobile-first approach
- Responsive navbar with toggle
- Flexible grid layouts
- Touch-friendly buttons
- Optimized images

## 🚀 Performance Optimizations

- Database query optimization
- Static file caching
- Image compression support
- Minimal JavaScript
- CSS minification ready

## 🔄 Future Enhancements

- ✨ Payment gateway integration (Razorpay/Stripe)
- ✨ Email notifications
- ✨ Event categories and tags
- ✨ User reviews and ratings
- ✨ Seat selection interface
- ✨ QR code tickets
- ✨ SMS notifications
- ✨ Advanced analytics dashboard

## 📞 Support & Troubleshooting

### Common Issues

**Port Already in Use**
```bash
python manage.py runserver 8001
```

**Database Errors**
```bash
python manage.py migrate --run-syncdb
```

**Static Files Not Loading**
```bash
python manage.py collectstatic --noinput
```

## 📄 License

This project is open-source and available for educational purposes.

## 👤 Author

Created as a comprehensive Django learning project demonstrating:
- Full-stack web development
- Database design & relationships
- User authentication & authorization
- CRUD operations
- Responsive web design
- Admin panel customization

---

**Happy Event Managing! 🎉**

For more information or issues, check the Django documentation:
- Django Docs: https://docs.djangoproject.com/
- Bootstrap Docs: https://getbootstrap.com/docs/
