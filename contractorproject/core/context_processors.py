def site_settings(request):
    """
    Context processor providing global company details, contact info,
    and quick stats to all templates.
    """
    return {
        'SITE_INFO': {
            'company_name': 'BUILDPRO & CO.',
            'tagline': 'Engineered for Excellence, Built for Generations',
            'phone': '+1 (800) 555-2845',
            'phone_raw': '+18005552845',
            'email': 'contact@buildproconstruction.com',
            'address': '742 Industrial Parkway, Suite 500, New York, NY 10001',
            'hours': 'Mon - Sat: 7:00 AM - 6:00 PM',
            'emergency': '24/7 On-Call Site Dispatch',
            'license_no': 'NYC-GC Lic. #948210-A',
            'years_experience': '25+',
        }
    }
