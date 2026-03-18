"""
Single thumbnail generator — TopupCuk only. Full premium design.
Loads real images from the web via Playwright.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path("c:/BACKTOCAMPUS/portfolio-web/public/thumbnails")

HTML = '''<!DOCTYPE html>
<html><head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#080818;
    font-family:'Inter',system-ui,sans-serif;
    color:#fff; overflow:hidden;
}

/* === NAV === */
.nav {
    display:flex; align-items:center; justify-content:space-between;
    padding:10px 28px;
    background:rgba(12,12,28,.95);
    border-bottom:1px solid rgba(255,255,255,.06);
    backdrop-filter:blur(12px);
}
.nav .logo {
    font-size:18px; font-weight:900; letter-spacing:-.5px;
}
.nav .logo .t { color:#818cf8; }
.nav .logo .c { color:#c084fc; }
.nav-center { display:flex; gap:20px; }
.nav-center a {
    font-size:11px; color:rgba(255,255,255,.5); text-decoration:none;
    font-weight:500; letter-spacing:.3px;
}
.nav-center a.active { color:#fff; }
.nav-right { display:flex; align-items:center; gap:12px; }
.nav-right .search {
    padding:5px 14px; background:rgba(255,255,255,.06);
    border:1px solid rgba(255,255,255,.08); border-radius:8px;
    font-size:10px; color:rgba(255,255,255,.4); width:160px;
}
.nav-right .avatar {
    width:28px; height:28px; border-radius:50%;
    background:linear-gradient(135deg,#818cf8,#c084fc);
}

/* === HERO === */
.hero {
    position:relative; padding:24px 28px 20px;
    background:linear-gradient(135deg,#0c0c28 0%,#1a1040 40%,#0f1a3a 70%,#0c0c28 100%);
    overflow:hidden;
}
.hero::before {
    content:''; position:absolute; top:-40px; right:-20px;
    width:300px; height:300px;
    background:radial-gradient(circle,rgba(129,140,248,.12) 0%,transparent 70%);
}
.hero::after {
    content:''; position:absolute; bottom:-60px; left:100px;
    width:200px; height:200px;
    background:radial-gradient(circle,rgba(192,132,252,.08) 0%,transparent 70%);
}
.hero-content { position:relative; z-index:1; }
.hero-badge {
    display:inline-block; padding:3px 10px;
    background:rgba(129,140,248,.15); border:1px solid rgba(129,140,248,.25);
    border-radius:20px; font-size:9px; color:#a5b4fc;
    font-weight:600; letter-spacing:.5px; margin-bottom:8px;
}
.hero h1 {
    font-size:24px; font-weight:800; line-height:1.15;
    letter-spacing:-.5px; margin-bottom:6px;
}
.hero h1 .grad {
    background:linear-gradient(135deg,#818cf8,#c084fc,#f0abfc);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.hero p { font-size:11px; color:rgba(255,255,255,.45); max-width:400px; }

/* stats strip */
.stats {
    display:flex; gap:24px; margin-top:12px;
}
.stat .val { font-size:16px; font-weight:800; color:#fff; }
.stat .val span { color:#818cf8; }
.stat .label { font-size:8px; color:rgba(255,255,255,.35); text-transform:uppercase; letter-spacing:.5px; margin-top:1px; }

/* === GAMES GRID === */
.section {
    padding:14px 28px 0;
}
.section-header {
    display:flex; justify-content:space-between; align-items:center;
    margin-bottom:10px;
}
.section-header h2 {
    font-size:13px; font-weight:700; letter-spacing:-.3px;
}
.section-header .tabs {
    display:flex; gap:6px;
}
.section-header .tab {
    padding:3px 10px; border-radius:6px; font-size:9px; font-weight:600;
    background:rgba(255,255,255,.04); color:rgba(255,255,255,.4);
    border:1px solid rgba(255,255,255,.06);
}
.section-header .tab.active {
    background:rgba(129,140,248,.15); color:#a5b4fc;
    border-color:rgba(129,140,248,.3);
}
.games {
    display:grid; grid-template-columns:repeat(5,1fr); gap:10px;
}
.game {
    background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.06);
    border-radius:12px; padding:10px;
    text-align:center;
    position:relative;
    transition:all .15s;
}
.game:hover { background:rgba(255,255,255,.06); border-color:rgba(129,140,248,.3); }
.game .badge {
    position:absolute; top:6px; right:6px;
    font-size:7px; font-weight:700; padding:2px 5px;
    border-radius:4px; color:#fff;
}
.badge-hot { background:#ef4444; }
.badge-new { background:#818cf8; }
.badge-sale { background:#f59e0b; }
.game-icon {
    width:48px; height:48px; border-radius:12px;
    margin:0 auto 6px;
    display:flex; align-items:center; justify-content:center;
    font-weight:800; color:#fff; font-size:13px;
    box-shadow:0 4px 12px rgba(0,0,0,.3);
    position:relative; overflow:hidden;
}
.game-icon::after {
    content:''; position:absolute; top:0; left:0; right:0; bottom:0;
    background:linear-gradient(135deg,rgba(255,255,255,.15) 0%,transparent 50%);
    border-radius:12px;
}
.game .name { font-size:10px; font-weight:600; color:rgba(255,255,255,.85); }
.game .price { font-size:9px; color:#818cf8; margin-top:2px; font-weight:500; }

/* === BOTTOM PROMO === */
.promos {
    display:flex; gap:10px; padding:12px 28px;
}
.promo-card {
    flex:1; padding:12px 16px;
    border-radius:12px; position:relative; overflow:hidden;
}
.promo-card::before {
    content:''; position:absolute; inset:0;
    background:linear-gradient(135deg,rgba(255,255,255,.08) 0%,transparent 100%);
}
.promo-card .label { font-size:8px; text-transform:uppercase; letter-spacing:.8px; opacity:.7; position:relative; }
.promo-card .title { font-size:13px; font-weight:700; position:relative; margin-top:2px; }
.promo-card .cta {
    display:inline-block; margin-top:6px; padding:3px 10px;
    background:rgba(255,255,255,.15); border-radius:6px;
    font-size:8px; font-weight:600; position:relative;
}
</style>
</head>
<body>

<div class="nav">
    <div class="logo"><span class="t">Topup</span><span class="c">Cuk</span></div>
    <div class="nav-center">
        <a class="active">Games</a>
        <a>Pulsa & Data</a>
        <a>E-Wallet</a>
        <a>Voucher</a>
    </div>
    <div class="nav-right">
        <div class="search">Search games, vouchers...</div>
        <div class="avatar"></div>
    </div>
</div>

<div class="hero">
    <div class="hero-content">
        <div class="hero-badge">INSTANT DELIVERY</div>
        <h1>Top up game favorit<br><span class="grad">dalam hitungan detik.</span></h1>
        <p>Pembayaran otomatis via QRIS, transfer bank, dan e-wallet. Diamonds, UC, dan voucher langsung masuk.</p>
        <div class="stats">
            <div class="stat"><div class="val">12<span>K+</span></div><div class="label">Transaksi</div></div>
            <div class="stat"><div class="val">99.8<span>%</span></div><div class="label">Success Rate</div></div>
            <div class="stat"><div class="val">&lt;30<span>s</span></div><div class="label">Delivery Time</div></div>
        </div>
    </div>
</div>

<div class="section">
    <div class="section-header">
        <h2>Popular Games</h2>
        <div class="tabs">
            <div class="tab active">All</div>
            <div class="tab">Mobile</div>
            <div class="tab">PC</div>
            <div class="tab">Console</div>
        </div>
    </div>
    <div class="games">
        <div class="game">
            <div class="badge badge-hot">HOT</div>
            <div class="game-icon" style="background:linear-gradient(135deg,#1a3fb8,#0a2074);">
                <span style="font-size:11px;letter-spacing:-.5px;">MLBB</span>
            </div>
            <div class="name">Mobile Legends</div>
            <div class="price">Rp 5.000</div>
        </div>
        <div class="game">
            <div class="game-icon" style="background:linear-gradient(135deg,#ff6d00,#e64a00);">
                <span>FF</span>
            </div>
            <div class="name">Free Fire</div>
            <div class="price">Rp 3.000</div>
        </div>
        <div class="game">
            <div class="badge badge-new">NEW</div>
            <div class="game-icon" style="background:linear-gradient(135deg,#00acc1,#00838f);">
                <span style="font-size:16px;font-weight:900;">G</span>
            </div>
            <div class="name">Genshin Impact</div>
            <div class="price">Rp 16.000</div>
        </div>
        <div class="game">
            <div class="game-icon" style="background:linear-gradient(135deg,#fd4556,#bd2130);">
                <span style="font-size:10px;letter-spacing:1px;">VAL</span>
            </div>
            <div class="name">Valorant</div>
            <div class="price">Rp 12.000</div>
        </div>
        <div class="game">
            <div class="badge badge-sale">-20%</div>
            <div class="game-icon" style="background:linear-gradient(135deg,#f9a825,#f57f17);">
                <span style="font-size:9px;letter-spacing:.5px;">PUBG</span>
            </div>
            <div class="name">PUBG Mobile</div>
            <div class="price">Rp 8.000</div>
        </div>
    </div>
</div>

<div class="promos">
    <div class="promo-card" style="background:linear-gradient(135deg,#312e81,#4c1d95);">
        <div class="label">Weekend Deal</div>
        <div class="title">ML Diamonds 10% OFF</div>
        <div class="cta">Claim Now</div>
    </div>
    <div class="promo-card" style="background:linear-gradient(135deg,#7f1d1d,#991b1b);">
        <div class="label">Flash Sale</div>
        <div class="title">FF Diamonds Rp 1.000</div>
        <div class="cta">Limited Stock</div>
    </div>
    <div class="promo-card" style="background:linear-gradient(135deg,#064e3b,#065f46);">
        <div class="label">New User</div>
        <div class="title">First Top-Up Free Ongkir</div>
        <div class="cta">Sign Up</div>
    </div>
</div>

</body></html>'''


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 800, "height": 450})

        # Wait for fonts to load
        page.set_content(HTML, wait_until="networkidle")
        page.wait_for_timeout(1500)  # extra time for Google Fonts

        out = OUT / "topupcuk.png"
        page.screenshot(path=str(out), type="png")
        print(f"Generated: {out}")

        browser.close()


if __name__ == "__main__":
    main()
