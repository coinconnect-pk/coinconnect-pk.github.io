---
layout: page
title: Topics
permalink: /topics/
description: Every article on CoinConnect Intelligence, grouped by the part of the market-entry problem it covers.
---

Analysis here is organised around the six problems an operator actually faces when taking a crypto business into a new market.

{% assign cats = site.categories | sort %}
{% if cats.size > 0 %}
{% for cat in cats %}
## {{ cat[0] }}

<ul>
{% for post in cat[1] %}
<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <span style="color:var(--text-faint);font-size:0.85rem;">&middot; {{ post.date | date: "%-d %b %Y" }}</span></li>
{% endfor %}
</ul>
{% endfor %}
{% else %}
Articles will be listed here as they publish.
{% endif %}

## What we deliberately do not cover

CoinConnect Intelligence is about commercial strategy: how to enter a market, find partners, launch, and compete. It is not a regulatory explainer.

Where a rule matters to a commercial decision, it appears as context inside an article. It is never the subject of one. For the regulatory detail itself — licensing requirements, compliance obligations, filing mechanics — go to the primary source, the regulator.
