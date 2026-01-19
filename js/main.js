document.addEventListener('DOMContentLoaded', () => {
    console.log('United Sports News website loaded successfully.');

    // Service Worker Registration
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('./sw.js')
                .then(registration => {
                    console.log('ServiceWorker registration successful with scope: ', registration.scope);
                }, err => {
                    console.log('ServiceWorker registration failed: ', err);
                });
        });
    }

    // Set current year in footer
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // Theme Toggle
    const toggleBtn = document.getElementById('theme-toggle');
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        if (toggleBtn) toggleBtn.textContent = 'Light Mode';
    }

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
                toggleBtn.textContent = 'Light Mode';
            } else {
                localStorage.setItem('theme', 'light');
                toggleBtn.textContent = 'Dark Mode';
            }
        });
    }

    // Search Functionality
    const searchInput = document.getElementById('search-input');
    const articleList = document.getElementById('article-list');

    if (searchInput && articleList) {
        // ⚡ Bolt Optimization: Cache article text to prevent DOM thrashing
        // and excessive reads during search operations.
        const articles = Array.from(articleList.getElementsByTagName('article'));
        const searchIndex = articles.map(article => ({
            element: article,
            text: article.textContent.toLowerCase()
        }));

        const performSearch = (term) => {
            // Use cached index for O(1) property access instead of DOM read
            searchIndex.forEach(item => {
                if (item.text.includes(term)) {
                    item.element.style.display = 'block';
                } else {
                    item.element.style.display = 'none';
                }
            });
        };

        // ⚡ Bolt Optimization: Debounce search to reduce main thread work
        const debounce = (func, wait) => {
            let timeout;
            return function(...args) {
                const context = this;
                clearTimeout(timeout);
                timeout = setTimeout(() => func.apply(context, args), wait);
            };
        };

        searchInput.addEventListener('input', debounce((e) => {
            const term = e.target.value.toLowerCase();
            performSearch(term);
        }, 300));
    }

    // Contact Form Validation
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (email && message) {
                alert('Thank you for your message! We will get back to you shortly.');
                contactForm.reset();
            } else {
                alert('Please fill in all fields.');
            }
        });
    }

    // Cookie Consent Logic
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptCookiesBtn = document.getElementById('accept-cookies');
    const cookiesAccepted = localStorage.getItem('cookiesAccepted');

    if (!cookiesAccepted && cookieBanner) {
        cookieBanner.style.display = 'block';
    }

    if (acceptCookiesBtn) {
        acceptCookiesBtn.addEventListener('click', () => {
            localStorage.setItem('cookiesAccepted', 'true');
            if (cookieBanner) {
                cookieBanner.style.display = 'none';
            }
        });
    }
});

// Simple toggle function for "Read More"
function toggleReadMore(btn) {
    const article = btn.parentElement;
    const moreText = article.querySelector('.more-text');

    if (moreText.style.display === 'none') {
        moreText.style.display = 'block';
        btn.textContent = 'Read Less';
    } else {
        moreText.style.display = 'none';
        btn.textContent = 'Read More';
    }
}

// Filter by Category
function filterByCategory(category) {
    const articleList = document.getElementById('article-list');
    if (!articleList) return;

    const articles = articleList.getElementsByTagName('article');

    Array.from(articles).forEach(article => {
        const cat = article.getAttribute('data-category');
        if (cat === category || category === 'All') {
            article.style.display = 'block';
        } else {
            article.style.display = 'none';
        }
    });
}
