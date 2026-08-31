"""
Generates the product pages from one shared chrome.

The site has no build step at serve time -- the generated HTML is committed and
GitHub Pages serves it directly. This script exists so the header, footer, fonts
and stylesheet link stay identical across every page instead of drifting apart
across eight hand-maintained files.

    python build.py
"""

import io
import os

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="canonical" href="https://kapapi.com/__PATH__">
<link rel="icon" href="__ICON__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/kapapi.css">
</head>
<body>

<header class="site-head">
  <div class="wrap">
    <a class="wordmark" href="/">
      <span class="mark" aria-hidden="true"><span></span><span></span><span></span></span>
      KaPaPi
    </a>
    <nav class="site-nav">
      <a href="/cleanpaste/">CleanPaste</a>
      <a href="/sortdoc/">SortDoc</a>
      <a href="https://github.com/kapapi-dev/__REPO__">Source</a>
    </nav>
  </div>
</header>

<main>
<section style="padding-top:3.5rem">
<div class="wrap wrap-narrow prose">
"""

FOOT = """
</div>
</section>
</main>

<footer class="site-foot">
  <div class="wrap">
    <a class="wordmark" href="/" style="font-size:1rem;text-decoration:none">
      <span class="mark" aria-hidden="true"><span></span><span></span><span></span></span>
      KaPaPi
    </a>
    <span class="spacer"></span>
    <a href="/__SLUG__/">__PRODUCT__</a>
    <a href="/__SLUG__/privacy.html">Privacy</a>
    <a href="/__SLUG__/terms.html">Terms</a>
    <a href="/__SLUG__/support.html">Support</a>
    <a href="mailto:support@kapapi.com">support@kapapi.com</a>
  </div>
</footer>

</body>
</html>
"""

ICONS = {
    "cleanpaste": (
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
        "%3Crect width='32' height='32' rx='7' fill='%230f7b8a'/%3E"
        "%3Crect x='7' y='8' width='18' height='3' rx='1.5' fill='%23fff'/%3E"
        "%3Crect x='7' y='14' width='18' height='3' rx='1.5' fill='%23fff'/%3E"
        "%3Crect x='7' y='20' width='6' height='3' rx='1.5' fill='%23fff'/%3E"
        "%3Crect x='16' y='20' width='9' height='3' rx='1.5' fill='%23d98218'/%3E%3C/svg%3E"
    ),
    "sortdoc": (
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
        "%3Crect width='32' height='32' rx='7' fill='%231f5fb8'/%3E"
        "%3Crect x='7' y='8' width='8' height='3' rx='1.5' fill='%23fff'/%3E"
        "%3Crect x='7' y='14' width='13' height='3' rx='1.5' fill='%23fff'/%3E"
        "%3Crect x='7' y='20' width='18' height='3' rx='1.5' fill='%23d98218'/%3E%3C/svg%3E"
    ),
}

REPOS = {"cleanpaste": "cleanpaste", "sortdoc": "sortdoc"}
NAMES = {"cleanpaste": "CleanPaste", "sortdoc": "SortDoc"}


def page(slug, filename, title, desc, body):
    html = (
        HEAD.replace("__TITLE__", title)
        .replace("__DESC__", desc)
        .replace("__PATH__", "%s/%s" % (slug, filename))
        .replace("__ICON__", ICONS[slug])
        .replace("__REPO__", REPOS[slug])
        + body
        + FOOT.replace("__SLUG__", slug).replace("__PRODUCT__", NAMES[slug])
    )
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), slug, filename)
    io.open(path, "w", encoding="utf-8", newline="\n").write(html)
    print("wrote %-28s %6d bytes" % (path.split(os.sep)[-2] + "/" + filename, len(html)))


if __name__ == "__main__":
    import content

    for slug, filename, title, desc, body in content.PAGES:
        page(slug, filename, title, desc, body)
