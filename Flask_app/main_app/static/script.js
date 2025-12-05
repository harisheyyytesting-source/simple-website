// Create floating particles dynamically
const numParticles = 50;
for (let i = 0; i < numParticles; i++) {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    particle.style.top = Math.random() * window.innerHeight + 'px';
    particle.style.left = Math.random() * window.innerWidth + 'px';
    particle.style.width = Math.random() * 6 + 4 + 'px';
    particle.style.height = particle.style.width;
    particle.style.animationDuration = Math.random() * 5 + 5 + 's';
    document.body.appendChild(particle);
}
