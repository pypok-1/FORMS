<p align="center">
  <img src="https://media.giphy.com/media/1NQ7m0gqsah1XS4vG1/giphy.gif" width="60" alt="Busy bee" />
</p>

<h1 align="center">
  <span style="font-size: 4em; font-weight: 800; background: linear-gradient(135deg, #c9822b 0%, #895100 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
    MELISSO
  </span>
</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Bodoni+Moda&weight=600&size=26&duration=3000&pause=1000&color=895100&center=true&vCenter=true&random=false&width=700&lines=Raw+Single-Origin+Cretan+Honey;Harvested+Above+1%2C200+Meters;Sealed+in+Beeswax%2C+Numbered+by+Hand" alt="Typing SVG" />
</p>

![Origin: Lefka Ori, Crete](https://img.shields.io/badge/Origin-Lefka%20Ori%2C%20Crete-c9822b?style=for-the-badge)
![Altitude: 1,200 m+](https://img.shields.io/badge/Altitude-1%2C200%20m%2B-895100?style=for-the-badge)
![Diastase: 34.2 DN](https://img.shields.io/badge/Diastase-34.2%20DN-994620?style=for-the-badge)
![Purity: up to 98.4%](https://img.shields.io/badge/Purity-98.4%25-7a5900?style=for-the-badge)

A small, deliberate web atelier for raw, single-origin Cretan honey — harvested in the White Mountains above the Aegean, unheated, unfiltered, and hand-sealed in beeswax. Browse the seasonal reserve, explore tasting notes and food pairings, and build a cart that remembers you across sessions. This is MELISSO.

---

## Table of Contents
- [About](#about)
- [Brand & Terroir](#brand--terroir)
- [What's In The Storefront Today](#whats-in-the-storefront-today)
- [What I Want To Build Next](#what-i-want-to-build-next)
- [Product Catalog](#product-catalog)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Install & Run](#install--run)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [A Note From The Author](#a-note-from-the-author)
- [License](#license)

---

## About

MELISSO is a full-stack storefront for artisanal Cretan honey, built with Flask and a hand-crafted Tailwind frontend. It is intentionally narrow in scope: a landing atelier, a product catalog, an interactive cart with server-side session persistence, and a shipping engine that rewards larger orders.

The project pairs a warm editorial design system with a straightforward backend. No bundler, no build step, no node_modules — clone, install Flask, run.

Project repository: [MELISSO](#)

---

## Brand & Terroir

| Attribute | Detail |
|---|---|
| Origin | Samaria Gorge biosphere, Lefka Ori, Crete |
| Altitude | 1,200 – 1,600 m |
| Coordinates | 35°18′ N, 24°02′ E |
| Extraction | Cold centrifugal, never above 35°C |
| Diastase Activity | > 34.2 DN |
| Moisture Content | < 15.1% |
| Pollen Purity | up to 98.4% (wild thyme varietals) |
| Annual Output | never exceeding 1,200 hand-numbered jars per batch |
| Wintering Reserve | > 40% of comb yield left to the colony |

**Ethical commitments.** No sugar feeding. No synthetic acaricides. No thermal processing. No antibiotics. Every seasonal release is tested by an independent laboratory at the University of Athens.

---

## What's In The Storefront Today

| Status | Feature | Notes |
|:---:|---|---|
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Landing atelier | Editorial hero, terroir badges, tech bar with harvest telemetry |
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Product catalog | Six varietals rendered from the `PRODUCTS` dict |
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Tasting notes & pairings | Flavor architecture cards with sensory sliders |
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Terroir narrative | Scroll-reveal section on apiary and craft |
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Community proofs | Testimonials and #MelissoMoments mosaic |
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Cart engine | Add, update, remove, live subtotal |
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Session persistence | Cart survives refresh via signed cookie |
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Shipping threshold | Free freight over €80, recalculated live |
| ![done](https://img.shields.io/badge/-DONE-895100?style=flat-square&logo=checkmarx&logoColor=white) | Responsive layout | Desktop, tablet, high-DPI displays |

---

<table>
<tr>
<td width="80" valign="middle">
  <img src="https://media.giphy.com/media/1NQ7m0gqsah1XS4vG1/giphy.gif" width="70" alt="Busy bee" />
</td>
<td valign="middle">
  <h2>What I Want To Build Next</h2>
</td>
</tr>
</table>

| Status | Feature | Notes |
|:---:|---|---|
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | More pages | Dedicated pages for Terroir, Rituals, Harvest Club, Journal, and Contact — the single-page atelier is not enough |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | Proper product database | Move the catalog out of a Python dict and into a real database (SQLite or PostgreSQL) with migrations |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | Expanded catalog | Grow the range well beyond six varietals — seasonal, reserve, and experimental batches |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | Slide-over cart drawer | Right-hand panel with backdrop blur — replaces the redirect to `/cart` |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | Shipping progress bar | Visual gamification of the €80 free-shipping threshold |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | Sommelier upsell in cart | One-click sample or accessory add-on at checkout |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | Stripe checkout | Multi-currency payment gateway with Stripe Elements and Apple Pay |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | Harvest Club tiers | Connoisseur, Grand Cru, Atelier Patron memberships |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | QR verification | Laboratory analysis printed on every jar label |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | B2B wholesale portal | For Michelin-starred establishments and specialty retail |
| ![planned](https://img.shields.io/badge/-PLANNED-c9822b?style=flat-square&logo=checkmarx&logoColor=white) | `localStorage` sync | Guest cart persistence across browser sessions |

---

## Product Catalog

| ID | Name | Weight | Price |
|---|---|---|---|
| `wild-thyme-reserve` | Wild Thyme Reserve | 250 g | €28.00 |
| `white-thistle-blossom` | White Thistle & Blossom | 450 g | €34.00 |
| `wild-pine-herbs` | Wild Pine & Mountain Herbs | 450 g | €38.00 |
| `oak-chestnut` | Cretan Oak & Wild Chestnut | 450 g | €42.00 |
| `raw-honeycomb` | Raw Honeycomb Reserve | 500 g | €42.00 |
| `tasting-trio` | Tasting Discovery Trio Box | 3 × 450 g | €95.00 |

The catalog lives in a single `PRODUCTS` dictionary in `app.py`. Adding a varietal is a one-line change.

---

## Tech Stack

<details>
<summary><b>Click to expand full tech stack</b></summary>

### **Backend**
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Jinja2-✓-B41717?style=for-the-badge&logo=jinja&logoColor=white" />
  <img src="https://img.shields.io/badge/Gunicorn-✓-499848?style=for-the-badge&logo=gunicorn&logoColor=white" />
</p>

### **Frontend**
<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Material_Symbols-✓-4285F4?style=for-the-badge&logo=google&logoColor=white" />
</p>

### **Design**
<p align="center">
  <img src="https://img.shields.io/badge/Bodoni_Moda-✓-1c1c19?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Plus_Jakarta_Sans-✓-1c1c19?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Google_Fonts-4285F4?style=for-the-badge&logo=googlefonts&logoColor=white" />
</p>

### **DevOps**
<p align="center">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>
</details>

---

## Getting Started

### Prerequisites

| Tool | Version | Badge |
|------|---------|-------|
| Python | 3.10+ | ![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python) |
| Flask | 3.0+ | ![Flask](https://img.shields.io/badge/Flask-3.0+-000000?logo=flask) |
| pip | any | ![pip](https://img.shields.io/badge/pip-✓-3776AB?logo=pypi) |

### Install & Run

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd melisso
    ```

2.  **Install dependencies:**
    ```bash
    pip install flask
    ```

3.  **Run the development server:**
    ```bash
    python Melisso/app.py
    ```

4.  **Open in your browser:**
    - Storefront — http://localhost:5000/
    - Cart — http://localhost:5000/cart

5.  **Production launch (behind a WSGI server):**
    ```bash
    gunicorn -w 4 -b 0.0.0.0:8000 app:app
    ```

---

## API Reference

All cart endpoints accept and return JSON. The cart is stored server-side in the signed Flask session cookie.

### Add item

```
POST /api/cart/add
```

```json
{ "product_id": "wild-thyme-reserve", "qty": 1 }
```

Returns the updated cart count and cart state.

### Update quantity

```
POST /api/cart/update
```

```json
{ "product_id": "wild-thyme-reserve", "qty": 3 }
```

Sending `qty: 0` removes the line. Returns recalculated subtotal, shipping, and total.

### Get cart

```
GET /api/cart
```

Returns hydrated line items with prices and line totals.

### Clear cart

```
POST /api/cart/clear
```

Empties the session cart. Available in the backend; wire it to a UI control as needed.

### Planned

- `POST /api/subscribe` — Harvest Club invitation dispatch
- `GET /api/products` — catalog with live batch counts
- `POST /api/checkout` — order orchestration with cold-shipping logistics

---

## Project Structure

```
melisso/
├── app.py                  # Flask app, routes, cart engine, product catalog
├── README.md
└── templates/
    ├── index.html          # Landing atelier
    └── cart.html           # Cart page
```

Product imagery is served from remote CDN URLs embedded in the templates. To self-host, replace the `image` fields in `PRODUCTS` and the `src` attributes in `index.html`.

---

## A Note From The Author

I was away from GitHub for a long time. Not a short break — a real one. Life rearranged itself, work rearranged itself, and for a while the only thing I was doing with code was thinking about it. Ideas kept arriving anyway. Sketches of interfaces, notes about how a checkout should feel, half-formed plans. Most of it never made it to a file.

This project is what happens when some of that finally lands.

I came back with a clearer picture of what I wanted to build, and I started building it — slowly, deliberately, and with a fair amount of help from AI tools along the way. Some parts of the code in this repository were drafted with assistance from language models. The direction, the taste, and the decisions about what to keep and what to throw out are mine. But I would rather say plainly that this was made in collaboration with modern tooling than pretend it appeared fully formed.

If you are reading this and you have also been away for a while: it is fine. The repositories will wait. The ideas will mostly wait too, and the ones that do not are not worth mourning. Start with what you remember. Ask for help. Ship something small.

I am back. Let us see what gets built.

---

## License

Released for personal and portfolio use. Product photography, brand marks, and the MELISSO name are the property of their respective owners. Commercial reuse of brand assets is not permitted without written consent.

For licensing, wholesale, or press inquiries, open an issue or reach out through the contact channels listed in the storefront footer.

---

<p align="center">
  <img src="https://media.giphy.com/media/1NQ7m0gqsah1XS4vG1/giphy.gif" width="60" alt="Busy bee" />
</p>
