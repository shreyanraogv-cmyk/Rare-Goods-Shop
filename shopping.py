import streamlit as st
import random

st.set_page_config(
    page_title="VAULT — Rare Finds",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

:root {
  --black:  #0a0a0a;
  --off:    #111111;
  --card:   #161616;
  --border: #2a2a2a;
  --gold:   #c9a84c;
  --gold2:  #e8cc80;
  --cream:  #f0e6d3;
  --red:    #c0392b;
  --muted:  #666666;
  --white:  #f5f5f0;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
  font-family: 'DM Mono', monospace;
  background: var(--black);
  color: var(--white);
}
.stApp {
  background:
    radial-gradient(ellipse 80% 40% at 50% -10%, rgba(201,168,76,0.08) 0%, transparent 60%),
    var(--black);
  min-height: 100vh;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2rem 4rem; max-width: 1280px; }

/* NOISE */
.stApp::before {
  content: '';
  position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
  opacity: .5;
}

/* HEADER */
.vault-header {
  text-align: center;
  padding: 3rem 0 2rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 2rem;
}
.vault-logo {
  font-family: 'Bebas Neue', cursive;
  font-size: clamp(64px, 10vw, 120px);
  letter-spacing: 0.25em;
  background: linear-gradient(135deg, var(--gold) 0%, var(--gold2) 50%, var(--gold) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
  display: block;
}
.vault-tagline {
  font-size: 11px;
  letter-spacing: 0.4em;
  color: var(--muted);
  margin-top: 8px;
  text-transform: uppercase;
}
.vault-divider {
  width: 60px; height: 1px;
  background: var(--gold);
  margin: 16px auto 0;
  opacity: 0.5;
}

/* STATS */
.stats-row {
  display: flex; gap: 1px;
  margin-bottom: 2rem;
  background: var(--border);
}
.stat-box {
  flex: 1; background: var(--card);
  padding: 20px; text-align: center;
}
.stat-num {
  font-family: 'Bebas Neue', cursive;
  font-size: 36px; color: var(--gold);
  letter-spacing: 0.1em; display: block;
}
.stat-label {
  font-size: 9px; letter-spacing: 0.25em;
  color: var(--muted); text-transform: uppercase;
  margin-top: 2px; display: block;
}

/* BRAND STRIP */
.brand-strip {
  display: flex; gap: 6px;
  flex-wrap: wrap; margin-bottom: 1.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--border);
}
.brand-chip {
  font-size: 9px; letter-spacing: 0.2em;
  text-transform: uppercase;
  padding: 6px 14px;
  border: 1px solid var(--border);
  background: var(--card);
  color: var(--muted);
  cursor: pointer;
  transition: all .15s;
  white-space: nowrap;
}
.brand-chip.active {
  border-color: var(--gold);
  color: var(--gold);
  background: rgba(201,168,76,0.08);
}
.brand-logo {
  font-size: 14px; margin-right: 4px;
}

/* PRODUCT CARD */
.product-card {
  background: var(--card);
  border: 1px solid var(--border);
  position: relative; overflow: hidden;
  transition: border-color .3s, transform .3s;
  height: 100%;
}
.product-card:hover {
  border-color: var(--gold);
  transform: translateY(-3px);
}
.product-card::after {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  opacity: 0; transition: opacity .3s;
}
.product-card:hover::after { opacity: 1; }

.product-img {
  width: 100%;
  aspect-ratio: 3/4;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 80px;
  background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
  border-bottom: 1px solid var(--border);
  position: relative;
  overflow: hidden;
  flex-direction: column;
  gap: 6px;
}
.brand-watermark {
  font-family: 'Bebas Neue', cursive;
  font-size: 11px;
  letter-spacing: 0.35em;
  color: rgba(201,168,76,0.25);
  text-transform: uppercase;
  margin-top: 4px;
}

.rarity-badge {
  position: absolute; top: 12px; left: 12px;
  font-size: 9px; letter-spacing: 0.2em;
  text-transform: uppercase;
  padding: 4px 10px; border: 1px solid;
}
.rarity-legendary { border-color:#c9a84c;color:#c9a84c;background:rgba(201,168,76,0.1); }
.rarity-ultra     { border-color:#9b59b6;color:#c39bd3;background:rgba(155,89,182,0.1); }
.rarity-rare      { border-color:#2980b9;color:#7fb3d3;background:rgba(41,128,185,0.1); }
.rarity-limited   { border-color:#c0392b;color:#e67e73;background:rgba(192,57,43,0.1); }

.stock-badge {
  position: absolute; top: 12px; right: 12px;
  font-size: 9px; letter-spacing: 0.1em;
  padding: 4px 8px;
  background: rgba(0,0,0,0.8);
  border: 1px solid var(--border);
  color: var(--muted);
}

/* brand logo pill on card */
.brand-pill-card {
  position: absolute; bottom: 10px; right: 10px;
  font-size: 8px; letter-spacing: 0.25em;
  text-transform: uppercase;
  padding: 3px 10px;
  background: rgba(0,0,0,0.85);
  border: 1px solid rgba(201,168,76,0.4);
  color: rgba(201,168,76,0.8);
}

.product-info { padding: 16px; }
.product-brand {
  font-size: 9px; letter-spacing: 0.3em;
  text-transform: uppercase; color: var(--gold);
  margin-bottom: 4px;
}
.product-name {
  font-family: 'Playfair Display', serif;
  font-size: 15px; color: var(--white);
  margin-bottom: 4px; line-height: 1.3;
}
.product-desc {
  font-size: 10px; color: var(--muted);
  line-height: 1.6; margin-bottom: 12px;
  letter-spacing: 0.04em;
}
.product-meta {
  display: flex; justify-content: space-between;
  align-items: flex-end; margin-bottom: 10px;
}
.product-price {
  font-family: 'Bebas Neue', cursive;
  font-size: 26px; letter-spacing: 0.05em;
  color: var(--cream);
}
.product-original {
  font-size: 10px; color: var(--muted);
  text-decoration: line-through;
}
.product-tags {
  display: flex; flex-wrap: wrap; gap: 4px;
  margin-bottom: 12px;
}
.tag {
  font-size: 8px; letter-spacing: 0.15em;
  text-transform: uppercase;
  padding: 3px 8px;
  border: 1px solid var(--border);
  color: var(--muted);
}

/* BUTTONS */
.stButton > button {
  font-family: 'DM Mono', monospace !important;
  font-size: 10px !important;
  letter-spacing: 0.25em !important;
  text-transform: uppercase !important;
  border-radius: 0 !important;
  padding: 12px 20px !important;
  width: 100% !important;
  transition: all .2s !important;
  border: 1px solid var(--gold) !important;
  background: transparent !important;
  color: var(--gold) !important;
}
.stButton > button:hover {
  background: var(--gold) !important;
  color: var(--black) !important;
}

/* INPUTS */
.stTextInput > div > div > input {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 0 !important;
  color: var(--white) !important;
  font-family: 'DM Mono', monospace !important;
  font-size: 12px !important;
  letter-spacing: 0.1em !important;
  padding: 12px 16px !important;
}
.stTextInput > div > div > input:focus {
  border-color: var(--gold) !important;
  box-shadow: 0 0 0 1px var(--gold) !important;
}
.stTextInput label { color:var(--muted)!important;font-size:10px!important;letter-spacing:0.2em!important; }
.stSelectbox > div > div {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 0 !important;
  color: var(--white) !important;
  font-family: 'DM Mono', monospace !important;
}
.stSelectbox label { color:var(--muted)!important;font-size:10px!important;letter-spacing:0.2em!important; }

/* CART */
.cart-header {
  font-family: 'Bebas Neue', cursive;
  font-size: 32px; letter-spacing: 0.2em;
  color: var(--gold); margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}
.cart-item {
  background: var(--card);
  border: 1px solid var(--border);
  padding: 14px; margin-bottom: 8px;
  display: flex; flex-direction: column; gap: 4px;
}
.cart-item-name {
  font-family: 'Playfair Display', serif;
  font-size: 13px; color: var(--white);
}
.cart-item-meta { font-size: 9px; color: var(--muted); letter-spacing: 0.1em; }
.cart-total {
  font-family: 'Bebas Neue', cursive;
  font-size: 28px; color: var(--cream);
  text-align: right; padding-top: 12px;
  border-top: 1px solid var(--border);
  letter-spacing: 0.1em;
}
.cart-empty {
  font-size: 11px; color: var(--muted);
  letter-spacing: 0.15em; text-align: center;
  padding: 32px 0;
}

/* TOAST */
.toast-msg {
  background: var(--card);
  border: 1px solid var(--gold);
  border-left: 3px solid var(--gold);
  padding: 12px 20px; font-size: 11px;
  letter-spacing: 0.15em; color: var(--gold);
  margin-bottom: 12px;
}

/* DETAIL */
.detail-price {
  font-family: 'Bebas Neue', cursive;
  font-size: 52px; color: var(--cream);
  letter-spacing: 0.05em;
}
.detail-brand {
  font-size: 10px; letter-spacing: 0.4em;
  color: var(--gold); text-transform: uppercase;
  margin-bottom: 8px;
}
.detail-name {
  font-family: 'Playfair Display', serif;
  font-size: 32px; color: var(--white);
  margin-bottom: 12px; line-height: 1.2;
}
.detail-desc {
  font-size: 12px; color: var(--muted);
  line-height: 1.9; letter-spacing: 0.05em;
  margin-bottom: 20px;
  border-left: 2px solid var(--gold);
  padding-left: 16px;
}
.spec-row {
  display: flex; justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
  font-size: 11px;
}
.spec-key { color:var(--muted);letter-spacing:0.15em;text-transform:uppercase; }
.spec-val { color:var(--white);letter-spacing:0.05em; }

/* TABS */
.stTabs [data-baseweb="tab-list"] {
  background: transparent;
  border-bottom: 1px solid var(--border);
  gap: 0;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important;
  border: none !important;
  border-bottom: 2px solid transparent !important;
  color: var(--muted) !important;
  font-family: 'DM Mono', monospace !important;
  font-size: 10px !important;
  letter-spacing: 0.25em !important;
  text-transform: uppercase !important;
  padding: 12px 20px !important;
  border-radius: 0 !important;
}
.stTabs [aria-selected="true"] {
  color: var(--gold) !important;
  border-bottom-color: var(--gold) !important;
}

/* SLIDER */
.stSlider > div { color: var(--muted); }
div[data-testid="stExpander"] {
  background: var(--card);
  border: 1px solid var(--border) !important;
  border-radius: 0 !important;
}
.stMarkdown p { font-size:12px;color:var(--muted);line-height:1.8; }
hr { border-color:var(--border);margin:1rem 0; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--black); }
::-webkit-scrollbar-thumb { background: var(--border); }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* GAMEOVER / WIN screens */
.gameover {
  text-align:center;padding:40px;
  background:linear-gradient(135deg,#fef2f2,#fee2e2);
  border:3px solid #ef4444;border-radius:24px;margin:20px 0;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# BRAND METADATA  (logo emoji + accent color)
# ─────────────────────────────────────────────
BRAND_META = {
    "Nike":              {"logo": "✔",  "color": "#f5f5f0"},
    "Jordan Brand":      {"logo": "🏀", "color": "#c0392b"},
    "Adidas":            {"logo": "〓", "color": "#f5f5f0"},
    "Rolex":             {"logo": "♛",  "color": "#c9a84c"},
    "Supreme":           {"logo": "⬛", "color": "#c0392b"},
    "Louis Vuitton":     {"logo": "✦",  "color": "#c9a84c"},
    "Dior":              {"logo": "✿",  "color": "#f5f5f0"},
    "Gucci":             {"logo": "◈",  "color": "#c9a84c"},
    "Prada":             {"logo": "▲",  "color": "#f5f5f0"},
    "Balenciaga":        {"logo": "◉",  "color": "#f5f5f0"},
    "Maison Margiela":   {"logo": "◌",  "color": "#f5f5f0"},
    "Rick Owens":        {"logo": "⬟",  "color": "#888"},
    "Kapital":           {"logo": "⊕",  "color": "#c9a84c"},
    "Undercover":        {"logo": "⊗",  "color": "#9b59b6"},
    "Comme des Garçons": {"logo": "◎",  "color": "#f5f5f0"},
    "Needles":           {"logo": "✂",  "color": "#c0392b"},
    "Visvim":            {"logo": "⌘",  "color": "#c9a84c"},
    "Yohji Yamamoto":    {"logo": "⊘",  "color": "#888"},
    "New Balance":       {"logo": "N",  "color": "#c0392b"},
    "Stone Island":      {"logo": "◈",  "color": "#f97316"},
    "Bottega Veneta":    {"logo": "⊞",  "color": "#7fc97f"},
    "Porter x Fragment": {"logo": "⊟",  "color": "#3b82f6"},
    "Engineered Garments":{"logo":"⊠",  "color": "#c9a84c"},
    "Paraboot":          {"logo": "⊡",  "color": "#c9a84c"},
}

# ─────────────────────────────────────────────
# PRODUCT DATA
# ─────────────────────────────────────────────
PRODUCTS = [

    # ── NIKE ──────────────────────────────────
    {
        "id": 1, "category": "Footwear",
        "brand": "Nike",
        "name": "Air Max 1 'Patta Waves' Monarch",
        "emoji": "👟", "price": 1850, "original": 160,
        "rarity": "Legendary", "stock": 1,
        "desc": "The Patta x Nike Air Max 1 'Waves' in Monarch colourway — arguably the most hyped Air Max 1 collab ever. Comes with all three lace sets, woven patch, and socks. DS with OG receipt.",
        "tags": ["Patta", "DS", "OG Receipt", "Collab"],
        "sizes": ["US 10"], "condition": "Deadstock",
        "provenance": "Patta Amsterdam raffle, 2021", "year": 2021,
    },
    {
        "id": 2, "category": "Footwear",
        "brand": "Nike",
        "name": "Dunk Low SP 'Strawberry Cough'",
        "emoji": "🍓", "price": 1100, "original": 120,
        "rarity": "Ultra Rare", "stock": 1,
        "desc": "Nike SB Dunk Low 'Strawberry Cough' — the weed-themed Nike SB that launched in 2020. Tie-dye canvas upper with hemp outsole. Completely sold out in minutes and never restocked.",
        "tags": ["SB", "DS", "2020", "Hemp"],
        "sizes": ["US 9.5"], "condition": "Deadstock",
        "provenance": "Nike SNKRS raffle, 2020", "year": 2020,
    },
    {
        "id": 3, "category": "Footwear",
        "brand": "Nike",
        "name": "Air Force 1 'Louis Vuitton' by Virgil",
        "emoji": "🤍", "price": 9500, "original": 2750,
        "rarity": "Legendary", "stock": 1,
        "desc": "Virgil Abloh's final collab — the Nike Air Force 1 x Louis Vuitton in white. Sold exclusively at Sotheby's auction. Comes with LV monogram box, dust bag, and authenticity certificate.",
        "tags": ["Virgil", "LV", "Sothebys", "Final Collab"],
        "sizes": ["US 10"], "condition": "Deadstock",
        "provenance": "Sotheby's Auction House, 2022", "year": 2022,
    },

    # ── JORDAN BRAND ──────────────────────────
    {
        "id": 4, "category": "Footwear",
        "brand": "Jordan Brand",
        "name": "Air Jordan 1 High OG 'Chicago' 1985",
        "emoji": "🏀", "price": 28000, "original": 65,
        "rarity": "Legendary", "stock": 1,
        "desc": "THE original. An authentic 1985 Air Jordan 1 High in Chicago colorway, worn and signed by a former NBA player. The sneaker that started it all. Comes with original laces and box fragments.",
        "tags": ["OG 1985", "Signed", "Chicago", "Holy Grail"],
        "sizes": ["US 11"], "condition": "7/10 (Worn once, 1985)",
        "provenance": "Authenticated by GOAT, private estate", "year": 1985,
    },
    {
        "id": 5, "category": "Footwear",
        "brand": "Jordan Brand",
        "name": "Travis Scott x Air Jordan 1 Low 'Reverse Mocha'",
        "emoji": "🤎", "price": 3400, "original": 150,
        "rarity": "Ultra Rare", "stock": 1,
        "desc": "Travis Scott's reverse Swoosh AJ1 Low in Mocha — one of the most coveted Travis collabs. Backwards Swoosh, premium suede, and hidden hangtag. DS with all extras and original receipt.",
        "tags": ["Travis Scott", "Cactus Jack", "DS", "Reverse Swoosh"],
        "sizes": ["US 10.5"], "condition": "Deadstock",
        "provenance": "Cactus Jack SNKRS drop, 2022", "year": 2022,
    },

    # ── ADIDAS ────────────────────────────────
    {
        "id": 6, "category": "Footwear",
        "brand": "Adidas",
        "name": "Yeezy Boost 350 V2 'Beluga 1.0'",
        "emoji": "🟠", "price": 1200, "original": 220,
        "rarity": "Rare", "stock": 2,
        "desc": "The original Beluga 1.0 — the Yeezy that broke the internet. Orange stripe, OG box. The first real mainstream Yeezy moment. Worn twice, near-mint soles, no yellowing.",
        "tags": ["Yeezy", "Kanye", "Beluga", "OG"],
        "sizes": ["US 9", "US 10"], "condition": "9/10",
        "provenance": "Adidas confirmed, 2016", "year": 2016,
    },
    {
        "id": 7, "category": "Footwear",
        "brand": "Adidas",
        "name": "Pharrell x NMD Hu 'Holi Festival'",
        "emoji": "🌈", "price": 780, "original": 220,
        "rarity": "Limited", "stock": 2,
        "desc": "Pharrell Williams x Adidas NMD Hu Trail 'Holi Festival' — vibrant hand-painted look across Primeknit upper. Only released in select markets. One of Pharrell's most visually stunning collabs.",
        "tags": ["Pharrell", "Holi", "Primeknit", "Limited"],
        "sizes": ["US 9", "US 11"], "condition": "9.5/10",
        "provenance": "Adidas flagship Mumbai, 2018", "year": 2018,
    },

    # ── ROLEX ─────────────────────────────────
    {
        "id": 8, "category": "Watches",
        "brand": "Rolex",
        "name": "Submariner Date 'Kermit' Ref. 16610LV",
        "emoji": "🟢", "price": 18500, "original": 6200,
        "rarity": "Legendary", "stock": 1,
        "desc": "The iconic Rolex Submariner 40th Anniversary 'Kermit' — green bezel on black dial. Ref. 16610LV from 2003. Full set with box, papers, hangtag, and original bracelet. Collector's holy grail.",
        "tags": ["Full Set", "Green Bezel", "40th Anniversary", "Holy Grail"],
        "sizes": ["40mm"], "condition": "9/10",
        "provenance": "Authorized Rolex dealer, Geneva 2003", "year": 2003,
    },
    {
        "id": 9, "category": "Watches",
        "brand": "Rolex",
        "name": "Daytona 'Paul Newman' Ref. 6239",
        "emoji": "⌚", "price": 185000, "original": 210,
        "rarity": "Legendary", "stock": 1,
        "desc": "The most legendary watch ever made. An authentic Paul Newman dial Daytona Ref. 6239 from 1968. Exotic dial in near-immaculate condition. Fully authenticated with provenance documentation from a private Swiss collector.",
        "tags": ["Paul Newman", "Exotic Dial", "1968", "Grail"],
        "sizes": ["37mm"], "condition": "8.5/10",
        "provenance": "Private Swiss estate, authenticated 2023", "year": 1968,
    },
    {
        "id": 10, "category": "Watches",
        "brand": "Rolex",
        "name": "GMT-Master II 'Batman' Ref. 116710BLNR",
        "emoji": "🌑", "price": 22000, "original": 9700,
        "rarity": "Ultra Rare", "stock": 1,
        "desc": "The Rolex GMT Batman — blue-and-black ceramic bezel, jubilee bracelet. Discontinued reference now commanding massive premiums. Full set, unworn, with stickers still on case back.",
        "tags": ["Batman", "Full Set", "Jubilee", "Discontinued"],
        "sizes": ["40mm"], "condition": "Unworn",
        "provenance": "Rolex AD London, 2020", "year": 2020,
    },

    # ── SUPREME ───────────────────────────────
    {
        "id": 11, "category": "Tops",
        "brand": "Supreme",
        "name": "Box Logo Hooded Sweatshirt FW18",
        "emoji": "🔴", "price": 1850, "original": 158,
        "rarity": "Legendary", "stock": 1,
        "desc": "Supreme FW18 Box Logo Hoodie in natural — the most coveted Supreme item from one of their most celebrated seasons. Heavyweight cotton, perfect boxy fit. Never worn, with original Supreme bag.",
        "tags": ["BOGO", "FW18", "Natural", "Heavyweight"],
        "sizes": ["L"], "condition": "Deadstock",
        "provenance": "Supreme New York, Lafayette St, 2018", "year": 2018,
    },
    {
        "id": 12, "category": "Accessories",
        "brand": "Supreme",
        "name": "Supreme x Louis Vuitton Duffle Bag",
        "emoji": "🎒", "price": 8500, "original": 3850,
        "rarity": "Legendary", "stock": 1,
        "desc": "The SS17 Supreme x Louis Vuitton red monogram keepall duffle — the collaboration that changed streetwear forever. Full LV set with strap, lock, clochette, and dust bag. Authenticated by ENTRUPY.",
        "tags": ["SS17", "LV Collab", "Red Monogram", "ENTRUPY"],
        "sizes": ["One Size"], "condition": "9/10",
        "provenance": "Louis Vuitton Paris pop-up, 2017", "year": 2017,
    },

    # ── LOUIS VUITTON ─────────────────────────
    {
        "id": 13, "category": "Accessories",
        "brand": "Louis Vuitton",
        "name": "Keepall 55 'Monogram Eclipse' by Virgil",
        "emoji": "🖤", "price": 4800, "original": 3200,
        "rarity": "Ultra Rare", "stock": 1,
        "desc": "Virgil Abloh's LV Eclipse monogram Keepall 55 with his signature printed interior and Off-White zip ties. From his final FW21 collection presented at the Louvre. Full set with LV dustbag.",
        "tags": ["Virgil", "FW21", "Eclipse", "Off-White"],
        "sizes": ["55"], "condition": "9.5/10",
        "provenance": "Louis Vuitton Paris flagship, 2021", "year": 2021,
    },

    # ── DIOR ──────────────────────────────────
    {
        "id": 14, "category": "Footwear",
        "brand": "Dior",
        "name": "Air Dior Jordan 1 High 'Dior Grey'",
        "emoji": "🩶", "price": 14500, "original": 2000,
        "rarity": "Legendary", "stock": 1,
        "desc": "The Air Dior — Jordan Brand x Dior collaboration, one of only 8,500 pairs produced globally. Dior oblique jacquard, tumbled leather, Dior brogue detail. With full Dior presentation box.",
        "tags": ["Kim Jones", "8500 Pairs", "Full Set", "Air Jordan"],
        "sizes": ["EU 43"], "condition": "Deadstock",
        "provenance": "Dior Paris boutique, 2020", "year": 2020,
    },

    # ── GUCCI ─────────────────────────────────
    {
        "id": 15, "category": "Accessories",
        "brand": "Gucci",
        "name": "GG Supreme Canvas Tote by Alessandro Michele",
        "emoji": "🌸", "price": 2200, "original": 1980,
        "rarity": "Rare", "stock": 2,
        "desc": "Alessandro Michele-era Gucci GG Supreme canvas tote with floral embroidery — from his debut SS16 collection that redefined Gucci. Sold out immediately. With original Gucci dust bag and box.",
        "tags": ["Alessandro Michele", "SS16", "Embroidery", "Full Set"],
        "sizes": ["One Size"], "condition": "9/10",
        "provenance": "Gucci Milan boutique, 2016", "year": 2016,
    },

    # ── PRADA ─────────────────────────────────
    {
        "id": 16, "category": "Accessories",
        "brand": "Prada",
        "name": "Re-Nylon Backpack 'Archive Black'",
        "emoji": "🎽", "price": 1650, "original": 1490,
        "rarity": "Limited", "stock": 1,
        "desc": "Prada Re-Nylon regenerated nylon backpack — from their landmark sustainability collection. Triangular enamel logo plaque, adjustable padded straps. Discontinued in this exact configuration.",
        "tags": ["Re-Nylon", "Sustainable", "Archive", "Triangular Logo"],
        "sizes": ["One Size"], "condition": "9.5/10",
        "provenance": "Prada Milano flagship, 2020", "year": 2020,
    },

    # ── BALENCIAGA ────────────────────────────
    {
        "id": 17, "category": "Footwear",
        "brand": "Balenciaga",
        "name": "Triple S 'Clear Sole' OG Colourway",
        "emoji": "⚪", "price": 920, "original": 895,
        "rarity": "Rare", "stock": 2,
        "desc": "The original Balenciaga Triple S that sparked the dad shoe revolution. OG clear sole version from SS17 — the one that started it all. Demna's game-changing silhouette that every brand then copied.",
        "tags": ["OG", "SS17", "Clear Sole", "Demna"],
        "sizes": ["EU 42", "EU 43"], "condition": "9/10",
        "provenance": "Balenciaga Paris boutique, 2017", "year": 2017,
    },
    {
        "id": 18, "category": "Outerwear",
        "brand": "Balenciaga",
        "name": "Cocoon Coat Oversized FW17",
        "emoji": "🧣", "price": 3200, "original": 4100,
        "rarity": "Ultra Rare", "stock": 1,
        "desc": "Demna's FW17 Balenciaga cocoon coat — the oversized silhouette that redefined power dressing. This piece was worn by a fashion editor in the original runway show review. Comes with Balenciaga garment bag.",
        "tags": ["FW17", "Demna", "Cocoon", "Runway"],
        "sizes": ["36 (fits OS)"], "condition": "9/10",
        "provenance": "Balenciaga Paris Fashion Week 2017", "year": 2017,
    },

    # ── MAISON MARGIELA ───────────────────────
    {
        "id": 19, "category": "Outerwear",
        "brand": "Maison Margiela",
        "name": "Replica Puffer Artisanal Destroyed",
        "emoji": "🧥", "price": 2850, "original": 3800,
        "rarity": "Legendary", "stock": 1,
        "desc": "Hand-distressed MM6 archive puffer, 2019 FW collection. One-of-a-kind destruction pattern applied by the Margiela atelier in Paris. Near-mint condition with original tags and authenticity card.",
        "tags": ["Archive", "FW19", "Paris", "Hand-Finished"],
        "sizes": ["S", "M"], "condition": "9.5/10",
        "provenance": "Margiela flagship, Paris 2019", "year": 2019,
    },

    # ── RICK OWENS ────────────────────────────
    {
        "id": 20, "category": "Outerwear",
        "brand": "Rick Owens",
        "name": "DRKSHDW Hooded Cargo Trench SS20",
        "emoji": "🪖", "price": 3100, "original": 4200,
        "rarity": "Rare", "stock": 2,
        "desc": "Rare Rick Owens DRKSHDW heavyweight cotton trench with asymmetric zip front and articulated cargo volumes. SS20 Tecuatl collection. Deadstock condition — one of the most wearable Rick pieces.",
        "tags": ["SS20", "Deadstock", "Tecuatl", "DRKSHDW"],
        "sizes": ["M", "L"], "condition": "Deadstock",
        "provenance": "Rick Owens Paris boutique, 2020", "year": 2020,
    },

    # ── VISVIM ────────────────────────────────
    {
        "id": 21, "category": "Bottoms",
        "brand": "Visvim",
        "name": "Hakama Trousers Indigo Sashiko",
        "emoji": "🎏", "price": 1850, "original": 2400,
        "rarity": "Legendary", "stock": 1,
        "desc": "Visvim Hakama-style trousers in hand-dyed indigo with traditional sashiko quilting. Hiroki Nakamura sourced the cotton from Tokushima prefecture. A wearable textile artwork.",
        "tags": ["Indigo", "Sashiko", "Hiroki", "Tokushima"],
        "sizes": ["2"], "condition": "9.5/10",
        "provenance": "Visvim DMVSA, Tokyo", "year": 2020,
    },

    # ── UNDERCOVER ────────────────────────────
    {
        "id": 22, "category": "Tops",
        "brand": "Undercover",
        "name": "FW02 'But Beautiful' Archive Knit",
        "emoji": "🧶", "price": 4200, "original": None,
        "rarity": "Legendary", "stock": 1,
        "desc": "Grail status Undercover FW02 'But Beautiful' knit. Jun Takahashi's most celebrated collection. Heavily distressed wool with embroidered text motifs. Museum-worthy piece from the best season in Undercover history.",
        "tags": ["FW02", "Grail", "Archive", "Jun Takahashi"],
        "sizes": ["M"], "condition": "7/10 (intentional distress)",
        "provenance": "Japanese archive collector, Tokyo", "year": 2002,
    },

    # ── KAPITAL ───────────────────────────────
    {
        "id": 23, "category": "Outerwear",
        "brand": "Kapital",
        "name": "Century Denim Boro Noragi",
        "emoji": "🥼", "price": 1640, "original": None,
        "rarity": "Ultra Rare", "stock": 1,
        "desc": "Kapital Hirata Atelier century denim noragi with hand-applied boro patchwork. Each piece is unique — this one features indigo, white, and rust sashiko stitching across the back panel.",
        "tags": ["Boro", "Japan", "Handmade", "Indigo"],
        "sizes": ["One Size"], "condition": "8/10",
        "provenance": "Kapital Kyoto HQ, 2021", "year": 2021,
    },

    # ── NEW BALANCE ───────────────────────────
    {
        "id": 24, "category": "Footwear",
        "brand": "New Balance",
        "name": "990v2 Made in USA 'Dirty White' OG",
        "emoji": "🤍", "price": 890, "original": 200,
        "rarity": "Limited", "stock": 1,
        "desc": "Original 1990s New Balance 990v2 Made in USA in the rare 'dirty white' colorway. Unworn with OG box and duster bag. True DS condition — a time capsule sneaker that predates the hype.",
        "tags": ["DS", "OG Box", "Made USA", "1990s"],
        "sizes": ["US 10"], "condition": "Deadstock",
        "provenance": "Private collector, Massachusetts", "year": 1997,
    },

    # ── STONE ISLAND ──────────────────────────
    {
        "id": 25, "category": "Outerwear",
        "brand": "Stone Island",
        "name": "Shadow Project Cargo Jogger SS19",
        "emoji": "🟠", "price": 890, "original": 1300,
        "rarity": "Rare", "stock": 2,
        "desc": "Stone Island Shadow Project cargo jogger from SS19 collection. Membrana TC fabric with garment-dyed finish. SISP's functional lab approach at its absolute finest. Sold out globally on release day.",
        "tags": ["SS19", "SISP", "Membrana", "Garment-Dyed"],
        "sizes": ["S", "M"], "condition": "9/10",
        "provenance": "Stone Island Milan flagship, 2019", "year": 2019,
    },
]

RARITY_ORDER = {"Legendary": 0, "Ultra Rare": 1, "Rare": 2, "Limited": 3}
CATEGORIES   = ["All"] + sorted(set(p["category"] for p in PRODUCTS))
ALL_BRANDS   = ["All Brands"] + sorted(set(p["brand"] for p in PRODUCTS))
SORT_OPTIONS = ["Rarity", "Price: Low to High", "Price: High to Low", "Year: Newest", "Year: Oldest"]

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "cart"           not in st.session_state: st.session_state.cart           = []
if "wishlist"       not in st.session_state: st.session_state.wishlist       = []
if "toast"          not in st.session_state: st.session_state.toast          = None
if "detail_id"      not in st.session_state: st.session_state.detail_id      = None
if "active_brand"   not in st.session_state: st.session_state.active_brand   = "All Brands"

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def add_to_cart(product):
    st.session_state.cart.append(product)
    st.session_state.toast = f"✦  {product['brand']} {product['name']} added to cart"

def toggle_wishlist(pid):
    if pid in st.session_state.wishlist:
        st.session_state.wishlist.remove(pid)
        st.session_state.toast = "✦  Removed from wishlist"
    else:
        st.session_state.wishlist.append(pid)
        st.session_state.toast = "✦  Saved to wishlist"

def cart_total():
    return sum(p["price"] for p in st.session_state.cart)

def filter_products(cat, brand, sort, search, max_price):
    prods = PRODUCTS[:]
    if cat != "All":
        prods = [p for p in prods if p["category"] == cat]
    if brand != "All Brands":
        prods = [p for p in prods if p["brand"] == brand]
    if search:
        q = search.lower()
        prods = [p for p in prods if
                 q in p["name"].lower() or
                 q in p["brand"].lower() or
                 any(q in t.lower() for t in p["tags"])]
    prods = [p for p in prods if p["price"] <= max_price]
    if sort == "Rarity":
        prods.sort(key=lambda x: RARITY_ORDER.get(x["rarity"], 9))
    elif sort == "Price: Low to High":
        prods.sort(key=lambda x: x["price"])
    elif sort == "Price: High to Low":
        prods.sort(key=lambda x: x["price"], reverse=True)
    elif sort == "Year: Newest":
        prods.sort(key=lambda x: x["year"], reverse=True)
    elif sort == "Year: Oldest":
        prods.sort(key=lambda x: x["year"])
    return prods

def rarity_class(r):
    return {
        "Legendary": "rarity-legendary",
        "Ultra Rare": "rarity-ultra",
        "Rare":       "rarity-rare",
        "Limited":    "rarity-limited",
    }.get(r, "rarity-rare")

def brand_logo(brand):
    return BRAND_META.get(brand, {}).get("logo", "◆")

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="vault-header">
  <span class="vault-logo">VAULT</span>
  <div class="vault-tagline">Authenticated Rare Garments, Footwear & Timepieces</div>
  <div class="vault-divider"></div>
</div>
""", unsafe_allow_html=True)

total_value     = sum(p["price"] for p in PRODUCTS)
legendary_count = sum(1 for p in PRODUCTS if p["rarity"] == "Legendary")
brand_count     = len(set(p["brand"] for p in PRODUCTS))

st.markdown(f"""
<div class="stats-row">
  <div class="stat-box">
    <span class="stat-num">{len(PRODUCTS)}</span>
    <span class="stat-label">Pieces Available</span>
  </div>
  <div class="stat-box">
    <span class="stat-num">{brand_count}</span>
    <span class="stat-label">Iconic Brands</span>
  </div>
  <div class="stat-box">
    <span class="stat-num">{legendary_count}</span>
    <span class="stat-label">Legendary Items</span>
  </div>
  <div class="stat-box">
    <span class="stat-num">${total_value:,}</span>
    <span class="stat-label">Total Vault Value</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TOAST
# ─────────────────────────────────────────────
if st.session_state.toast:
    st.markdown(f'<div class="toast-msg">{st.session_state.toast}</div>', unsafe_allow_html=True)
    st.session_state.toast = None

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["SHOP THE VAULT", "CART", "WISHLIST"])

# ═══════════════════════════════════════════════
# TAB 1 — SHOP
# ═══════════════════════════════════════════════
with tab1:

    # ── BRAND QUICK-FILTER STRIP ──
    # Build brand chips: show brand logo + name, highlight active
    major_brands = [
        "Nike", "Jordan Brand", "Adidas", "Rolex",
        "Supreme", "Louis Vuitton", "Dior", "Gucci",
        "Prada", "Balenciaga", "Maison Margiela", "Rick Owens",
        "Kapital", "Undercover", "Visvim", "New Balance",
        "Stone Island",
    ]
    # Only show brands that exist in products
    existing_brands = [b for b in major_brands if any(p["brand"] == b for p in PRODUCTS)]

    st.markdown("**SHOP BY BRAND**")
    brand_cols = st.columns(len(existing_brands) + 1)
    with brand_cols[0]:
        active = st.session_state.active_brand == "All Brands"
        if st.button("ALL BRANDS", key="brand_all"):
            st.session_state.active_brand = "All Brands"
            st.rerun()

    for i, b in enumerate(existing_brands):
        with brand_cols[i + 1]:
            meta = BRAND_META.get(b, {})
            logo = meta.get("logo", "◆")
            label = f"{logo} {b.split()[0].upper()}"  # first word only to save space
            is_active = st.session_state.active_brand == b
            btn_label = f"[{label}]" if is_active else label
            if st.button(btn_label, key=f"brand_{b}"):
                st.session_state.active_brand = b
                st.rerun()

    st.markdown("---")

    # ── FILTERS ──
    f1, f2, f3, f4 = st.columns([2, 2, 2, 2])
    with f1:
        search = st.text_input("SEARCH", placeholder="brand, name, tag...", label_visibility="visible")
    with f2:
        cat = st.selectbox("CATEGORY", CATEGORIES)
    with f3:
        sort = st.selectbox("SORT BY", SORT_OPTIONS)
    with f4:
        max_price = st.slider("MAX PRICE ($)", 100, 200000, 200000, step=500)

    filtered = filter_products(cat, st.session_state.active_brand, sort, search, max_price)

    active_brand_label = st.session_state.active_brand
    st.markdown(f"""
    <div style="font-size:10px;letter-spacing:0.25em;color:var(--muted);
                text-transform:uppercase;margin-bottom:1.5rem">
      — {len(filtered)} pieces found
      {f'· filtered by <span style="color:var(--gold)">{active_brand_label}</span>' if active_brand_label != "All Brands" else ""} —
    </div>
    """, unsafe_allow_html=True)

    # ── PRODUCT DETAIL VIEW ──
    if st.session_state.detail_id:
        prod = next((p for p in PRODUCTS if p["id"] == st.session_state.detail_id), None)
        if prod:
            st.markdown("---")
            d1, d2 = st.columns([1, 1], gap="large")
            bm = BRAND_META.get(prod["brand"], {})
            with d1:
                st.markdown(f"""
                <div class="product-img" style="aspect-ratio:1/1;font-size:100px;
                     border:1px solid var(--border);margin-bottom:16px;min-height:320px">
                  <span class="rarity-badge {rarity_class(prod['rarity'])}">{prod['rarity']}</span>
                  {prod['emoji']}
                  <div class="brand-watermark">{prod['brand'].upper()}</div>
                </div>
                """, unsafe_allow_html=True)
                tags_html = "".join(f'<span class="tag">{t}</span>' for t in prod["tags"])
                st.markdown(f'<div class="product-tags">{tags_html}</div>', unsafe_allow_html=True)

            with d2:
                in_wish = prod["id"] in st.session_state.wishlist
                orig_line = (f'<div style="font-size:10px;color:var(--muted);'
                             f'text-decoration:line-through;letter-spacing:0.1em">'
                             f'Original retail: ${prod["original"]:,}</div>'
                             if prod["original"] else "")
                st.markdown(f"""
                <div class="detail-brand">{bm.get('logo','')} {prod['brand']}</div>
                <div class="detail-name">{prod['name']}</div>
                <div class="detail-price">${prod['price']:,}</div>
                {orig_line}
                <br>
                <div class="detail-desc">{prod['desc']}</div>
                """, unsafe_allow_html=True)

                specs = [
                    ("Condition",  prod["condition"]),
                    ("Provenance", prod["provenance"]),
                    ("Year",       str(prod["year"])),
                    ("Stock",      f"{prod['stock']} remaining"),
                    ("Sizes",      " / ".join(prod["sizes"])),
                ]
                for key, val in specs:
                    st.markdown(f"""
                    <div class="spec-row">
                      <span class="spec-key">{key}</span>
                      <span class="spec-val">{val}</span>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                ba1, ba2, ba3 = st.columns([2, 1, 1])
                with ba1:
                    if st.button("ADD TO CART", key=f"detail_cart_{prod['id']}"):
                        add_to_cart(prod)
                        st.rerun()
                with ba2:
                    wish_label = "♥ SAVED" if in_wish else "♡ SAVE"
                    if st.button(wish_label, key=f"detail_wish_{prod['id']}"):
                        toggle_wishlist(prod["id"])
                        st.rerun()
                with ba3:
                    if st.button("← BACK", key="back_btn"):
                        st.session_state.detail_id = None
                        st.rerun()
            st.markdown("---")

    # ── PRODUCT GRID ──
    cols = st.columns(3, gap="medium")
    for i, prod in enumerate(filtered):
        with cols[i % 3]:
            in_wish = prod["id"] in st.session_state.wishlist
            in_cart = any(c["id"] == prod["id"] for c in st.session_state.cart)
            bm      = BRAND_META.get(prod["brand"], {})
            orig_tag = (f'<div class="product-original">Was ${prod["original"]:,}</div>'
                        if prod["original"] else "")
            tags_html = "".join(f'<span class="tag">{t}</span>' for t in prod["tags"][:3])

            st.markdown(f"""
            <div class="product-card">
              <div class="product-img">
                <span class="rarity-badge {rarity_class(prod['rarity'])}">{prod['rarity']}</span>
                <span class="stock-badge">{'LAST 1' if prod['stock'] == 1 else f'{prod["stock"]} LEFT'}</span>
                <span class="brand-pill-card">{bm.get('logo','')} {prod['brand'].upper()}</span>
                {prod['emoji']}
                <div class="brand-watermark">{prod['brand'].upper()}</div>
              </div>
              <div class="product-info">
                <div class="product-brand">{bm.get('logo','')} {prod['brand']}</div>
                <div class="product-name">{prod['name']}</div>
                <div class="product-desc">{prod['desc'][:100]}...</div>
                <div class="product-tags">{tags_html}</div>
                <div class="product-meta">
                  <div>
                    <div class="product-price">${prod['price']:,}</div>
                    {orig_tag}
                  </div>
                  <div style="font-size:10px;color:var(--muted)">{prod['condition']}</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            b1, b2, b3 = st.columns([2, 1, 1])
            with b1:
                btn_label = "✓ IN CART" if in_cart else "ADD TO CART"
                if st.button(btn_label, key=f"cart_{prod['id']}_{i}"):
                    add_to_cart(prod)
                    st.rerun()
            with b2:
                w_label = "♥" if in_wish else "♡"
                if st.button(w_label, key=f"wish_{prod['id']}_{i}"):
                    toggle_wishlist(prod["id"])
                    st.rerun()
            with b3:
                if st.button("↗", key=f"detail_{prod['id']}_{i}"):
                    st.session_state.detail_id = prod["id"]
                    st.rerun()

            st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# TAB 2 — CART
# ═══════════════════════════════════════════════
with tab2:
    st.markdown('<div class="cart-header">YOUR CART</div>', unsafe_allow_html=True)

    if not st.session_state.cart:
        st.markdown('<div class="cart-empty">— YOUR CART IS EMPTY —</div>', unsafe_allow_html=True)
    else:
        for i, item in enumerate(st.session_state.cart):
            bm = BRAND_META.get(item["brand"], {})
            c1, c2, c3 = st.columns([1, 4, 1])
            with c1:
                st.markdown(f'<div style="font-size:36px;text-align:center">{item["emoji"]}</div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                <div class="cart-item">
                  <div style="font-size:9px;letter-spacing:0.25em;color:var(--gold);margin-bottom:2px">
                    {bm.get('logo','')} {item['brand'].upper()}
                  </div>
                  <div class="cart-item-name">{item['name']}</div>
                  <div class="cart-item-meta">{item['rarity']} · {item['condition']}</div>
                  <div style="font-family:'Bebas Neue',cursive;font-size:22px;color:var(--cream);
                              letter-spacing:0.05em">${item['price']:,}</div>
                </div>
                """, unsafe_allow_html=True)
            with c3:
                if st.button("REMOVE", key=f"remove_{i}"):
                    st.session_state.cart.pop(i)
                    st.session_state.toast = "✦  Item removed from cart"
                    st.rerun()

        st.markdown("---")
        st.markdown(f'<div class="cart-total">TOTAL — ${cart_total():,}</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        ch1, ch2 = st.columns(2)
        with ch1:
            if st.button("CLEAR CART", key="clear_cart"):
                st.session_state.cart = []
                st.session_state.toast = "✦  Cart cleared"
                st.rerun()
        with ch2:
            if st.button("CHECKOUT →", key="checkout"):
                total = cart_total()
                st.session_state.toast = f"✦  Order confirmed — ${total:,} — All pieces will be shipped insured & authenticated"
                st.session_state.cart = []
                st.rerun()

# ═══════════════════════════════════════════════
# TAB 3 — WISHLIST
# ═══════════════════════════════════════════════
with tab3:
    st.markdown('<div class="cart-header">WISHLIST</div>', unsafe_allow_html=True)
    wished = [p for p in PRODUCTS if p["id"] in st.session_state.wishlist]

    if not wished:
        st.markdown('<div class="cart-empty">— NOTHING SAVED YET —</div>', unsafe_allow_html=True)
    else:
        wc = st.columns(3, gap="medium")
        for i, prod in enumerate(wished):
            with wc[i % 3]:
                bm = BRAND_META.get(prod["brand"], {})
                tags_html = "".join(f'<span class="tag">{t}</span>' for t in prod["tags"][:2])
                st.markdown(f"""
                <div class="product-card">
                  <div class="product-img" style="aspect-ratio:1/1">
                    <span class="rarity-badge {rarity_class(prod['rarity'])}">{prod['rarity']}</span>
                    {prod['emoji']}
                    <div class="brand-watermark">{prod['brand'].upper()}</div>
                  </div>
                  <div class="product-info">
                    <div class="product-brand">{bm.get('logo','')} {prod['brand']}</div>
                    <div class="product-name">{prod['name']}</div>
                    <div class="product-tags">{tags_html}</div>
                    <div class="product-price">${prod['price']:,}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
                wb1, wb2 = st.columns(2)
                with wb1:
                    if st.button("ADD TO CART", key=f"w_cart_{prod['id']}"):
                        add_to_cart(prod)
                        st.rerun()
                with wb2:
                    if st.button("REMOVE", key=f"w_rem_{prod['id']}"):
                        toggle_wishlist(prod["id"])
                        st.rerun()
                st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div style="border-top:1px solid var(--border);margin-top:4rem;padding-top:2rem;
            text-align:center;font-size:9px;letter-spacing:0.3em;
            color:var(--muted);text-transform:uppercase">
  VAULT — Est. 2024 — All pieces 100% authenticated · Insured worldwide shipping · No replicas, ever
  <br><br>
  <span style="color:rgba(201,168,76,0.3)">
    Nike · Jordan · Adidas · Rolex · Supreme · Louis Vuitton · Dior · Gucci · Prada · Balenciaga · Margiela · Rick Owens
  </span>
</div>
""", unsafe_allow_html=True)