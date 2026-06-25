// Modal functionality
function openModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

// Cerrar modal al hacer clic fuera
window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
        closeModal();
    }
}

// Cerrar modal con tecla ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});

// Manejar envío del formulario
const modalForm = document.querySelector('.modal__form');
if (modalForm) {
    modalForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('¡Noticia publicada exitosamente!');
        closeModal();
        modalForm.reset();
    });
}
