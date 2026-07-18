# Vanika's DevOps Portfolio

[![Static site quality checks](https://github.com/E-Vanika/Vanika-Portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/E-Vanika/Vanika-Portfolio/actions/workflows/ci.yml)
[![Deploy static site to GitHub Pages](https://github.com/E-Vanika/Vanika-Portfolio/actions/workflows/deploy.yml/badge.svg)](https://github.com/E-Vanika/Vanika-Portfolio/actions/workflows/deploy.yml)

A responsive, terminal-inspired portfolio that presents my DevOps and SRE work: cloud infrastructure, GitOps delivery, observability, resilience, security automation, and cost optimisation.

## Highlights

- Application delivery with Terraform, Amazon EKS, Flux, and GitHub Actions.
- Multi-region resilience patterns with automated RDS snapshot replication and restore testing.
- Redis-to-Valkey migration that reduced cache infrastructure costs by 33%.
- EKS upgrades, Grafana and CloudWatch observability, and on-call ownership.
- AI-assisted SRE enablement through service-flow analysis and a Wiki MCP integration.

## Delivery pipeline

```text
Pull request → Python quality checks → review and merge
main/master push → Python quality gate → GitHub Pages artifact → deployment
```

The repository uses GitHub-hosted runners, so contributors do not need to install CI tooling locally.

- `.github/workflows/ci.yml` validates every pull request targeting `main` or `master`.
- `.github/workflows/deploy.yml` validates the site, then deploys it to GitHub Pages only if validation succeeds.
- `.github/dependabot.yml` opens weekly updates for GitHub Actions dependencies.
- `scripts/validate_site.py` is a dependency-free Python quality gate that checks page structure, responsive metadata, image alt text, local asset files, and in-page anchors.

## Run the validation locally

Python 3.10+ is sufficient; no third-party packages are needed.

```powershell
python scripts/validate_site.py
```

## Publish the site

1. Push the project to the `main` branch.
2. In the repository, open **Settings → Pages**.
3. Set **Build and deployment → Source** to **GitHub Actions**.
4. Watch the deployment in the **Actions** tab; the successful deployment job provides the public URL.

For a project repository, the address is typically `https://E-Vanika.github.io/Vanika-Portfolio/`.
