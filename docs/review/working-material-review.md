# Working material review — November 24, 2026

Reviewed `C:\Apps\Website reviews 2026-11-17\Working material` recursively. At review start it contained 2,318 files across three areas. The companion `inventory-review.txt` in that source folder records each original file's relative path, byte size, and SHA-256 digest. No source file was deleted or modified during this review; the inventory report was added afterward and is not included in its own listing.

## Peer research (2,263 files)

- `Crayon.json` contains 365 ranked records with no duplicate hostnames. It has 291 author/illustrator entries, 40 story/activity entries, and 34 coloring/craft/classroom entries. The November 19 published comparison describes a selected sample of 200 Crayon peers with 199 additional destinations (399 pages total); this register is a larger candidate/ranking pool, not an unrecorded second production implementation.
- The capture cache has 2,239 JSON files, all valid JSON. 1,918 have parsed source URLs; 321 are explicit fetch-error records (DNS failure, TLS/hostname mismatch, timeout, remote close, or a blocked/challenge page), not successful captured pages. Keep these as excluded/rejected research evidence rather than treating them as verified peers.
- The logs show candidate/rank stages, and the final rankings report the expected 200-entry sample/category counts. `metrics.json`, `Crayon.json`, `Oneirodex.json`, and `Portfolio.json` are research inputs/results. The three HTML files are scraped reference pages; the three Markdown files retain source lists. No new Crayon feature requirement was found beyond the published review and roadmap.

## Website checks (28 files)

- Crayon's `build.py`, `deep.py`, and `inspect-peers.py` are historical implementation/research scripts. The generator references an obsolete `/tmp/kite-execution-Q3Kg7J` handoff path and old review checkout layout; it is not a repeatable build for the current repo. Do not use it as the source of truth. The resulting nature-card, reader, picker, and print work is represented in the published `dist/` site, and the reported K02/K03 checks match recorded review results.
- The 15 browser scripts, 8 Python scripts, 1 Ruby script, 1 JS file and 3 package manifests belong to the portfolio, Crayon, and Oneirodex review tracks. They are verification/editing helpers with stale platform-specific paths in places; they do not constitute additional files to publish into the Crayon site. Oneirodex's `cleanup.cjs` is a targeted stylesheet cleanup helper; inspect its current target before any reuse.
- No unfinished command or unrecorded Crayon feature was identified from the source and result files. Historical scripts should remain archival unless a maintainer relocates their inputs and re-runs them in a supported checkout.

## Portfolio Pages build (27 files)

A separate generated portfolio site, not Crayon Kite. It remains a sibling working artifact and does not belong in the Crayon repository.

## Release-status correction

The parent `crayon-kite/README.md` still says all three projects are local working copies and public release is pending. That is stale for Crayon Kite: GitHub `main` is at `63599ae`, GitHub Pages deployment run `45533781673` succeeded, and live route readback returned HTTP 200 for both landing pages, Birdhouse Home, nature cards, the Welcome Tree index/story 20, and all ten coloring routes. Physical printer/AirPrint, family and assistive-technology review, owner approval of proposed character art, audio playback/rights, and roadmap feature acceptance remain open as recorded in this repo's `docs/review/RELEASE-STATUS.md`.

The 600-site/560-extra-page comparison in the parent README is a separate aggregate across three projects; this review did not re-run its external-source checks. The 321 fetch-error cache entries are reported separately and are not part of successful page evidence.
