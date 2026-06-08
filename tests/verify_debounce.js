// Debounce function implementation to be used in main.js
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Test harness
console.log('Starting Debounce Verification...');

let executionCount = 0;
const expensiveOperation = () => {
    executionCount++;
    console.log('Expensive operation executed!');
};

const debouncedOperation = debounce(expensiveOperation, 100);

// Simulate rapid events (e.g., typing)
console.log('Simulating rapid events...');
debouncedOperation();
debouncedOperation();
debouncedOperation();
debouncedOperation();

// Wait to see if it executes only once
setTimeout(() => {
    console.log(`Execution count: ${executionCount}`);
    if (executionCount === 1) {
        console.log('✅ SUCCESS: Debounce prevented unnecessary executions.');
    } else {
        console.error(`❌ FAILURE: Expected 1 execution, but got ${executionCount}.`);
        process.exit(1);
    }
}, 500);
