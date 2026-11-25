# Crayon Kite · Engineering handoff

## Chirps character studio

The new studio defines each bird through its silhouette, markings, gestures and story choices. It contains the cast lineup, four three-pose sheets, full-resolution masters, screen exports and a local site integration for the hero and four character cards.

[Open the illustrated character book](chirps-studio/index.html) · [Read the artist and engineering handoff](chirps-studio/ART-DIRECTION.md) · [Inspect the integration and artwork checks](chirps-studio/verification.json)

## Build new features and artwork

Start with **Chirps nature-card maker**, a working local concept for this site. Open the preview in a browser, try both choices, then save or print the result. The feature brief has the production file plan, editorial dependencies, acceptance checks, and three more original feature briefs. The art guide includes a generated master, two web sizes and placement instructions.

[Open the interactive preview](features/preview.html) · [Read the feature and artwork roadmap](features/FEATURES.md) · [Inspect the art files](features/ARTWORK.md) · [See the feature test evidence](features/verification.json)

To run the prototype checks, install dependencies as described below, then run `node features/verify-feature.cjs` from the handoff directory. The existing site review and its regression checks follow.

## Start here

**Assignment for a fresh agent.** Start in dist. Run K01, K02 and K05, inspect the reference diff, and verify both the paper dimensions and the art. Keep K03 and K04 as separate open tasks until the actual Birdhouse link and thumbnail requests pass.

