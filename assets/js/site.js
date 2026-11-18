/* FORWARD COFFEE — shared site behaviour */
(() => {
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));

  /* ------------------------------------------------------------------ *
   * Mobile navigation
   * ------------------------------------------------------------------ */
  const menuToggle = $('#menu-toggle');
  const mobileNav = $('#mobile-nav');
  const menuIcon = $('#menu-icon');

  if (menuToggle && mobileNav) {
    const setOpen = (open) => {
      mobileNav.hidden = !open;
      menuToggle.setAttribute('aria-expanded', String(open));
      menuToggle.setAttribute('aria-label', open ? 'Tutup menu' : 'Buka menu');
      if (menuIcon) menuIcon.textContent = open ? 'close' : 'menu';
    };

    menuToggle.addEventListener('click', () => setOpen(mobileNav.hidden));
    $$('a', mobileNav).forEach((link) => link.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && !mobileNav.hidden) setOpen(false);
    });
    window.addEventListener('resize', () => {
      if (window.innerWidth >= 1024) setOpen(false);
    });
  }

  /* ------------------------------------------------------------------ *
   * Toast
   * ------------------------------------------------------------------ */
  const toastEl = $('#toast-notification');
  const toastMessage = $('#toast-message');
  let toastTimer;

  const showToast = (message) => {
    if (!toastEl) return;
    if (toastMessage) toastMessage.textContent = message;
    toastEl.classList.remove('translate-y-20', 'opacity-0', 'pointer-events-none');
    toastEl.classList.add('translate-y-0', 'opacity-100');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toastEl.classList.add('translate-y-20', 'opacity-0', 'pointer-events-none');
      toastEl.classList.remove('translate-y-0', 'opacity-100');
    }, 3200);
  };

  /* ------------------------------------------------------------------ *
   * Reading list (local to this browser)
   * ------------------------------------------------------------------ */
  const BOOKMARK_KEY = 'fc-reading-list';

  const readList = () => {
    try {
      const stored = JSON.parse(localStorage.getItem(BOOKMARK_KEY) || '[]');
      return Array.isArray(stored) ? stored : [];
    } catch (error) {
      return [];
    }
  };

  const writeList = (list) => {
    try {
      localStorage.setItem(BOOKMARK_KEY, JSON.stringify(list));
    } catch (error) {
      /* storage can be unavailable in private windows — the toggle still works visually */
    }
  };

  const bookmarkHandlers = [
    { selector: '#bookmark-lead', id: 'arabica-vs-robusta', label: 'Esai' },
    { selector: '#save-article-btn', id: 'arabica-vs-robusta', label: 'Esai' },
    { selector: '#bookmark-essay-btn', id: 'arabica-vs-robusta', label: 'Esai' },
  ];

  bookmarkHandlers.forEach(({ selector, id, label }) => {
    const button = $(selector);
    if (!button) return;

    const icon = button.querySelector('.material-symbols-outlined');
    const isSaved = () => readList().includes(id);

    const paint = () => {
      const saved = isSaved();
      if (icon) icon.textContent = saved ? 'bookmark' : 'bookmark_border';
      button.setAttribute('aria-pressed', String(saved));
    };

    paint();
    button.addEventListener('click', () => {
      const list = readList();
      const index = list.indexOf(id);
      const adding = index === -1;
      if (adding) list.push(id);
      else list.splice(index, 1);
      writeList(list);
      paint();
      showToast(
        adding
          ? `${label} disimpan ke daftar baca Anda.`
          : `${label} dihapus dari daftar baca Anda.`
      );
    });
  });

  /* ------------------------------------------------------------------ *
   * Share essay
   * ------------------------------------------------------------------ */
  const shareButton = $('#share-essay-btn');
  if (shareButton) {
    shareButton.addEventListener('click', async () => {
      const payload = {
        title: document.title,
        text: 'Arabica vs Robusta — Forward Coffee Journal',
        url: window.location.href,
      };

      try {
        if (navigator.share) {
          await navigator.share(payload);
          return;
        }
        await navigator.clipboard.writeText(payload.url);
        showToast('Tautan esai disalin ke clipboard.');
      } catch (error) {
        showToast('Tautan esai: ' + payload.url);
      }
    });
  }

  /* ------------------------------------------------------------------ *
   * Coffee Journal — search + category filters
   * ------------------------------------------------------------------ */
  const searchInput = $('#journal-search');
  const filterGroup = $('#category-filter-group');
  const articlesGrid = $('#journal-articles-grid');

  if (articlesGrid) {
    const cards = $$('article', articlesGrid);
    const emptyState = document.createElement('p');
    emptyState.className =
      'col-span-full text-center font-body-md text-body-md text-on-surface-variant py-12';
    emptyState.textContent = 'Belum ada catatan yang cocok. Coba kata kunci atau kategori lain.';
    emptyState.style.display = 'none';
    articlesGrid.after(emptyState);

    let activeFilter = 'all';

    const applyFilters = () => {
      const term = (searchInput ? searchInput.value : '').trim().toLowerCase();
      let visible = 0;

      cards.forEach((card) => {
        const matchesCategory =
          activeFilter === 'all' || card.dataset.category === activeFilter;
        const matchesTerm =
          term.length === 0 || card.textContent.toLowerCase().includes(term);
        const show = matchesCategory && matchesTerm;

        card.style.display = show ? '' : 'none';
        if (show) visible += 1;
      });

      emptyState.style.display = visible === 0 ? '' : 'none';
    };

    if (filterGroup) {
      $$('.journal-filter-btn', filterGroup).forEach((button) => {
        button.addEventListener('click', () => {
          activeFilter = button.dataset.filter || 'all';

          $$('.journal-filter-btn', filterGroup).forEach((peer) => {
            const isActive = peer === button;
            peer.classList.toggle('bg-primary-container', isActive);
            peer.classList.toggle('text-on-primary', isActive);
            peer.classList.toggle('bg-surface-container-high', !isActive);
            peer.classList.toggle('text-on-surface', !isActive);
            peer.setAttribute('aria-pressed', String(isActive));
          });

          applyFilters();
        });
      });
    }

    if (searchInput) {
      searchInput.addEventListener('input', applyFilters);
      searchInput.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
          searchInput.value = '';
          applyFilters();
          searchInput.blur();
        }
      });
    }

    applyFilters();
  }

  /* ------------------------------------------------------------------ *
   * Flavor lexicon
   * ------------------------------------------------------------------ */
  const LEXICON = {
    floral: {
      badge: 'Floral Aromatic Family',
      terroir: 'Typical: Gayo Highland Washed • 1,600+ MASL',
      title: 'Jasmine & White Blossom Aromatics',
      desc: 'Delicate, volatile monoterpenes like linalool create ethereal perfume top-notes. These fragile aromatics evaporate rapidly under excessively boiling water and harsh agitation.',
      temp: '91°C – 93°C',
      grind: 'Medium-Coarse Burrs',
      radar: '50,15 78,50 62,80 38,80 22,50',
      acidity: 'Acidity: High',
      sweetness: 'Sweetness: Gentle',
      body: 'Body: Silky Light',
    },
    'brown-sugar': {
      badge: 'Sweet & Caramel Family',
      terroir: 'Typical: Java Preanger Natural • 1,300 MASL',
      title: 'Aren Palm Sugar & Toasted Caramel',
      desc: 'Gula aren dan karamelisasi glukosa membentuk lapisan manis yang lembap dan dalam. Suhu seduh rendah menjaga gula tetap utuh, tanpa rasa gosong yang menutupi buahnya.',
      temp: '88°C – 90°C',
      grind: 'Fine Espresso',
      radar: '50,24 74,46 64,78 40,82 28,54',
      acidity: 'Acidity: Low',
      sweetness: 'Sweetness: Deep',
      body: 'Body: Syrupy',
    },
    citrus: {
      badge: 'Bright Acidic Family',
      terroir: 'Typical: Aceh Gayo Honey • 1,500 MASL',
      title: 'Bergamot, Lemon Zest & Stone Fruit',
      desc: 'Asam sitrat dan malat dari proses honey memunculkan kilau jeruk yang tajam. Rasio seduh 1:16 dan gilingan medium menjaga kecerahan tanpa rasa cuka.',
      temp: '92°C – 94°C',
      grind: 'Medium Burrs',
      radar: '50,18 82,48 58,74 34,78 24,46',
      acidity: 'Acidity: Bright',
      sweetness: 'Sweetness: Crisp',
      body: 'Body: Tea-Like',
    },
    cacao: {
      badge: 'Deep Roast Family',
      terroir: 'Typical: Lampung Robusta • 800 MASL',
      title: 'Dark Cacao Nibs & Bitter Chocolate',
      desc: 'Reaksi Maillard pada sangrai gelap membentuk pirazin dan furan yang pekat. Ekstraksi lebih panjang memberi tekstur beludru dengan aftertaste kakao yang panjang.',
      temp: '94°C – 96°C',
      grind: 'Fine-Medium Burrs',
      radar: '50,28 70,52 66,82 36,84 30,50',
      acidity: 'Acidity: Low',
      sweetness: 'Sweetness: Bittersweet',
      body: 'Body: Heavy Crema',
    },
    spice: {
      badge: 'Warm Spice Family',
      terroir: 'Typical: Bali Kintamani Natural • 1,200 MASL',
      title: 'Cinnamon, Clove & Brown Nutmeg',
      desc: 'Senyawa kayu manis dan eugenol muncul dari fermentasi natural yang matang sempurna. Seduhan lebih pelan menonjolkan rempah hangat di tengah rasa manis.',
      temp: '90°C – 92°C',
      grind: 'Medium-Coarse Burrs',
      radar: '50,22 76,50 60,78 38,80 26,52',
      acidity: 'Acidity: Mellow',
      sweetness: 'Sweetness: Warm',
      body: 'Body: Round',
    },
    bergamot: {
      badge: 'Tea-Like Aromatic Family',
      terroir: 'Typical: Flores Bajawa Washed • 1,400 MASL',
      title: 'Earl Grey, Bergamot Peel & Black Tea',
      desc: 'Aroma teh hitam muncul dari profil washed yang bersih dan sangrai terang. Gunakan air lunak agar tanin tidak mendominasi dan bergamot tetap terbaca.',
      temp: '90°C – 93°C',
      grind: 'Medium Burrs',
      radar: '50,20 78,46 60,76 36,79 24,48',
      acidity: 'Acidity: Bright',
      sweetness: 'Sweetness: Delicate',
      body: 'Body: Light Tea',
    },
  };

  const lexiconButtons = $$('.lexicon-btn');

  if (lexiconButtons.length) {
    const fields = {
      badge: $('#flavor-badge'),
      terroir: $('#flavor-terroir'),
      title: $('#flavor-title'),
      desc: $('#flavor-desc'),
      temp: $('#flavor-temp'),
      grind: $('#flavor-grind'),
      radar: $('#radar-poly'),
      acidity: $('#flavor-acidity'),
      sweetness: $('#flavor-sweetness'),
      body: $('#flavor-body'),
    };

    const setText = (node, value) => {
      if (node) node.textContent = value;
    };

    lexiconButtons.forEach((button) => {
      button.addEventListener('click', () => {
        const flavor = LEXICON[button.dataset.flavor];
        if (!flavor) return;

        lexiconButtons.forEach((peer) => {
          const isActive = peer === button;
          peer.classList.toggle('bg-primary-container', isActive);
          peer.classList.toggle('text-on-primary', isActive);
          peer.classList.toggle('shadow-sm', isActive);
          peer.classList.toggle('bg-surface-container-lowest', !isActive);
          peer.classList.toggle('text-on-surface', !isActive);
          peer.setAttribute('aria-pressed', String(isActive));
        });

        setText(fields.badge, flavor.badge);
        setText(fields.terroir, flavor.terroir);
        setText(fields.title, flavor.title);
        setText(fields.desc, flavor.desc);
        setText(fields.temp, flavor.temp);
        setText(fields.grind, flavor.grind);
        setText(fields.acidity, flavor.acidity);
        setText(fields.sweetness, flavor.sweetness);
        setText(fields.body, flavor.body);
        if (fields.radar) fields.radar.setAttribute('points', flavor.radar);
      });
    });
  }

  /* ------------------------------------------------------------------ *
   * Morning Dispatch subscription form
   * ------------------------------------------------------------------ */
  const dispatchForm = $('#dispatch-form');
  if (dispatchForm) {
    dispatchForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const email = $('#subscriber-email');
      const name = $('#subscriber-name');

      if (email && !email.checkValidity()) {
        email.reportValidity();
        return;
      }

      const firstName = name && name.value.trim() ? name.value.trim().split(' ')[0] : 'Kawan';
      showToast(`Terima kasih, ${firstName}. Sampai jumpa di edisi Sabtu berikutnya.`);
      dispatchForm.reset();
    });
  }
})();
