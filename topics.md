---
layout: page
title: Topics
permalink: /topics/
description: Every article on CoinConnect Intelligence, grouped by the part of Pakistan's virtual asset framework it covers.
---

Analysis here is organised around the seven areas of Pakistan's virtual asset framework that a regulated business has to deal with.

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

## How this is written

Every article is written from the published documents themselves and cites the provision it relies on. Where the exact wording carries the obligation, that wording is quoted directly.

Where the framework is genuinely unclear, or guidance has not yet been issued, the article says so rather than smoothing over it.

This is information and analysis, not legal advice. See the [editorial policy]({{ '/editorial-policy/' | relative_url }}) for the full standards.
