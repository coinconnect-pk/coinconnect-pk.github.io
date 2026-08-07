# The publishing queue

This folder holds finished articles waiting to go out. **Two are released per day** — 06:00 and 18:00 PKT — lowest number first.

Articles are **written in advance, in batches, and banked here** rather than generated on the day. Nothing in this repository calls a model API — a Claude Pro subscription cannot be called from CI, and writing from primary documents needs the documents in hand anyway.

The writing brief is in `../CONTENT-PROMPT.md`.

## Naming

```
001-why-distribution-beats-product.md
002-how-exchanges-pick-a-market.md
003-what-a-listing-actually-costs.md
```

Three digits, then a dash, then a slug. The number decides publication order and nothing else. The publisher stamps the real date on the article when it goes out, so nothing in here carries a meaningful date.

## What happens on publish

1. The publisher takes the lowest-numbered file.
2. It validates it against every house rule (see `../overrides/README.md`).
3. If it passes, it stamps today's date, moves it to `_posts/`, and **deletes it from this folder**.
4. If it fails, nothing publishes and the Actions run goes red with the reason.

The file leaving this folder *is* the record that it published. Git history holds the rest, and `_data/published-log.csv` keeps a running list.

## Reordering

Rename the files. `007-` becomes `002-` and it jumps the queue. Order is purely numeric, so leaving gaps is fine and makes inserting easier.

## Refilling

The publisher prints a warning in the Actions log when **fourteen or fewer** articles remain — about a week's worth at two a day. That is the signal to write a new batch.

If the queue empties completely, nothing goes out and the run logs `QUEUE EMPTY`. It does not fail loudly, and it does not put out anything half-finished — it just stops until you refill it.

## Editing a queued article

Just edit the file here on GitHub and commit. It has not gone out yet, so there is no correction notice needed and no URL to break.
