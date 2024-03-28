const switcher = document.getElementById('theme-switcher');
const html = document.body;

var object = document.querySelector('object[name="resume"]');

// Check for saved theme choice and apply it
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    console.log(`Saved theme: ${savedTheme}`);
    html.classList.add(savedTheme);
    if (savedTheme === 'dark-theme' && object) {
        object.setAttribute('data', 'Research_Resume_Dark.pdf');
    }
}

switcher.addEventListener('click', () => {
    // Add transition class before switching theme
    html.classList.add('transition');

    // Toggle dark theme class on html element
    html.classList.toggle('dark-theme');

    // Save theme choice
    if (html.classList.contains('dark-theme')) {
        localStorage.setItem('theme', 'dark-theme');
        if (object) {
            object.setAttribute('data', 'Research_Resume_Dark.pdf');
        }
    } else {
        if (object) {
            object.setAttribute('data', 'Research_Resume.pdf');
        }
        localStorage.removeItem('theme');
    }

    // Remove transition class after switching theme
    setTimeout(() => {
        html.classList.remove('transition');
    }, 500);
});