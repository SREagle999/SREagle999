#!/usr/bin/env python3
"""Generates the light/dark SVG cards used by README.md into ../assets.

Run:  python scripts/build.py
Edit the CARDS / ABOUT / HEADER data below, re-run, commit the assets.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

THEMES = {
    "dark": dict(bg="#0D1117", border="#30363D", text="#E6EDF3", muted="#8B949E",
                 accent="#58A6FF", green="#3FB950", chip="#161B22"),
    "light": dict(bg="#F6F8FA", border="#D0D7DE", text="#1F2328", muted="#59636E",
                  accent="#0969DA", green="#1A7F37", chip="#EAEEF2"),
}
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def t(s):
    return escape(s)


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{t(title)}">'
            f'<title>{t(title)}</title>{body}</svg>')


# ---------------------------------------------------------------- header
HEADER = dict(
    name="Gabe Harris",
    sub="Mathematics with Computing  /  MIT  /  Class of 2030",
    tags=["numerical linear algebra", "GPU computing", "ML for physical systems", "embedded systems"],
)


def header(c):
    w, h = 1000, 210
    body = f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12" fill="{c["bg"]}" stroke="{c["border"]}"/>'
    body += f'<text x="48" y="92" font-family="{SANS}" font-size="54" font-weight="700" fill="{c["text"]}">{t(HEADER["name"])}</text>'
    body += f'<rect x="48" y="108" width="64" height="4" rx="2" fill="{c["accent"]}"/>'
    body += f'<text x="48" y="146" font-family="{MONO}" font-size="18" fill="{c["muted"]}">{t(HEADER["sub"])}</text>'
    x = 48
    for tag in HEADER["tags"]:
        tw = int(len(tag) * 8.6 + 28)
        body += f'<rect x="{x}" y="164" width="{tw}" height="28" rx="14" fill="{c["chip"]}" stroke="{c["border"]}"/>'
        body += f'<text x="{x + tw/2}" y="183" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c["accent"]}">{t(tag)}</text>'
        x += tw + 10
    return svg(w, h, body, f'{HEADER["name"]}. {HEADER["sub"]}.')


# ----------------------------------------------------------------- about
ABOUT_USER = "gabe@mit"
ABOUT = [
    ("education", "MIT, B.S. Mathematics with Computing, May 2030"),
    ("research", "CSAIL Julia Lab  +  Boriskina Group (META Lab)"),
    ("focus", "numerical linear algebra, GPU computing, scientific ML"),
    ("systems", "MIT Satellite Team, NASA F Prime, embedded C/C++"),
    ("industry", "Data Analyst & Engineer, Capital One"),
    ("languages", "Python, C++, C, Julia, SQL, TypeScript, MATLAB"),
    ("tools", "PyTorch, CUDA, OpenCV, FastAPI, Elasticsearch, AWS"),
    ("recognition", "HackMIT 2026 2nd place (team), AFROTC scholar, National Merit"),
]


def about(c):
    w = 1000
    row = 30
    h = 116 + row * len(ABOUT)
    body = f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12" fill="{c["bg"]}" stroke="{c["border"]}"/>'
    for i, col in enumerate(["#FF5F56", "#FFBD2E", "#27C93F"]):
        body += f'<circle cx="{28 + i*20}" cy="26" r="6" fill="{col}"/>'
    body += f'<text x="{w/2}" y="31" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c["muted"]}">{t(ABOUT_USER)}: ~</text>'
    body += f'<line x1="0" y1="48" x2="{w}" y2="48" stroke="{c["border"]}"/>'
    body += f'<text x="32" y="82" font-family="{MONO}" font-size="15" fill="{c["green"]}">$ whoami</text>'
    y = 82 + row
    for k, v in ABOUT:
        body += (f'<text x="32" y="{y}" font-family="{MONO}" font-size="15">'
                 f'<tspan fill="{c["accent"]}" font-weight="700">{t(k)}</tspan>'
                 f'<tspan fill="{c["muted"]}">:</tspan></text>')
        body += f'<text x="190" y="{y}" font-family="{MONO}" font-size="15" fill="{c["text"]}">{t(v)}</text>'
        y += row
    return svg(w, h, body, f"{ABOUT_USER}: " + "; ".join(f"{k}: {v}" for k, v in ABOUT))


# ----------------------------------------------------------------- cards
CARDS = {
    "m3": dict(
        title="M3 Math Modeling",
        lines=["Heatwave-vulnerability and gambling-risk",
               "models: ODEs, regression, PCA, Monte Carlo,",
               "sensitivity analysis. Advanced past Triage."],
        tags=["Python", "LaTeX"],
        alt="M3 Math Modeling Challenge: heatwave and gambling-risk models using ODEs, regression, PCA, Monte Carlo, and sensitivity analysis.",
    ),
    "nullmap": dict(
        title="nullMap",
        lines=["Literature-review pipeline for null results:",
               "BM25 + kNN retrieval, rank fusion, meta-analysis.",
               "2nd place, HackMIT Elastic Track (team)."],
        tags=["Python", "TypeScript", "FastAPI", "Elasticsearch"],
        alt="nullMap: null-results literature review pipeline with hybrid retrieval and meta-analysis. 2nd place, HackMIT Elastic Track, team project.",
    ),
}


def card(c, d):
    w, h = 490, 190
    body = f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" fill="{c["bg"]}" stroke="{c["border"]}"/>'
    body += f'<rect x="0.5" y="14" width="4" height="30" fill="{c["accent"]}"/>'
    body += f'<text x="24" y="40" font-family="{SANS}" font-size="20" font-weight="700" fill="{c["accent"]}">{t(d["title"])}</text>'
    y = 70
    for ln in d["lines"]:
        body += f'<text x="24" y="{y}" font-family="{SANS}" font-size="14" fill="{c["text"]}">{t(ln)}</text>'
        y += 22
    x = 24
    for tag in d["tags"]:
        tw = int(len(tag) * 7.4 + 22)
        body += f'<rect x="{x}" y="148" width="{tw}" height="24" rx="12" fill="{c["chip"]}" stroke="{c["border"]}"/>'
        body += f'<text x="{x + tw/2}" y="164" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{t(tag)}</text>'
        x += tw + 8
    return svg(w, h, body, d["alt"])


def main():
    for name, c in THEMES.items():
        (OUT / f"header-{name}.svg").write_text(header(c), encoding="utf-8")
        (OUT / f"about-{name}.svg").write_text(about(c), encoding="utf-8")
        for key, d in CARDS.items():
            (OUT / f"card-{key}-{name}.svg").write_text(card(c, d), encoding="utf-8")
    print("wrote", len(list(OUT.glob("*.svg"))), "svgs to", OUT)


if __name__ == "__main__":
    main()
