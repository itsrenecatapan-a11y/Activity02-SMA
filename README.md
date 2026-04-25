<div align="center">
  <img src="https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/layers.svg" alt="Portfolio Layers" width="48" height="48" />
  <h1>Rene's Personal Portfolio</h1>
  <p>
    <b>A modern, high-end multipage Streamlit application built with Python, featuring custom glassmorphism styling, native light/dark mode, and interactive GSAP-inspired scroll animations.</b>
  </p>

  <a href="https://streamlit.io">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  </a>
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  </a>
</div>

<br />

## Overview

This repository contains the source code for my interactive portfolio. Rather than relying on standard website builders, this platform is built entirely in Python utilizing Streamlit. The project transcends default Streamlit aesthetics by injecting extensive custom CSS, creating a highly polished, responsive interface with fluid typography and elegant state transitions.

The portfolio is structured as a multipage application detailing my academic background, technical skills, creative directions, and event coordination experiences.

## Technical Highlights

*   **Custom Framework Bypassing:** Overrides standard Streamlit DOM elements to implement a cohesive design system using `:root` CSS variables.
*   **Dual Theming (Light/Dark):** True, seamless toggle-based theming synchronized with session state to ensure persisting styles without widget desynchronization bugs.
*   **Glassmorphism Engine:** Employs localized `backdrop-filter: blur(16px)` on transparent cards mapping to the dynamic theme variables.
*   **Typography:** Integrates *Playfair Display* for striking, elegant headers alongside *Outfit* for highly legible body text.
*   **Dynamic Animations:** 
    *   Pure CSS typing effects via stepping and blinking cursors.
    *   Intersection Observer API injected via JavaScript components to trigger fade-in `reveal` animations on scroll.
    *   Floating radial gradients driving ambient background elements.

## Project Structure

```text
├── Home.py                  # Entry point & hero section with typing animations
├── pages/                   # Multi-page routing directories
│   ├── 2_About.py           # Personal background, vision, and academic history
│   ├── 3_Skills.py          # Technical/creative abilities and conferences attended 
│   ├── 4_Projects.py        # Image gallery showcasing event coordination and design
│   └── 5_Contact.py         # Social links and direct contact channels
├── style.py                 # Core design engine: master CSS, SVG dictionaries, and UI components
├── requirements.txt         # Production dependencies for cloud environments
└── pictures/                # Local gallery assets
```

## Local Development

To run this application locally, a working Python environment is required.

**1. Clone the repository:**
```bash
git clone <repository-url>
cd <repository-directory>
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Launch the application:**
```bash
streamlit run Home.py
```
*The application will boot up at `http://localhost:8501/` by default.*

## Design Philosophy

The visual aesthetic aims for a high-end, soft, and feminine "Blush & Rose" presentation that communicates approachability while maintaining strict professional legibility. To execute this, the architecture rejects Streamlit's default components. It replaces them with inline SVGs to reduce external requests, implements squircle layouts for softening UI constraints, and dictates meticulously paced transition timings (`cubic-bezier` curves) to ensure that the interface feels tactile rather than purely mechanical.

<br />

<div align="center">
  <p>Designed and Developed by <b>Rene</b></p>
</div>