// 1. Variables and Data Types
const standardGreeting = "Hello"; 
let totalUserCount = 42;          
let systemIsActive = true;       

// 2. Simple Function
function calculateTotal(price, taxRate) {
    return price * (1 + taxRate);
}

// 3. Conditional Statements (If / Else)
if (systemIsActive) {
    console.log(`${standardGreeting}, system is fully operational.`);
} else {
    console.log("System offline.");
}

// 4. Array and Basic Loop
const priorityItems = ["Server", "Database", "API Gateway"];

console.log("Checking modern priority structures:");
priorityItems.forEach((item, index) => {
    console.log(`Resource ${index + 1}: ${item}`);
});

// 5. Execution of Function
const productFinalPrice = calculateTotal(100, 0.15);
console.log(`Final Price with taxes: $${productFinalPrice}`);
