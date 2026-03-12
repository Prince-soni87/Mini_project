// Chat functionality
function sendMessage() {
    let input = document.getElementById("user-input")
    let msg = input.value

    fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        let chat = document.getElementById("chat-box")
        chat.innerHTML += `<p><b>You:</b> ${msg}</p>`
        chat.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`
        input.value = ""
        chat.scrollTop = chat.scrollHeight
    })
    .catch(err => console.error(err))
}

// Landing Page Interactivity
document.addEventListener('DOMContentLoaded', function() {
    // Parallax effect on mouse move
    const landingWrapper = document.querySelector('.landing-wrapper');
    const blobs = document.querySelectorAll('.bg-blob');
    
    if (landingWrapper) {
        document.addEventListener('mousemove', (e) => {
            const x = e.clientX / window.innerWidth;
            const y = e.clientY / window.innerHeight;
            
            blobs.forEach((blob, index) => {
                const depth = (index + 1) * 20;
                blob.style.transform = `translate(${x * depth}px, ${y * depth}px)`;
            });
        });
    }

    // Feature cards hover effect with 3D tilt
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(10px)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)';
        });
    });

    // Smooth scroll for CTA button
    const ctaBtn = document.querySelector('.cta-btn');
    if (ctaBtn) {
        ctaBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const href = ctaBtn.getAttribute('href');
            if (href) {
                window.location.href = href;
            }
        });
    }

    // Scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    featureCards.forEach(card => {
        observer.observe(card);
    });
});
