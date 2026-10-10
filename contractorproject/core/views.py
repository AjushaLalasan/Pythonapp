import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Service, Project, ProjectCategory, Testimonial, QuoteRequest, ContactMessage, CompanyStat
from .forms import QuoteRequestForm, ContactForm


def home(request):
    """
    Main landing page showcasing services, portfolio, interactive estimator,
    company statistics, testimonials, and quick quote form.
    """
    featured_services = Service.objects.filter(is_featured=True)[:6]
    all_services = Service.objects.all()
    featured_projects = Project.objects.filter(is_featured=True).select_related('category')[:8]
    categories = ProjectCategory.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    stats = CompanyStat.objects.all()

    quote_form = QuoteRequestForm()
    contact_form = ContactForm()

    if request.method == 'POST' and 'quote_submit' in request.POST:
        quote_form = QuoteRequestForm(request.POST)
        if quote_form.is_valid():
            quote = quote_form.save()
            messages.success(request, f"Thank you, {quote.full_name}! Your quote request has been received. Our chief estimator will reach out within 24 hours.")
            return redirect('home')
        else:
            messages.error(request, "Please check the form for errors.")

    context = {
        'featured_services': featured_services,
        'all_services': all_services,
        'featured_projects': featured_projects,
        'categories': categories,
        'testimonials': testimonials,
        'stats': stats,
        'quote_form': quote_form,
        'contact_form': contact_form,
    }
    return render(request, 'core/index.html', context)


def services_list(request):
    """List of all construction services offered."""
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})


def service_detail(request, slug):
    """Detail view for a specific construction service."""
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.exclude(id=service.id)[:4]
    quote_form = QuoteRequestForm(initial={'project_type': 'commercial'})
    return render(request, 'core/service_detail.html', {
        'service': service,
        'related_services': related_services,
        'quote_form': quote_form
    })


def projects_list(request):
    """Showcase gallery of projects with filtering by category."""
    categories = ProjectCategory.objects.all()
    category_slug = request.GET.get('category')
    
    projects = Project.objects.all().select_related('category')
    current_category = None
    if category_slug:
        current_category = get_object_or_404(ProjectCategory, slug=category_slug)
        projects = projects.filter(category=current_category)

    return render(request, 'core/projects.html', {
        'projects': projects,
        'categories': categories,
        'current_category': current_category
    })


def project_detail(request, slug):
    """Detailed case study view of a completed project."""
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    return render(request, 'core/project_detail.html', {
        'project': project,
        'related_projects': related_projects
    })


def about_us(request):
    """About company history, team, safety policy, and certifications."""
    stats = CompanyStat.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)[:4]
    return render(request, 'core/about.html', {
        'stats': stats,
        'testimonials': testimonials
    })


def contact(request):
    """Contact page with inquiries form and office details."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            messages.success(request, f"Thank you {contact_msg.name}! Your message has been sent successfully. We will contact you shortly.")
            return redirect('contact')
        else:
            messages.error(request, "Please correct the highlighted fields below.")
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})


@require_POST
def api_request_quote(request):
    """AJAX endpoint for instant quote request submission with real-time UI response."""
    try:
        data = json.loads(request.body.decode('utf-8'))
        form = QuoteRequestForm(data)
    except Exception:
        form = QuoteRequestForm(request.POST)

    if form.is_valid():
        quote = form.save()
        return JsonResponse({
            'status': 'success',
            'message': f'Quote request #{quote.id} created! We will contact {quote.email} shortly.',
            'quote_id': quote.id
        })
    else:
        return JsonResponse({
            'status': 'error',
            'errors': form.errors.get_json_data()
        }, status=400)


def api_project_detail(request, pk):
    """AJAX endpoint for project quick view modal."""
    project = get_object_or_404(Project, pk=pk)
    return JsonResponse({
        'id': project.id,
        'title': project.title,
        'category': project.category.name if project.category else 'General Construction',
        'location': project.location,
        'client': project.client_name,
        'completion_year': project.completion_year,
        'area': project.area_sqft,
        'budget': project.budget,
        'short_summary': project.short_summary,
        'full_description': project.full_description,
        'challenge': project.challenge,
        'solution': project.solution,
        'image_url': project.image_url,
        'url': project.get_absolute_url()
    })
