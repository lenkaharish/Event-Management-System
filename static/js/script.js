// Form validation
document.addEventListener('DOMContentLoaded', function() {
    // Validate email format
    const emailInputs = document.querySelectorAll('input[type="email"]');
    emailInputs.forEach(input => {
        input.addEventListener('blur', function() {
            const email = this.value;
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (email && !emailRegex.test(email)) {
                this.classList.add('is-invalid');
            } else {
                this.classList.remove('is-invalid');
            }
        });
    });

    // Validate number fields
    const numberInputs = document.querySelectorAll('input[type="number"]');
    numberInputs.forEach(input => {
        input.addEventListener('change', function() {
            if (this.min && parseInt(this.value) < parseInt(this.min)) {
                this.value = this.min;
            }
            if (this.max && parseInt(this.value) > parseInt(this.max)) {
                this.value = this.max;
            }
        });
    });

    // Validate required fields on form submit
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.classList.add('is-invalid');
                    isValid = false;
                } else {
                    field.classList.remove('is-invalid');
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });

    // Auto-dismiss alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 4000);
    });

    // Search filter for events
    const searchInput = document.getElementById('id_search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            // Real-time search can be implemented here
        });
    }

    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('a[href*="/delete/"]');
    deleteButtons.forEach(button => {
        if (!button.form) {
            button.addEventListener('click', function(e) {
                if (!confirm('Are you sure you want to delete this?')) {
                    e.preventDefault();
                }
            });
        }
    });
});

// Format currency
function formatCurrency(value) {
    return '₹' + parseFloat(value).toFixed(2);
}

// Show notification
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.insertBefore(alertDiv, document.body.firstChild);
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// Calculate ticket price
function calculatePrice(quantity, pricePerTicket) {
    return quantity * pricePerTicket;
}
