# 🔒 VAULT — Authenticated Rare Finds

A luxury resale storefront built with **Streamlit** — showcasing rare sneakers, watches, clothing, and accessories from iconic brands like Nike, Rolex, Supreme, and Louis Vuitton. Features a full shopping experience with cart, wishlist, product detail views, and advanced filtering.

---

## ✨ Features

- 🛍️ **25 curated products** across Footwear, Watches, Tops, Bottoms, Outerwear, and Accessories
- 🏷️ **4 rarity tiers** — Legendary, Ultra Rare, Rare, and Limited
- 🔍 **Search & filter** by brand, category, price range, and sort order
- 🏢 **Brand quick-filter strip** — one-click filtering by 17 iconic brands
- 🛒 **Shopping cart** with running total and checkout flow
- ♡ **Wishlist** — save pieces and move them to cart later
- 🔎 **Product detail view** — full specs including condition, provenance, year, and sizes
- 📊 **Vault stats** — live total pieces, brands, legendary count, and total vault value
- 🎨 **Luxury dark UI** — Bebas Neue + Playfair Display + DM Mono, gold accents, noise texture
- 📱 **Responsive 3-column grid** with hover effects and rarity badges

---

## 🏷️ Brands Featured

Nike · Jordan Brand · Adidas · Rolex · Supreme · Louis Vuitton · Dior · Gucci · Prada · Balenciaga · Maison Margiela · Rick Owens · Kapital · Undercover · Visvim · New Balance · Stone Island

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | App UI, tabs, state management |
| Python `random` | Random selection utilities |
| HTML/CSS (inline) | Custom luxury dark theme |
| Streamlit `session_state` | Cart, wishlist, and UI state |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/vault-store.git
cd vault-store
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run vault.py
```

The app opens at `http://localhost:8501`

> **No API key required!** Fully self-contained — all product data is built into the app.

---

## 📁 Project Structure

```
vault-store/
│
├── vault.py             # Main application file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📦 requirements.txt

```
streamlit
```

---

## 🖥️ App Structure

The app has three main tabs:

**SHOP THE VAULT**
- Brand quick-filter strip at the top
- Search, category, sort, and price filters
- 3-column product grid with rarity badges and stock indicators
- Click `↗` on any product to open its full detail page with specs and provenance

**CART**
- View all added items with brand, name, rarity, condition, and price
- Remove individual items or clear the entire cart
- Checkout button confirms the order

**WISHLIST**
- Save products with `♡` from the shop grid
- Move saved items to cart or remove them

---

## 🚀 Deploy Online for Free

1. Push to a **GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and select `vault.py` as the main file
4. Click **Deploy** — get a shareable link like `yourapp.streamlit.app`

No secrets or environment variables needed.

---

## ⚠️ Known Limitations

- Cart and wishlist data lives in `session_state` — it resets on page refresh
- The checkout button is UI-only and does not process real payments
- Product data is hardcoded — adding new products requires editing `vault.py`
- For a real store, you would connect a database and a payment provider like Stripe

---

## 🙋 About the Developer

Built by **Shreyan** — Grade 10 student at Chirec International School, passionate about Physics, Economics, and building cool things with Python.

- 📧 Email: Shreyan.rao.gv@gmail.com
- 🐙 GitHub: [@shreyanraogv-cmyk](https://github.com/shreyanraogv-cmyk)

---
