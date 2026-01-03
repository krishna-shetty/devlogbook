document.addEventListener("DOMContentLoaded", function () {
  // gsap.to(".cover__title--bop", {
  //   y: -4,
  //   repeat: -1,
  //   duration: 0.86,
  //   yoyo: true,
  //   ease: "power2.inOut"
  // });

  gsap.to(".--shake", {
    x: 1,
    y: -1,
    repeat: -1,
    duration: 0.1,
    yoyo: true,
    ease: "power2.inOut"
  });

gsap.to(".scroll-indicator--bop", {
  y: -10,
  repeat: -1,
  duration: 1.5,
  yoyo: true,
  ease: "elastic.out(1, 0.8)"
});

gsap.from(".cover__title--bop", {
  scale: 0.9,
  ease: "back.out(1.7)",
  duration: 1,
  repeat: -1,
  yoyo: true
});

  const scrollIndicators = document.querySelectorAll('.scroll-indicator');
  let isScrolling = false;

  // Function to check if the screen is small
  function isSmallScreen() {
    return window.innerWidth <= 1166;
  }

  function updateScrollIndicators() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (isSmallScreen()) {
      // Always hide on small screens
      gsap.set(scrollIndicators, { opacity: 0 });
      return;
    }

    if (scrollTop > 50) {
      if (!isScrolling) {
        isScrolling = true;
        gsap.to(scrollIndicators, {
          opacity: 0,
          duration: 0.3,
          ease: "power2.out"
        });
      }
    } else {
      if (isScrolling) {
        isScrolling = false;
        gsap.to(scrollIndicators, {
          opacity: 1,
          duration: 0.3,
          ease: "power2.out"
        });
      }
    }
  }

  window.addEventListener('scroll', updateScrollIndicators);
  window.addEventListener('resize', updateScrollIndicators);
  window.addEventListener('load', updateScrollIndicators);
});