**Reference point.** Public repository [cephyrixzyth/crayon-kite](https://github.com/cephyrixzyth/crayon-kite/tree/dd6007ce69a1682e93ba968c87c7a4bbd13e3014), main at `dd6007ce69a1682e93ba968c87c7a4bbd13e3014`, reconfirmed November 17, 2026. Use the active checkout for implementation. If it has moved, rerun the baseline before applying any suggested edits, and record the new SHA.

| Work in this order | Completion evidence | Dependency or boundary |
| --- | --- | --- |
| 1 · Print and card visibility | K01, K02, plus K05 and PDF artwork check | Independent. Start here before adding art or new activities. |
| 2 · Printable identities | K03, deep links, history, script-free route | Set the stable ID convention before generating activity pages. |
| 3 · Preview assets and print readiness | K04, network bytes, slow image races | Use the same sheet ID in the thumbnail, full art and download. |
| 4 · Content and deployment | Story-to-paper exercise, dist smoke test | Publish only available story material and owner-approved terms. |

**Jump to the implementation steps.** [1. Print exactly the chosen sheet on the chosen paper](#implementation-1) · [2. Keep the complete shelf at every width](#implementation-2) · [3. Give every activity a stable identity](#implementation-3) · [4. Make the picker fast without reducing print quality](#implementation-4) · [5. Complete a story-to-paper journey](#implementation-5) · [6. Share the shell and put validation before publishing](#implementation-6)

**Find the code.** Run this in the repository root to locate the exact symbols and their current line numbers.

```sh
rg -n '@page|@media print|last-child|data-file|selected-art|print-button|upload-pages-artifact' dist/index.html dist/budgie-adventures/index.html .github/workflows/deploy-pages.yml
```

### Run the handoff from a fresh checkout

The kit runs in its own directory. It reads a separate checkout without starting a public server. Install Node.js 22 or newer, Git, and Chromium or Chrome. The tested runtime was v24.22.1 on darwin with Chromium/Chrome 157.0.8103.79 and Playwright Core 1.62.1. The package lists exact direct dependency versions.

1. Open a terminal in the extracted handoff directory. Copy the following commands for a fresh baseline. For an existing checkout, set `SITE_CHECKOUT` to its absolute path and skip the clone and switch commands.

```sh
HANDOFF_DIR="$(pwd)"
SITE_CHECKOUT="$(mktemp -d)/crayon-kite"
git clone https://github.com/cephyrixzyth/crayon-kite.git "$SITE_CHECKOUT"
git -C "$SITE_CHECKOUT" switch --detach dd6007ce69a1682e93ba968c87c7a4bbd13e3014
npm install --ignore-scripts --no-audit --no-fund
npx --no-install playwright-core install chromium
node "$HANDOFF_DIR/verify.cjs" "$SITE_CHECKOUT"
```

2. If using an already installed browser, set `BROWSER_PATH` to its executable before the test and skip the Chromium download. For example, on macOS use `export BROWSER_PATH='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'`. A managed Node installation may instead supply these exact libraries via `NODE_PATH`. For the portfolio contrast check, an existing axe 4.10.3 browser bundle can be supplied via `AXE_PATH`. All paths in commands refer to the machine running the handoff.
3. Compare the JSON output with [the clean baseline](baseline.json). Exit 0 means every selected expectation passed, 1 means at least one behavior failed, and 2 means a check or its setup errored. Missing dependencies also produce a Node startup error. Investigate error text before interpreting a broken selector, missing browser or incomplete install as a product finding.
4. Read the [reference diff](reference.patch) first. The commands below try it in the disposable checkout and run only its repaired behaviors plus a known-good control. In an existing implementation branch, adapt the specific changes after checking the current source.

```sh
git -C "$SITE_CHECKOUT" apply --check "$HANDOFF_DIR/reference.patch"
git -C "$SITE_CHECKOUT" apply "$HANDOFF_DIR/reference.patch"
node "$HANDOFF_DIR/verify.cjs" "$SITE_CHECKOUT" K01 K02 K05
```

5. Rerun the full suite after your own change. Compare the named checks with [the reference trial](trial.json). Finish the corresponding manual acceptance rows before marking a ticket complete. For a human-driven preview use `python3 -m http.server 8000 --bind 127.0.0.1 --directory "$SITE_CHECKOUT/dist"` and open [localhost](http://127.0.0.1:8000/).

### Expected results

| Check | Behavior | Clean reviewed commit | Same commit + reference patch |
| --- | --- | --- | --- |
| K01 | Ten sheets × two PDF paper settings | FAIL | PASS |
| K02 | Two shelves across eleven widths | FAIL | PASS |
| K03 | Home Birdhouse link and reload | FAIL | FAIL |
| K04 | Dedicated thumbnail URLs | FAIL | FAIL |
| K05 | Ten selected images and metadata | PASS | PASS |

The full trial deliberately retains open backlog items. Check IDs, selector names, and content counts refer to this revision. When an approved redesign changes markup or adds content, update the fixture deliberately and preserve the visitor-facing assertion. The runner serves local files with known MIME types, blocks third-party traffic, and creates a fresh browser context per check. Actual Pages headers, fonts, analytics, CDN configuration and operator publishing settings are separate checks. The baseline and reference trial record the same base commit; the trial also records local changes.

### Inspect the art as well as the page count

The optional second-stage check needs Poppler’s `pdftoppm`, Python 3, and Pillow. Run K01 with an evidence directory. Its JSON `evidence` value names the new subdirectory containing the 20 PDFs.

```sh
node "$HANDOFF_DIR/verify.cjs" "$SITE_CHECKOUT" K01 --evidence ./print-results
# Replace the example path below with the evidence value reported by K01.
python3 "$HANDOFF_DIR/check-artwork.py" "$SITE_CHECKOUT" "./print-results/site-check-EXAMPLE"
```

K01 checks page count and actual paper dimensions. The second command also checks nonblank art, agreement with the named source drawing, and an ink margin. It compares first-page raster images against the ten originals. Run both commands together. [Recorded artwork results](trial-artwork.json)

## Implementation brief for the next agent

Begin with paper output. In the clean-checkout rerun, **every one of the ten drawings produced four pages** on Letter and four on the requested A4 setting. With CSS paper size honored, all ten A4 requests still produced Letter-size pages. The included CSS repair fixed both defects. This is the first change a family would feel.

### The path from a home card to a printed sheet

| Entry point | Current behavior | Place to edit |
| --- | --- | --- |
| The home Birdhouse invitation | Navigates to the adventure page’s generic coloring fragment | Second book card in `dist/index.html` |
| Story shelf | Three cards at phone and desktop widths, two on tablet. The first opens a native details element. | Both page styles and `#stories` in `dist/budgie-adventures/index.html` |
| Sheet selector | Ten buttons carry file/title/description/alt fields. The click handler immediately updates preview metadata and image src. | `.color-picker`, `#selected-art` and the final inline script |
| Print path | The button calls `window.print()`. Native print applies the same CSS to a full-length page. | `@page`, `@media print`, the selected image, and its layout ancestors |
| Deployment | The Pages workflow uploads the checked-in `dist/` directory | `.github/workflows/deploy-pages.yml`, `dist/CNAME`, both HTML entry points |

<a id="implementation-1"></a>

### Change 1 · Print exactly the chosen sheet on the chosen paper

**Reproduce.** From a fresh desktop browser choose Sky Song, wait until it is visible, then print to PDF. Repeat for Flower Garden, the one landscape original. For browser-independent review collect 20 PDFs with K01. The baseline hid the rest of the site using visibility, so its layout still consumed paper. A fixed drawing repeated on each page. Independently, the fixed Letter page rule overrode A4.

**Implementation.** The reference patch retains the actual selected image as the only printable content. Its print CSS removes sibling branches from layout and resets the selected image’s ancestor grid, spacing, clipping, and width. The art stays in normal flow, uses contain, and respects the browser paper setting. This approach avoids synchronizing a second image. If the DOM hierarchy changes, revisit each ancestor selector. A standalone printable route is another valid design if native Print and the page button agree.

**Image readiness.** The reference patch fixes layout after an image loads. Finish the selection-to-print transition separately. On a sheet change, mark the new selection as loading, temporarily disable the page’s Print button, decode the chosen image, and check that the chosen ID is still current before enabling Print. A slow Birdhouse decode must not re-enable Print after the reader has chosen Sky Song. On failure keep the title and error associated with the correct sheet, offer Retry or the direct original, and avoid printing the last successful sheet by mistake. Test Back and reload during a pending load. Browser-menu Print cannot be disabled by a button; a direct per-sheet document with the correct image and a loading fallback makes that path easier to reason about.

**Paper checks.**

| Property | How to verify | Acceptance |
| --- | --- | --- |
| Page count | Parse each PDF with K01 | Exactly one page for each of 10 × 2 combinations |
| Actual paper | Inspect the PDF media box with CSS paper preference enabled | Letter approximately 612 × 792 pt; A4 approximately 595 × 842 pt |
| Correct drawing | Rasterize page one, compare against all ten original PNGs, inspect the nearest match and visible margins | Every named export matches its own original. Page centering and containment retain the entire drawing. |
| Real-world print | Physical printer and iOS/Safari print preview, then native browser Print after changing the sheet | Correct sheet, readable lines, no site chrome, no cut-off art. Record device and paper. |

**Measured repair.** K01 produced twenty one-page, correct-size exports. The separate raster check matched all twenty to the intended originals and found at least 19 pixels from ink to the page edge at its 512 px test scale. One page can still contain the wrong drawing; this second check catches blank and swapped outputs. Physical paper and AirPrint remain separate release checks.

<a id="implementation-2"></a>

### Change 2 · Keep the complete shelf at every width

Remove the two rules that set the final card to display none. Let two-column layouts wrap the third card onto another row. The small-screen rules currently switch that card back on, which is why only the middle widths fail. After verifying the simple fix, remove the now-redundant last-child show rule in a separate cleanup. Keep the page’s normal card display type intact.

**Boundary matrix.** Home switches from the mobile layout after 620 px and stops hiding the card after 850 px. The adventure equivalents are 640 px and 860 px. K02 checks each threshold, both immediate sides relevant to the two layouts, 768 px and desktop. Inspect widths around 620/621, 640/641, 850/851, and 860/861. Check touch targets and row order as well as counts. A third visible Sky Song card still needs an actual destination when its text invites a click.

<a id="implementation-3"></a>

### Change 3 · Give every activity a stable identity

**Suggested identity scheme.** Use short durable IDs such as `birdhouse-home` and `sky-song`, independent of ordering and translated title. Keep the existing PNG filenames working. Define a small manifest record containing ID, title, description, alt, source filename, thumbnail filename, orientation, and optional related story ID. Optional editorial fields include a materials note, reading prompt, and permission statement supplied by the owner.

1. Choose one canonical share route per sheet. A static route such as `/budgie-adventures/color/birdhouse-home/` supports sharing, saving and script-free use. A query such as `?sheet=birdhouse-home#color` is a smaller first step; a separate static download anchor is then needed for script-free access. Do not invent unique HTML routes without generating them into the uploaded directory.
2. Make the home Birdhouse invitation open the actual Birdhouse activity. Keep a separate broad “Browse all ten” action. Give normal links meaningful hrefs before enhancing them with an inline picker. K03 follows the real card and reloads the destination.
3. Route all selection changes through one function. Resolve a requested slug, update title/description/alt, set one selected control, set image and download target, and restore selection from history. Use pushState for explicit selections and handle popstate without adding another history entry. If using static routes with ordinary navigation, browser history already does this.
4. Keep one representation of the default sheet. Set the initial image metadata from the manifest; a generic page may default to Hello, Chirps, while a named route must preserve its chosen ID. For unknown or removed slugs render a usable collection link. Check direct loads, refresh, Back, Forward and a copied URL in a new browser context.
5. Give every sheet a descriptive download filename. “Download” must deliver the original or a verified print PDF. Preserve full resolution for the printed activity. Verify all ten destinations after deploying under the real base path. A filename containing spaces or punctuation in the title should still map to a stable slug.

**Data example.** For Birdhouse Home the reviewed file is `02-birdhouse-home.png`, a 1024 × 1536 portrait. Reuse its existing title and alt. Flower Garden is 1536 × 1024 landscape; infer orientation from the master’s dimensions instead of assuming every page is portrait. In this dataset print-paper orientation and source-art orientation are independent. Both paper sizes can contain a landscape drawing on a single page.

<a id="implementation-4"></a>

### Change 4 · Make the picker fast without reducing print quality

The ten originals occupy 15,965,033 bytes. The thumbnails reuse those originals in a cropped 4:3 frame. Produce separate previews at an appropriate rendered size and a higher-density variant where worthwhile. Use a format and compression that keep thin black outlines clear. Set intrinsic dimensions, use contain, and keep the full original for printing or downloading.

**Build sequence.** Read the manifest → load each master → derive thumbnail and dimensions → emit the page metadata and static links → verify referenced outputs → assemble `dist/`. Generate files with stable names or supply cache-safe versioning when replacing art. Store source masters outside a generated-only output directory if you introduce a clean build, and copy them explicitly. Today the checked-in masters are under `dist/assets/free-coloring/`; deleting dist before a source migration would delete the inputs.

**Network check.** K04 compares the URL of each loaded thumbnail with the URL of the selected master. It does not measure byte transfer. On an empty-cache mobile profile also record initial requests, transferred bytes before first interaction, and additional bytes after choosing the last sheet. A reasonable initial design budget is 250 KB for ten small previews combined. Judge the budget alongside visible line quality. Selecting a second image offline should show useful retry/download feedback if its full master was never cached.

<a id="implementation-5"></a>

### Change 5 · Complete a story-to-paper journey

**Home.** Lead with two concrete actions, “Read the story starter” and “Choose a free coloring sheet.” Keep the bookshelf for browsing titles, and place the series development status beside titles. A parent arriving directly from a shared activity link needs a route back to the series. Replace generic emoji with approved character art gradually, starting with the featured story and its paired sheet.

**Story page.** Use the existing excerpt, an approved reading prompt, and one related activity. Let the excerpt expand through native details or a direct readable page. Give the forthcoming second story an honest status and make the ten-tale map show which stops can be opened. If a destination is still unwritten, present its title as editorial text. The approved title and availability belong in one place so the home and adventure pages agree.

**Grown-up information.** Put the paper setup, writing/reading age, credits, and approved use terms near the print action. Move the optional player near the song activity with a deliberate listening action. If the external frame is blocked, collapse it to a concise fallback. Verify the privacy description against the actual external media and analytics behavior. The site already supports browsing without accounts, uploads or comments.

**Content completion test.** Ask a grown-up to start on home, find Birdhouse, print one complete sheet, go back to the excerpt, and find another activity. Note confusing terms, taps that miss their target, printer setup and whether the child recognizes the same character in the story and drawing. A print-dialog-open event cannot confirm that a physical page printed.

<a id="implementation-6"></a>

### Change 6 · Share the shell and put validation before publishing

Extract the base colors, type, links and existing menu interactions into shared files served under `dist/`. Leave print rules and page-specific illustrations scoped to their route. Preserve the root, `/budgie-adventures/`, fragment links, asset URLs, favicon and CNAME. Test the shared links twice, once from a nested activity page where relative paths resolve differently.

If templates become useful, establish a new source directory first, generate into a temporary output directory, and compare both pages and all assets before switching the workflow. Configure the Pages workflow to validate the exact directory it subsequently uploads. A preview served from the repository root can conceal broken paths because production serves `dist/` as the root. Roll back by republishing the previous verified artifact or reverting the relevant change through the owner’s release process.

**Completion note.** Report the tested SHA, K01–K05 results, PDF media boxes, visible art identity, which deep link opened Birdhouse, and which physical devices were checked. Name editorial items awaiting manuscript, artwork or permission confirmation. The tested patch addresses pagination, paper size and responsive card visibility. Selection races, shareable pages, performance, and the finished story map are separate deliverables.


---

# Original review and source evidence

## What the family site should do

A grown-up visiting with a four- to eight-year-old should be able to recognize the Chirps, choose a short story or a coloring sheet, and get a usable page onto paper. The product already has one three-paragraph starter, a recurring cast, and ten original-site printable assets. The fastest improvement is to make those existing activities easier to reach and reliable to print.

**Keep** the clearly stated in-development book status, native story disclosure, large page-choice buttons, friendly character names, and account-free reading and coloring. Each of the ten selectors loaded a real drawing with an accessible description. Both public HTML pages matched the checked-out source after newline normalization. [Book status](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/index.html#L114-L122) · [Activity picker](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L265-L294)

|Reference|What the reference does|What fits Crayon Kite|
|---|---|---|
|Bluey|Connects a familiar character to a named, shareable activity page with a direct Download action.|Give Birdhouse Home its own usable link, a full drawing preview, and a print or download action. Link a Chirps story back to the related sheet. [Bluey activity](https://www.bluey.tv/make/bluey-colouring-sheet/)|
|Crayola|Makes free coloring pages a visible destination and groups activities for browsing.|Surface the ten free sheets on the home page under “Color & print.” At this size, a simple illustrated grid with names is sufficient. [Free coloring pages](https://www.crayola.com/free-coloring-pages)|

## Bugs and behavior to fix

### P1 · “Print this page” produced four copies of one drawing

After selecting Sky Song and letting the image decode, Chromium’s print-to-PDF emitted four pages with Letter settings and four with A4 settings. All four Letter pages rasterized to identical images. The CSS hides the site with visibility, which preserves its paginated layout, and positions the selected picture fixed on the page. The stylesheet also explicitly requests Letter. [Print rules](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L114-L122) · [Print button](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L338-L349)

![Four identical Sky Song sheets from the baseline Letter export](baseline-print.jpg)

**Fix · Small.** Create a dedicated print root containing just the selected art in normal flow. During print, remove the rest of the document from layout. Fit the entire drawing inside the printable area, respect the selected paper size, and decode the selected image before enabling Print. Give native browser printing the same result as the page button.

**Accept when** every sheet prints exactly once at Letter and A4. Test all four borders on the landscape Flower Garden and a portrait sheet. A temporary print-root trial yielded one page for all 20 sheet/paper combinations. A physical printer and mobile print dialogs still need release checks.

### P1 · The adventure map disappears at tablet widths and lacks a destination

At 768 px both shelves showed two cards. At 390 and 1440 px both showed three. The home stylesheet hides the last book from 621–850 px and the adventure stylesheet hides the last story from 641–860 px. The missing item is the Sky Song/map card. On larger screens the home link lands at the general story shelf and “See where the map leads” is a span, so there is still no navigable map. [Home breakpoint](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/index.html#L84-L89) · [Story breakpoint](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L147-L176) · [Map copy](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L251-L260)

**Fix · Small for visibility, medium for the map.** Let cards wrap naturally at tablet widths. Until there is a map, use a plainly labelled series preview. Then link to a real map containing the available story, future story names where approved, and the current place in the sequence.

**Accept when** all three cards remain available at 620, 640, 768, 850, and 861 px. Every action-styled label reaches meaningful content with keyboard and touch. A planned tale can carry a plain status label.

### P2 · The birdhouse invitation opens the wrong drawing

The home card invites visitors to try the free birdhouse page but links only to the coloring section. A fresh visit there selected “Hello, Chirps!” Birdhouse Home is the second drawing. Selecting a sheet updates the DOM but leaves no shareable selection. [Home invitation](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/index.html#L117-L119) · [Initial picker](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L269-L289) · [Selection handler](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L338-L347)

**Fix · Small.** Add stable sheet IDs and resolve them on entry, or publish a small static page per sheet. Point the home card directly to Birdhouse Home. Keep a generic link for browsing all ten. Use ordinary links for a direct art or printable fallback when scripts are unavailable.

**Accept when** a fresh visit from the home card displays Birdhouse Home in the title, image, selected choice, and print output. A shared link restores it on another device. Unknown sheet IDs land on an explained default.

### P2 · The preview strip uses full print images as thumbnails

Every picker image points to its full PNG. The ten originals total 15,965,033 bytes, ranging from 1.45 to 1.80 MB apiece. Lazy loading postpones some requests, so the initial transfer depends on viewport and scroll position. The 4:3 cropped previews also cut away part of nine portrait illustrations. [Image styling](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L103-L115) · [Ten thumbnail URLs](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L272-L283)

**Fix · Medium.** Produce small, high-contrast preview files and keep original resolution for the chosen printable. Set intrinsic sizes. Show the entire drawing with a neutral border. Load the selected master on demand, and handle a loading or failed image without printing a previous sheet.

**Accept when** opening the picker does not request multiple unselected print masters, every preview shows the complete drawing, and the printer still receives the intended original or print PDF. A proposed starting budget is 250 KB total for ten thumbnails. Measure it on an empty cache.

### P2 · Core controls have no useful script-free path

The ten thumbnails and first picture are present in HTML. The other choices and Print are buttons with JS-only behavior. The narrow navigation on both pages also requires script. A partially loaded page looks interactive while offering the default image and story sample only. [Mobile navigation](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/index.html#L85-L89) · [Activity actions](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L273-L294) · [Event setup](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L322-L349)

**Fix · Medium.** Make each activity reachable through a normal link. Enhance that navigation into an inline picker when scripts are available. Expose a direct downloadable sheet and keep the basic navigation available on first paint. Announce a short selected-title update where the preview is below the visible strip.

**Accept when** a parent can open the third sheet with JS disabled, save or print that sheet, and return to the shelf. With JS enabled, keyboard and touch users can choose all ten with the selected title and preview in agreement.

## Finish the experience

### First release · Make a complete read-and-color visit

Lead with two actions, “Read the story starter” and “Choose a free coloring page.” Link the starter directly, show its approximate reading time after timing a real read-aloud, and follow the final paragraph with a question a child can answer and the corresponding activity. The current first card takes a visitor to the top of the whole story world. Other cards describe future adventures. [Home cards](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/index.html#L114-L121) · [Story starter](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L239-L259)

**Acceptance.** A grown-up goes from home to the first paragraph in one activation, opens a related drawing, prints one sheet, and returns to the story. The site accurately distinguishes a finished free sample from a book in development.

### First release · Give each drawing a useful activity page

Reuse the existing title, description, and alternative text. Add the full preview, a plainly labelled print action, an original-resolution download or single-page PDF, and a link back to the collection. If the publisher permits classroom copying, state the permitted use in ordinary language. Use the same stable URL for links from stories and a teacher’s shared bookmarks. [Existing per-sheet data](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L272-L292)

**Acceptance.** Each of ten links opens the right art in a fresh browser. The filename identifies the activity after download. Check Letter and A4, portrait and landscape originals, color and grayscale, and a phone’s share or print sheet.

### Next release · Give the Chirps a recognizable story world

The two hero sections already show the family’s own artwork. Several shelf covers and cast cards use generic emoji. Reuse approved character art for Daisy, Chip, Caty, and Bella. Pair each character with one distinguishing feature, a short line from the sample, and a related activity. Give the series map a current stop, an available sample, and clearly labelled upcoming stops. [Story covers](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L245-L259) · [Character cards](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L297-L304)

**Acceptance.** A child can recognize a character on the shelf and on its coloring page. Every map stop with an action has a real destination. Publishing the next story should require one content addition, its approved illustration, and its activity link.

### Next release · Put music and grown-up information where they help

The Udio player appears before the adventure heading. On small screens the iframe alone is 210 px tall. The live embed returned HTTP 200 during review. In a local dependency-failure test its occupied area remained above the story. A returned document does not show whether audio completed. Move the optional song beside the Sky Song content, keep the main story and coloring actions first, and provide a compact fallback. [Song embed](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L209-L217) · [Mobile size](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L154-L165)

**For grown-ups.** Put reading age, printable formats, paper/ink tips, and available usage permissions together. Explain that listening uses an external player and that the site uses aggregate analytics. Review the service’s behavior before making broader privacy claims. Keep the existing no-account route. [Current grown-up notes](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L307-L317) · [Site analytics and scope](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/README.md#L3-L9)

**Acceptance.** Blocking the embed leaves story and print actions in place. Opening music is a deliberate choice. Families can find paper setup and usage notes from the chosen drawing.

### Later · Prepare the book release without announcing one prematurely

Create a reusable title page for an approved excerpt, series order, cover art, author or illustrator credit, availability, and related free sheets. Give each public title and activity an absolute canonical URL and a meaningful social preview. Add purchase links and product availability only when the publisher has an actual release and destination. A ten-page download pack is a useful later addition once individual sheets pass print QA. [Current release wording](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/index.html#L114-L122) · [Deployment scope](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/README.md#L7-L17)

## Clean up the code

|Change|Why it matters here|Safe migration and check|
|---|---|---|
|Clarify what is authored and what ships|The repository tracks the two HTML pages under dist, and Pages uploads that folder directly. Treat it as the current production source until a source-to-dist build exists.|Start by extracting shared files within dist. If templates are added, make a clean build generate both existing routes and the assets before deployment. Preserve the custom domain file. [Pages workflow](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/.github/workflows/deploy-pages.yml#L16-L36)|
|Share the small navigation behavior|Both documents contain near-duplicate menu CSS and toggle handlers with slightly different names and breakpoints.|Use a shared menu script and base styles. Keep page-specific art and type local. Add Escape, focus return, and a resize reset. Check both pages and hash links at 320 px, tablet width, and short landscape. [Home menu](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/index.html#L141-L156) · [Adventure menu](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L322-L337)|
|Describe each printable once|Filename, title, alt text, initial preview, and selected state are scattered across attributes and markup. Every future download format adds another chance to drift.|Create a small manifest with stable ID, original, preview, orientation, title, description, and related story. Generate static links and the initial view from those same records. Check every named file and verify a unique ID per sheet. [Picker data](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L269-L294)|
|Simplify print and styling rules|There is an unreferenced print-only class, hard-coded Letter sizing, and duplicate last-card hide/show pairs. Their interaction already affects real output.|Keep screen and print rules in focused files. Remove the old rules only after comparing the 20 outputs and desktop/tablet/mobile shelves. Add metadata to identify each printed sheet if it fits inside the verified one-page layout. [Print and responsive CSS](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/budgie-adventures/index.html#L116-L154)|
|Add a check before the existing deploy step|The workflow checks out, configures Pages, and uploads dist directly. It has no validation job for the core activity.|Verify both routes, assets, deep links, card counts at tablet width, and the ten one-page exports. Only then upload the validated folder. Retain the simple static deployment. [Workflow](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/.github/workflows/deploy-pages.yml#L16-L36)|

## Delivery and verification

**Release 1 · Deliver the right paper.** Fix print pagination, stable sheet links, hidden tablet cards, and thumbnail size. Have one adult use a physical printer and another use mobile print preview. Verify that selecting a new drawing immediately before printing cannot print the old art.

**Release 2 · Finish one complete adventure.** The writer and illustrator approve the read-aloud sample, character imagery, and related printable. Connect those through the shelf and story map. Observe whether a family can find the named activity, print once, and return without assistance. Browser print-dialog events cannot tell you whether paper came out.

**Release 3 · Grow the catalog deliberately.** Add a second complete read-and-color pair using the manifest, then publish a pack or book page when the content and rights are ready. Cross-check preview metadata, printable filenames, and navigation from a shared activity link before release.

**Evidence and limits.** Tested both pages, ten image selections, five viewport sizes, and Chromium PDF generation. The initial desktop axe 4.10.3 WCAG A/AA tag scan reported zero violations on the two local first-party pages. The optional embed was blocked for that scan. Reading comprehension, screen-reader usability, Safari/AirPrint, and physical print quality need human checks. File weights describe assets on disk. Effort labels are relative planning estimates.
