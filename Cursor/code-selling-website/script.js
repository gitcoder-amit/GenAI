document.addEventListener(DOMContentLoaded, () => {
    console.log(CodeMarket website loaded successfully!);

    // Example: Basic interactivity for buttons
    const exploreButton = document.querySelector(.hero button);
    if (exploreButton) {
        exploreButton.addEventListener(click, () => {
            alert(Exploring our code collection!);
            // In a real app, this would scroll to the listings or navigate
        });
    }

    const viewDetailButtons = document.querySelectorAll(.code-card button);
    viewDetailButtons.forEach(button => {
        button.addEventListener(click, (event) => {
            const cardTitle = event.target.closest(.code-card).querySelector(h3).textContent;
            alert(`Viewing details for: ${cardTitle}`);
            // In a real app, this would navigate to a product detail page
        });
    });
});
