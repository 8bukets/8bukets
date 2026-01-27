const fs = require('fs');
const vm = require('vm');
const path = require('path');

// Mock DOM elements
class MockElement {
    constructor(tagName, id) {
        this.tagName = tagName;
        this.id = id;
        this.classList = {
            add: () => {},
            remove: () => {},
            toggle: () => {},
            contains: () => false
        };
        this.style = { display: 'block' };
        this.textContent = "Some text content";
        this.value = "";
        this.listeners = {};
        this.children = [];
    }

    addEventListener(event, callback) {
        if (!this.listeners[event]) {
            this.listeners[event] = [];
        }
        this.listeners[event].push(callback);
    }

    trigger(event, eventData) {
        if (this.listeners[event]) {
            this.listeners[event].forEach(cb => cb(eventData));
        }
    }

    getElementsByTagName(tagName) {
        // This is the heavy operation we want to track
        global.heavyOperationCount++;
        return this.children.filter(c => c.tagName.toLowerCase() === tagName.toLowerCase());
    }
}

// Global counters
global.heavyOperationCount = 0;

// Setup Mock Environment
const documentMock = {
    addEventListener: (event, callback) => {
        if (event === 'DOMContentLoaded') {
            // Store to call later
            global.domLoadedCallback = callback;
        }
    },
    getElementById: (id) => {
        if (id === 'search-input') return global.searchInput;
        if (id === 'article-list') return global.articleList;
        return new MockElement('div', id);
    },
    body: new MockElement('body')
};

const navigatorMock = {}; // No serviceWorker to avoid errors
const windowMock = {
    addEventListener: () => {},
    localStorage: {
        getItem: () => null,
        setItem: () => {}
    }
};

// Setup specific elements
global.searchInput = new MockElement('input', 'search-input');
global.articleList = new MockElement('div', 'article-list');

// Add some dummy articles
for (let i = 0; i < 5; i++) {
    const article = new MockElement('article');
    article.textContent = "Football match result " + i;
    global.articleList.children.push(article);
}

// Create Sandbox
const sandbox = {
    document: documentMock,
    window: windowMock,
    navigator: navigatorMock,
    localStorage: windowMock.localStorage,
    console: { log: () => {} }, // Silence logs
    setTimeout: setTimeout,
    clearTimeout: clearTimeout,
    Array: Array,
    alert: () => {}
};

// Read main.js
const code = fs.readFileSync(path.join(__dirname, '../js/main.js'), 'utf8');

// Run code
vm.createContext(sandbox);
vm.runInContext(code, sandbox);

// Trigger DOMContentLoaded to initialize logic
if (global.domLoadedCallback) {
    global.domLoadedCallback();
}

// Simulation
async function runTest() {
    console.log("Starting simulation...");
    const inputs = ['f', 'fo', 'foo', 'foot', 'footb', 'footba', 'footbal', 'football'];

    // Simulate typing with 50ms interval
    for (const text of inputs) {
        global.searchInput.value = text;
        global.searchInput.trigger('input', { target: global.searchInput });
        await new Promise(resolve => setTimeout(resolve, 50));
    }

    // Wait for debounce if any
    await new Promise(resolve => setTimeout(resolve, 500));

    console.log(`Inputs simulated: ${inputs.length}`);
    console.log(`Heavy operations (search) executed: ${global.heavyOperationCount}`);

    if (global.heavyOperationCount >= inputs.length) {
        console.log("FAIL: Search executed for every input (No debounce).");
        process.exit(1);
    } else if (global.heavyOperationCount <= 2) {
        console.log("PASS: Search executed significantly fewer times than inputs.");
        process.exit(0);
    } else {
        console.log("WARN: Some debounce might be present but not effective enough?");
        process.exit(1);
    }
}

runTest();
