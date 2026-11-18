---
name: Warm Editorial Quietude
colors:
  surface: '#fdf9f0'
  surface-dim: '#dddad1'
  surface-bright: '#fdf9f0'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3ea'
  surface-container: '#f1eee5'
  surface-container-high: '#ece8df'
  surface-container-highest: '#e6e2d9'
  on-surface: '#1c1c16'
  on-surface-variant: '#444842'
  inverse-surface: '#31302b'
  inverse-on-surface: '#f4f0e7'
  outline: '#747871'
  outline-variant: '#c4c8c0'
  surface-tint: '#566153'
  primary: '#000200'
  on-primary: '#ffffff'
  primary-container: '#151f14'
  on-primary-container: '#7c8879'
  inverse-primary: '#becab9'
  secondary: '#675d4e'
  on-secondary: '#ffffff'
  secondary-container: '#eee1cd'
  on-secondary-container: '#6d6353'
  tertiary: '#010201'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1d17'
  on-tertiary-container: '#85857d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae6d4'
  primary-fixed-dim: '#becab9'
  on-primary-fixed: '#141e13'
  on-primary-fixed-variant: '#3f4a3d'
  secondary-fixed: '#eee1cd'
  secondary-fixed-dim: '#d2c5b2'
  on-secondary-fixed: '#211b0f'
  on-secondary-fixed-variant: '#4e4637'
  tertiary-fixed: '#e4e3d9'
  tertiary-fixed-dim: '#c8c7be'
  on-tertiary-fixed: '#1b1c16'
  on-tertiary-fixed-variant: '#474740'
  background: '#fdf9f0'
  on-background: '#1c1c16'
  surface-variant: '#e6e2d9'
typography:
  display-hero:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 54px
  display-hero-mobile:
    fontFamily: Newsreader
    fontSize: 34px
    fontWeight: '400'
    lineHeight: 40px
  headline-lg:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '500'
    lineHeight: 44px
  headline-lg-mobile:
    fontFamily: Newsreader
    fontSize: 26px
    fontWeight: '500'
    lineHeight: 32px
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  headline-sm:
    fontFamily: Newsreader
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  subhead:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 22px
    letterSpacing: 0.04em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 19px
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.12em
  label-subtle:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  margin: 1.25rem
  margin-desktop: 2.5rem
  space-xs: 0.375rem
  space-sm: 0.75rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.25rem
---

## Brand & Style

This design system expresses a serene, contemporary coffee publication ethos rooted in Indonesian everyday life—embodying *"Menemani perjalanan sehari-hari"* and *"Move Forward, One Sip at a Time."* 

The aesthetic is an editorial coffee journal: warm, grounded, intentional, and quiet in its confidence. It deliberately shuns transactional noise, hard sale prompts, checkout carts, and badge-cluttered e-commerce patterns. Instead, it invites the reader into sensory narratives, brewing origin vignettes, bottle tasting notes, and physical neighborhood rituals.

### Visual Pillars
- **Warm Minimalist Editorial:** Spacious typographic hierarchy pairing high-character serif titles with disciplined, modern grotesque body typography.
- **Ambient Tactility:** Organic off-white and warm cream canvas colors reminiscent of heavy uncoated paper stock, grounded by deep forest green accents and warm beige containers.
- **Mobile-First Intimacy:** Tactile cards with gentle rounded corners, thumb-friendly targets, and quiet sticky micro-headers that stay out of the reader’s focus.

## Colors

The palette draws directly from roasted beans, steamed milk, and botanical depths. 

- **Primary (`#151F14` — Deep Forest Green):** The brand anchor. Applied to titles, key focal borders, primary navigational icons, and structural anchor elements.
- **Secondary (`#D8CBB8` — Sandstone Beige):** Warm structural tone. Used for subtle card borders, secondary containers, and dividers.
- **Tertiary (`#24251F` — Charcoal Earth):** The deep reading color for long-form narrative text, captions, and fine metadata. It provides softer, less abrasive contrast than absolute black.
- **Neutral Canvas (`#F5F1E8` — Warm Cream):** The ambient background surface that bathes the viewport in a comfortable, non-glare, paper-like warmth.
- **Highlight Pure White (`#FFFFFF`):** Reserved strictly for elevated cards, modal sheets, and inner content plates that require visual crispness against the cream backdrop.

## Typography

The type system blends the literary grace of **Newsreader** with the clean, legible precision of **Plus Jakarta Sans**. 

