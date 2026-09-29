const initializeSite = () => {
  document.querySelectorAll('header nav').forEach((nav) => {
    const button = document.createElement('button');
    button.className = 'mobile-nav-toggle lg:hidden';
    button.type = 'button';
    button.setAttribute('aria-label', 'Open navigation');
    button.setAttribute('aria-expanded', 'false');
    button.textContent = '☰';
    nav.before(button);

    button.addEventListener('click', () => {
      const isOpen = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!isOpen));
      button.setAttribute('aria-label', isOpen ? 'Open navigation' : 'Close navigation');
      button.textContent = isOpen ? '☰' : '×';
      nav.classList.toggle('mobile-nav-open', !isOpen);
    });
  });

  document.querySelectorAll('form[data-enquiry-form]').forEach((form) => {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const accessKey = form.elements.access_key.value.trim();
      const status = form.querySelector('[data-form-status]');
      const submitButton = form.querySelector('button[type="submit"]');

      if (!accessKey || accessKey === 'YOUR_WEB3FORMS_ACCESS_KEY') {
        status.textContent = 'The enquiry form is not connected yet. Please email lily@carameldigitalstudio.com directly.';
        return;
      }

      status.textContent = 'Sending your enquiry…';
      submitButton.disabled = true;

      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        body: new FormData(form)
      })
        .then(async (response) => {
          const result = await response.json();
          if (!response.ok || !result.success) {
            throw new Error(result.message || 'The enquiry could not be sent. Please email directly instead.');
          }
          form.reset();
          status.textContent = 'Thank you. Your enquiry has been sent.';
        })
        .catch((error) => {
          status.textContent = error.message || 'The enquiry could not be sent. Please email directly instead.';
        })
        .finally(() => {
          submitButton.disabled = false;
        });
    });
  });
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeSite, { once: true });
} else {
  initializeSite();
}