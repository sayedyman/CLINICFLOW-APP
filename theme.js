(function() {
    function applyTheme(theme) {
        if (theme === 'dark') {
            document.documentElement.classList.add('dark-theme');
        } else {
            document.documentElement.classList.remove('dark-theme');
        }
        
        // Update icons if element exists
        updateThemeUI(theme);
    }

    function updateThemeUI(theme) {
        const themeIcon = document.getElementById('themeIcon');
        const themeText = document.getElementById('themeValueText');
        
        if (themeIcon) {
            if (theme === 'dark') {
                // Moon icon
                themeIcon.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                </svg>`;
                themeIcon.style.color = '#e2e8f0';
                themeIcon.style.background = '#2d3748';
            } else {
                // Sun icon
                themeIcon.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="5"></circle>
                    <line x1="12" y1="1" x2="12" y2="3"></line>
                    <line x1="12" y1="21" x2="12" y2="23"></line>
                    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                    <line x1="1" y1="12" x2="3" y2="12"></line>
                    <line x1="21" y1="12" x2="23" y2="12"></line>
                    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                </svg>`;
                themeIcon.style.color = '#64748b';
                themeIcon.style.background = '#f1f5f9';
            }
        }
        
        if (typeof translations !== 'undefined' && themeText) {
            let lang = localStorage.getItem('lang') || 'ar';
            let key = theme === 'dark' ? 'theme_dark' : 'theme_light';
            if (translations[key] && translations[key][lang]) {
                themeText.innerText = translations[key][lang];
            }
        }
    }

    // Attach to window
    window.toggleTheme = function() {
        let current = localStorage.getItem('theme') || 'light';
        let newTheme = current === 'light' ? 'dark' : 'light';
        localStorage.setItem('theme', newTheme);
        applyTheme(newTheme);
    };

    let savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);

    // After DOM loaded, update UI in case translation runs late
    document.addEventListener('DOMContentLoaded', () => {
        let current = localStorage.getItem('theme') || 'light';
        updateThemeUI(current);
        
        // Attach click listener for index.html item
        const toggleBtn = document.getElementById('themeToggleBtn');
        if (toggleBtn) {
            // Need to handle both the click and translation overrides
            toggleBtn.addEventListener('click', () => {
                window.toggleTheme();
            });
        }
    });

})();
