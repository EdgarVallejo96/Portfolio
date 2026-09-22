document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.getElementById('navToggle');
    var nav = document.getElementById('siteNav');
    var cvBtn = document.getElementById('cvDownloadBtn');
    var langBtns = document.querySelectorAll('.lang-btn');

    if (cvBtn && langBtns.length) {
        langBtns.forEach(function (btn) {
            btn.addEventListener('click', function () {
                var lang = btn.dataset.lang;
                langBtns.forEach(function (b) {
                    b.classList.toggle('active', b === btn);
                });
                cvBtn.setAttribute('href', cvBtn.dataset['cv' + lang.charAt(0).toUpperCase() + lang.slice(1)]);
                cvBtn.textContent = cvBtn.dataset['label' + lang.charAt(0).toUpperCase() + lang.slice(1)];
            });
        });
    }

    if (toggle && nav) {
        toggle.addEventListener('click', function () {
            var isOpen = nav.classList.toggle('open');
            toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        });

        nav.querySelectorAll('.nav-link').forEach(function (link) {
            link.addEventListener('click', function () {
                nav.classList.remove('open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }
});
