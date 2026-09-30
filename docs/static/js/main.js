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

    document.querySelectorAll('.project-image.has-carousel').forEach(function (container) {
        var photos = container.querySelectorAll('.project-photo');
        var dots = container.querySelectorAll('.carousel-dot');
        var current = 0;

        var show = function (index) {
            photos[current].classList.remove('active');
            if (dots[current]) dots[current].classList.remove('active');
            current = (index + photos.length) % photos.length;
            photos[current].classList.add('active');
            if (dots[current]) dots[current].classList.add('active');
        };
        container.showPhoto = show;

        var prevBtn = container.querySelector('.carousel-prev');
        var nextBtn = container.querySelector('.carousel-next');

        if (prevBtn) {
            prevBtn.addEventListener('click', function (e) {
                e.stopPropagation();
                show(current - 1);
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', function (e) {
                e.stopPropagation();
                show(current + 1);
            });
        }
    });

    var lightbox = document.getElementById('lightbox');
    var lightboxImage = document.getElementById('lightboxImage');
    var lightboxClose = document.getElementById('lightboxClose');
    var lightboxPrev = document.getElementById('lightboxPrev');
    var lightboxNext = document.getElementById('lightboxNext');
    var lightboxDots = document.getElementById('lightboxDots');
    var triggers = document.querySelectorAll('.js-lightbox-trigger');

    if (lightbox && lightboxImage && triggers.length) {
        var group = [];
        var index = 0;
        var container = null;

        var render = function () {
            lightboxImage.setAttribute('src', group[index].getAttribute('src'));
            lightboxImage.setAttribute('alt', group[index].getAttribute('alt'));
            if (container && container.showPhoto) container.showPhoto(index);
            Array.prototype.forEach.call(lightboxDots.children, function (dot, i) {
                dot.classList.toggle('active', i === index);
            });
        };

        var step = function (delta) {
            if (group.length < 2) return;
            index = (index + delta + group.length) % group.length;
            render();
        };

        var openLightbox = function (img) {
            container = img.closest('.project-image');
            group = Array.prototype.slice.call(container.querySelectorAll('.js-lightbox-trigger'));
            index = group.indexOf(img);
            var multiple = group.length > 1;
            lightboxPrev.hidden = !multiple;
            lightboxNext.hidden = !multiple;
            lightboxDots.innerHTML = '';
            if (multiple) {
                group.forEach(function (_, i) {
                    var dot = document.createElement('button');
                    dot.type = 'button';
                    dot.className = 'carousel-dot';
                    dot.setAttribute('aria-label', 'Photo ' + (i + 1) + ' of ' + group.length);
                    dot.addEventListener('click', function () {
                        index = i;
                        render();
                    });
                    lightboxDots.appendChild(dot);
                });
            }
            render();
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
                openLightbox(img);
            });
            img.addEventListener('keydown', function (e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    openLightbox(img);
                }
            });
        });

        lightboxClose.addEventListener('click', closeLightbox);
        lightboxPrev.addEventListener('click', function () { step(-1); });
        lightboxNext.addEventListener('click', function () { step(1); });

        lightbox.addEventListener('click', function (e) {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });

        document.addEventListener('keydown', function (e) {
            if (!lightbox.classList.contains('open')) return;
            if (e.key === 'Escape') closeLightbox();
            else if (e.key === 'ArrowLeft') step(-1);
            else if (e.key === 'ArrowRight') step(1);
        });
    }
});
