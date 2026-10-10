import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=80)),
                ('number_value', models.CharField(help_text='e.g. 250+, 24, 99.8%', max_length=30)),
                ('icon', models.CharField(default='fas fa-check-circle', max_length=50)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=35)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('is_resolved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=90, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Project Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='QuoteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=35)),
                ('project_type', models.CharField(choices=[('commercial', 'Commercial Construction'), ('residential', 'Residential & Luxury Homes'), ('renovation', 'Renovation & Remodeling'), ('civil', 'Civil & Infrastructure'), ('industrial', 'Industrial Warehousing'), ('other', 'Other Specialized Project')], default='commercial', max_length=40)),
                ('estimated_budget', models.CharField(choices=[('under_50k', 'Under $50,000'), ('50k_150k', '$50,000 - $150,000'), ('150k_500k', '$150,000 - $500,000'), ('500k_1m', '$500,000 - $1,000,000'), ('1m_plus', '$1,000,000+')], default='150k_500k', max_length=40)),
                ('property_size', models.CharField(blank=True, help_text='e.g. 5,000 sq ft', max_length=50)),
                ('timeframe', models.CharField(choices=[('immediate', 'Immediate (Within 1 Month)'), ('1_3_months', '1 - 3 Months'), ('3_6_months', '3 - 6 Months'), ('planning', 'Planning / Flexible')], default='1_3_months', max_length=30)),
                ('site_location', models.CharField(blank=True, max_length=200)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('new', 'New Request'), ('in_review', 'In Review'), ('contacted', 'Client Contacted'), ('proposal_sent', 'Proposal Sent'), ('won', 'Project Won'), ('closed', 'Closed')], default='new', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=160, unique=True)),
                ('icon', models.CharField(default='fas fa-hard-hat', help_text='FontAwesome icon class name (e.g. fas fa-hard-hat, fas fa-building, fas fa-tools)', max_length=50)),
                ('short_description', models.CharField(max_length=255)),
                ('full_description', models.TextField()),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('features_list', models.TextField(blank=True, help_text='Enter key features separated by line breaks')),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=120)),
                ('company_or_role', models.CharField(max_length=150)),
                ('avatar_url', models.URLField(blank=True, max_length=500, null=True)),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('quote', models.TextField()),
                ('project_name', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('client_name', models.CharField(default='Confidential Client', max_length=150)),
                ('location', models.CharField(default='Metro City, USA', max_length=150)),
                ('completion_year', models.CharField(default='2024', max_length=20)),
                ('area_sqft', models.CharField(blank=True, help_text='e.g. 48,000 sq. ft.', max_length=50)),
                ('budget', models.CharField(blank=True, help_text='e.g. $4.5 Million', max_length=50)),
                ('short_summary', models.CharField(max_length=255)),
                ('full_description', models.TextField()),
                ('challenge', models.TextField(blank=True, help_text='Challenges faced during this project')),
                ('solution', models.TextField(blank=True, help_text='Innovative engineering solutions applied')),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('is_featured', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='core.projectcategory')),
            ],
            options={
                'ordering': ['order', '-created_at'],
            },
        ),
    ]
