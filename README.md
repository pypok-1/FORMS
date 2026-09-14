## FORMS
# MELISSO (v1.0.0)

A lightweight, artisanal web atelier and full-stack e-commerce engine for raw Cretan honey. Built with Flask and a custom Tailwind CSS frontend, focusing on zero-dependency builds, server-side session management, and editorial design UI.

![MELISSO Banner](https://i.postimg.cc/Y0DL5Pqy/image.png)

---

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Execution](#installation--execution)
- [Project Architecture](#project-architecture)
- [Current State & Roadmap](#current-state--roadmap)
- [Author's Note](#authors-note)

---

## Overview

**MELISSO** is a targeted full-stack e-commerce application designed for an artisanal Cretan honey storefront. The project emphasizes clean code structure, rapid load times, and an editorial design philosophy without relying on complex JS bundlers or node_modules dependencies.

The system handles product showcases, tasting matchers, interactive server-persisted carts, and business logic for dynamic shipping calculation.

---

## Key Features

- **Editorial E-Commerce Experience:** Landing page atelier featuring raw single-origin varietals, terroir storytelling, and scroll-reveal interactions.
- **Interactive Cart & Session Persistence:** Dynamic server-side cart state management preserved across user sessions.
- **Sommelier Tasting Matcher:** Interactive sensory matcher and food pairing guide with sensory slider parameters.
- **Dynamic Shipping Engine:** Automated freight calculations with built-in free shipping thresholds (€80+).
- **Accessibility & Motion Design:** Full responsive layout, reduced-motion media query support, and optimized typography pairings (*Bodoni Moda* & *Plus Jakarta Sans*).

---

## Tech Stack

### Core Technologies
- **Backend:** Python 3.10+, Flask 3.0, Jinja2, Gunicorn
- **Frontend:** HTML5, Tailwind CSS 3.x, Native JavaScript (ES6+)
- **Design & Typography:** Material Symbols, Google Fonts (*Bodoni Moda*, *Plus Jakarta Sans*)
- **VCS & DevOps:** Git, GitHub

### Design Decisions
- **Zero Build-Step:** Avoids Node.js dependency pipelines (`node_modules`) for lightweight deployment and simple maintainability.
- **Server-Side Rendering:** Uses Jinja2 templates combined with dynamic client-side JS enhancements for reactive UI components.

---

## Getting Started

### Prerequisites

| Component | Minimum Version | Requirement |
|-----------|-----------------|-------------|
| **Python**| `3.10+`         | Runtime environment |
| **Flask** | `3.0+`          | Web framework |
| **pip**   | Latest          | Package manager |

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd melisso
