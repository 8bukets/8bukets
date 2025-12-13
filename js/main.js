document.addEventListener('DOMContentLoaded', () => {
    console.log('United Sports News website loaded successfully.');

    // Set current year in footer
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
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