- **Editorial Serifs (Newsreader):** Used for large narrative headers, sensory tasting titles, quotes, and issue volume markers. It lends human warmth and stillness to the screen.
- **Modern Sans (Plus Jakarta Sans):** Delivers clean readability for body stories, tasting profiles (sweetness, acidity, body), preparation instructions, and interactive pills.
- **Eyebrows & Chapter Labels:** Rendered in `label-caps` with uppercase transformation and extended tracking (`0.12em`) to function as quiet journalistic sub-sections without dominating screen weight.

## Layout & Spacing

The layout is built upon an editorial fluid canvas optimized for single-column mobile reading and refined multi-column presentation on larger screens.

- **Mobile Canvas:** Outer boundary defaults to `1.25rem` (`20px`) margins, maximizing viewport real estate for storytelling and bottle photography while maintaining comfortable finger-edge boundaries.
- **Desktop/Tablet Reflow:** Fluid column scaling up to a disciplined max-width container (`860px` for essay articles; `1180px` for the coffee profile index) flanked by `2.5rem` outer margins.
- **Vertical Rhythm:** Generous section spacing (`space-xl`) between editorial chapters, keeping page sections uncluttered and calm.

## Elevation & Depth

Visual hierarchy relies on quiet surface contrast and paper-like outlines rather than artificial volumetric drop shadows.

- **Surface Tiers:**
  - **Base Canvas:** Neutral Warm Cream (`#F5F1E8`).
  - **Elevated Editorial Plates:** Pure White (`#FFFFFF`) containers resting directly atop the canvas.
  - **Recessed / Callout Plates:** Sandstone Beige (`#D8CBB8` at 35% opacity) for tasting notes, origin facts, and quote blocks.
- **Low-Contrast Ghost Outlines:** Cards and interactive elements use a delicate `1px` border of `#D8CBB8` (or 15% opacity Forest Green `#151F14`), preventing optical harshness.
- **Atmospheric Shadow:** When subtle floating interaction is required (such as sticky bottom action pills or audio play bars), a faint ambient blur is applied: `0 8px 24px rgba(21, 31, 20, 0.06)`.

## Shapes

The design uses balanced, modern curves (`roundedness: 2`, `8px` / `0.5rem` base radius) reflecting smooth glass bottles and gentle ceramic contours.

- **Cards & Plates:** Styled with `rounded-lg` (`16px` / `1rem`) for approachable, tactile comfort on touch screens.
- **Interactive Badges & Pill Buttons:** Styled with full pill radiuses (`9999px`) to emphasize touch-friendliness and dynamic flow.
- **Hero Image Masks:** Styled with `rounded-xl` (`24px` / `1.5rem`) to frame brew visuals and café spaces with soft, editorial refinement.

## Components

### Sticky Mobile Editorial Header
A compact, non-intrusive top bar (`54px` height) with a frosted Warm Cream finish (`rgba(245, 241, 232, 0.88)` with `backdrop-filter: blur(12px)`). Contains the brand mark at center and an unobtrusive menu trigger at the flank. Zero shopping cart or badge triggers.

### Buttons & Interactive Links
- **Primary Editorial Button:** Deep Forest Green (`#151F14`) background, Pure White (`#FFFFFF`) label, rounded pill (`9999px`), `12px 24px` padding. Delivers actions like *"Baca Kisah"* (Read Story) or *"Kunjungi Barista"*.
- **Ghost Action:** Clear background with a `1px` solid Forest Green or Beige outline and Charcoal text. Used for secondary navigation and filter selections.

### Story & Drink Profile Cards
- **Variant 1 (Tasting Journal Card):** Pure White surface, `16px` rounded corners, subtle `1px` `#D8CBB8` border. High-aspect ratio bottle and beverage photography framed with minimal padding (`12px`), followed by the drink title in `headline-md`, origin notes, and sensory ingredient badges.
- **Variant 2 (Journal Essay Card):** Soft warm beige background, left-aligned Newsreader typography, with read times and volume dates rendered in `label-caps`.

### Tasting & Origin Chips
Compact, pill-shaped tags (`4px 12px` padding) with a `12px` font size. Rendered with transparent fills and delicate `1px` Sandstone Beige borders. Text in Charcoal `#24251F`. Used to classify drink attributes (e.g., *"Aren Palm Sugar"*, *"Slow-Steeped"*, *"Velvety Milk"*).

### Sensory Detail Panels
Structured key-value pairs separated by thin `#D8CBB8` horizontal rules (`1px`). Left label in `label-caps` (`Charcoal` at 60% opacity), right evaluation in `body-sm` (`Forest Green` font weight 600).

### Form Inputs (Journal Subscription / Guestbook)
Clean, border-bottom or soft rounded fill fields using Warm Cream or Pure White surfaces with a subtle `#D8CBB8` boundary. Clean typography with no aggressive focus outlines—focus state transitions smoothly to Deep Forest Green `#151F14` at `1.5px` border width.