from django.core.management.base import BaseCommand
from core.models import Service, ProjectCategory, Project, Testimonial, CompanyStat


class Command(BaseCommand):
    help = 'Seeds initial construction services, projects, stats, and testimonials'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Starting construction data seeding...'))

        # 1. Company Stats
        CompanyStat.objects.all().delete()
        stats_data = [
            {'label': 'Years in Industry', 'number_value': '25+', 'icon': 'fas fa-calendar-check', 'order': 1},
            {'label': 'Completed Projects', 'number_value': '380+', 'icon': 'fas fa-building', 'order': 2},
            {'label': 'Certified Engineers', 'number_value': '95+', 'icon': 'fas fa-hard-hat', 'order': 3},
            {'label': 'Safety Compliance', 'number_value': '100%', 'icon': 'fas fa-shield-alt', 'order': 4},
        ]
        for s in stats_data:
            CompanyStat.objects.create(**s)
        self.stdout.write(self.style.SUCCESS(f'Created {len(stats_data)} company stats.'))

        # 2. Project Categories
        categories_data = [
            'Commercial Building',
            'Residential & Luxury',
            'Renovation & Remodel',
            'Civil & Infrastructure',
            'Industrial Logistics',
        ]
        cat_objs = {}
        for cname in categories_data:
            obj, _ = ProjectCategory.objects.get_or_create(name=cname)
            cat_objs[cname] = obj
        self.stdout.write(self.style.SUCCESS(f'Created {len(cat_objs)} project categories.'))

        # 3. Services
        Service.objects.all().delete()
        services_data = [
            {
                'title': 'Commercial Construction',
                'icon': 'fas fa-building',
                'short_description': 'Turnkey commercial building solutions from multi-story corporate towers to dynamic retail complexes.',
                'full_description': 'Our commercial construction division delivers world-class facilities built for productivity, longevity, and modern aesthetics. We integrate Building Information Modeling (BIM), energy-efficient HVAC, and reinforced seismic structural frameworks tailored for heavy commercial demands.',
                'image_url': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1000&q=80',
                'features_list': 'LEED & Green Building Certification\nFast-track construction methodologies\nPre-construction budgeting & feasibility\nAdvanced BIM 3D clash detection\nComprehensive site logistics & safety oversight',
                'order': 1,
                'is_featured': True
            },
            {
                'title': 'Residential & Custom Estates',
                'icon': 'fas fa-home',
                'short_description': 'Bespoke custom homes, modern villas, and multi-unit residential communities crafted to perfection.',
                'full_description': 'From minimalist hillside residences to sprawling luxury compounds, we turn architectural visions into timeless homes. Every residence benefits from custom millwork, smart home automation pre-wiring, and ultra-high thermal efficiency insulation systems.',
                'image_url': 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1000&q=80',
                'features_list': 'Custom architectural craftsmanship\nEnergy-independent solar roofing integration\nSmart home automation infrastructure\nLuxury interior finishes & stone masonry\nTurnkey landscape and pool engineering',
                'order': 2,
                'is_featured': True
            },
            {
                'title': 'Renovation & Structural Retrofitting',
                'icon': 'fas fa-tools',
                'short_description': 'Revitalizing historic landmarks, modernizing commercial interiors, and seismic retrofits.',
                'full_description': 'Transforming existing spaces requires delicate structural expertise and acute respect for historical heritage. Our team specializes in gut rehabilitations, load-bearing wall removals, foundation underpinning, and energy efficiency upgrades for aging structures.',
                'image_url': 'https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1000&q=80',
                'features_list': 'Historic preservation compliance\nStructural foundation underpinning\nComplete interior spatial redesigns\nMEP system modernizations\nZero-downtime occupied facility renovations',
                'order': 3,
                'is_featured': True
            },
            {
                'title': 'Civil Infrastructure & Earthworks',
                'icon': 'fas fa-road',
                'short_description': 'Heavy civil engineering, urban roadways, deep foundations, and municipal drainage systems.',
                'full_description': 'The bedrock of community development starts underground. We manage heavy mass excavation, geotechnical soil stabilization, reinforced highway bridges, stormwater detention facilities, and municipal utility trunklines.',
                'image_url': 'https://images.unsplash.com/photo-1541888946425-d0fbb18615f3?auto=format&fit=crop&w=1000&q=80',
                'features_list': 'Mass earthmoving and site grading\nStormwater retention and drainage mains\nReinforced concrete retaining walls\nHeavy machinery GPS grading fleet\nEnvironmental erosion control compliance',
                'order': 4,
                'is_featured': True
            },
            {
                'title': 'Architectural & Engineering Design',
                'icon': 'fas fa-drafting-compass',
                'short_description': 'Integrated structural engineering, 3D parametric blueprints, and municipal permit processing.',
                'full_description': 'Our in-house architects and structural engineers collaborate closely with field superintendents to ensure designs are structurally robust, cost-effective to construct, and fully aligned with local building codes and zoning laws.',
                'image_url': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1000&q=80',
                'features_list': 'Full CAD and Revit 3D drafting\nStructural calculations & PE stamping\nExpedited zoning & permit filings\nValue engineering cost optimizations\n3D photorealistic walkthrough renders',
                'order': 5,
                'is_featured': True
            },
            {
                'title': 'General Contracting & Site Management',
                'icon': 'fas fa-clipboard-check',
                'short_description': 'Comprehensive project oversight, supply chain assurance, and strict OSHA safety compliance.',
                'full_description': 'Leave the complexities of subcontractor scheduling, material procurement, inspections, and quality assurance to certified master builders. We maintain strict milestones, transparent real-time financial reporting, and zero-compromise safety protocols.',
                'image_url': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=1000&q=80',
                'features_list': 'Dedicated on-site project superintendents\nReal-time client progress portal\nRigorous OSHA safety compliance programs\nVetted subcontractor network\nComprehensive warranty & punch-list resolution',
                'order': 6,
                'is_featured': True
            }
        ]
        for s in services_data:
            Service.objects.create(**s)
        self.stdout.write(self.style.SUCCESS(f'Created {len(services_data)} services.'))

        # 4. Projects
        Project.objects.all().delete()
        projects_data = [
            {
                'title': 'Apex Downtown Financial Tower',
                'category': cat_objs['Commercial Building'],
                'client_name': 'Apex Capital Group',
                'location': 'Financial District, Metro City',
                'completion_year': '2024',
                'area_sqft': '185,000 sq. ft.',
                'budget': '$24.5 Million',
                'short_summary': 'A 28-story LEED Gold certified commercial headquarters featuring high-performance curtain walls and subterranean parking.',
                'full_description': 'This landmark commercial project was engineered with seismic dampeners, smart climate zoned glass facades, and four levels of underground reinforced parking. Delivered on a constrained urban footprint surrounded by active transit lines.',
                'challenge': 'Severe site congestion with zero laydown room requiring just-in-time crane deliveries in the heart of downtown.',
                'solution': 'Implemented night-shift prefabricated steel truss assembly with precision 4D BIM scheduling to avoid street closures.',
                'image_url': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1000&q=80',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Vista Grande Hillside Residence',
                'category': cat_objs['Residential & Luxury'],
                'client_name': 'Private Family Estate',
                'location': 'Highland Ridge, CA',
                'completion_year': '2023',
                'area_sqft': '9,200 sq. ft.',
                'budget': '$4.2 Million',
                'short_summary': 'An ultra-modern cantilevered villa featuring panoramic glass elevations and an infinity pool engineered over steep terrain.',
                'full_description': 'Engineered on a 42-degree rocky incline, this private luxury home showcases seamless indoor-outdoor living, architectural fair-faced concrete walls, customized rift-sawn white oak millwork, and off-grid solar storage.',
                'challenge': 'Challenging geotechnical soil conditions with severe slope stabilization requirements.',
                'solution': 'Drilled 36 deep bedrock friction caissons with high-tensile ground anchors to secure the cantilevered foundation.',
                'image_url': 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1000&q=80',
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'The Ironworks Creative Lofts',
                'category': cat_objs['Renovation & Remodel'],
                'client_name': 'Ironworks Urban Development',
                'location': 'Historic Arts District',
                'completion_year': '2024',
                'area_sqft': '64,000 sq. ft.',
                'budget': '$7.8 Million',
                'short_summary': 'Complete historic restoration and adaptive reuse of a 1912 locomotive foundry into 40 collaborative design studios.',
                'full_description': 'Preserved authentic riveted iron trusses, exposed original reclaimed red brick masonry, while installing brand new state-of-the-art geothermal heating, acoustic insulation, and high-efficiency double-hung replica windows.',
                'challenge': 'Deteriorated century-old masonry mortar and hazardous material abatement without harming landmark details.',
                'solution': 'Employed specialized lime-mortar repointing techniques and micro-abrasive cleaning under strict state historical board supervision.',
                'image_url': 'https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1000&q=80',
                'is_featured': True,
                'order': 3
            },
            {
                'title': 'North Valley Logistics & Distribution Center',
                'category': cat_objs['Industrial Logistics'],
                'client_name': 'Pan-Continental Freight',
                'location': 'North Logistics Corridor',
                'completion_year': '2023',
                'area_sqft': '320,000 sq. ft.',
                'budget': '$16.2 Million',
                'short_summary': 'Tilt-up concrete distribution warehouse with 40-foot clear heights, 64 dock doors, and high-tolerance laser-screed floors.',
                'full_description': 'Built for high-volume automated robotics sorting, this colossal industrial facility features superflat FF/FL slab specifications, high-bay ESFR fire suppression, and a reinforced 12-acre heavy trailer staging yard.',
                'challenge': 'Tight 9-month delivery deadline ahead of peak holiday e-commerce operations.',
                'solution': 'Employed on-site tilt-up wall panel casting concurrently with roof truss prefabrication, shaving 8 weeks off conventional schedules.',
                'image_url': 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1000&q=80',
                'is_featured': True,
                'order': 4
            },
            {
                'title': 'Grand River Parkway Viaduct',
                'category': cat_objs['Civil & Infrastructure'],
                'client_name': 'Department of Transportation',
                'location': 'Grand River Crossing',
                'completion_year': '2022',
                'area_sqft': '1.4 Mile Corridor',
                'budget': '$31.0 Million',
                'short_summary': 'A four-lane pre-stressed concrete overpass built across an active wetland habitat with zero environmental disruption.',
                'full_description': 'A crucial regional transit artery incorporating continuous post-tensioned box girders, seismic expansion joints, and integrated wildlife corridor passageways beneath the main deck.',
                'challenge': 'Strict environmental conservation regulations prohibiting heavy equipment in protected wetlands.',
                'solution': 'Constructed temporary elevated falsework trestles to advance construction from above without ground disturbance.',
                'image_url': 'https://images.unsplash.com/photo-1545558014-8692077e9b5c?auto=format&fit=crop&w=1000&q=80',
                'is_featured': True,
                'order': 5
            },
            {
                'title': 'St. Jude Clinical & Research Pavilion',
                'category': cat_objs['Commercial Building'],
                'client_name': 'Horizon Health Network',
                'location': 'Medical Center Blvd',
                'completion_year': '2024',
                'area_sqft': '95,000 sq. ft.',
                'budget': '$18.5 Million',
                'short_summary': 'Advanced outpatient clinical facility equipped with negative-pressure surgical suites and shielded MRI bays.',
                'full_description': 'Medical construction requires extreme engineering tolerance. This facility features independent vibration-isolated foundations for imaging equipment, cleanroom HEPA airflow, and dual redundant emergency power generators.',
                'challenge': 'Complex hospital electromagnetic shielding and medical gas piping integration within ceiling plenums.',
                'solution': 'Applied millimeter-precision 3D laser scanning to map existing MEP networks and avoid structural clashes.',
                'image_url': 'https://images.unsplash.com/photo-1587293852726-70cdb56c2866?auto=format&fit=crop&w=1000&q=80',
                'is_featured': True,
                'order': 6
            }
        ]
        for p in projects_data:
            Project.objects.create(**p)
        self.stdout.write(self.style.SUCCESS(f'Created {len(projects_data)} projects.'))

        # 5. Testimonials
        Testimonial.objects.all().delete()
        testimonials_data = [
            {
                'client_name': 'Marcus Vance',
                'company_or_role': 'Managing Director, Apex Capital Group',
                'avatar_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80',
                'rating': 5,
                'quote': 'BuildPro delivered our 28-story downtown headquarters on budget and two months ahead of schedule. Their safety culture and craftsmanship on site are second to none in the industry.',
                'project_name': 'Apex Downtown Financial Tower'
            },
            {
                'client_name': 'Victoria Sterling',
                'company_or_role': 'Principal Architect, Studio Forma',
                'avatar_url': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=200&q=80',
                'rating': 5,
                'quote': 'Finding a general contractor that respects intricate architectural details without cutting corners is rare. The BuildPro team solved our cantilevered engineering hurdles with brilliance.',
                'project_name': 'Vista Grande Hillside Residence'
            },
            {
                'client_name': 'Robert Chen',
                'company_or_role': 'Chief Operations Officer, Pan-Continental',
                'avatar_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=200&q=80',
                'rating': 5,
                'quote': 'Our 320,000 sq ft logistics facility needed absolute precision for robotic sorting systems. BuildPro exceeded FF/FL flatness requirements and handled all permitting without friction.',
                'project_name': 'North Valley Logistics Center'
            },
            {
                'client_name': 'Caroline Dupuis',
                'company_or_role': 'Heritage Preservation Board Member',
                'avatar_url': 'https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=200&q=80',
                'rating': 5,
                'quote': 'The Ironworks renovation demanded care and reverence for historical masonry. BuildPro restored century-old steel and brickwork into an architectural gem that the community adores.',
                'project_name': 'The Ironworks Creative Lofts'
            }
        ]
        for t in testimonials_data:
            Testimonial.objects.create(**t)
        self.stdout.write(self.style.SUCCESS(f'Created {len(testimonials_data)} testimonials.'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded all initial construction data!'))
