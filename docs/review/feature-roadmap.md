# Crayon Kite · New features and artwork

## Build the Chirps nature-card maker first

A grown-up wants a five-minute activity they can do with a child today, even if they are staying indoors. The current site has an excerpt, ten selectable coloring images and a song. The nature-card maker creates a new activity from two choices, then sends the family to paper or conversation. Each output has a place, three editorially written prompts and space to draw. Children can tell their answers aloud. [Reviewed site](https://github.com/cephyrixzyth/crayon-kite/tree/dd6007ce69a1682e93ba968c87c7a4bbd13e3014)

[Open the working preview](preview.html) · [Open the original artwork](art/garden-listening-trail-master.png) · [See prototype check results](verification.json)

### The six cards

| Setting | Look for shapes | Listen for rhythm | Imagine a story |
| --- | --- | --- | --- |
| **At a window** | Find a round shape and a corner, trace an outline, then draw or describe it. | Hear a repeated sound or watch a repeated movement, tap it back, then draw dots or describe the rhythm. | Choose something that could carry a feather, imagine a landing spot, then sketch or tell an ending. |
| **In the garden** | Compare two leaf shapes, trace their edges, then sketch or describe the difference. | Pause with a grown-up, listen or watch a stem, then echo and record a pattern. | Pick a visible clue, imagine why a budgie would pause, then draw or tell what it discovers. |

The preview includes the six complete drafts. They are original activity prompts for the handoff. They do not establish new story canon or book availability. The feature needs neither a microphone nor location access. The family chooses a setting, and the drawing remains on paper.

### Production implementation

1. Publish a proposed `dist/budgie-adventures/nature-cards/index.html` route and link it from Color & Make and the grown-up section. Use “Make a nature card” as the action. Preserve direct access to the existing free sheets.
2. Store a stable place ID and activity ID, three short prompts, a nonvisual or spoken alternative where applicable, and the source illustration ID. Keep the default card in plain HTML. Load and render the chosen record when scripting is available. A child should be able to understand a single prompt without remembering a paragraph.
3. Print only the chosen title, prompts, and drawing space. Use the actual paper setting and keep decorative full-color art off the ink-light sheet. Letter and A4 must each make one correctly sized page. “Save card text” should retain the spoken alternatives and a descriptive filename. A future illustrated printable could use approved outline art with generous ink margins.
4. Keep the two selections in allowlisted fragment fields so a grown-up can reopen a card. Keep answers, names, photos and precise locations out of the interface. A window option, a visual alternative for the listening card, and a spoken alternative to drawing make the activity feasible in more settings.
5. The supplied picture uses the checked-in family drawing as a character reference. Ask the owner to review proportions, markings and palette before treating it as a final series illustration. Leave story titles, ages and availability aligned with approved copy.
6. Publish into the actual Pages artifact under `dist/`. From the nested route test assets, home, the story shelf and the coloring picker. Test a household printer or AirPrint before making a physical-print claim. When more cards are added, generate the chooser and print output from the same records.

**Acceptance.** A family can reach the maker, choose a place and activity, print one usable page and explain the first prompt. The title, exported text, paper and reload state must all refer to the same combination. A missing illustration should leave all three prompts legible. Observe whether the adult needs to rephrase a prompt and whether there is enough room to draw. Revise the wording before adding more combinations.

## Three further builds

| Feature | First usable slice | What to make | Completion test |
| --- | --- | --- | --- |
| **Arrange a three-panel story** | A child orders three wordless scenes, tells an ending, then prints their sequence. | Three original approved panels of a simple action, stable panel IDs, visible earlier/later buttons, optional drag, and a printed sequence using the chosen order. | All six possible orders survive reorder and print. Keyboard controls work without drag. Invite different endings without a “wrong answer” message. |
| **Fold-and-tell tabletop theater** | Print one birdhouse backdrop and character cards for a grown-up to prepare; use a prompt to stage a tiny scene. | Ink-light outlines, distinct cut and fold conventions, separate high-contrast assembly directions, plus a flat-card option. Create one physical prototype before expanding the cast. | A grown-up assembles it from the supplied pages. Printed alignment works on Letter and A4, and families who skip cutting can still use the cards laid flat. |
| **Read together with a narrator** | Play a short owner-approved excerpt, pause, repeat a paragraph or read along with its matching text. | A cleared recording, exact transcript, paragraph timestamps, and playback buttons. Keep the existing story text accessible ahead of loading the audio. | Text, narration and highlighted paragraph agree after pause, replay and seeking. Reading works with audio blocked. Record voice and excerpt permissions before publication. |

**Sequence.** The nature cards can use the supplied drafts immediately for local testing. The story sequencer is the next digital build after three illustrations are approved. The theater depends on a successful paper assembly. The narrator depends on rights-cleared audio and an exact transcript. None of these additions needs child profiles or user uploads.

## Art direction and production

**Supplied asset.** Four budgies gather by a small birdhouse and pond. The tall tufted bird has teardrop chest markings; the medium birds have a zigzag and plain forehead respectively; the small bird has a star. The checked-in monochrome family drawing supplied those identifiers. The new watercolor palette and garden setting are concept directions. The preview uses the illustration as an activity opener. [Family reference](https://github.com/cephyrixzyth/crayon-kite/blob/dd6007ce69a1682e93ba968c87c7a4bbd13e3014/dist/assets/chirps-family.jpg)

**Next artwork.** For the three-panel sequencer, lock character size ratios, camera angle, wing markings and the key prop before drawing the individual panels. Give each panel a readable silhouette at phone width. For the theater, design a separate black-line master with thick outlines, broad tabs and a printed size guide. For the narrator, use one scene image per approved passage and keep the words as HTML.

**Art review.** Check four visible faces and identifying marks at 320 px. Fit the full family into the frame; leave body parts and tail tips visible. In the preview the print page uses the space for the child’s own drawing. Use a short descriptive alt when the scene is a prompt; use empty alt when it repeats the immediately adjacent explanation. Full generated master, web variants and production notes are included. [Asset files and provenance](ARTWORK.md)

## What the next agent can run

From this directory, run `node verify-feature.cjs` after installing the dependencies in the parent handoff. The checks exercise all six combinations, downloads, invalid input, mobile widths, and one-page Letter/A4 output. Set `FEATURE_PDF_DIR` to keep the PDFs, or `BROWSER_PATH` to use an installed Chrome. The earlier K01–K05 checks still cover the existing coloring-sheet flow.