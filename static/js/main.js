document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.getElementById('navToggle');
    var nav = document.getElementById('siteNav');

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

    var lightbox = document.getElementById('lightbox');
    var lightboxImage = document.getElementById('lightboxImage');
    var lightboxClose = document.getElementById('lightboxClose');
    var triggers = document.querySelectorAll('.js-lightbox-trigger');

    if (lightbox && lightboxImage && triggers.length) {
        var openLightbox = function (src, alt) {
            lightboxImage.setAttribute('src', src);
            lightboxImage.setAttribute('alt', alt);
            lightbox.classList.add('open');
            lightbox.setAttribute('aria-hidden', 'false');
        };

        var closeLightbox = function () {
            lightbox.classList.remove('open');
            lightbox.setAttribute('aria-hidden', 'true');
            lightboxImage.setAttribute('src', '');
        };

        triggers.forEach(function (img) {
            img.addEventListener('click', function () {
                openLightbox(img.getAttribute('src'), img.getAttribute('alt'));
            });
            img.addEventListener('keydown', function (e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    openLightbox(img.getAttribute('src'), img.getAttribute('alt'));
                }
            });
        });

        lightboxClose.addEventListener('click', closeLightbox);

        lightbox.addEventListener('click', function (e) {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && lightbox.classList.contains('open')) {
                closeLightbox();
            }
        });
    }
});
