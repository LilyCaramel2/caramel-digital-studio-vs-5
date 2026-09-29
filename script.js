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
      const fields = new FormData(form);
      const name = String(fields.get('name') || '').trim();
      const email = String(fields.get('email') || '').trim();
      const business = String(fields.get('business') || '').trim();
      const message = String(fields.get('message') || '').trim();
      const subject = business ? `Project enquiry: ${business}` : 'Caramel Digital Studio project enquiry';
      const body = [`Name: ${name}`, `Email: ${email}`, `Business or project: ${business || 'Not provided'}`, '', message].join('\n');
      window.location.href = `mailto:lily@carameldigitalstudio.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
  });
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeSite, { once: true });
} else {
  initializeSite();
}