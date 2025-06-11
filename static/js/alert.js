/* jshint esversion: 6 */
/* global bootstrap */

/**
 * Auto-dismiss Bootstrap alert messages after 3 seconds.
 */
document.addEventListener('DOMContentLoaded', function () {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      bootstrap.Alert.getOrCreateInstance(alert).close();
    }, 3000);
  });
});