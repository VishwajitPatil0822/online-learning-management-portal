document.addEventListener("DOMContentLoaded", function() {
    const slider = document.querySelector(".slider");
    const slides = document.querySelectorAll(".slider img");
    const totalSlides = slides.length;
    const slideWidth = slides[0].clientWidth;
    let currentIndex = 0;

    const dots = document.querySelectorAll(".slider-nav .dot");
    const leftArrow = document.querySelector(".slider-arrow-left");
    const rightArrow = document.querySelector(".slider-arrow-right");

    function updateDots() {
        dots.forEach((dot, index) => {
            dot.style.opacity = index === currentIndex ? "1" : "0.5";
        });
    }

    function scrollToSlide(index) {
        slider.scrollLeft = index * slideWidth;
        updateDots();
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % totalSlides;
        scrollToSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        scrollToSlide(currentIndex);
    }

    rightArrow.addEventListener("click", nextSlide);
    leftArrow.addEventListener("click", prevSlide);

    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            currentIndex = index;
            scrollToSlide(currentIndex);
        });
    });

    updateDots();
});
