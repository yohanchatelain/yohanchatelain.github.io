const switcher = document.getElementById('theme-switcher');
const body = document.body;

// Check for saved theme choice and apply it
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    body.classList.add(savedTheme);
}

if (switcher) switcher.addEventListener('click', () => {
    // Add transition class before switching theme
    body.classList.add('transition');

    // Toggle dark theme class on html element
    body.classList.toggle('dark-theme');

    // Save theme choice
    const isDark = body.classList.contains('dark-theme');
    if (isDark) {
        localStorage.setItem('theme', 'dark-theme');
    } else {
        localStorage.removeItem('theme');
    }

    // Remove transition class after switching theme
    setTimeout(() => {
        body.classList.remove('transition');
    }, 500);
});
