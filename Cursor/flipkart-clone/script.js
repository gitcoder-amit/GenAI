const products = [
    { name: "Smartphone", price: "₹15,000" },
    { name: "Headphones", price: "₹2,000" },
    { name: "Laptop", price: "₹45,000" },
    { name: "Watch", price: "₹3,000" }
];

const grid = document.getElementById('product-grid');

products.forEach(product => {
    const card = document.createElement('div');
    card.className = 'product-card';
    card.innerHTML = `<h3>${product.name}</h3><p>${product.price}</p><button>Add to Cart</button>`;
    grid.appendChild(card);
});
