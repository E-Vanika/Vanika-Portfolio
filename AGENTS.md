# Portfolio Builder Guide

This file is intentionally LLM-agnostic. Any coding assistant or contributor can use it to create, tailor, and maintain a high-quality DevOps portfolio in this repository.

## Goal

Build a fast, accessible, single-page portfolio that communicates real DevOps and SRE impact through outcomes, architecture patterns, and automation—not a generic tool list.

## Project conventions

- Keep the site dependency-free: semantic HTML5 in `index.html` and vanilla CSS in `styles.css`.
- Do not add a UI framework, build system, tracking script, or external font unless explicitly requested.
- Preserve the terminal-inspired dark design, responsive layout, and keyboard-accessible navigation.
- Keep all portfolio content professional, concise, and suitable for public sharing.
- Do not expose employer-internal names, URLs, repository details, credentials, incident data, customer information, or screenshots without explicit permission.

## Personalising the portfolio

1. Read the source material supplied by the portfolio owner.
2. Extract only verified accomplishments, technologies, and measurable outcomes.
3. Rewrite internal project names into public-safe descriptions such as "multi-region recovery automation" or "cloud platform delivery."
4. Prefer outcome-oriented wording: what problem existed, what was built, and what changed.
5. Keep numbers only when the owner has confirmed them. Never invent MTTR, availability, cost, or performance metrics.
6. Update the hero, metrics, showcase cards, and contact links together so they tell one consistent story.

## Required page structure

- A navigation bar with a visible system-status indicator.
- A concise DevOps-focused hero statement and a call to action.
- An impact/metrics section containing verified signals or outcomes.
- Architecture and engineering-impact cards. Each card should contain a public-safe title, a short problem-and-outcome summary, tool tags, and a small inline diagram.
- A contact section with the owner’s approved GitHub, LinkedIn, and email links.

## Design and accessibility rules

- Use CSS Grid or Flexbox; verify the layout at narrow mobile widths.
- Keep strong text contrast against the `#0f172a` background.
- Use one `main` landmark, one `title`, and a viewport meta tag.
- Give meaningful images `alt` text. Decorative visuals should be represented with CSS or marked appropriately.
- Keep motion subtle and respect `prefers-reduced-motion`.
- Keep project cards free of placeholder external links. Use public links only when approved by the owner.

## Quality and delivery workflow

- Run `python scripts/validate_site.py` when Python is available. It checks document structure, internal anchors, local assets, and image alt text without third-party packages.
- Pull requests run `.github/workflows/ci.yml`.
- Pushes to `main` or `master` run `.github/workflows/deploy.yml`; validation must pass before deployment to GitHub Pages.
- Keep workflow permissions least-privilege. The deployment job alone may use `pages: write` and `id-token: write`.
- Do not commit secrets. Use repository secrets for any future integrations that require credentials.

## Completion checklist

- [ ] No confidential or unapproved content is present.
- [ ] Contact links are accurate and intentional.
- [ ] All claimed outcomes are verified by the owner.
- [ ] Mobile and desktop layouts remain usable.
- [ ] The static-site validator passes.
- [ ] Changes are committed with a clear message and pushed to the deployment branch.
