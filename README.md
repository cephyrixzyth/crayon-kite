# Crayon Kite

Crayon Kite makes story-filled coloring books for little artists. This site has two pages:

- `dist/index.html` — the Crayon Kite brand and book shelf.
- `dist/budgie-adventures/index.html` — Budgie Adventures with The Chirps, including a story starter and printable activity.

The static site uses Cloudflare Web Analytics for page-view reporting on `crayonkite.com`, with a separate analytics property from the Oneirodex and personal sites. It has no account creation, comments, messaging, or user uploads. Manuscripts and products are still in development; this site does not claim to sell a released book or accept payments.

## Deploy

The GitHub Actions workflow in `.github/workflows/deploy-pages.yml` publishes the `dist/` folder to GitHub Pages whenever `main` changes or the workflow is started manually. In repository Settings → Pages, select **GitHub Actions** as the publishing source. Set the custom domain there; DNS records for the apex domain belong at the domain registrar.

## Local preview

Serve the `dist/` folder with any static web server. The home page is `/` and the Budgie Adventures page is `/budgie-adventures/`.

