# How to publish your own article on any day

**Malik — this is for you. No software to install. Everything happens in your web browser.**

The blog publishes one article every morning at 6:00am Pakistan time, on its own. You do not need to do anything for that to happen.

This page is for the days when you want to publish **your own** article instead — a reaction to news, a take you want out that day, something tied to a meeting.

---

## The short version

You put your article in a folder named after the date you want it to appear. That morning, the blog publishes yours instead of the queued one.

**Nothing is lost.** The article that was queued for that day simply moves to the next day. The queue never skips and never burns a slot.

---

## Step by step

### 1. Open the repository

Go to your CoinConnect blog repository on GitHub and sign in if it asks.

### 2. Start a new file

Near the top right, click the **`Add file`** button, then choose **`Create new file`**.

### 3. Type the file path

You will see a box at the top with the repository name and an empty field next to it.

Type this into that field, changing the date to the day you want the article to appear:

```
overrides/2026-08-15/article.md
```

**Type the forward slashes `/` as you go.** GitHub creates the folders automatically as you type them. You do not need to make the folders separately.

The date must be written **year-month-day**, with dashes, four digits then two then two. `2026-08-15`, not `15-08-2026` and not `2026-8-15`.

The file must be called **`article.md`** exactly.

### 4. Paste the settings block

In the big text box underneath, start with this block, exactly as shown:

```
---
layout: post
title: "Your headline goes here"
date: 2026-08-15 09:00:00 +0500
categories: [Market Entry]
author: "Malik Abbas"
description: "One sentence saying what the reader will learn. Between 120 and 165 characters."
---
```

Then write your article below it.

**Four things to get right:**

- Keep the three dashes `---` on their own lines, top and bottom.
- The **date** must match the folder name.
- **categories** must be exactly one of: `Market Entry`, `Listings`, `PR & Comms`, `Partnerships`, `Positioning`, `Market Data`
- **description** must be between 120 and 165 characters. Shorter or longer and the publisher rejects it.

### 5. Write in Markdown

Markdown is just plain text with a few marks for formatting:

| To get this | Type this |
|---|---|
| A section heading | `## Your heading here` |
| **Bold text** | `**bold text**` |
| A bullet point | `- your point` |
| A numbered point | `1. your point` |
| A link | `[the words](https://coinconnect.site)` |

Leave a blank line between paragraphs.

### 6. Save it

Scroll to the bottom. Click the green **`Commit changes`** button, then **`Commit changes`** again in the box that appears.

**That is it.** The article publishes on the morning of the date you chose.

---

## Do it before 6:00am

The blog checks for your article at 6:00am Pakistan time. Add it any time before then — the night before is safest.

**Missed the deadline, or want it live right now?**

1. Click the **`Actions`** tab at the top of the repository
2. Click **`Daily article`** in the left-hand list
3. Click **`Run workflow`** on the right
4. Tick **`force`**
5. Click the green **`Run workflow`**

It publishes within about two minutes.

**Want to check it passes the rules without publishing it?** Same steps, but tick **`dry_run`** instead of `force`. It will tell you exactly what is wrong, and change nothing.

---

## The house rules

These are checked by machine. If your article breaks one, it will not publish, and the Actions log will tell you which rule you broke.

- **1200 to 2100 words**
- **At least four `##` headings**
- **Must end with a section called `## About this analysis`**
- **Title under 75 characters**
- **Description between 120 and 165 characters**
- **Category must be one of the six**
- **At most one link to coinconnect.site**
- **No links except** to the approved list: coinconnect.site, and official sources (PVARA, SECP, State Bank, FBR, FATF, World Bank, IMF, Chainalysis, Statista)

### The two rules that matter most

**1. Never write a headline about regulation.**

The publisher will block any title or description containing terms like *VASP licence*, *PVARA licensing*, *NOC application*, *travel rule*, *AML/CFT*, *fit and proper*, *goAML*, *MLRO*, and others.

This is deliberate. Those keywords belong to **Sarzif Policy**, which is Noor Aslam's separate company with 120 queued articles on exactly those terms. If this blog competes for them, both sites lose, and so does your working relationship.

Regulation is allowed **inside** an article as context. It may never be what the article is *about*.

**2. Never write a claim you cannot evidence.**

The machine cannot check this one. You have to.

- Do not name a client, partner or exchange unless you can show a document, or they have said it publicly themselves.
- Describe finished relationships in the past tense, or leave them out.
- Do not describe work covered by an NDA, even indirectly.
- If a figure is not from a named source you can point to, do not print it.

A single unverifiable boast can cost more than the blog will ever earn. Leave it out.

---

## A template to start from

Copy everything below into a new file and edit it.

```
---
layout: post
title: "How exchanges choose which market to enter next"
date: 2026-08-15 09:00:00 +0500
categories: [Market Entry]
author: "Malik Abbas"
description: "Most expansion decisions come down to four variables, and user count is the least important of them. Here is the framework operators actually use."
---

Two or three short paragraphs setting up why this matters to someone running a
crypto business. No heading above this part. Get to the point fast.

## What actually drives the decision?

Answer the question here in 40 to 60 words. Keep it complete on its own, so a
reader who stops here still has the answer. Then carry on with the detail below.

More explanation. Then a list:

- First point
- Second point
- Third point

## Who gets this wrong, and how?

Another short answer, then the detail.

## What does a realistic sequence look like?

1. First step
2. Second step
3. Third step

## What should an operator do first?

Practical, specific, and honest about what you do not know.

## About this analysis

This is commercial analysis drawn from CoinConnect's market entry work in
Pakistan and South Asia. It reflects judgement about how these markets behave,
not established fact, and readers should test it against their own situation.

Nothing here is legal, tax or investment advice.
```

---

## Common mistakes

| What went wrong | The fix |
|---|---|
| Article did not appear | Folder date did not match the day. Check the folder name spelling |
| Actions shows a red X | Open the run and read the log — it names the exact rule you broke |
| "SARZIF COLLISION" in the log | Your headline uses a regulatory keyword. Rewrite the title around the commercial angle |
| "description is N chars" | Your description is outside 120–165 characters. Count it and adjust |
| Page looks broken | A `---` line is missing or has spaces around it. Exactly three dashes, on their own line |
| Two articles published | You added an override *and* ran the workflow with `force` ticked |

---

## Adding a reference document

You can put a PDF or any other file in the same dated folder. Only `article.md` gets published — everything else just stays in the repository as your working record.

---

## If something breaks

Take a screenshot of what you see and send it on. **Do not delete anything and try again** — it is much easier to fix while the mistake is still visible.
