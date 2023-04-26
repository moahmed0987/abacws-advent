function hideFlash(idx) {
    document.getElementById(idx).style.display = "none";
    // document.querySelector(".alert-message").style.display = "none";
}

document.addEventListener('DOMContentLoaded', function() {

    var alerts = document.querySelectorAll('.alert-message');

    alerts.forEach(function(alert) {
    setTimeout(function() {
        alert.classList.add('fade-out');
        setTimeout(function() {
        alert.parentNode.removeChild(alert);
        }, 500);
    }, 5000); // 5 seconds
    });
    });