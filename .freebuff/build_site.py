"""Assemble the FORWARD COFFEE website from the Stitch export set.

Run from the project root:  python .freebuff/build_site.py
Outputs: index.html, about.html, journal.html, article.html, assets/img/*
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from urllib.request import Request, urlopen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "stitch_forward_coffee_brand_platform")

PAGES = [
    {
        "key": "home",
        "dir": "forward_coffee_desktop_homepage",
        "out": "index.html",
        "nav": "home",
        "title": "FORWARD COFFEE — Kopi Botolan & Jurnal Kopi Harian",
        "desc": "Forward Coffee menemani perjalanan sehari-hari: kopi botolan batch kecil dari nusantara, cerita origin, dan jurnal kopi harian.",
    },
    {
        "key": "about",
        "dir": "about_forward_coffee_desktop",
        "out": "about.html",
        "nav": "about",
        "title": "About Forward Coffee — Filosofi & Kerajinan",
        "desc": "Kisah Forward Coffee: kopi yang menemani secara tenang, diseduh dalam batch kecil dengan biji pilihan nusantara.",
    },
    {
        "key": "journal",
        "dir": "coffee_journal_forward_coffee_desktop",
        "out": "journal.html",
        "nav": "coffee-journal",
        "title": "Coffee Journal — Edisi & Catatan Seduh",
        "desc": "Coffee Journal Forward Coffee: catatan seduh, ilmu sangrai, origin, dan ritual kopi harian.",
    },
    {
        "key": "article",
        "dir": "article_detail_forward_coffee_desktop",
        "out": "article.html",
        "nav": "coffee-journal",
        "title": "Arabica vs Robusta — Forward Coffee Journal",
        "desc": "Anatomi Arabica dan Robusta: ketinggian tanam, kadar kafein, tekstur, dan catatan rasa dari laboratorium Forward Coffee.",
    },
]

NAV_ITEMS = [
    ("index.html", "Home", "home"),
    ("about.html", "About", "about"),
    ("index.html#our-coffee", "Our Coffee", "our-coffee"),
    ("journal.html", "Coffee Journal", "coffee-journal"),
    ("index.html#community", "Community", "community"),
    ("index.html#contact", "Contact", "contact"),
]

PATH_MAP = {
    "home": "index.html",
    "about": "about.html",
    "our-coffee": "index.html#our-coffee",
    "coffee-journal": "journal.html",
    "community": "index.html#community",
    "contact": "index.html#contact",
}

LINK_BASE = (
    "relative py-space-xs font-body-md text-body-md text-on-surface-variant "
    "hover:text-primary-container transition-colors "
    "after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full "
    "after:h-[1.5px] after:bg-primary-container after:scale-x-0 after:origin-left "
    "after:transition-transform hover:after:scale-x-100"
)

LINK_ACTIVE = (
    "relative py-space-xs transition-colors "
    "after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-full "
    "after:h-[1.5px] after:bg-primary-container after:origin-left "
    "after:transition-transform text-primary-container font-semibold after:scale-x-100"
)

FONT_LINK = (
    '<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@'
    "0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&amp;family=Plus+Jakarta+Sans:"
    'wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>'
    '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:'
    'opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>'
)


def read(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def write(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


# ---------------------------------------------------------------- template
def build_header(active: str) -> str:
    desktop = []
    mobile = []
    for href, label, key in NAV_ITEMS:
        if key == active:
            desktop.append(
                f'<a aria-current="page" class="{LINK_ACTIVE}" href="{href}">{label}</a>'
            )
            mobile.append(
                '<a aria-current="page" class="block py-space-sm border-b '
                'border-outline-variant/40 font-body-md text-body-md '
                f'text-primary-container font-semibold" href="{href}">{label}</a>'
            )
        else:
            desktop.append(f'<a class="{LINK_BASE}" href="{href}">{label}</a>')
            mobile.append(
                '<a class="block py-space-sm border-b border-outline-variant/40 '
                'font-body-md text-body-md text-on-surface-variant '
                f'hover:text-primary-container transition-colors" href="{href}">{label}</a>'
            )

    return (
        '<header class="fixed top-0 left-0 w-full z-50 bg-surface/90 backdrop-blur-md '
        'shadow-[0_1px_8px_rgba(21,31,20,0.04)]">'
        '<div class="h-16 max-w-7xl mx-auto px-margin md:px-margin-desktop flex items-center justify-between">'
        '<div class="flex items-center gap-space-sm">'
        '<a class="group flex items-center gap-space-sm shrink-0" '
        'aria-label="Forward Coffee — Home" href="index.html">'
        '<img alt="" aria-hidden="true" class="h-9 w-auto shrink-0" '
        'src="assets/img/logo-forward.svg" width="62" height="131">'
        '<span class="font-headline-sm text-headline-sm tracking-tight text-primary-container '
        'whitespace-nowrap group-hover:text-primary transition-colors">FORWARD COFFEE</span>'
        "</a></div>"
        f'<nav class="hidden lg:flex items-center gap-space-lg" aria-label="Navigasi utama">{"".join(desktop)}</nav>'
        '<div class="flex items-center gap-space-md">'
        '<a class="hidden sm:inline-flex items-center gap-space-xs px-space-md py-space-xs '
        'rounded-full bg-surface-container-high text-primary-container font-label-subtle '
        'text-label-subtle hover:bg-secondary-container hover:text-on-secondary-fixed '
        'transition-colors shadow-[0_1px_4px_rgba(21,31,20,0.04)]" href="journal.html">'
        '<span class="w-1.5 h-1.5 rounded-full bg-primary-container"></span>'
        '<span>Issue #142</span><span class="text-on-surface-variant">•</span>'
        '<span class="hidden md:inline">Daily Briefing</span></a>'
        '<button aria-controls="mobile-nav" aria-expanded="false" aria-label="Buka menu" '
        'class="lg:hidden flex items-center justify-center p-space-xs text-primary-container" '
        'id="menu-toggle" type="button">'
        '<span class="material-symbols-outlined" id="menu-icon">menu</span>'
        "</button></div></div>"
        '<div class="lg:hidden border-t border-outline-variant/40 bg-surface/95 backdrop-blur-md" '
        'id="mobile-nav" hidden>'
        '<nav aria-label="Navigasi seluler" class="max-w-7xl mx-auto px-margin py-space-sm flex flex-col">'
        f'{"".join(mobile)}'
        '<a class="mt-space-md mb-space-sm inline-flex items-center justify-center rounded-full '
        'bg-primary-container text-on-primary font-subhead text-subhead px-space-lg py-space-sm" '
        'href="journal.html">Baca Daily Briefing</a>'
        "</nav></div></header>"
    )


FOOTER_LINKS = [
    ("index.html", "Home"),
    ("about.html", "About Forward"),
    ("index.html#our-coffee", "Our Coffee Vignettes"),
    ("journal.html", "Coffee Journal Editions"),
    ("index.html#community", "Community &amp; Salons"),
    ("index.html#contact", "Barista Inquiries"),
]

FOOTER = (
    '<footer class="w-full bg-primary-container text-on-primary py-space-xl">'
    '<div class="max-w-7xl mx-auto px-margin md:px-margin-desktop">'
    '<div class="grid grid-cols-1 md:grid-cols-12 gap-space-xl pb-space-xl">'
    '<div class="md:col-span-5 flex flex-col justify-between space-y-space-md"><div>'
    '<span class="font-headline-md text-headline-md tracking-tight block text-surface">FORWARD COFFEE</span>'
    '<p class="font-headline-sm text-headline-sm italic text-tertiary-fixed mt-space-xs font-normal">'
    "“Move Forward, One Sip at a Time.”</p>"
    '<p class="font-body-sm text-body-sm text-tertiary-fixed-dim mt-space-sm max-w-sm">'
    "Menemani perjalanan sehari-hari. A quiet editorial coffee journal capturing origin terroir, "
    "slow-steeped craft, and morning rituals across the Indonesian archipelago.</p></div>"
    '<div class="flex items-center gap-space-sm pt-space-xs">'
    '<span class="w-2 h-2 rounded-full bg-primary-fixed"></span>'
    '<span class="font-label-caps text-label-caps uppercase tracking-wider text-tertiary-fixed-dim">'
    "Jakarta • Bandung • Bali</span></div></div>"
    '<div class="md:col-span-3 space-y-space-sm">'
    '<h3 class="font-label-caps text-label-caps uppercase tracking-widest text-tertiary-fixed-dim">'
    "Navigasi Editorial</h3><ul class=\"space-y-space-xs\">"
    + "".join(
        '<li><a class="font-body-sm text-body-sm text-tertiary-fixed hover:text-surface '
        f'transition-colors block" href="{href}">{label}</a></li>'
        for href, label in FOOTER_LINKS
    )
    + "</ul></div>"
    '<div class="md:col-span-4 space-y-space-sm">'
    '<h3 class="font-label-caps text-label-caps uppercase tracking-widest text-tertiary-fixed-dim">'
    "Sambung Rasa &amp; Ruang</h3>"
    '<p class="font-body-sm text-body-sm text-tertiary-fixed-dim">'
    "Hubungi meja editorial atau barista kurator kami untuk diskusi origin, kolaborasi sastra kopi, "
    "dan reservasi seduh khusus.</p>"
    '<div class="flex flex-col gap-space-xs pt-space-xs">'
    '<a class="inline-flex items-center gap-space-xs font-body-sm text-body-sm text-tertiary-fixed '
    'hover:text-surface transition-colors" href="https://instagram.com/forwardcoffee_" '
    'rel="noopener noreferrer" target="_blank">'
    '<span class="material-symbols-outlined text-sm">alternate_email</span>'
    "<span>@forwardcoffee_</span></a>"
    '<a class="inline-flex items-center gap-space-xs font-body-sm text-body-sm text-tertiary-fixed '
    'hover:text-surface transition-colors" href="index.html#contact">'
    '<span class="material-symbols-outlined text-sm">chat</span>'
    "<span>WhatsApp Concierge (+62 811-FORWARD)</span></a>"
    '<a class="inline-flex items-center gap-space-xs font-body-sm text-body-sm text-tertiary-fixed '
    'hover:text-surface transition-colors" href="journal.html">'
    '<span class="material-symbols-outlined text-sm">auto_stories</span>'
    "<span>Read Daily Briefing Archive</span></a>"
    "</div></div></div>"
    '<div class="pt-space-lg flex flex-col md:flex-row items-center justify-between gap-space-md '
    'text-tertiary-fixed-dim">'
    '<p class="font-body-sm text-body-sm">© 2026 Forward Coffee Roasters &amp; Publishing. All rights reserved.</p>'
    '<div class="flex items-center gap-space-lg font-label-subtle text-label-subtle">'
    '<span class="italic font-headline-sm text-headline-sm text-tertiary-fixed">'
    "Menemani perjalanan sehari-hari</span></div></div></div></footer>"
)

TOAST = (
    '<div aria-live="polite" aria-atomic="true" id="toast-notification" '
    'class="fixed bottom-6 right-6 z-[60] transform translate-y-20 opacity-0 '
    'pointer-events-none transition-all duration-300 bg-primary-container text-on-primary '
    'px-space-md py-space-sm rounded-lg shadow-xl flex items-center gap-space-xs '
    'font-body-sm text-body-sm" role="status">'
    '<span class="material-symbols-outlined text-primary-fixed text-base">check_circle</span>'
    '<span id="toast-message">Tersimpan.</span></div>'
)


def build_page(page: dict, body_main: str, body_class: str, html_open: str) -> str:
    return (
        "<!DOCTYPE html>\n"
        f'{html_open}\n<head><meta charset="utf-8"/>'
        '<meta content="width=device-width, initial-scale=1.0" name="viewport"/>'
        f"<title>{page['title']}</title>"
        f'<meta name="description" content="{page["desc"]}"/>'
        '<meta content="#fdf9f0" name="theme-color"/>'
        '<link href="https://fonts.googleapis.com" rel="preconnect"/>'
        '<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>'
        + FONT_LINK
        + '<link href="assets/css/tailwind.css" rel="stylesheet"/></head>'
        f'<body class="{body_class}">'
        + build_header(page["nav"])
        + body_main
        + FOOTER
        + TOAST
        + '<script defer src="assets/js/site.js"></script></body></html>\n'
    )


# ---------------------------------------------------------------- images
def localise_images(pages: dict[str, str]) -> dict[str, str]:
    urls: list[str] = []
    for html in pages.values():
        for url in re.findall(r'src="(https://lh3\.googleusercontent\.com[^"]+)"', html):
            if url not in urls:
                urls.append(url)

    mapping: dict[str, str] = {}
    out_dir = os.path.join(ROOT, "assets", "img")
    os.makedirs(out_dir, exist_ok=True)

    for index, url in enumerate(urls, start=1):
        digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
        cached = [
            name
            for name in os.listdir(out_dir)
            if name.startswith("img-") and f"-{digest}." in name
        ]
        if cached:
            mapping[url] = f"assets/img/{cached[0]}"
            continue
        try:
            request = Request(
                url,
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
                    )
                },
            )
            with urlopen(request, timeout=45) as response:
                data = response.read()
                content_type = response.headers.get("Content-Type", "image/jpeg")
        except Exception as error:  # keep the remote asset if the download fails
            print(f"  ! image {index} failed ({error}); keeping remote URL", file=sys.stderr)
            continue

        if data[:8] == b"\x89PNG\r\n\x1a\n":
            ext = "png"
        elif data[:4] == b"RIFF" and data[8:12] == b"WEBP":
            ext = "webp"
        else:
            ext = "jpg"

        name = f"img-{index:02d}-{digest}.{ext}"
        with open(os.path.join(out_dir, name), "wb") as handle:
            handle.write(data)
        mapping[url] = f"assets/img/{name}"

    print(f"  images: {len(mapping)}/{len(urls)} downloaded")
    return mapping


# ---------------------------------------------------------------- helpers
def fix_images(html: str, mapping: dict[str, str]) -> str:
    for url, path in mapping.items():
        html = html.replace(url, path)

    counter = {"n": 0}

    def handle(match: re.Match[str]) -> str:
        tag = match.group(0)
        alt = re.search(r'data-alt="([^"]*)"', tag)
        tag = re.sub(r'\s*data-alt="[^"]*"', "", tag)
        if alt and " alt=" not in tag:
            tag = tag.replace("/>", f' alt="{alt.group(1)}"/>') if tag.endswith("/>") else tag[:-1] + f' alt="{alt.group(1)}">'
        counter["n"] += 1
        if counter["n"] > 2 and "loading=" not in tag:
            tag = tag.replace("/>", ' loading="lazy" decoding="async"/>') if tag.endswith("/>") else tag[:-1] + ' loading="lazy" decoding="async">'
        return tag

    return re.sub(r"<img\b[^>]*>", handle, html)


def rewrite_paths(html: str) -> str:
    for key, href in PATH_MAP.items():
        html = html.replace(f'data-path="{key}" href="#"', f'data-path="{key}" href="{href}"')
        html = html.replace(f'href="#" data-path="{key}"', f'href="{href}" data-path="{key}"')
    return html


def add_anchor(html: str, comment: str, anchor: str) -> str:
    pattern = re.compile(
        r"(<!--\s*SECTION\s+" + comment + r"\b.*?-->\s*<section)(\s+class=\")", re.S
    )
    return pattern.sub(
        lambda m: f'{m.group(1)} id="{anchor}" class="scroll-mt-20 ', html, count=1
    )


def transform(page: dict, html: str) -> str:
    key = page["key"]

    # drop the duplicated toast the article export ships with
    html = re.sub(
        r'<div[^>]*id="toast-notification"[^>]*>.*?</div>\s*',
        "",
        html,
        count=1,
        flags=re.S,
    )

    html = rewrite_paths(html)

    if key == "home":
        html = add_anchor(html, "04", "our-coffee")
        html = add_anchor(html, "06", "community")
        html = add_anchor(html, "08", "contact")
        # story cards in "What's Brewing?" get a real destination
        html = re.sub(
            r'<span class="(font-label-subtle text-label-subtle text-primary-container '
            r'group-hover:underline inline-flex items-center gap-1)">\s*([^<]+?)\s*</span>',
            lambda m: f'<a class="\1" href="journal.html">{m.group(2)}</a>',
            html,
        )
        # the featured knowledge essay is the Arabica vs Robusta article
        html = re.sub(
            r'data-path="coffee-journal" href="journal\.html">(\s*)<span>Baca Artikel Lengkap</span>',
            r'data-path="coffee-journal" href="article.html">\1<span>Baca Artikel Lengkap</span>',
            html,
            count=1,
        )

    if key == "about":
        html = html.replace('href="#">', 'href="index.html#contact">', 1)

    if key == "journal":
        html = html.replace('href="#flavor-lexicon"', 'href="article.html"')
        html = re.sub(
            r'<button class="([^"]*)" type="button">\s*<span>Read Note</span>'
            r'\s*<span class="material-symbols-outlined text-sm">arrow_forward</span>\s*</button>',
            r'<a class="\1" href="article.html"><span>Read Note</span>'
            r'<span class="material-symbols-outlined text-sm">arrow_forward</span></a>',
            html,
        )
        # identifiers the lexicon panel updates at runtime
        html = html.replace(
            "<span>Acidity: High</span>", '<span id="flavor-acidity">Acidity: High</span>'
        )
        html = html.replace(
            "<span>Sweetness: Gentle</span>",
            '<span id="flavor-sweetness">Sweetness: Gentle</span>',
        )
        html = html.replace(
            "<span>Body: Silky Light</span>", '<span id="flavor-body">Body: Silky Light</span>'
        )

    if key == "article":
        html = re.sub(
            r'<a class="hover:text-primary-container transition-colors" href="#">Coffee Journal</a>',
            '<a class="hover:text-primary-container transition-colors" href="journal.html">Coffee Journal</a>',
            html,
        )
        html = re.sub(
            r'(<a class="[^"]*" href=")#(">\s*<span>View All Journal</span>)',
            r"\1journal.html\2",
            html,
        )
        html = html.replace(
            'class="group bg-surface-container-lowest rounded-xl overflow-hidden shadow-sm '
            'hover:shadow-md transition-all duration-300 flex flex-col" href="#"',
            'class="group bg-surface-container-lowest rounded-xl overflow-hidden shadow-sm '
            'hover:shadow-md transition-all duration-300 flex flex-col" href="journal.html"',
        )

    leftover = re.findall(r'href="#"(?!\s)', html)
    if leftover:
        print(f"  warning: {len(leftover)} empty link(s) left on {page['out']}", file=sys.stderr)

    return html


# ---------------------------------------------------------------- config
def write_tailwind_config(export_html: str) -> None:
    match = re.search(r"tailwind\.config=(\{.*?\});</script>", export_html, re.S)
    if not match:
        raise SystemExit("Could not find the exported tailwind config")
    theme = match.group(1)
    config = (
        "/* Generated from the Stitch export — design tokens live here. */\n"
        "const tokens = " + theme + ";\n\n"
        "module.exports = {\n"
        "  ...tokens,\n"
        "  content: ['./*.html', './assets/js/**/*.js'],\n"
        "};\n"
    )
    write(os.path.join(ROOT, "tailwind.config.js"), config)
    print("  tailwind.config.js written")


# ---------------------------------------------------------------- main
def main() -> None:
    pages: dict[str, str] = {}
    meta: dict[str, dict] = {}

    for page in PAGES:
        source = read(os.path.join(SRC, page["dir"], "code.html"))
        body_class = re.search(r'<body\s+class="([^"]+)"', source).group(1)
        html_open = re.search(r"<html[^>]*>", source).group(0)
        main_html = source[source.index("<main"): source.rindex("</main>") + len("</main>")]
        pages[page["key"]] = main_html
        meta[page["key"]] = {"body_class": body_class, "html_open": html_open}

    write_tailwind_config(read(os.path.join(SRC, "forward_coffee_desktop_homepage", "code.html")))

    mapping = localise_images(pages)

    # the Stitch export ships one dead placeholder URL on the About page — point it
    # at the studio bottle photograph the rest of the brand set uses.
    homepage = read(os.path.join(SRC, "forward_coffee_desktop_homepage", "code.html"))
    hero_tag = re.search(
        r'<img[^>]*data-alt="Warm studio aesthetic shot of two Forward Coffee glass bottles[^"]*"[^>]*>',
        homepage,
    )
    dead_url = "https://lh3.googleusercontent.com/aida/ALJJyrDaJ7B5jP-Z7lD-f-n2c4k_9G7L8TqP1uD4E1bA3tXoY6mK8xP4c6e9w7-r1zG0vB8m"
    if hero_tag:
        hero_src = re.search(r'src="([^"]+)"', hero_tag.group(0)).group(1)
        if hero_src in mapping:
            mapping[dead_url] = mapping[hero_src]

    for page in PAGES:
        main_html = pages[page["key"]]
        main_html = fix_images(main_html, mapping)
        main_html = transform(page, main_html)
        document = build_page(page, main_html, meta[page["key"]]["body_class"], meta[page["key"]]["html_open"])
        write(os.path.join(ROOT, page["out"]), document)
        print(f"  built {page['out']}")


if __name__ == "__main__":
    main()
