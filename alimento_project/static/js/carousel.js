function changeSlide() {
    let nextBtn = document.querySelector('a.carousel-control-next');
    setInterval(() => {
        nextBtn.click();
    }, 5000)
}
changeSlide();