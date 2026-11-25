# Crayon Kite

Crayon Kite makes story-filled coloring books for little artists. The home page links families to the Budgie Adventures shelf, ten individual printable pages, the six nature cards and the Welcome Tree read-aloud collection. Each reader and printable has a static HTML entry point under `dist/budgie-adventures/`. The activity pages and their original drawings also work with JavaScript disabled.

The static site uses Cloudflare Web Analytics for page-view reporting on `crayonkite.com`, with a separate analytics property from the Oneirodex and personal sites. It has no account creation, comments, messaging, or user uploads. Manuscripts and products are still in development; this site does not claim to sell a released book or accept payments.

## Deploy

The GitHub Actions workflow in `.github/workflows/deploy-pages.yml` publishes the `dist/` folder to GitHub Pages whenever `main` changes or the workflow is started manually. In repository Settings → Pages, select **GitHub Actions** as the publishing source. Set the custom domain there; DNS records for the apex domain belong at the domain registrar.

## Local preview

Run `python3 scripts/check-site.py` to validate the Pages artifact. Serve the `dist/` folder with any static web server. The home page is `/` and the Budgie Adventures page is `/budgie-adventures/`.

