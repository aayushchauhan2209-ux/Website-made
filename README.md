# Maison d'Or Haute Joaillerie Showcase & Private Owner Studio

A full-stack, commercially viable luxury jewelry showcase website and private owner management studio built with **FastAPI (Python 3.14)**, **Jinja2 responsive luxury SSR templates**, **Bespoke Luxury CSS Design System**, **SQLite + PostgreSQL Prisma Production Schema**, **Pillow Secure Media Pipeline**, and **PBKDF2-HMAC-SHA256 / JWT Authentication with Instant Token Revocation**.

---

## 💎 Core Architecture & Architectural Boundaries

1. **Showcase & Concierge Only**:
   - In strict compliance with commercial high-jewelry requirements, this application does **NOT** contain shopping carts, checkout forms, payment gateways, or public courier ordering.
   - High jewelry acquisitions are conducted through **Private Atelier Concierge Services**.

2. **Dual-Flow Conversion Mechanism**:
   - **Concierge Modal**: Interactive booking & custom commission inquiry with appointment time selection and preferred communication channel (WhatsApp, Telephone, Email, Salon Viewing).
   - **Pre-Filled WhatsApp Deep Link**: Dynamic one-click international deep link (`wa.me`) automatically pre-populated with jewel title, SKU, carat weight, metal type, valuation, and formal greeting.

3. **Dynamic White-Label Design System**:
   - Zero hardcoded jeweler identities. All branding attributes (Maison Name, Tagline, Brand Provenance Story, Atelier Address, Phone, Email, WhatsApp line, Currency Symbol, and Trust Assurances) are dynamically managed via `StoreSettings`.
   - **Live Theme Customizer**: Real-time hex color pickers in the Owner Studio driving CSS root variables (`--gold-primary`, `--emerald-accent`, `--bg-primary`, `--bg-surface`, `--text-primary`).

4. **Hardened Server-Side Security**:
   - **PBKDF2-HMAC-SHA256 (150,000 rounds)** password hashing with cryptographic salt and constant-time comparison (`secrets.compare_digest`).
   - **Stateless JWT** delivered via `httpOnly`, `SameSite: Lax` secure cookies.
   - **Instant Session Revocation**: Every authenticated request validates `token_version` against the database record. Logging out or revoking credentials immediately invalidates all active sessions globally.

5. **Pillow Secure Media Pipeline**:
   - **Magic-Byte Inspection**: Validates binary file headers to prevent malicious payloads masquerading as images.
   - **EXIF Stripping**: Sanitizes GPS coordinates, camera serials, and device metadata for client privacy.
   - **Auto-Orientation & Downsampling**: High-quality Lanczos resampling into optimized WebP formats (up to 2400px high-res stage + 600px thumbnails).

6. **Relational Database & Backups**:
   - Local storage: **SQLite** configured with `WAL` journal mode and foreign key pragmas.
   - **Automated Point-in-Time Backups**: 1-click SQLite online backup snapshot creation in `backups/`.
   - **Production PostgreSQL Schema**: Complete `prisma/schema.prisma` definition ready for cloud deployment.

---

## 🏛️ Public Showcase Features

- **Atmospheric Haute Joaillerie Hero**: Ambient golden glow, trust assurances bar, and luxury typography (`Cinzel`, `Cormorant Garamond`, `Plus Jakarta Sans`).
- **Interactive High-Jewelry Vault (`/showcase`)**: Live filtering by Category, Gemstone (Diamond, Emerald, Sapphire, Ruby, Pearl), Metal (Platinum, Yellow Gold, Rose Gold, White Gold), Atelier Availability, and Price Sorting.
- **High-Resolution Product Showcase (`/showcase/{slug}`)**:
  - Interactive **2.2x High-Definition Zoom Magnifier Lens**.
  - Multi-angle gallery thumbnail switcher.
  - Comprehensive **Haute Joaillerie Spec Matrix** (Metal purity, gross weight, carat weight, cut, color, clarity, gemological certificate #).
  - Dual Conversion Action Box (Modal Form + WhatsApp VIP Concierge).
- **Haute Joaillerie Lookbook (`/lookbook`)**: Curated architectural collections and narratives.
- **Bespoke Craftsmanship Story (`/bespoke`)**: 4-stage bespoke commission progression and consultation scheduler.
- **Private Salons & Concierge (`/contact`)**: Place Vendôme Paris & Fifth Avenue New York salon details with direct transmission form.

---

## 👑 Private Owner Studio Backoffice (`/studio`)

- **Executive KPI Dashboard**: Live metrics for Active Leads, New Leads, Vault Pieces, Masterpiece counts, and Total Inventory Valuation.
- **Jewelry Catalog Manager (`/studio/items`)**: Complete inventory control, new creation studio with multi-image drag-and-drop uploader, and quick status toggles.
- **Concierge CRM Leads Manager (`/studio/inquiries`)**: Lead triaging with 1-click client WhatsApp outreach, 1-click email, 1-click phone call, status updates, and private jeweler notes.
- **Lookbook & Category Manager (`/studio/categories`)**: Create and organize collections.
- **White-Label Branding & Theme Hub (`/studio/settings`)**: Live theme color picker, store copy editor, WhatsApp line configurator, and SQLite / JSON database backup exporter.

---

## 🚀 Quick Start Guide

### 1. Requirements & Dependencies
Ensure Python 3.9+ is installed. Install all dependencies:
```bash
pip install -r requirements.txt
```

### 2. Launch the Application
Run the runner script:
```bash
python run.py
```

### 3. Access URLs & Default Master Credentials
- **Public High Jewelry Showcase**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Private Owner Studio**: [http://127.0.0.1:8000/studio/login](http://127.0.0.1:8000/studio/login)
- **Master Jeweler Credentials**:
  - **Username / Email**: `admin` or `owner@maisondor.luxury`
  - **Master Password**: `ImperialVault2026!`

---

## 🧪 Running Automated Tests

Run the complete test suite:
```bash
python -m unittest tests/test_luxury_studio.py
```
