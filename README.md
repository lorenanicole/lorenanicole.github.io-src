# lorenamesa.com

Source repository for [lorenamesa.com](https://lorenamesa.com) — technical blog and professional platform by Lorena Mesa.

## About

This site showcases:
- **Technical writing** on Python, AI/LLM integration, backend engineering, and open source
- **Speaking history** and conference talks
- **Community leadership** work (PyLadies, Python Software Foundation)
- **Consulting availability** for technical teams

Built with [Pelican](https://getpelican.com/) and deployed via GitHub Pages.

## Stack

- **Static Site Generator**: Pelican 4.9+
- **Python**: 3.9+
- **Dependency Management**: Poetry
- **Theme**: Custom minimal theme
- **Hosting**: GitHub Pages

## Local Development

### Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/) (install with: `curl -sSL https://install.python-poetry.org | python3 -`)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lorenanicole/lorenanicole.github.io-src.git
   cd lorenanicole.github.io-src
   ```

2. **Install dependencies with Poetry**:
   ```bash
   poetry install
   ```

3. **Generate the site**:
   ```bash
   poetry run pelican content -o output -s pelicanconf.py
   ```

4. **View locally** (optional):
   ```bash
   cd output
   python -m http.server 8000
   ```
   Then open http://localhost:8000 in your browser.

## Project Structure

```
.
├── content/
│   ├── articles/        # Blog posts (markdown)
│   └── pages/          # Static pages (about, speaking, etc.)
├── custom-theme/       # Pelican theme
│   ├── static/css/     # Minimal CSS
│   └── templates/      # Jinja2 templates
├── pelicanconf.py      # Pelican configuration
├── publishconf.py      # Publishing configuration
├── pyproject.toml      # Poetry dependencies
└── output/             # Generated site (git submodule)
```

## Writing Content

### Blog Posts

Create a new file in `content/articles/` with markdown frontmatter:

```markdown
Title: Your Post Title
Date: 2026-09-27
Category: Python
Tags: ai, backend, tutorial
Summary: A brief summary of the post

Your content here...
```

### Pages

Create a new file in `content/pages/` for static pages like About, Speaking, etc.:

```markdown
Template: generic_page
Title: Page Title
Slug: page-slug
Summary: Brief description

Page content...
```

## Building & Publishing

### Build the site:
```bash
poetry run pelican content -o output -s pelicanconf.py
```

### Publish (GitHub Pages):
The `output/` directory is a git submodule pointing to the published repository. To publish:

```bash
cd output
git add .
git commit -m "Update site"
git push origin main
cd ..
git add output
git commit -m "Update published output"
git push origin main
```

## Design & Styling

The custom theme uses:
- **Typography-first design** (Tailwind CSS)
- **Modern fonts** (Inter body, Space Grotesk headers)
- **Dark mode support** (via `prefers-color-scheme`)
- **Responsive layout** (mobile-friendly)
- **Green accent color** (#059669)
- **Structured data** (JSON-LD schema for SEO)

## SEO & Analytics

- **Structured data**: JSON-LD (Person, BlogPosting, BreadcrumbList)
- **Meta tags**: OpenGraph, Twitter Card
- **Feeds**: Atom and RSS available
- **Sitemap**: Auto-generated at `/sitemap.xml`
- **Analytics**: Google Analytics configured in `pelicanconf.py`

## License

Content and design © 2014-2026 Lorena Mesa. All rights reserved.

The Pelican theme code is available under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

## Questions?

Reach out at me@lorenamesa.com or via [Substack](https://substack.com/@lorenamesa).
