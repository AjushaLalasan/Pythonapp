# BuildPro & Co. - Construction & Contractor Platform

A full-featured, modern, and responsive website built for a construction company, general contractor, and civil engineering firm using **Python, Django, HTML5, CSS3, and JavaScript**.

---

## 🌟 Key Features

### 1. Interactive Construction Cost Estimator
- **Dynamic Calculation Engine**: Users can select project type (*Commercial, Residential, Renovation, Industrial*), adjust total square footage with a real-time slider (500 to 25,000+ sq ft), select finish grade (*Standard, Premium, Luxury*), and toggle engineering add-ons (*Solar Net-Zero, Smart Building Automation, Seismic Foundations, Drainage*).
- **Instant Feasibility Readout**: Calculates estimated budget windows and projected delivery timelines on the fly.
- **Auto-populate Action**: One click automatically scrolls down and transfers the chosen parameters directly into the Quote Request Form.

### 2. Portfolio & Case Studies Gallery
- **Multi-Category Filter**: Instant tab filtering across *Commercial Building, Residential & Luxury, Renovation & Remodel, Civil & Infrastructure, and Industrial Logistics*.
- **Quick-View AJAX Modal**: View high-resolution site photography, challenge/solution breakdowns, and technical specs without leaving the gallery.
- **Detailed Case Study Pages**: Complete project breakdowns including budget, area, location, structural challenges, and engineering solutions.

### 3. Specialized Services Suite
- Dedicated capability pages covering turnkey construction disciplines.
- 4-Stage Construction Process walkthrough (*Feasibility & BIM, Procurement, Heavy Structural Build, Commissioning & Handover*).

### 4. High-Converting Quote Request & Lead Generation
- Captures client contact details, project classification, square footage, budget tier, and architectural notes.
- Dual submission mode: Supports seamless asynchronous **AJAX** submission with live validation badges, falling back gracefully to standard Django POST.
- Direct integration with the Django admin dashboard.

### 5. Contractor Management & Admin Portal
- Fully customized Django Admin interface for:
  - Adding and modifying **Projects** and **Services**
  - Tracking and managing client **Quote Requests** (`New`, `In Review`, `Contacted`, `Proposal Sent`, `Won`, `Closed`)
  - Reviewing **Contact Inquiries** and marking them as resolved
  - Managing **Testimonials** and **Company Statistics**

### 6. Modern Responsive UI/UX
- Industrial safety color scheme: Construction Amber (`#f59e0b`), Midnight Slate (`#0f172a`), and Crisp White.
- Sticky navigation header with scroll elevation.
- Mobile sliding drawer menu with backdrop blur.
- Fully responsive across desktop, tablet, and mobile devices.

---

## 🚀 Quick Start Guide

### 1. Install Dependencies
Make sure you have Python 3.9+ installed:
```bash
pip install -r requirements.txt
```

### 2. Apply Database Migrations
Run the pre-configured database migrations to initialize SQLite:
```bash
python manage.py migrate
```

### 3. Seed Realistic Construction Data
Populate the database with pre-built construction services, portfolio projects, client testimonials, and company statistics:
```bash
python manage.py seed_data
```

### 4. Create an Administrator Account
Create a superuser to access the management portal:
```bash
python manage.py createsuperuser
```

### 5. Launch the Development Server
```bash
python manage.py runserver
```

Now open your browser and navigate to:
- **Public Website**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Dashboard**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ☁️ Deploying to Render

The repository includes a `render.yaml` Blueprint at its root. In Render, create a
new Blueprint from the repository; the configuration uses `contractorproject/` as
the service root, collects static files during build, applies migrations at startup,
and runs the app with Gunicorn.

Before deploying, create a Render PostgreSQL database and set `DATABASE_URL` on the
web service to the database's **Internal Database URL**. The Blueprint generates
a `SECRET_KEY` and disables `DEBUG` in production. The app reads Render's
`RENDER_EXTERNAL_HOSTNAME` automatically; set `ALLOWED_HOSTS` or
`CSRF_TRUSTED_ORIGINS` only if you use additional custom domains.

The app uses SQLite automatically when `DATABASE_URL` is not set, which is
convenient for local development but is not durable storage for a deployed service.
After deployment, create an administrator with
`python manage.py createsuperuser` from the Render shell.

---

## 📁 Project Architecture

```
contractorproject/
│
├── manage.py                          # Django management entrypoint
├── requirements.txt                   # Project Python dependencies
├── README.md                          # Project documentation
│
├── contractorproject/                 # Project configuration
│   ├── __init__.py
│   ├── settings.py                    # Settings, apps, templates, static/media paths
│   ├── urls.py                        # Root URL routing
│   ├── wsgi.py                        # WSGI entrypoint
│   └── asgi.py                        # ASGI entrypoint
│
├── core/                              # Main construction web application
│   ├── __init__.py
│   ├── apps.py                        # Core application config
│   ├── models.py                      # Service, Project, Testimonial, QuoteRequest, etc.
│   ├── views.py                       # Page controllers & JSON API endpoints
│   ├── urls.py                        # URL patterns (services, projects, quote, contact)
│   ├── forms.py                       # QuoteRequestForm & ContactForm
│   ├── admin.py                       # Customized Django Admin with filters & status badges
│   ├── context_processors.py          # Global company details & hotline info
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py            # Pre-configured schema migration
│   └── management/
│       └── commands/
│           ├── __init__.py
│           └── seed_data.py           # Command to seed initial high-quality contractor data
│
├── templates/                         # HTML5 Django templates
│   ├── base.html                      # Layout, sticky header, mobile drawer, modal, footer
│   └── core/
│       ├── index.html                 # Homepage with Hero, Calculator, Services, Portfolio, Quotes
│       ├── services.html              # Services listing page
│       ├── service_detail.html        # Detailed technical breakdown for individual service
│       ├── projects.html              # Filterable portfolio gallery
│       ├── project_detail.html        # Full project case study & specs
│       ├── about.html                 # Heritage, safety credentials, executive team
│       └── contact.html               # Dispatch hotline, contact form, interactive FAQs
│
└── static/                            # Static frontend assets
    ├── css/
    │   └── style.css                  # Custom responsive CSS design system
    └── js/
        └── main.js                    # Cost calculator, mobile drawer, portfolio filters, AJAX
```

---

## 🛠️ Customization

- **Company Details**: Edit `core/context_processors.py` to change company name, phone hotline, address, emergency dispatch, and license number across all pages.
- **Branding & Colors**: Edit `:root` variables in `static/css/style.css` (e.g. `--primary` for brand color).
- **Adding Projects/Services**: Use the Django Admin portal at `/admin/` to upload new projects, update project statuses, or edit services.
