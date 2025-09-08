const switcher = document.getElementById('theme-switcher');
const body = document.body;

function getResumeEl() {
  return document.querySelector('object[name="resume"], iframe[name="resume"]');
}

function setResumeToLightPDF() {
  const el = getResumeEl();
  if (!el) return;
  const lightSrc = '/Research_Resume.pdf';
  const tag = el.tagName.toLowerCase();
  if (tag === 'iframe') {
    el.setAttribute('src', lightSrc);
  } else {
    el.setAttribute('data', lightSrc);
  }

  const link = document.getElementById('resume-download');
  if (link) {
    link.setAttribute('href', lightSrc);
  }
}

// Check for saved theme choice and apply it
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    body.classList.add(savedTheme);
}
// Ensure resume always points to the light PDF
setResumeToLightPDF();

if (switcher) switcher.addEventListener('click', () => {
    // Add transition class before switching theme
    body.classList.add('transition');

    // Toggle dark theme class on html element
    body.classList.toggle('dark-theme');

    // Save theme choice
    const isDark = body.classList.contains('dark-theme');
    if (isDark) {
        localStorage.setItem('theme', 'dark-theme');
        setResumeToLightPDF();
    } else {
        setResumeToLightPDF();
        localStorage.removeItem('theme');
    }

    // Remove transition class after switching theme
    setTimeout(() => {
        body.classList.remove('transition');
    }, 500);
});
