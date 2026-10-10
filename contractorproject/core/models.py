from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    icon = models.CharField(
        max_length=50, 
        default="fas fa-hard-hat", 
        help_text="FontAwesome icon class name (e.g. fas fa-hard-hat, fas fa-building, fas fa-tools)"
    )
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    features_list = models.TextField(
        help_text="Enter key features separated by line breaks",
        blank=True
    )
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

    def features(self):
        if not self.features_list:
            return []
        return [f.strip() for f in self.features_list.split('\n') if f.strip()]


class ProjectCategory(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Project Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(
        ProjectCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='projects'
    )
    client_name = models.CharField(max_length=150, default="Confidential Client")
    location = models.CharField(max_length=150, default="Metro City, USA")
    completion_year = models.CharField(max_length=20, default="2024")
    area_sqft = models.CharField(max_length=50, blank=True, help_text="e.g. 48,000 sq. ft.")
    budget = models.CharField(max_length=50, blank=True, help_text="e.g. $4.5 Million")
    short_summary = models.CharField(max_length=255)
    full_description = models.TextField()
    challenge = models.TextField(blank=True, help_text="Challenges faced during this project")
    solution = models.TextField(blank=True, help_text="Innovative engineering solutions applied")
    image_url = models.URLField(max_length=500, blank=True, null=True)
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class Testimonial(models.Model):
    client_name = models.CharField(max_length=120)
    company_or_role = models.CharField(max_length=150)
    avatar_url = models.URLField(max_length=500, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5)
    quote = models.TextField()
    project_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.company_or_role}"

    @property
    def star_range(self):
        return range(self.rating)

    @property
    def empty_star_range(self):
        return range(5 - self.rating)


class QuoteRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'New Request'),
        ('in_review', 'In Review'),
        ('contacted', 'Client Contacted'),
        ('proposal_sent', 'Proposal Sent'),
        ('won', 'Project Won'),
        ('closed', 'Closed'),
    ]

    PROJECT_TYPE_CHOICES = [
        ('commercial', 'Commercial Construction'),
        ('residential', 'Residential & Luxury Homes'),
        ('renovation', 'Renovation & Remodeling'),
        ('civil', 'Civil & Infrastructure'),
        ('industrial', 'Industrial Warehousing'),
        ('other', 'Other Specialized Project'),
    ]

    BUDGET_CHOICES = [
        ('under_50k', 'Under $50,000'),
        ('50k_150k', '$50,000 - $150,000'),
        ('150k_500k', '$150,000 - $500,000'),
        ('500k_1m', '$500,000 - $1,000,000'),
        ('1m_plus', '$1,000,000+'),
    ]

    TIMEFRAME_CHOICES = [
        ('immediate', 'Immediate (Within 1 Month)'),
        ('1_3_months', '1 - 3 Months'),
        ('3_6_months', '3 - 6 Months'),
        ('planning', 'Planning / Flexible'),
    ]

    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=35)
    project_type = models.CharField(max_length=40, choices=PROJECT_TYPE_CHOICES, default='commercial')
    estimated_budget = models.CharField(max_length=40, choices=BUDGET_CHOICES, default='150k_500k')
    property_size = models.CharField(max_length=50, blank=True, help_text="e.g. 5,000 sq ft")
    timeframe = models.CharField(max_length=30, choices=TIMEFRAME_CHOICES, default='1_3_months')
    site_location = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Quote #{self.id} - {self.full_name} ({self.get_project_type_display()})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=35, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name}: {self.subject}"


class CompanyStat(models.Model):
    label = models.CharField(max_length=80)
    number_value = models.CharField(max_length=30, help_text="e.g. 250+, 24, 99.8%")
    icon = models.CharField(max_length=50, default="fas fa-check-circle")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.number_value} - {self.label}"
