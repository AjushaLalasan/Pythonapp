/**
 * BUILDPRO & CO. - INTERACTIVE CONTRACTOR JAVASCRIPT
 * Handles mobile nav, interactive cost calculator, portfolio filtering,
 * modal quick-views, and AJAX form submissions.
 */

document.addEventListener('DOMContentLoaded', () => {

    /* ==========================================================================
       1. MOBILE DRAWER NAVIGATION
       ========================================================================== */
    const mobileBtn = document.getElementById('mobileMenuBtn');
    const drawer = document.getElementById('mobileDrawer');
    const backdrop = document.getElementById('drawerBackdrop');
    const drawerCloseBtn = document.getElementById('drawerCloseBtn');

    function openMobileMenu() {
        if (drawer && backdrop) {
            drawer.classList.add('open');
            backdrop.classList.add('open');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeMobileMenu() {
        if (drawer && backdrop) {
            drawer.classList.remove('open');
            backdrop.classList.remove('open');
            document.body.style.overflow = '';
        }
    }

    if (mobileBtn) mobileBtn.addEventListener('click', openMobileMenu);
    if (drawerCloseBtn) drawerCloseBtn.addEventListener('click', closeMobileMenu);
    if (backdrop) backdrop.addEventListener('click', closeMobileMenu);

    // Close drawer when clicking a drawer link
    document.querySelectorAll('.drawer-nav a').forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });

    /* ==========================================================================
       2. STICKY HEADER & BACK-TO-TOP BUTTON
       ========================================================================== */
    const backToTopBtn = document.getElementById('backToTopBtn');
    const header = document.getElementById('siteHeader');

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;

        // Header elevation on scroll
        if (header) {
            if (scrollY > 50) {
                header.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.4)';
            } else {
                header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.2)';
            }
        }

        // Back to top visibility
        if (backToTopBtn) {
            if (scrollY > 350) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        }
    });

    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ==========================================================================
       3. INTERACTIVE CONSTRUCTION COST ESTIMATOR
       ========================================================================== */
    const sqftSlider = document.getElementById('sqftSlider');
    const sqftBadge = document.getElementById('sqftBadge');
    const typeButtons = document.querySelectorAll('.js-calc-type');
    const tierButtons = document.querySelectorAll('.js-calc-tier');
    const extraCheckboxes = document.querySelectorAll('.js-calc-extra');

    const estimateDisplay = document.getElementById('calcEstimateDisplay');
    const timelineDisplay = document.getElementById('calcTimelineDisplay');
    const specAreaDisplay = document.getElementById('calcSpecArea');
    const specTypeDisplay = document.getElementById('calcSpecType');
    const specTierDisplay = document.getElementById('calcSpecTier');
    const applyToQuoteBtn = document.getElementById('applyEstimateToQuote');

    // Base square-foot rates by project type
    const BASE_RATES = {
        'residential': 175,
        'commercial': 225,
        'renovation': 130,
        'industrial': 150
    };

    // Quality tier multipliers
    const TIER_MULTIPLIERS = {
        'standard': 1.0,
        'premium': 1.35,
        'luxury': 1.75
    };

    let selectedType = 'commercial';
    let selectedTier = 'premium';

    function formatCurrency(amount) {
        return '$' + Math.round(amount).toLocaleString('en-US');
    }

    function calculateEstimate() {
        if (!sqftSlider || !estimateDisplay) return;

        const sqft = parseInt(sqftSlider.value, 10);
        if (sqftBadge) sqftBadge.textContent = `${sqft.toLocaleString()} sq ft`;
        if (specAreaDisplay) specAreaDisplay.textContent = `${sqft.toLocaleString()} sq ft`;

        const baseRate = BASE_RATES[selectedType] || 200;
        const tierMultiplier = TIER_MULTIPLIERS[selectedTier] || 1.0;

        let totalBaseCost = sqft * baseRate * tierMultiplier;

        // Sum additional features
        let extrasTotal = 0;
        extraCheckboxes.forEach(cb => {
            if (cb.checked) {
                extrasTotal += parseFloat(cb.dataset.cost || 0);
            }
        });

        const totalEstimated = totalBaseCost + extrasTotal;
        const lowEstimate = totalEstimated * 0.92;
        const highEstimate = totalEstimated * 1.10;

        estimateDisplay.textContent = `${formatCurrency(lowEstimate)} - ${formatCurrency(highEstimate)}`;

        // Calculate timeline estimate
        let months = 3;
        if (sqft > 15000) months = 18;
        else if (sqft > 8000) months = 12;
        else if (sqft > 4000) months = 8;
        else if (sqft > 2000) months = 5;

        if (selectedTier === 'luxury') months += 2;
        if (timelineDisplay) {
            timelineDisplay.innerHTML = `Estimated Timeline: <strong>${months} - ${months + 3} Months</strong>`;
        }
    }

    // Bind type selector buttons
    typeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            typeButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedType = btn.dataset.type;
            if (specTypeDisplay) specTypeDisplay.textContent = btn.querySelector('span')?.textContent || selectedType;
            calculateEstimate();
        });
    });

    // Bind tier selector buttons
    tierButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            tierButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedTier = btn.dataset.tier;
            if (specTierDisplay) specTierDisplay.textContent = btn.querySelector('span')?.textContent || selectedTier;
            calculateEstimate();
        });
    });

    // Bind slider and checkboxes
    if (sqftSlider) sqftSlider.addEventListener('input', calculateEstimate);
    extraCheckboxes.forEach(cb => cb.addEventListener('change', calculateEstimate));

    // Initialize calculator
    if (sqftSlider) calculateEstimate();

    // Button: Send estimate to quote form
    if (applyToQuoteBtn) {
        applyToQuoteBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const quoteSection = document.getElementById('quote-section');
            if (quoteSection) {
                quoteSection.scrollIntoView({ behavior: 'smooth' });

                // Fill quote inputs if present
                const typeInput = document.getElementById('id_project_type');
                const sqftInput = document.getElementById('id_property_size');
                const messageInput = document.getElementById('id_message');

                if (typeInput) {
                    typeInput.value = selectedType;
                }
                if (sqftInput && sqftSlider) {
                    sqftInput.value = `${sqftSlider.value} sq ft (${selectedTier} Tier)`;
                }
                if (messageInput) {
                    messageInput.value = `I generated an estimate using the Cost Calculator: ${sqftSlider.value} sq ft, ${selectedType} project with ${selectedTier} tier finishes. Looking forward to discussing details!`;
                }
            }
        });
    }

    /* ==========================================================================
       4. PORTFOLIO FILTERING
       ========================================================================== */
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.dataset.filter;

            projectCards.forEach(card => {
                const cardCategory = card.dataset.category;
                if (filterValue === 'all' || cardCategory === filterValue) {
                    card.style.display = 'block';
                    card.style.opacity = '0';
                    setTimeout(() => {
                        card.style.transition = 'opacity 0.4s ease';
                        card.style.opacity = '1';
                    }, 50);
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    /* ==========================================================================
       5. PROJECT QUICK-VIEW MODAL (AJAX)
       ========================================================================== */
    const modal = document.getElementById('projectQuickModal');
    const modalCloseBtn = document.getElementById('modalCloseBtn');
    const modalContent = document.getElementById('modalContentBody');
    const quickViewButtons = document.querySelectorAll('.js-quick-view-btn');

    function closeModal() {
        if (modal) {
            modal.classList.remove('show');
            modal.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        }
    }

    if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeModal);
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });
    }
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });

    quickViewButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const projectId = btn.dataset.projectId;
            if (!projectId || !modal || !modalContent) return;

            modalContent.innerHTML = `
                <div class="modal-loader">
                    <i class="fas fa-spinner fa-spin fa-2x"></i>
                    <p style="margin-top: 1rem;">Loading project specifications...</p>
                </div>
            `;
            modal.classList.add('show');
            modal.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';

            fetch(`/api/projects/${projectId}/`)
                .then(res => {
                    if (!res.ok) throw new Error('Failed to load project details');
                    return res.json();
                })
                .then(data => {
                    modalContent.innerHTML = `
                        <div class="modal-project-content">
                            <div class="modal-project-img-wrap">
                                <img src="${data.image_url || 'https://images.unsplash.com/photo-1541888946425-d0fbb18615f3?auto=format&fit=crop&w=800&q=80'}" alt="${data.title}" class="modal-project-img">
                            </div>
                            <div class="modal-project-body">
                                <span class="section-tag">${data.category}</span>
                                <h2>${data.title}</h2>
                                <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 1.5rem;">${data.short_summary}</p>
                                
                                <div class="estimate-specs">
                                    <div class="spec-row"><span>Location:</span> <strong>${data.location}</strong></div>
                                    <div class="spec-row"><span>Client:</span> <strong>${data.client}</strong></div>
                                    <div class="spec-row"><span>Completion:</span> <strong>${data.completion_year}</strong></div>
                                    <div class="spec-row"><span>Total Area:</span> <strong>${data.area || 'N/A'}</strong></div>
                                    <div class="spec-row"><span>Capital Budget:</span> <strong>${data.budget || 'Confidential'}</strong></div>
                                </div>

                                <div style="display: flex; gap: 0.75rem; margin-top: 2rem;">
                                    <a href="${data.url}" class="btn btn-primary btn-sm">Full Case Study</a>
                                    <a href="#quote-section" class="btn btn-outline-dark btn-sm" onclick="document.getElementById('projectQuickModal').classList.remove('show'); document.body.style.overflow='';">Inquire Similar</a>
                                </div>
                            </div>
                        </div>
                    `;
                })
                .catch(err => {
                    modalContent.innerHTML = `
                        <div style="padding: 3rem; text-align: center;">
                            <i class="fas fa-exclamation-triangle" style="font-size: 2.5rem; color: #ef4444; margin-bottom: 1rem;"></i>
                            <h3>Unable to load project</h3>
                            <p style="color: #64748b;">Could not fetch project data. Please try again later.</p>
                        </div>
                    `;
                });
        });
    });

    /* ==========================================================================
       6. AJAX QUOTE FORM SUBMISSION (With Graceful Fallback)
       ========================================================================== */
    const quoteForm = document.getElementById('ajaxQuoteForm');
    const quoteStatusBox = document.getElementById('quoteFormStatus');

    if (quoteForm && quoteStatusBox) {
        quoteForm.addEventListener('submit', (e) => {
            // Optional AJAX enhancement: Let standard POST proceed if preferred,
            // or submit smoothly via AJAX if requested.
            // Here we provide instant AJAX validation feedback.
            e.preventDefault();

            const submitBtn = quoteForm.querySelector('button[type="submit"]');
            const originalBtnHtml = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting Request...';

            const formData = new FormData(quoteForm);

            fetch('/api/quote/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(res => res.json())
            .then(data => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHtml;

                if (data.status === 'success') {
                    quoteStatusBox.innerHTML = `
                        <div class="alert alert-success" style="margin-top: 1.5rem;">
                            <i class="fas fa-check-circle" style="font-size: 1.3rem;"></i>
                            <div>
                                <strong>Request Sent!</strong>
                                <p style="margin: 0; font-size: 0.88rem;">${data.message}</p>
                            </div>
                        </div>
                    `;
                    quoteForm.reset();
                } else {
                    let errorMsg = 'Please verify your form details.';
                    if (data.errors) {
                        const keys = Object.keys(data.errors);
                        if (keys.length > 0) {
                            errorMsg = data.errors[keys[0]][0].message;
                        }
                    }
                    quoteStatusBox.innerHTML = `
                        <div class="alert alert-error" style="margin-top: 1.5rem;">
                            <i class="fas fa-exclamation-triangle"></i>
                            <div><strong>Submission Error:</strong> ${errorMsg}</div>
                        </div>
                    `;
                }
            })
            .catch(err => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHtml;
                // If AJAX network fails, submit as standard browser form
                quoteForm.submit();
            });
        });
    }

});
