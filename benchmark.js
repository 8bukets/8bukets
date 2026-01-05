const { JSDOM } = require('jsdom');

// Create a mock DOM
const dom = new JSDOM(`
  <!DOCTYPE html>
  <body>
    <input id="search-input" />
    <div id="article-list">
      <!-- Generate 1000 articles to make the performance cost measurable -->
      ${Array(1000).fill(0).map((_, i) => `
        <article>
          <h3>Article Title ${i}</h3>
          <p>Some content that contains keywords like football, basketball, and more. ${i}</p>
        </article>
      `).join('')}
    </div>
  </body>
`);

global.document = dom.window.document;
global.window = dom.window;

// Load the script logic (simplified for node environment)
// We'll mimic the logic in main.js
const searchInput = document.getElementById('search-input');
const articleList = document.getElementById('article-list');

// Original implementation logic
function originalHandler(e) {
    const term = e.target.value.toLowerCase();
    const articles = articleList.getElementsByTagName('article');

    Array.from(articles).forEach(article => {
        const text = article.textContent.toLowerCase();
        if (text.includes(term)) {
            article.style.display = 'block';
        } else {
            article.style.display = 'none';
        }
    });
}

// Simulate rapid typing
console.time('Typing Simulation (No Debounce)');
for (let i = 0; i < 100; i++) {
    const event = { target: { value: 'test ' + i } };
    originalHandler(event);
}
console.timeEnd('Typing Simulation (No Debounce)');
