"""
Generate all portfolio thumbnail PNGs (800x450) via Playwright.
Each thumbnail is a unique, premium UI design rendered from HTML/CSS.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path("c:/BACKTOCAMPUS/portfolio-web/public/thumbnails")
OUT.mkdir(parents=True, exist_ok=True)

FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">'
)
FONT_LINK_MONO = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">'
)


# ============================================================
# 0. TOPUPCUK (approved reference design)
# ============================================================
def html_topupcuk():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#080818;
    font-family:'Inter',system-ui,sans-serif;
    color:#fff; overflow:hidden;
}
.nav {
    display:flex; align-items:center; justify-content:space-between;
    padding:10px 28px;
    background:rgba(12,12,28,.95);
    border-bottom:1px solid rgba(255,255,255,.06);
    backdrop-filter:blur(12px);
}
.nav .logo { font-size:18px; font-weight:900; letter-spacing:-.5px; }
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
.hero h1 { font-size:24px; font-weight:800; line-height:1.15; letter-spacing:-.5px; margin-bottom:6px; }
.hero h1 .grad {
    background:linear-gradient(135deg,#818cf8,#c084fc,#f0abfc);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.hero p { font-size:11px; color:rgba(255,255,255,.45); max-width:400px; }
.stats { display:flex; gap:24px; margin-top:12px; }
.stat .val { font-size:16px; font-weight:800; color:#fff; }
.stat .val span { color:#818cf8; }
.stat .label { font-size:8px; color:rgba(255,255,255,.35); text-transform:uppercase; letter-spacing:.5px; margin-top:1px; }
.section { padding:14px 28px 0; }
.section-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; }
.section-header h2 { font-size:13px; font-weight:700; letter-spacing:-.3px; }
.section-header .tabs { display:flex; gap:6px; }
.section-header .tab {
    padding:3px 10px; border-radius:6px; font-size:9px; font-weight:600;
    background:rgba(255,255,255,.04); color:rgba(255,255,255,.4);
    border:1px solid rgba(255,255,255,.06);
}
.section-header .tab.active {
    background:rgba(129,140,248,.15); color:#a5b4fc;
    border-color:rgba(129,140,248,.3);
}
.games { display:grid; grid-template-columns:repeat(5,1fr); gap:10px; }
.game {
    background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.06);
    border-radius:12px; padding:10px; text-align:center; position:relative;
}
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
.promos { display:flex; gap:10px; padding:12px 28px; }
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
</style></head><body>
<div class="nav">
    <div class="logo"><span class="t">Topup</span><span class="c">Cuk</span></div>
    <div class="nav-center">
        <a class="active">Games</a><a>Pulsa & Data</a><a>E-Wallet</a><a>Voucher</a>
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
            <div class="tab active">All</div><div class="tab">Mobile</div><div class="tab">PC</div><div class="tab">Console</div>
        </div>
    </div>
    <div class="games">
        <div class="game">
            <div class="badge badge-hot">HOT</div>
            <div class="game-icon" style="background:linear-gradient(135deg,#1a3fb8,#0a2074);"><span style="font-size:11px;letter-spacing:-.5px;">MLBB</span></div>
            <div class="name">Mobile Legends</div><div class="price">Rp 5.000</div>
        </div>
        <div class="game">
            <div class="game-icon" style="background:linear-gradient(135deg,#ff6d00,#e64a00);"><span>FF</span></div>
            <div class="name">Free Fire</div><div class="price">Rp 3.000</div>
        </div>
        <div class="game">
            <div class="badge badge-new">NEW</div>
            <div class="game-icon" style="background:linear-gradient(135deg,#00acc1,#00838f);"><span style="font-size:16px;font-weight:900;">G</span></div>
            <div class="name">Genshin Impact</div><div class="price">Rp 16.000</div>
        </div>
        <div class="game">
            <div class="game-icon" style="background:linear-gradient(135deg,#fd4556,#bd2130);"><span style="font-size:10px;letter-spacing:1px;">VAL</span></div>
            <div class="name">Valorant</div><div class="price">Rp 12.000</div>
        </div>
        <div class="game">
            <div class="badge badge-sale">-20%</div>
            <div class="game-icon" style="background:linear-gradient(135deg,#f9a825,#f57f17);"><span style="font-size:9px;letter-spacing:.5px;">PUBG</span></div>
            <div class="name">PUBG Mobile</div><div class="price">Rp 8.000</div>
        </div>
    </div>
</div>
<div class="promos">
    <div class="promo-card" style="background:linear-gradient(135deg,#312e81,#4c1d95);">
        <div class="label">Weekend Deal</div><div class="title">ML Diamonds 10% OFF</div><div class="cta">Claim Now</div>
    </div>
    <div class="promo-card" style="background:linear-gradient(135deg,#7f1d1d,#991b1b);">
        <div class="label">Flash Sale</div><div class="title">FF Diamonds Rp 1.000</div><div class="cta">Limited Stock</div>
    </div>
    <div class="promo-card" style="background:linear-gradient(135deg,#064e3b,#065f46);">
        <div class="label">New User</div><div class="title">First Top-Up Free Ongkir</div><div class="cta">Sign Up</div>
    </div>
</div>
</body></html>'''


# ============================================================
# 1. EPIC-RPG — Dark fantasy RPG combat UI
# ============================================================
def html_epic_rpg():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#0a0510;
    font-family:'Inter',system-ui,sans-serif;
    color:#e0d6c8; overflow:hidden;
    position:relative;
}
body::before {
    content:''; position:absolute; inset:0;
    background:
        radial-gradient(ellipse at 50% 30%, rgba(80,20,80,.25) 0%, transparent 60%),
        radial-gradient(ellipse at 20% 80%, rgba(120,30,30,.15) 0%, transparent 50%);
}

/* TOP BAR */
.top-bar {
    display:flex; justify-content:space-between; align-items:center;
    padding:6px 16px;
    background:rgba(0,0,0,.6);
    border-bottom:1px solid rgba(160,100,200,.15);
    position:relative; z-index:2;
}
.zone-name { font-size:10px; font-weight:700; color:#c9a0dc; letter-spacing:1px; text-transform:uppercase; }
.floor-info { font-size:9px; color:rgba(200,180,160,.5); }
.top-stats { display:flex; gap:14px; }
.top-stat { font-size:9px; color:rgba(200,180,160,.6); }
.top-stat b { color:#e8d5a3; }

/* MAIN LAYOUT */
.main { display:flex; height:calc(100% - 30px); position:relative; z-index:2; }

/* LEFT PANEL: Party */
.party-panel {
    width:145px; padding:8px;
    background:rgba(0,0,0,.4);
    border-right:1px solid rgba(160,100,200,.1);
}
.party-title { font-size:8px; text-transform:uppercase; letter-spacing:1px; color:rgba(200,180,160,.4); margin-bottom:6px; }
.party-member {
    padding:6px; margin-bottom:4px;
    background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.05);
    border-radius:6px;
}
.party-member.active { border-color:rgba(160,100,200,.3); background:rgba(160,100,200,.08); }
.pm-row { display:flex; align-items:center; gap:6px; margin-bottom:3px; }
.pm-avatar {
    width:22px; height:22px; border-radius:4px;
    display:flex; align-items:center; justify-content:center;
    font-size:9px; font-weight:800; color:#fff;
}
.pm-info .pm-name { font-size:9px; font-weight:600; }
.pm-info .pm-class { font-size:7px; color:rgba(200,180,160,.4); }
.bar-row { display:flex; gap:3px; }
.hp-bar, .mp-bar {
    height:4px; border-radius:2px; flex:1;
    position:relative; overflow:hidden;
}
.hp-bar { background:rgba(200,50,50,.2); }
.mp-bar { background:rgba(50,80,200,.2); }
.hp-bar .fill { position:absolute; top:0; left:0; height:100%; border-radius:2px; background:linear-gradient(90deg,#c0392b,#e74c3c); }
.mp-bar .fill { position:absolute; top:0; left:0; height:100%; border-radius:2px; background:linear-gradient(90deg,#2980b9,#3498db); }
.bar-label { font-size:6px; color:rgba(200,180,160,.4); margin-top:1px; display:flex; justify-content:space-between; }

/* CENTER: Battle area */
.battle-area {
    flex:1; position:relative; overflow:hidden;
    display:flex; flex-direction:column;
}
.battle-scene {
    flex:1; position:relative;
    background:
        radial-gradient(ellipse at 50% 60%, rgba(90,30,90,.2) 0%, transparent 50%),
        linear-gradient(180deg, rgba(20,10,30,.3) 0%, rgba(10,5,16,0) 100%);
    display:flex; align-items:center; justify-content:center;
}
/* Monster */
.monster {
    text-align:center; position:relative;
}
.monster-body {
    width:120px; height:140px; margin:0 auto;
    background:
        radial-gradient(ellipse at 50% 40%, rgba(140,40,40,.6) 0%, rgba(60,10,60,.4) 50%, transparent 80%);
    border-radius:50% 50% 40% 40%;
    position:relative;
    box-shadow:0 0 40px rgba(140,40,40,.3), 0 0 80px rgba(80,20,80,.15);
}
.monster-body::before {
    content:''; position:absolute; top:30px; left:50%; transform:translateX(-50%);
    width:50px; height:20px;
    background:radial-gradient(ellipse, rgba(255,60,60,.8) 0%, transparent 70%);
    border-radius:50%;
    box-shadow:0 0 15px rgba(255,60,60,.5);
}
.monster-body::after {
    content:''; position:absolute; top:55px; left:50%; transform:translateX(-50%);
    width:30px; height:15px;
    background:radial-gradient(ellipse, rgba(200,160,40,.4) 0%, transparent 70%);
    border-radius:50%;
}
.monster-name-bar {
    margin-top:6px;
    background:rgba(0,0,0,.5); border:1px solid rgba(140,40,40,.3);
    border-radius:6px; padding:4px 12px; display:inline-block;
}
.monster-name-bar .mn { font-size:10px; font-weight:700; color:#e8a0a0; }
.monster-name-bar .ml { font-size:8px; color:rgba(200,180,160,.4); margin-left:6px; }
.boss-hp {
    width:200px; height:6px; background:rgba(200,50,50,.15);
    border-radius:3px; margin:4px auto 0; overflow:hidden;
}
.boss-hp .fill { height:100%; width:68%; background:linear-gradient(90deg,#8b0000,#dc143c,#ff4500); border-radius:3px; }

/* Damage numbers */
.dmg {
    position:absolute; font-weight:900; text-shadow:0 2px 8px rgba(0,0,0,.8);
    animation:none;
}
.dmg-1 { top:60px; right:180px; font-size:22px; color:#ff4444; transform:rotate(-12deg); }
.dmg-2 { top:40px; left:200px; font-size:16px; color:#ffaa00; transform:rotate(8deg); }
.dmg-3 { top:90px; right:160px; font-size:13px; color:#44ff44; }
.dmg-miss { top:75px; left:170px; font-size:11px; color:rgba(200,180,160,.4); font-style:italic; }

/* COMBAT LOG */
.combat-log {
    height:60px; padding:4px 12px;
    background:rgba(0,0,0,.5);
    border-top:1px solid rgba(160,100,200,.1);
    overflow:hidden;
}
.log-line { font-size:8px; line-height:1.5; color:rgba(200,180,160,.5); }
.log-line .actor { color:#c9a0dc; font-weight:600; }
.log-line .ability { color:#e8d5a3; font-weight:600; }
.log-line .dmg-val { color:#ff6b6b; font-weight:700; }
.log-line .heal-val { color:#6bff6b; font-weight:700; }

/* ACTION BAR */
.action-bar {
    display:flex; gap:6px; padding:6px 12px;
    background:rgba(0,0,0,.6);
    border-top:1px solid rgba(160,100,200,.15);
}
.action-btn {
    flex:1; padding:8px 4px; text-align:center;
    background:rgba(160,100,200,.1);
    border:1px solid rgba(160,100,200,.2);
    border-radius:8px;
    font-size:9px; font-weight:700; text-transform:uppercase; letter-spacing:.5px;
    color:#c9a0dc;
}
.action-btn.primary {
    background:linear-gradient(135deg,rgba(180,60,60,.3),rgba(140,40,40,.4));
    border-color:rgba(200,60,60,.4);
    color:#ffa0a0;
}
.action-btn .hotkey { font-size:7px; color:rgba(200,180,160,.3); display:block; margin-top:1px; }

/* RIGHT: minimap & inventory */
.right-panel {
    width:130px; padding:8px;
    background:rgba(0,0,0,.4);
    border-left:1px solid rgba(160,100,200,.1);
    display:flex; flex-direction:column; gap:6px;
}
.minimap {
    height:100px;
    background:rgba(20,10,30,.6);
    border:1px solid rgba(160,100,200,.12);
    border-radius:6px;
    position:relative; overflow:hidden;
}
.minimap-title { position:absolute; top:3px; left:5px; font-size:7px; text-transform:uppercase; letter-spacing:.5px; color:rgba(200,180,160,.35); }
.minimap-grid {
    position:absolute; inset:14px 4px 4px 4px;
    display:grid; grid-template-columns:repeat(6,1fr); grid-template-rows:repeat(5,1fr); gap:1px;
}
.mg-cell { background:rgba(100,60,120,.1); border-radius:1px; }
.mg-cell.wall { background:rgba(60,30,80,.4); }
.mg-cell.player { background:rgba(100,200,255,.6); box-shadow:0 0 4px rgba(100,200,255,.4); }
.mg-cell.enemy { background:rgba(255,80,80,.5); }
.mg-cell.chest { background:rgba(230,190,60,.5); }

.inv-title { font-size:8px; text-transform:uppercase; letter-spacing:1px; color:rgba(200,180,160,.4); }
.inv-grid {
    display:grid; grid-template-columns:repeat(4,1fr); gap:3px;
}
.inv-slot {
    aspect-ratio:1; background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.06);
    border-radius:4px; position:relative;
    display:flex; align-items:center; justify-content:center;
}
.inv-slot.filled::after {
    content:''; width:60%; height:60%; border-radius:3px;
}
.inv-slot.s-weapon::after { background:linear-gradient(135deg,#c0392b,#8b0000); }
.inv-slot.s-potion::after { background:linear-gradient(135deg,#27ae60,#1e8449); border-radius:50%; }
.inv-slot.s-shield::after { background:linear-gradient(135deg,#2980b9,#1a5276); }
.inv-slot.s-scroll::after { background:linear-gradient(135deg,#e8d5a3,#c19a3e); }
.inv-slot.s-ring::after { background:linear-gradient(135deg,#c084fc,#7c3aed); border-radius:50%; width:50%; height:50%; }
.inv-slot.s-gem::after { background:linear-gradient(135deg,#00bcd4,#006064); transform:rotate(45deg); width:45%; height:45%; }
.inv-slot .qty { position:absolute; bottom:1px; right:2px; font-size:6px; color:rgba(200,180,160,.5); }

.buff-row { display:flex; gap:3px; }
.buff {
    width:20px; height:20px; border-radius:4px;
    display:flex; align-items:center; justify-content:center;
    font-size:8px; font-weight:700;
    border:1px solid;
}
.buff.str { background:rgba(200,60,60,.15); border-color:rgba(200,60,60,.3); color:#ff8080; }
.buff.def { background:rgba(60,120,200,.15); border-color:rgba(60,120,200,.3); color:#80b0ff; }
.buff.spd { background:rgba(60,200,120,.15); border-color:rgba(60,200,120,.3); color:#80ffa0; }
</style></head><body>

<div class="top-bar">
    <div><span class="zone-name">Abyssal Sanctum</span> <span class="floor-info">Floor 7 / Chamber 3</span></div>
    <div class="top-stats">
        <div class="top-stat"><b>Wave</b> 3/5</div>
        <div class="top-stat"><b>Gold</b> 12,847</div>
        <div class="top-stat"><b>EXP</b> +2,340</div>
    </div>
</div>

<div class="main">
    <!-- Party Panel -->
    <div class="party-panel">
        <div class="party-title">Party</div>
        <div class="party-member active">
            <div class="pm-row">
                <div class="pm-avatar" style="background:linear-gradient(135deg,#c0392b,#7b241c);">K</div>
                <div class="pm-info"><div class="pm-name">Kael</div><div class="pm-class">Lv.42 Dark Knight</div></div>
            </div>
            <div class="bar-row"><div class="hp-bar"><div class="fill" style="width:78%;"></div></div><div class="mp-bar"><div class="fill" style="width:45%;"></div></div></div>
            <div class="bar-label"><span>HP 1,247/1,600</span><span>MP 180/400</span></div>
        </div>
        <div class="party-member">
            <div class="pm-row">
                <div class="pm-avatar" style="background:linear-gradient(135deg,#2980b9,#1a5276);">L</div>
                <div class="pm-info"><div class="pm-name">Lyra</div><div class="pm-class">Lv.40 Archmage</div></div>
            </div>
            <div class="bar-row"><div class="hp-bar"><div class="fill" style="width:92%;"></div></div><div class="mp-bar"><div class="fill" style="width:30%;"></div></div></div>
            <div class="bar-label"><span>HP 830/900</span><span>MP 210/700</span></div>
        </div>
        <div class="party-member">
            <div class="pm-row">
                <div class="pm-avatar" style="background:linear-gradient(135deg,#27ae60,#1e8449);">V</div>
                <div class="pm-info"><div class="pm-name">Vex</div><div class="pm-class">Lv.41 Ranger</div></div>
            </div>
            <div class="bar-row"><div class="hp-bar"><div class="fill" style="width:55%;"></div></div><div class="mp-bar"><div class="fill" style="width:60%;"></div></div></div>
            <div class="bar-label"><span>HP 610/1,100</span><span>MP 300/500</span></div>
        </div>
        <div class="party-member">
            <div class="pm-row">
                <div class="pm-avatar" style="background:linear-gradient(135deg,#f39c12,#d68910);">S</div>
                <div class="pm-info"><div class="pm-name">Sera</div><div class="pm-class">Lv.39 Priestess</div></div>
            </div>
            <div class="bar-row"><div class="hp-bar"><div class="fill" style="width:100%;"></div></div><div class="mp-bar"><div class="fill" style="width:15%;"></div></div></div>
            <div class="bar-label"><span>HP 750/750</span><span>MP 90/600</span></div>
        </div>
        <div style="margin-top:6px;">
            <div class="party-title">Buffs</div>
            <div class="buff-row">
                <div class="buff str">S</div>
                <div class="buff def">D</div>
                <div class="buff spd">H</div>
            </div>
        </div>
    </div>

    <!-- Battle Area -->
    <div class="battle-area">
        <div class="battle-scene">
            <div class="dmg dmg-1">-347</div>
            <div class="dmg dmg-2">-128</div>
            <div class="dmg dmg-3">+205</div>
            <div class="dmg dmg-miss">MISS</div>
            <div class="monster">
                <div class="monster-body"></div>
                <div class="monster-name-bar">
                    <span class="mn">Shadow Wyrm</span><span class="ml">Lv.45 BOSS</span>
                </div>
                <div class="boss-hp"><div class="fill"></div></div>
            </div>
        </div>
        <div class="combat-log">
            <div class="log-line"><span class="actor">Kael</span> uses <span class="ability">Abyssal Cleave</span> dealing <span class="dmg-val">347</span> damage!</div>
            <div class="log-line"><span class="actor">Shadow Wyrm</span> casts <span class="ability">Dark Breath</span> -- <span class="actor">Vex</span> takes <span class="dmg-val">128</span> damage</div>
            <div class="log-line"><span class="actor">Sera</span> casts <span class="ability">Divine Light</span> -- <span class="actor">Kael</span> heals <span class="heal-val">205</span> HP</div>
            <div class="log-line"><span class="actor">Lyra</span> casts <span class="ability">Frost Nova</span> -- Shadow Wyrm is <span style="color:#80d0ff;">FROZEN</span> for 2 turns</div>
        </div>
        <div class="action-bar">
            <div class="action-btn primary">Attack<span class="hotkey">[1]</span></div>
            <div class="action-btn">Skills<span class="hotkey">[2]</span></div>
            <div class="action-btn">Items<span class="hotkey">[3]</span></div>
            <div class="action-btn">Defend<span class="hotkey">[4]</span></div>
            <div class="action-btn">Flee<span class="hotkey">[5]</span></div>
        </div>
    </div>

    <!-- Right Panel -->
    <div class="right-panel">
        <div class="minimap">
            <div class="minimap-title">Minimap</div>
            <div class="minimap-grid">
                <div class="mg-cell wall"></div><div class="mg-cell wall"></div><div class="mg-cell"></div><div class="mg-cell"></div><div class="mg-cell wall"></div><div class="mg-cell wall"></div>
                <div class="mg-cell wall"></div><div class="mg-cell"></div><div class="mg-cell"></div><div class="mg-cell enemy"></div><div class="mg-cell"></div><div class="mg-cell wall"></div>
                <div class="mg-cell"></div><div class="mg-cell"></div><div class="mg-cell player"></div><div class="mg-cell"></div><div class="mg-cell"></div><div class="mg-cell"></div>
                <div class="mg-cell wall"></div><div class="mg-cell"></div><div class="mg-cell"></div><div class="mg-cell"></div><div class="mg-cell chest"></div><div class="mg-cell wall"></div>
                <div class="mg-cell wall"></div><div class="mg-cell wall"></div><div class="mg-cell"></div><div class="mg-cell wall"></div><div class="mg-cell wall"></div><div class="mg-cell wall"></div>
            </div>
        </div>
        <div class="inv-title">Inventory</div>
        <div class="inv-grid">
            <div class="inv-slot filled s-weapon"></div>
            <div class="inv-slot filled s-shield"></div>
            <div class="inv-slot filled s-potion"><span class="qty">x5</span></div>
            <div class="inv-slot filled s-scroll"><span class="qty">x2</span></div>
            <div class="inv-slot filled s-ring"></div>
            <div class="inv-slot filled s-gem"><span class="qty">x3</span></div>
            <div class="inv-slot filled s-potion"><span class="qty">x8</span></div>
            <div class="inv-slot"></div>
            <div class="inv-slot"></div>
            <div class="inv-slot"></div>
            <div class="inv-slot"></div>
            <div class="inv-slot"></div>
        </div>
    </div>
</div>
</body></html>'''


# ============================================================
# 2. PROMOVIDEOHUB — Video editing dashboard
# ============================================================
def html_promovideohub():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#111118;
    font-family:'Inter',system-ui,sans-serif;
    color:#fff; overflow:hidden;
    display:flex; flex-direction:column;
}

/* TOP BAR */
.topbar {
    display:flex; align-items:center; justify-content:space-between;
    padding:6px 16px;
    background:#0c0c14;
    border-bottom:1px solid rgba(224,64,251,.1);
}
.topbar .logo { font-size:14px; font-weight:800; }
.topbar .logo .p { color:#e040fb; }
.topbar .logo .h { color:#ea80fc; }
.topbar-center { display:flex; gap:16px; }
.topbar-center a { font-size:9px; color:rgba(255,255,255,.4); text-decoration:none; font-weight:500; }
.topbar-center a.active { color:#e040fb; }
.topbar-right { display:flex; gap:8px; align-items:center; }
.tb-btn {
    padding:4px 10px; border-radius:6px; font-size:8px; font-weight:600;
    background:rgba(224,64,251,.15); border:1px solid rgba(224,64,251,.25);
    color:#ea80fc;
}
.tb-btn.primary { background:linear-gradient(135deg,#e040fb,#ab47bc); color:#fff; border:none; }

/* MAIN LAYOUT */
.workspace { display:flex; flex:1; overflow:hidden; }

/* LEFT: Media Library */
.media-lib {
    width:155px; background:#0a0a12;
    border-right:1px solid rgba(255,255,255,.06);
    display:flex; flex-direction:column;
}
.ml-header {
    padding:8px 10px 6px;
    font-size:9px; font-weight:700; color:rgba(255,255,255,.5);
    text-transform:uppercase; letter-spacing:.5px;
    border-bottom:1px solid rgba(255,255,255,.04);
}
.ml-search {
    margin:6px 8px; padding:4px 8px;
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.06);
    border-radius:4px; font-size:8px; color:rgba(255,255,255,.3);
}
.ml-clips { flex:1; padding:4px 8px; overflow:hidden; }
.ml-clip {
    display:flex; gap:6px; padding:5px 6px; margin-bottom:3px;
    background:rgba(255,255,255,.02);
    border:1px solid rgba(255,255,255,.04);
    border-radius:6px; align-items:center;
}
.ml-clip.active { border-color:rgba(224,64,251,.3); background:rgba(224,64,251,.06); }
.ml-thumb {
    width:40px; height:24px; border-radius:3px; flex-shrink:0;
}
.ml-clip-info .clip-name { font-size:8px; font-weight:600; color:rgba(255,255,255,.7); }
.ml-clip-info .clip-dur { font-size:7px; color:rgba(255,255,255,.3); }

/* CENTER: Preview */
.preview-area {
    flex:1; display:flex; flex-direction:column;
    background:#0d0d16;
}
.preview-viewport {
    flex:1; position:relative;
    background:linear-gradient(135deg,#0f0818 0%,#1a0e28 50%,#0d0d16 100%);
    display:flex; align-items:center; justify-content:center;
    margin:8px;
    border-radius:8px;
    border:1px solid rgba(255,255,255,.04);
    overflow:hidden;
}
.preview-viewport::before {
    content:''; position:absolute; inset:0;
    background:
        linear-gradient(45deg, transparent 48%, rgba(224,64,251,.04) 50%, transparent 52%),
        linear-gradient(-45deg, transparent 48%, rgba(224,64,251,.04) 50%, transparent 52%);
}
.play-btn {
    width:48px; height:48px; border-radius:50%;
    background:rgba(224,64,251,.2);
    border:2px solid rgba(224,64,251,.5);
    display:flex; align-items:center; justify-content:center;
    position:relative; z-index:2;
}
.play-btn::after {
    content:''; width:0; height:0;
    border-left:16px solid #e040fb;
    border-top:10px solid transparent;
    border-bottom:10px solid transparent;
    margin-left:3px;
}
.preview-time {
    position:absolute; bottom:8px; left:12px;
    font-size:10px; font-weight:600; color:rgba(255,255,255,.6);
    font-variant-numeric:tabular-nums;
}
.preview-res {
    position:absolute; bottom:8px; right:12px;
    font-size:8px; color:rgba(255,255,255,.3);
    background:rgba(0,0,0,.4); padding:2px 6px; border-radius:3px;
}
.preview-title-overlay {
    position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
    text-align:center; z-index:1;
}
.preview-title-overlay h2 {
    font-size:20px; font-weight:800;
    background:linear-gradient(135deg,#e040fb,#ea80fc);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    margin-bottom:4px;
}
.preview-title-overlay p { font-size:9px; color:rgba(255,255,255,.3); }

/* RIGHT: Effects Panel */
.effects-panel {
    width:165px; background:#0a0a12;
    border-left:1px solid rgba(255,255,255,.06);
    display:flex; flex-direction:column;
}
.ep-tabs {
    display:flex; border-bottom:1px solid rgba(255,255,255,.06);
}
.ep-tab {
    flex:1; padding:6px 4px; text-align:center;
    font-size:8px; font-weight:600; color:rgba(255,255,255,.3);
    border-bottom:2px solid transparent;
}
.ep-tab.active { color:#e040fb; border-bottom-color:#e040fb; }
.ep-content { padding:8px 10px; flex:1; overflow:hidden; }
.ep-group { margin-bottom:8px; }
.ep-group-title { font-size:8px; font-weight:600; color:rgba(255,255,255,.4); margin-bottom:4px; text-transform:uppercase; letter-spacing:.3px; }
.slider-row {
    display:flex; align-items:center; gap:6px; margin-bottom:5px;
}
.slider-label { font-size:8px; color:rgba(255,255,255,.5); width:55px; }
.slider-track {
    flex:1; height:3px; background:rgba(255,255,255,.08);
    border-radius:2px; position:relative;
}
.slider-fill {
    position:absolute; top:0; left:0; height:100%;
    background:linear-gradient(90deg,#e040fb,#ea80fc);
    border-radius:2px;
}
.slider-fill::after {
    content:''; position:absolute; right:-4px; top:-3px;
    width:8px; height:8px; border-radius:50%;
    background:#e040fb; border:2px solid #1a1a2e;
}
.slider-val { font-size:7px; color:rgba(255,255,255,.3); width:24px; text-align:right; }
.color-row { display:flex; gap:4px; margin-bottom:5px; }
.color-swatch {
    width:18px; height:18px; border-radius:4px; border:1px solid rgba(255,255,255,.1);
}
.color-swatch.active { border-color:#e040fb; box-shadow:0 0 6px rgba(224,64,251,.3); }

/* TIMELINE */
.timeline {
    height:105px; background:#08080f;
    border-top:1px solid rgba(255,255,255,.06);
    display:flex; flex-direction:column;
}
.tl-toolbar {
    display:flex; align-items:center; justify-content:space-between;
    padding:4px 12px;
    border-bottom:1px solid rgba(255,255,255,.04);
}
.tl-tools { display:flex; gap:8px; }
.tl-tool {
    font-size:8px; color:rgba(255,255,255,.3); font-weight:500;
}
.tl-tool.active { color:#e040fb; }
.tl-time { font-size:8px; color:rgba(255,255,255,.3); font-variant-numeric:tabular-nums; }
.tl-tracks { flex:1; display:flex; flex-direction:column; padding:4px 0; position:relative; }
.tl-track {
    display:flex; align-items:center; height:18px; margin-bottom:2px;
}
.tl-track-label {
    width:60px; padding-left:8px; font-size:7px; font-weight:600;
    color:rgba(255,255,255,.3); text-transform:uppercase;
}
.tl-track-clips {
    flex:1; height:100%; position:relative; margin-right:8px;
}
.tl-clip {
    position:absolute; height:100%; border-radius:3px;
    display:flex; align-items:center; padding:0 4px;
    font-size:6px; font-weight:600; color:rgba(255,255,255,.7);
    overflow:hidden;
}
.tl-clip::after {
    content:''; position:absolute; inset:0;
    background:linear-gradient(90deg,rgba(255,255,255,.06),transparent 30%,transparent 70%,rgba(255,255,255,.06));
}
.playhead {
    position:absolute; top:0; bottom:0; left:40%; width:1px;
    background:#e040fb;
    z-index:5;
}
.playhead::before {
    content:''; position:absolute; top:-3px; left:-4px;
    width:9px; height:6px; background:#e040fb;
    clip-path:polygon(0 0, 100% 0, 50% 100%);
}
</style></head><body>

<div class="topbar">
    <div class="logo"><span class="p">Promo</span><span class="h">VideoHub</span></div>
    <div class="topbar-center">
        <a class="active">Editor</a><a>Templates</a><a>Stock</a><a>Audio</a><a>My Projects</a>
    </div>
    <div class="topbar-right">
        <div class="tb-btn">Preview</div>
        <div class="tb-btn primary">Export</div>
    </div>
</div>

<div class="workspace">
    <div class="media-lib">
        <div class="ml-header">Media Library</div>
        <div class="ml-search">Search clips...</div>
        <div class="ml-clips">
            <div class="ml-clip active">
                <div class="ml-thumb" style="background:linear-gradient(135deg,#e040fb,#7b1fa2);"></div>
                <div class="ml-clip-info"><div class="clip-name">Intro_v2.mp4</div><div class="clip-dur">00:04.2</div></div>
            </div>
            <div class="ml-clip">
                <div class="ml-thumb" style="background:linear-gradient(135deg,#1e88e5,#0d47a1);"></div>
                <div class="ml-clip-info"><div class="clip-name">Product_Hero.mp4</div><div class="clip-dur">00:12.8</div></div>
            </div>
            <div class="ml-clip">
                <div class="ml-thumb" style="background:linear-gradient(135deg,#43a047,#1b5e20);"></div>
                <div class="ml-clip-info"><div class="clip-name">Testimonial_01.mp4</div><div class="clip-dur">00:08.1</div></div>
            </div>
            <div class="ml-clip">
                <div class="ml-thumb" style="background:linear-gradient(135deg,#ef6c00,#bf360c);"></div>
                <div class="ml-clip-info"><div class="clip-name">CTA_Slide.mp4</div><div class="clip-dur">00:03.5</div></div>
            </div>
            <div class="ml-clip">
                <div class="ml-thumb" style="background:linear-gradient(135deg,#5c6bc0,#283593);"></div>
                <div class="ml-clip-info"><div class="clip-name">Outro_Logo.mp4</div><div class="clip-dur">00:05.0</div></div>
            </div>
            <div class="ml-clip">
                <div class="ml-thumb" style="background:linear-gradient(135deg,#ab47bc,#6a1b9a);"></div>
                <div class="ml-clip-info"><div class="clip-name">BG_Music.mp3</div><div class="clip-dur">01:30.0</div></div>
            </div>
            <div class="ml-clip">
                <div class="ml-thumb" style="background:linear-gradient(135deg,#ec407a,#880e4f);"></div>
                <div class="ml-clip-info"><div class="clip-name">SFX_Whoosh.wav</div><div class="clip-dur">00:01.2</div></div>
            </div>
        </div>
    </div>

    <div class="preview-area">
        <div class="preview-viewport">
            <div class="preview-title-overlay">
                <h2>Your Brand Story</h2>
                <p>Professional Promo Video Template</p>
            </div>
            <div class="play-btn"></div>
            <div class="preview-time">00:04.20 / 00:34.60</div>
            <div class="preview-res">1920x1080 | 60fps</div>
        </div>
    </div>

    <div class="effects-panel">
        <div class="ep-tabs">
            <div class="ep-tab active">Effects</div>
            <div class="ep-tab">Text</div>
            <div class="ep-tab">Audio</div>
        </div>
        <div class="ep-content">
            <div class="ep-group">
                <div class="ep-group-title">Color Grading</div>
                <div class="slider-row"><span class="slider-label">Brightness</span><div class="slider-track"><div class="slider-fill" style="width:60%;"></div></div><span class="slider-val">+12</span></div>
                <div class="slider-row"><span class="slider-label">Contrast</span><div class="slider-track"><div class="slider-fill" style="width:72%;"></div></div><span class="slider-val">+18</span></div>
                <div class="slider-row"><span class="slider-label">Saturation</span><div class="slider-track"><div class="slider-fill" style="width:55%;"></div></div><span class="slider-val">+8</span></div>
                <div class="slider-row"><span class="slider-label">Temperature</span><div class="slider-track"><div class="slider-fill" style="width:45%;"></div></div><span class="slider-val">-3</span></div>
            </div>
            <div class="ep-group">
                <div class="ep-group-title">LUT Presets</div>
                <div class="color-row">
                    <div class="color-swatch active" style="background:linear-gradient(135deg,#e040fb,#7b1fa2);"></div>
                    <div class="color-swatch" style="background:linear-gradient(135deg,#ff9800,#e65100);"></div>
                    <div class="color-swatch" style="background:linear-gradient(135deg,#26a69a,#004d40);"></div>
                    <div class="color-swatch" style="background:linear-gradient(135deg,#42a5f5,#0d47a1);"></div>
                    <div class="color-swatch" style="background:linear-gradient(135deg,#ec407a,#880e4f);"></div>
                </div>
            </div>
            <div class="ep-group">
                <div class="ep-group-title">Motion</div>
                <div class="slider-row"><span class="slider-label">Zoom</span><div class="slider-track"><div class="slider-fill" style="width:30%;"></div></div><span class="slider-val">1.2x</span></div>
                <div class="slider-row"><span class="slider-label">Rotation</span><div class="slider-track"><div class="slider-fill" style="width:50%;"></div></div><span class="slider-val">0</span></div>
                <div class="slider-row"><span class="slider-label">Speed</span><div class="slider-track"><div class="slider-fill" style="width:65%;"></div></div><span class="slider-val">1.0x</span></div>
            </div>
            <div class="ep-group">
                <div class="ep-group-title">Transitions</div>
                <div class="slider-row"><span class="slider-label">Fade In</span><div class="slider-track"><div class="slider-fill" style="width:40%;"></div></div><span class="slider-val">0.5s</span></div>
                <div class="slider-row"><span class="slider-label">Fade Out</span><div class="slider-track"><div class="slider-fill" style="width:40%;"></div></div><span class="slider-val">0.5s</span></div>
            </div>
        </div>
    </div>
</div>

<div class="timeline">
    <div class="tl-toolbar">
        <div class="tl-tools">
            <span class="tl-tool active">Select</span>
            <span class="tl-tool">Cut</span>
            <span class="tl-tool">Trim</span>
            <span class="tl-tool">Split</span>
        </div>
        <div class="tl-time">00:04.20</div>
    </div>
    <div class="tl-tracks">
        <div class="playhead"></div>
        <div class="tl-track">
            <div class="tl-track-label">Video 1</div>
            <div class="tl-track-clips">
                <div class="tl-clip" style="left:0; width:15%; background:linear-gradient(90deg,#7b1fa2,#e040fb);">Intro</div>
                <div class="tl-clip" style="left:16%; width:35%; background:linear-gradient(90deg,#0d47a1,#1e88e5);">Product Hero</div>
                <div class="tl-clip" style="left:52%; width:25%; background:linear-gradient(90deg,#1b5e20,#43a047);">Testimonial</div>
                <div class="tl-clip" style="left:78%; width:10%; background:linear-gradient(90deg,#bf360c,#ef6c00);">CTA</div>
                <div class="tl-clip" style="left:89%; width:11%; background:linear-gradient(90deg,#283593,#5c6bc0);">Outro</div>
            </div>
        </div>
        <div class="tl-track">
            <div class="tl-track-label">Video 2</div>
            <div class="tl-track-clips">
                <div class="tl-clip" style="left:20%; width:28%; background:rgba(224,64,251,.2); border:1px solid rgba(224,64,251,.3);">Overlay</div>
            </div>
        </div>
        <div class="tl-track">
            <div class="tl-track-label">Text</div>
            <div class="tl-track-clips">
                <div class="tl-clip" style="left:5%; width:12%; background:rgba(255,214,0,.2); border:1px solid rgba(255,214,0,.3);">Title</div>
                <div class="tl-clip" style="left:55%; width:15%; background:rgba(255,214,0,.2); border:1px solid rgba(255,214,0,.3);">Quote</div>
                <div class="tl-clip" style="left:80%; width:8%; background:rgba(255,214,0,.2); border:1px solid rgba(255,214,0,.3);">CTA</div>
            </div>
        </div>
        <div class="tl-track">
            <div class="tl-track-label">Audio</div>
            <div class="tl-track-clips">
                <div class="tl-clip" style="left:0; width:100%; background:rgba(76,175,80,.15); border:1px solid rgba(76,175,80,.25);">BG Music</div>
            </div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# 3. OPENCLAW — AI Chat Interface (Telegram-style)
# ============================================================
def html_openclaw():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK_MONO + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#0e1621;
    font-family:'Inter',system-ui,sans-serif;
    color:#fff; overflow:hidden;
    display:flex;
}

/* LEFT SIDEBAR */
.sidebar {
    width:240px; background:#0e1621;
    border-right:1px solid rgba(255,255,255,.06);
    display:flex; flex-direction:column;
}
.sb-header {
    padding:10px 14px;
    display:flex; align-items:center; justify-content:space-between;
    border-bottom:1px solid rgba(255,255,255,.06);
}
.sb-header h1 { font-size:14px; font-weight:800; }
.sb-header h1 .oc { color:#5ebbf7; }
.sb-new-btn {
    padding:3px 8px; border-radius:5px; font-size:8px; font-weight:600;
    background:rgba(94,187,247,.15); color:#5ebbf7; border:1px solid rgba(94,187,247,.2);
}
.sb-search {
    margin:8px 12px; padding:6px 10px;
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.06);
    border-radius:8px; font-size:9px; color:rgba(255,255,255,.3);
}
.sb-chats { flex:1; overflow:hidden; }
.chat-item {
    display:flex; gap:10px; padding:8px 14px;
    border-bottom:1px solid rgba(255,255,255,.03);
    align-items:flex-start;
}
.chat-item.active { background:rgba(94,187,247,.08); }
.chat-avatar {
    width:36px; height:36px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:12px; font-weight:800; flex-shrink:0;
}
.chat-info { flex:1; min-width:0; }
.chat-info .chat-name { font-size:10px; font-weight:600; color:rgba(255,255,255,.85); }
.chat-info .chat-preview { font-size:8px; color:rgba(255,255,255,.35); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; margin-top:1px; }
.chat-meta { text-align:right; flex-shrink:0; }
.chat-meta .chat-time { font-size:7px; color:rgba(255,255,255,.25); }
.chat-meta .unread {
    display:inline-block; min-width:14px; height:14px; border-radius:7px;
    background:#5ebbf7; font-size:7px; font-weight:700; color:#0e1621;
    text-align:center; line-height:14px; margin-top:3px;
}

/* CHAT AREA */
.chat-area {
    flex:1; display:flex; flex-direction:column;
    background:#17212b;
}
.chat-header {
    padding:8px 16px;
    background:#1c2936;
    border-bottom:1px solid rgba(255,255,255,.06);
    display:flex; align-items:center; gap:10px;
}
.ch-avatar {
    width:32px; height:32px; border-radius:50%;
    background:linear-gradient(135deg,#5ebbf7,#3d8bc9);
    display:flex; align-items:center; justify-content:center;
    font-size:11px; font-weight:800;
}
.ch-info .ch-name { font-size:11px; font-weight:700; }
.ch-info .ch-status { font-size:8px; color:rgba(255,255,255,.35); }

.messages { flex:1; padding:12px 16px; overflow:hidden; display:flex; flex-direction:column; gap:6px; }

.msg {
    max-width:75%; padding:8px 12px;
    border-radius:12px; position:relative;
    font-size:10px; line-height:1.5;
}
.msg-bot {
    background:#1c2936;
    border:1px solid rgba(255,255,255,.06);
    align-self:flex-start;
    border-bottom-left-radius:4px;
}
.msg-user {
    background:rgba(94,187,247,.15);
    border:1px solid rgba(94,187,247,.15);
    align-self:flex-end;
    border-bottom-right-radius:4px;
    color:rgba(255,255,255,.9);
}
.msg-sender { font-size:8px; font-weight:700; color:#5ebbf7; margin-bottom:2px; }
.msg-time { font-size:7px; color:rgba(255,255,255,.2); margin-top:3px; text-align:right; }

.code-block {
    background:#0e1621; border:1px solid rgba(255,255,255,.08);
    border-radius:6px; padding:6px 8px; margin:4px 0;
    font-family:'JetBrains Mono',monospace; font-size:8px;
    color:#a0c4e0; line-height:1.6; overflow:hidden;
}
.code-block .kw { color:#c678dd; }
.code-block .fn { color:#61afef; }
.code-block .str { color:#98c379; }
.code-block .cm { color:#5c6370; }
.code-block .num { color:#d19a66; }

.typing-indicator {
    align-self:flex-start;
    display:flex; gap:4px; padding:8px 14px;
    background:#1c2936; border:1px solid rgba(255,255,255,.06);
    border-radius:12px; border-bottom-left-radius:4px;
}
.typing-dot {
    width:5px; height:5px; border-radius:50%;
    background:rgba(94,187,247,.4);
}
.typing-dot:nth-child(2) { opacity:.6; }
.typing-dot:nth-child(3) { opacity:.3; }

/* INPUT BAR */
.input-bar {
    padding:8px 16px;
    background:#1c2936;
    border-top:1px solid rgba(255,255,255,.06);
    display:flex; gap:8px; align-items:center;
}
.input-field {
    flex:1; padding:8px 12px;
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.08);
    border-radius:20px;
    font-size:10px; color:rgba(255,255,255,.4);
}
.send-btn {
    width:32px; height:32px; border-radius:50%;
    background:linear-gradient(135deg,#5ebbf7,#3d8bc9);
    display:flex; align-items:center; justify-content:center;
}
.send-btn::after {
    content:''; width:0; height:0;
    border-left:10px solid #fff;
    border-top:6px solid transparent;
    border-bottom:6px solid transparent;
    margin-left:2px;
}
</style></head><body>

<div class="sidebar">
    <div class="sb-header">
        <h1><span class="oc">Open</span>Claw</h1>
        <div class="sb-new-btn">+ New Chat</div>
    </div>
    <div class="sb-search">Search conversations...</div>
    <div class="sb-chats">
        <div class="chat-item active">
            <div class="chat-avatar" style="background:linear-gradient(135deg,#5ebbf7,#3d8bc9);">AI</div>
            <div class="chat-info"><div class="chat-name">OpenClaw Assistant</div><div class="chat-preview">Here is the refactored code with proper error handling...</div></div>
            <div class="chat-meta"><div class="chat-time">2m ago</div></div>
        </div>
        <div class="chat-item">
            <div class="chat-avatar" style="background:linear-gradient(135deg,#ef5350,#c62828);">Py</div>
            <div class="chat-info"><div class="chat-name">Python Debugger</div><div class="chat-preview">The issue is in line 42 where the async handler...</div></div>
            <div class="chat-meta"><div class="chat-time">1h ago</div><div class="unread">3</div></div>
        </div>
        <div class="chat-item">
            <div class="chat-avatar" style="background:linear-gradient(135deg,#66bb6a,#2e7d32);">DB</div>
            <div class="chat-info"><div class="chat-name">SQL Optimizer</div><div class="chat-preview">Add an index on user_id column for faster queries...</div></div>
            <div class="chat-meta"><div class="chat-time">3h ago</div></div>
        </div>
        <div class="chat-item">
            <div class="chat-avatar" style="background:linear-gradient(135deg,#ffa726,#ef6c00);">TS</div>
            <div class="chat-info"><div class="chat-name">TypeScript Helper</div><div class="chat-preview">You can use discriminated unions to narrow the type...</div></div>
            <div class="chat-meta"><div class="chat-time">5h ago</div></div>
        </div>
        <div class="chat-item">
            <div class="chat-avatar" style="background:linear-gradient(135deg,#ab47bc,#6a1b9a);">Rx</div>
            <div class="chat-info"><div class="chat-name">React Architect</div><div class="chat-preview">Split this into smaller composable hooks and memoize...</div></div>
            <div class="chat-meta"><div class="chat-time">1d ago</div><div class="unread">1</div></div>
        </div>
        <div class="chat-item">
            <div class="chat-avatar" style="background:linear-gradient(135deg,#78909c,#37474f);">Dk</div>
            <div class="chat-info"><div class="chat-name">Docker Expert</div><div class="chat-preview">Multi-stage build will reduce image size by 80%...</div></div>
            <div class="chat-meta"><div class="chat-time">2d ago</div></div>
        </div>
    </div>
</div>

<div class="chat-area">
    <div class="chat-header">
        <div class="ch-avatar">AI</div>
        <div class="ch-info">
            <div class="ch-name">OpenClaw Assistant</div>
            <div class="ch-status">online -- GPT-4 Turbo -- context: 12,847 tokens</div>
        </div>
    </div>
    <div class="messages">
        <div class="msg msg-user">
            Can you refactor this Express route to use proper error handling and input validation?
            <div class="msg-time">14:32</div>
        </div>
        <div class="msg msg-bot">
            <div class="msg-sender">OpenClaw</div>
            Sure! Here is the refactored version with Zod validation and centralized error handling:
            <div class="code-block">
<span class="kw">import</span> { z } <span class="kw">from</span> <span class="str">'zod'</span>;
<span class="kw">import</span> { asyncHandler } <span class="kw">from</span> <span class="str">'../utils'</span>;

<span class="kw">const</span> <span class="fn">schema</span> = z.<span class="fn">object</span>({
  email: z.<span class="fn">string</span>().<span class="fn">email</span>(),
  name: z.<span class="fn">string</span>().<span class="fn">min</span>(<span class="num">2</span>).<span class="fn">max</span>(<span class="num">50</span>),
});

router.<span class="fn">post</span>(<span class="str">'/users'</span>, <span class="fn">asyncHandler</span>(<span class="kw">async</span> (req, res) => {
  <span class="kw">const</span> data = schema.<span class="fn">parse</span>(req.body);
  <span class="kw">const</span> user = <span class="kw">await</span> User.<span class="fn">create</span>(data);
  res.<span class="fn">json</span>({ success: <span class="num">true</span>, data: user });
}));
            </div>
            Key changes: 1) Added Zod schema for input validation 2) Wrapped in asyncHandler to catch errors 3) Returns consistent response format.
            <div class="msg-time">14:32</div>
        </div>
        <div class="msg msg-user">
            What about rate limiting?
            <div class="msg-time">14:33</div>
        </div>
        <div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        </div>
    </div>
    <div class="input-bar">
        <div class="input-field">Type a message... (Shift+Enter for new line)</div>
        <div class="send-btn"></div>
    </div>
</div>

</body></html>'''


# ============================================================
# 4. JOBBOARD — Clean job listing platform
# ============================================================
def html_jobboard():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#f8fafc;
    font-family:'Inter',system-ui,sans-serif;
    color:#1e293b; overflow:hidden;
}

/* NAV */
.nav {
    display:flex; align-items:center; justify-content:space-between;
    padding:8px 24px;
    background:#fff;
    border-bottom:1px solid #e2e8f0;
    box-shadow:0 1px 3px rgba(0,0,0,.04);
}
.nav .logo { font-size:16px; font-weight:800; letter-spacing:-.5px; }
.nav .logo .j { color:#3b82f6; }
.nav-links { display:flex; gap:18px; }
.nav-links a { font-size:10px; color:#64748b; text-decoration:none; font-weight:500; }
.nav-links a.active { color:#3b82f6; font-weight:600; }
.nav-right { display:flex; gap:8px; }
.nav-btn {
    padding:4px 12px; border-radius:6px; font-size:9px; font-weight:600;
}
.nav-btn.outline { border:1px solid #e2e8f0; color:#475569; background:#fff; }
.nav-btn.primary { background:#3b82f6; color:#fff; }

/* HERO */
.hero {
    background:linear-gradient(135deg,#1e40af 0%,#3b82f6 50%,#60a5fa 100%);
    padding:16px 24px;
    text-align:center; position:relative; overflow:hidden;
}
.hero::before {
    content:''; position:absolute; top:-30px; right:60px;
    width:120px; height:120px;
    background:radial-gradient(circle,rgba(255,255,255,.1) 0%,transparent 70%);
    border-radius:50%;
}
.hero h1 { font-size:18px; font-weight:800; color:#fff; margin-bottom:4px; }
.hero p { font-size:10px; color:rgba(255,255,255,.7); margin-bottom:10px; }
.search-bar {
    display:flex; gap:6px; max-width:500px; margin:0 auto;
}
.search-input {
    flex:1; padding:7px 12px; border-radius:8px;
    background:#fff; font-size:10px; color:#94a3b8;
    border:none; box-shadow:0 2px 8px rgba(0,0,0,.1);
}
.search-btn {
    padding:7px 16px; border-radius:8px;
    background:#1e40af; font-size:10px; font-weight:600;
    color:#fff;
}

/* CONTENT */
.content { display:flex; padding:12px 24px; gap:16px; }

/* FILTERS */
.filters {
    width:170px; flex-shrink:0;
}
.filter-group { margin-bottom:12px; }
.fg-title { font-size:9px; font-weight:700; color:#334155; text-transform:uppercase; letter-spacing:.5px; margin-bottom:6px; }
.filter-opt {
    display:flex; align-items:center; gap:6px;
    font-size:9px; color:#64748b; margin-bottom:4px;
}
.checkbox {
    width:12px; height:12px; border-radius:3px;
    border:1.5px solid #cbd5e1; flex-shrink:0;
}
.checkbox.checked { background:#3b82f6; border-color:#3b82f6; position:relative; }
.checkbox.checked::after {
    content:''; position:absolute; top:1px; left:3px;
    width:4px; height:7px;
    border-right:1.5px solid #fff; border-bottom:1.5px solid #fff;
    transform:rotate(40deg);
}
.salary-range {
    height:4px; background:#e2e8f0; border-radius:2px;
    margin:8px 0 4px; position:relative;
}
.salary-range .fill { position:absolute; left:20%; right:30%; height:100%; background:#3b82f6; border-radius:2px; }
.salary-labels { display:flex; justify-content:space-between; font-size:7px; color:#94a3b8; }

/* JOB CARDS */
.jobs { flex:1; display:flex; flex-direction:column; gap:8px; }
.job-card {
    background:#fff; border:1px solid #e2e8f0;
    border-radius:10px; padding:12px 14px;
    display:flex; gap:10px; align-items:flex-start;
    box-shadow:0 1px 3px rgba(0,0,0,.04);
    position:relative;
}
.job-card:hover { border-color:#3b82f6; box-shadow:0 2px 8px rgba(59,130,246,.1); }
.company-logo {
    width:36px; height:36px; border-radius:8px;
    display:flex; align-items:center; justify-content:center;
    font-size:10px; font-weight:800; color:#fff; flex-shrink:0;
}
.job-info { flex:1; }
.job-title { font-size:11px; font-weight:700; color:#1e293b; margin-bottom:2px; }
.job-company { font-size:9px; color:#64748b; margin-bottom:4px; }
.job-meta { display:flex; gap:8px; flex-wrap:wrap; }
.job-tag {
    padding:2px 6px; border-radius:4px; font-size:7px; font-weight:600;
}
.tag-remote { background:#dbeafe; color:#1d4ed8; }
.tag-full { background:#dcfce7; color:#166534; }
.tag-part { background:#fef3c7; color:#92400e; }
.tag-senior { background:#ede9fe; color:#5b21b6; }
.tag-mid { background:#fce7f3; color:#9d174d; }
.tag-hybrid { background:#e0f2fe; color:#075985; }
.job-salary {
    position:absolute; top:12px; right:14px;
    font-size:11px; font-weight:700; color:#3b82f6;
}
.job-posted { font-size:7px; color:#94a3b8; margin-top:3px; }
</style></head><body>

<div class="nav">
    <div class="logo"><span class="j">Job</span>Board</div>
    <div class="nav-links">
        <a class="active">Browse Jobs</a><a>Companies</a><a>Salaries</a><a>Resources</a>
    </div>
    <div class="nav-right">
        <div class="nav-btn outline">Sign In</div>
        <div class="nav-btn primary">Post a Job</div>
    </div>
</div>

<div class="hero">
    <h1>Find your dream tech job</h1>
    <p>12,847 developer jobs from 3,200+ companies worldwide</p>
    <div class="search-bar">
        <div class="search-input">Job title, skills, or company...</div>
        <div class="search-input" style="flex:.6;">Location or Remote</div>
        <div class="search-btn">Search</div>
    </div>
</div>

<div class="content">
    <div class="filters">
        <div class="filter-group">
            <div class="fg-title">Job Type</div>
            <div class="filter-opt"><div class="checkbox checked"></div>Full-time (8,420)</div>
            <div class="filter-opt"><div class="checkbox checked"></div>Remote (5,130)</div>
            <div class="filter-opt"><div class="checkbox"></div>Part-time (1,240)</div>
            <div class="filter-opt"><div class="checkbox"></div>Contract (890)</div>
            <div class="filter-opt"><div class="checkbox"></div>Internship (340)</div>
        </div>
        <div class="filter-group">
            <div class="fg-title">Experience</div>
            <div class="filter-opt"><div class="checkbox checked"></div>Senior (3,200)</div>
            <div class="filter-opt"><div class="checkbox"></div>Mid-level (4,100)</div>
            <div class="filter-opt"><div class="checkbox"></div>Junior (2,800)</div>
            <div class="filter-opt"><div class="checkbox"></div>Lead (980)</div>
        </div>
        <div class="filter-group">
            <div class="fg-title">Salary Range</div>
            <div class="salary-range"><div class="fill"></div></div>
            <div class="salary-labels"><span>$40k</span><span>$80k - $140k</span><span>$200k+</span></div>
        </div>
        <div class="filter-group">
            <div class="fg-title">Tech Stack</div>
            <div class="filter-opt"><div class="checkbox checked"></div>React (2,100)</div>
            <div class="filter-opt"><div class="checkbox"></div>Python (1,900)</div>
            <div class="filter-opt"><div class="checkbox"></div>Node.js (1,700)</div>
            <div class="filter-opt"><div class="checkbox"></div>TypeScript (1,500)</div>
        </div>
    </div>

    <div class="jobs">
        <div class="job-card">
            <div class="company-logo" style="background:linear-gradient(135deg,#3b82f6,#1d4ed8);">S</div>
            <div class="job-info">
                <div class="job-title">Senior Full-Stack Engineer</div>
                <div class="job-company">Stripe -- San Francisco, CA (Remote OK)</div>
                <div class="job-meta">
                    <div class="job-tag tag-remote">Remote</div>
                    <div class="job-tag tag-full">Full-time</div>
                    <div class="job-tag tag-senior">Senior</div>
                </div>
                <div class="job-posted">Posted 2 hours ago -- 48 applicants</div>
            </div>
            <div class="job-salary">$180-220k</div>
        </div>
        <div class="job-card">
            <div class="company-logo" style="background:linear-gradient(135deg,#10b981,#059669);">V</div>
            <div class="job-info">
                <div class="job-title">Frontend Developer (React/Next.js)</div>
                <div class="job-company">Vercel -- Worldwide (Remote)</div>
                <div class="job-meta">
                    <div class="job-tag tag-remote">Remote</div>
                    <div class="job-tag tag-full">Full-time</div>
                    <div class="job-tag tag-mid">Mid-level</div>
                </div>
                <div class="job-posted">Posted 5 hours ago -- 92 applicants</div>
            </div>
            <div class="job-salary">$140-170k</div>
        </div>
        <div class="job-card">
            <div class="company-logo" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);">N</div>
            <div class="job-info">
                <div class="job-title">Backend Engineer (Python/Go)</div>
                <div class="job-company">Notion -- New York, NY (Hybrid)</div>
                <div class="job-meta">
                    <div class="job-tag tag-hybrid">Hybrid</div>
                    <div class="job-tag tag-full">Full-time</div>
                    <div class="job-tag tag-senior">Senior</div>
                </div>
                <div class="job-posted">Posted 1 day ago -- 156 applicants</div>
            </div>
            <div class="job-salary">$160-200k</div>
        </div>
        <div class="job-card">
            <div class="company-logo" style="background:linear-gradient(135deg,#f59e0b,#d97706);">L</div>
            <div class="job-info">
                <div class="job-title">DevOps / SRE Engineer</div>
                <div class="job-company">Linear -- Remote (EU timezone)</div>
                <div class="job-meta">
                    <div class="job-tag tag-remote">Remote</div>
                    <div class="job-tag tag-full">Full-time</div>
                    <div class="job-tag tag-mid">Mid-level</div>
                </div>
                <div class="job-posted">Posted 2 days ago -- 67 applicants</div>
            </div>
            <div class="job-salary">$120-150k</div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# 5. EVENT-PLATFORM — Event analytics dashboard
# ============================================================
def html_event_platform():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#0f0a1a;
    font-family:'Inter',system-ui,sans-serif;
    color:#fff; overflow:hidden;
    display:flex;
}

/* SIDEBAR */
.sidebar {
    width:56px; background:#0a0612;
    border-right:1px solid rgba(168,85,247,.1);
    display:flex; flex-direction:column; align-items:center;
    padding:12px 0; gap:16px;
}
.sb-logo {
    width:32px; height:32px; border-radius:8px;
    background:linear-gradient(135deg,#a855f7,#7c3aed);
    display:flex; align-items:center; justify-content:center;
    font-size:12px; font-weight:900;
}
.sb-item {
    width:32px; height:32px; border-radius:8px;
    display:flex; align-items:center; justify-content:center;
    background:rgba(255,255,255,.03);
    position:relative;
}
.sb-item.active { background:rgba(168,85,247,.15); }
.sb-item.active::before {
    content:''; position:absolute; left:-12px; top:6px;
    width:3px; height:20px; border-radius:0 3px 3px 0;
    background:#a855f7;
}
.sb-dot {
    width:6px; height:6px; border-radius:50%;
}

/* MAIN */
.main { flex:1; display:flex; flex-direction:column; overflow:hidden; }

/* TOP BAR */
.topbar {
    display:flex; align-items:center; justify-content:space-between;
    padding:10px 20px;
    border-bottom:1px solid rgba(255,255,255,.06);
}
.topbar h1 { font-size:14px; font-weight:800; }
.topbar h1 span { color:#a855f7; }
.topbar-right { display:flex; gap:8px; align-items:center; }
.date-range {
    padding:4px 10px; border-radius:6px; font-size:8px; font-weight:500;
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08);
    color:rgba(255,255,255,.5);
}
.tb-avatar {
    width:26px; height:26px; border-radius:50%;
    background:linear-gradient(135deg,#a855f7,#7c3aed);
}

/* METRICS */
.metrics {
    display:grid; grid-template-columns:repeat(4,1fr); gap:10px;
    padding:12px 20px;
}
.metric-card {
    padding:12px;
    background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.06);
    border-radius:10px;
    position:relative; overflow:hidden;
}
.metric-card::before {
    content:''; position:absolute; top:0; right:0;
    width:60px; height:60px;
    border-radius:50%;
    opacity:.08;
}
.mc-label { font-size:8px; color:rgba(255,255,255,.4); text-transform:uppercase; letter-spacing:.5px; margin-bottom:4px; }
.mc-val { font-size:18px; font-weight:800; }
.mc-val .accent { color:#a855f7; }
.mc-change { font-size:8px; margin-top:2px; font-weight:600; }
.mc-change.up { color:#22c55e; }
.mc-change.down { color:#ef4444; }
.mc-spark {
    display:flex; align-items:flex-end; gap:2px; height:20px; margin-top:4px;
}
.mc-spark .bar {
    width:4px; border-radius:2px 2px 0 0;
    background:rgba(168,85,247,.3);
}

/* CHART + TABLE */
.dashboard { display:flex; gap:12px; padding:0 20px 12px; flex:1; }

.chart-panel {
    flex:1;
    background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.06);
    border-radius:10px;
    padding:12px; display:flex; flex-direction:column;
}
.chart-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; }
.chart-title { font-size:11px; font-weight:700; }
.chart-tabs { display:flex; gap:4px; }
.chart-tab {
    padding:2px 8px; border-radius:4px; font-size:7px; font-weight:600;
    background:rgba(255,255,255,.04); color:rgba(255,255,255,.4);
}
.chart-tab.active { background:rgba(168,85,247,.15); color:#c084fc; }
.chart-area { flex:1; position:relative; display:flex; flex-direction:column; justify-content:flex-end; }
.chart-grid { display:flex; align-items:flex-end; gap:6px; flex:1; padding:0 4px; }
.chart-bar-group { flex:1; display:flex; flex-direction:column; align-items:center; gap:2px; }
.chart-bar {
    width:100%; border-radius:3px 3px 0 0;
    position:relative;
}
.chart-bar.primary { background:linear-gradient(180deg,#a855f7,#7c3aed); }
.chart-bar.secondary { background:rgba(168,85,247,.2); }
.chart-label { font-size:6px; color:rgba(255,255,255,.25); text-align:center; }
.chart-y-axis {
    position:absolute; left:0; top:0; bottom:16px;
    display:flex; flex-direction:column; justify-content:space-between;
    width:30px;
}
.chart-y-label { font-size:6px; color:rgba(255,255,255,.2); text-align:right; }

/* TABLE */
.table-panel {
    width:280px;
    background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.06);
    border-radius:10px;
    padding:12px; display:flex; flex-direction:column;
}
.table-title { font-size:11px; font-weight:700; margin-bottom:8px; }
.table-header {
    display:grid; grid-template-columns:1fr 60px 50px 50px;
    gap:4px; padding-bottom:6px;
    border-bottom:1px solid rgba(255,255,255,.06);
    margin-bottom:4px;
}
.th { font-size:7px; color:rgba(255,255,255,.3); text-transform:uppercase; letter-spacing:.3px; font-weight:600; }
.table-row {
    display:grid; grid-template-columns:1fr 60px 50px 50px;
    gap:4px; padding:5px 0;
    border-bottom:1px solid rgba(255,255,255,.03);
    align-items:center;
}
.tr-name { font-size:8px; font-weight:600; }
.tr-date { font-size:7px; color:rgba(255,255,255,.35); }
.tr-val { font-size:8px; font-weight:600; }
.tr-val.purple { color:#c084fc; }
.status-badge {
    font-size:6px; font-weight:700; padding:2px 5px; border-radius:3px;
    text-align:center;
}
.status-live { background:rgba(34,197,94,.15); color:#22c55e; }
.status-upcoming { background:rgba(168,85,247,.15); color:#c084fc; }
.status-sold { background:rgba(239,68,68,.15); color:#ef4444; }
</style></head><body>

<div class="sidebar">
    <div class="sb-logo">E</div>
    <div class="sb-item active"><div class="sb-dot" style="background:#a855f7;"></div></div>
    <div class="sb-item"><div class="sb-dot" style="background:rgba(255,255,255,.2);"></div></div>
    <div class="sb-item"><div class="sb-dot" style="background:rgba(255,255,255,.2);"></div></div>
    <div class="sb-item"><div class="sb-dot" style="background:rgba(255,255,255,.2);"></div></div>
    <div class="sb-item"><div class="sb-dot" style="background:rgba(255,255,255,.2);"></div></div>
</div>

<div class="main">
    <div class="topbar">
        <h1><span>Event</span> Analytics</h1>
        <div class="topbar-right">
            <div class="date-range">Mar 1 - Mar 18, 2026</div>
            <div class="tb-avatar"></div>
        </div>
    </div>

    <div class="metrics">
        <div class="metric-card" style="--c:#a855f7;">
            <div class="mc-label">Tickets Sold</div>
            <div class="mc-val">24,<span class="accent">847</span></div>
            <div class="mc-change up">+12.4% vs last month</div>
            <div class="mc-spark">
                <div class="bar" style="height:40%;"></div><div class="bar" style="height:55%;"></div><div class="bar" style="height:45%;"></div><div class="bar" style="height:70%;"></div><div class="bar" style="height:60%;"></div><div class="bar" style="height:85%;"></div><div class="bar" style="height:90%;"></div>
            </div>
        </div>
        <div class="metric-card">
            <div class="mc-label">Revenue</div>
            <div class="mc-val">$<span class="accent">1.2</span>M</div>
            <div class="mc-change up">+8.7% vs last month</div>
            <div class="mc-spark">
                <div class="bar" style="height:35%;"></div><div class="bar" style="height:50%;"></div><div class="bar" style="height:55%;"></div><div class="bar" style="height:60%;"></div><div class="bar" style="height:70%;"></div><div class="bar" style="height:75%;"></div><div class="bar" style="height:95%;"></div>
            </div>
        </div>
        <div class="metric-card">
            <div class="mc-label">Capacity Fill</div>
            <div class="mc-val">87<span class="accent">%</span></div>
            <div class="mc-change up">+3.2% vs last month</div>
            <div class="mc-spark">
                <div class="bar" style="height:60%;"></div><div class="bar" style="height:65%;"></div><div class="bar" style="height:70%;"></div><div class="bar" style="height:72%;"></div><div class="bar" style="height:78%;"></div><div class="bar" style="height:80%;"></div><div class="bar" style="height:87%;"></div>
            </div>
        </div>
        <div class="metric-card">
            <div class="mc-label">Active Events</div>
            <div class="mc-val">18</div>
            <div class="mc-change down">-2 vs last month</div>
            <div class="mc-spark">
                <div class="bar" style="height:80%;"></div><div class="bar" style="height:75%;"></div><div class="bar" style="height:90%;"></div><div class="bar" style="height:70%;"></div><div class="bar" style="height:85%;"></div><div class="bar" style="height:60%;"></div><div class="bar" style="height:72%;"></div>
            </div>
        </div>
    </div>

    <div class="dashboard">
        <div class="chart-panel">
            <div class="chart-header">
                <div class="chart-title">Ticket Sales Trend</div>
                <div class="chart-tabs">
                    <div class="chart-tab active">Daily</div>
                    <div class="chart-tab">Weekly</div>
                    <div class="chart-tab">Monthly</div>
                </div>
            </div>
            <div class="chart-area">
                <div class="chart-grid">
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:40%;"></div><div class="chart-label">1</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:55%;"></div><div class="chart-label">2</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:35%;"></div><div class="chart-label">3</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:70%;"></div><div class="chart-label">4</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:60%;"></div><div class="chart-label">5</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:85%;"></div><div class="chart-label">6</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:75%;"></div><div class="chart-label">7</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:90%;"></div><div class="chart-label">8</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:65%;"></div><div class="chart-label">9</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:78%;"></div><div class="chart-label">10</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:88%;"></div><div class="chart-label">11</div></div>
                    <div class="chart-bar-group"><div class="chart-bar primary" style="height:95%;"></div><div class="chart-label">12</div></div>
                    <div class="chart-bar-group"><div class="chart-bar secondary" style="height:50%;"></div><div class="chart-label">13</div></div>
                    <div class="chart-bar-group"><div class="chart-bar secondary" style="height:42%;"></div><div class="chart-label">14</div></div>
                </div>
            </div>
        </div>

        <div class="table-panel">
            <div class="table-title">Upcoming Events</div>
            <div class="table-header">
                <div class="th">Event</div><div class="th">Date</div><div class="th">Sold</div><div class="th">Status</div>
            </div>
            <div class="table-row">
                <div class="tr-name">TechConf 2026</div>
                <div class="tr-date">Mar 25</div>
                <div class="tr-val purple">4,200</div>
                <div class="status-badge status-live">LIVE</div>
            </div>
            <div class="table-row">
                <div class="tr-name">DevSummit Asia</div>
                <div class="tr-date">Apr 2</div>
                <div class="tr-val purple">2,800</div>
                <div class="status-badge status-upcoming">SOON</div>
            </div>
            <div class="table-row">
                <div class="tr-name">Music Festival</div>
                <div class="tr-date">Apr 10</div>
                <div class="tr-val purple">8,500</div>
                <div class="status-badge status-sold">SOLD OUT</div>
            </div>
            <div class="table-row">
                <div class="tr-name">AI Workshop</div>
                <div class="tr-date">Apr 15</div>
                <div class="tr-val purple">340</div>
                <div class="status-badge status-upcoming">SOON</div>
            </div>
            <div class="table-row">
                <div class="tr-name">Startup Pitch</div>
                <div class="tr-date">Apr 20</div>
                <div class="tr-val purple">1,100</div>
                <div class="status-badge status-live">LIVE</div>
            </div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# 6. CHEATMC — Game prediction / tournament tool
# ============================================================
def html_cheatmc():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#0a0e14;
    font-family:'Inter',system-ui,sans-serif;
    color:#e0e0e0; overflow:hidden;
    display:flex; flex-direction:column;
}

/* HEADER */
.header {
    display:flex; align-items:center; justify-content:space-between;
    padding:8px 20px;
    background:rgba(0,0,0,.4);
    border-bottom:1px solid rgba(0,255,200,.1);
}
.logo { font-size:16px; font-weight:900; letter-spacing:-.5px; }
.logo .ch { color:#00e5cc; }
.logo .mc { color:#0ff; }
.header-tabs { display:flex; gap:12px; }
.header-tab { font-size:9px; font-weight:600; color:rgba(255,255,255,.3); }
.header-tab.active { color:#00e5cc; }
.match-info {
    padding:3px 10px; border-radius:6px; font-size:8px; font-weight:600;
    background:rgba(0,229,204,.1); border:1px solid rgba(0,229,204,.2);
    color:#00e5cc;
}

/* MATCH HEADER */
.match-header {
    display:flex; align-items:center; justify-content:center; gap:20px;
    padding:10px 20px;
    background:linear-gradient(180deg, rgba(0,229,204,.04) 0%, transparent 100%);
}
.team-badge {
    text-align:center; width:100px;
}
.team-logo {
    width:40px; height:40px; border-radius:10px; margin:0 auto 4px;
    display:flex; align-items:center; justify-content:center;
    font-size:13px; font-weight:900; color:#fff;
    box-shadow:0 4px 12px rgba(0,0,0,.3);
}
.team-name { font-size:10px; font-weight:700; }
.team-record { font-size:7px; color:rgba(255,255,255,.3); }
.vs-box { text-align:center; }
.vs-text { font-size:18px; font-weight:900; color:rgba(255,255,255,.15); }
.match-stage { font-size:8px; color:#00e5cc; font-weight:600; margin-top:2px; }

/* PREDICTION BAR */
.pred-section { padding:0 20px 8px; }
.pred-bar-container { display:flex; align-items:center; gap:8px; margin-bottom:6px; }
.pred-pct { font-size:14px; font-weight:800; width:50px; }
.pred-pct.green { color:#00e5cc; }
.pred-pct.red { color:#ef4444; }
.pred-bar { flex:1; height:8px; border-radius:4px; background:rgba(255,255,255,.06); overflow:hidden; display:flex; }
.pred-fill-l { height:100%; background:linear-gradient(90deg,#00e5cc,#00b4a0); border-radius:4px 0 0 4px; }
.pred-fill-r { height:100%; background:linear-gradient(90deg,#ef4444,#dc2626); border-radius:0 4px 4px 0; }

/* BRACKET */
.content { display:flex; flex:1; gap:12px; padding:0 20px 10px; overflow:hidden; }

.bracket {
    flex:1; display:flex; gap:8px; align-items:center;
}
.bracket-round {
    display:flex; flex-direction:column; gap:8px; flex:1;
}
.round-label { font-size:7px; text-transform:uppercase; letter-spacing:.8px; color:rgba(255,255,255,.25); text-align:center; margin-bottom:4px; font-weight:600; }
.bracket-match {
    background:rgba(255,255,255,.03);
    border:1px solid rgba(255,255,255,.06);
    border-radius:8px; overflow:hidden;
}
.bm-team {
    display:flex; align-items:center; justify-content:space-between;
    padding:5px 8px;
    font-size:8px; font-weight:600;
    border-bottom:1px solid rgba(255,255,255,.04);
}
.bm-team:last-child { border-bottom:none; }
.bm-team.winner { background:rgba(0,229,204,.06); }
.bm-left { display:flex; align-items:center; gap:5px; }
.bm-icon {
    width:14px; height:14px; border-radius:3px;
    display:flex; align-items:center; justify-content:center;
    font-size:6px; font-weight:800; color:#fff;
}
.bm-score { font-weight:800; }
.bm-score.win { color:#00e5cc; }
.bm-score.lose { color:rgba(255,255,255,.3); }
.bm-pred {
    font-size:7px; padding:1px 4px; border-radius:3px;
    font-weight:600;
}
.bm-pred.high { background:rgba(0,229,204,.15); color:#00e5cc; }
.bm-pred.low { background:rgba(239,68,68,.1); color:#ef4444; }
.bm-pred.mid { background:rgba(245,158,11,.1); color:#f59e0b; }

/* STATS PANEL */
.stats-panel {
    width:220px;
    background:rgba(255,255,255,.02);
    border:1px solid rgba(255,255,255,.06);
    border-radius:10px;
    padding:10px;
    display:flex; flex-direction:column; gap:8px;
}
.sp-title { font-size:9px; font-weight:700; color:rgba(255,255,255,.6); text-transform:uppercase; letter-spacing:.5px; }
.sp-row { display:flex; justify-content:space-between; align-items:center; font-size:8px; }
.sp-label { color:rgba(255,255,255,.4); }
.sp-val { font-weight:700; }
.sp-val.green { color:#00e5cc; }
.sp-val.red { color:#ef4444; }
.sp-val.yellow { color:#f59e0b; }
.sp-divider { height:1px; background:rgba(255,255,255,.04); }
.kd-bars { display:flex; gap:3px; margin-top:4px; }
.kd-bar { flex:1; height:24px; border-radius:3px 3px 0 0; display:flex; flex-direction:column; justify-content:flex-end; align-items:center; }
.kd-fill { width:100%; border-radius:3px 3px 0 0; }
.kd-label { font-size:5px; color:rgba(255,255,255,.25); margin-top:1px; }
</style></head><body>

<div class="header">
    <div class="logo"><span class="ch">Cheat</span><span class="mc">MC</span></div>
    <div class="header-tabs">
        <div class="header-tab active">Predictions</div>
        <div class="header-tab">Tournaments</div>
        <div class="header-tab">Leaderboard</div>
        <div class="header-tab">History</div>
    </div>
    <div class="match-info">LIVE -- VCT Masters Shanghai</div>
</div>

<div class="match-header">
    <div class="team-badge">
        <div class="team-logo" style="background:linear-gradient(135deg,#00e5cc,#009688);">SEN</div>
        <div class="team-name">Sentinels</div>
        <div class="team-record">W18-L4 | Map WR: 82%</div>
    </div>
    <div class="vs-box">
        <div class="vs-text">VS</div>
        <div class="match-stage">Grand Final -- BO5</div>
    </div>
    <div class="team-badge">
        <div class="team-logo" style="background:linear-gradient(135deg,#ef4444,#991b1b);">PRX</div>
        <div class="team-name">Paper Rex</div>
        <div class="team-record">W16-L6 | Map WR: 74%</div>
    </div>
</div>

<div class="pred-section">
    <div class="pred-bar-container">
        <div class="pred-pct green">64%</div>
        <div class="pred-bar">
            <div class="pred-fill-l" style="width:64%;"></div>
            <div class="pred-fill-r" style="width:36%;"></div>
        </div>
        <div class="pred-pct red">36%</div>
    </div>
</div>

<div class="content">
    <div class="bracket">
        <div class="bracket-round">
            <div class="round-label">Quarterfinals</div>
            <div class="bracket-match">
                <div class="bm-team winner"><div class="bm-left"><div class="bm-icon" style="background:#00e5cc;">S</div>SEN</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred high">78%</div><div class="bm-score win">2</div></div></div>
                <div class="bm-team"><div class="bm-left"><div class="bm-icon" style="background:#6366f1;">DRX</div>DRX</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred low">22%</div><div class="bm-score lose">0</div></div></div>
            </div>
            <div class="bracket-match">
                <div class="bm-team winner"><div class="bm-left"><div class="bm-icon" style="background:#ef4444;">PRX</div>PRX</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred mid">55%</div><div class="bm-score win">2</div></div></div>
                <div class="bm-team"><div class="bm-left"><div class="bm-icon" style="background:#3b82f6;">C9</div>C9</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred mid">45%</div><div class="bm-score lose">1</div></div></div>
            </div>
            <div class="bracket-match">
                <div class="bm-team winner"><div class="bm-left"><div class="bm-icon" style="background:#f59e0b;">FNC</div>FNC</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred high">68%</div><div class="bm-score win">2</div></div></div>
                <div class="bm-team"><div class="bm-left"><div class="bm-icon" style="background:#8b5cf6;">TH</div>TH</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred low">32%</div><div class="bm-score lose">0</div></div></div>
            </div>
        </div>
        <div class="bracket-round">
            <div class="round-label">Semifinals</div>
            <div class="bracket-match">
                <div class="bm-team winner"><div class="bm-left"><div class="bm-icon" style="background:#00e5cc;">S</div>SEN</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred high">71%</div><div class="bm-score win">2</div></div></div>
                <div class="bm-team"><div class="bm-left"><div class="bm-icon" style="background:#f59e0b;">FNC</div>FNC</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred low">29%</div><div class="bm-score lose">1</div></div></div>
            </div>
            <div class="bracket-match">
                <div class="bm-team winner"><div class="bm-left"><div class="bm-icon" style="background:#ef4444;">PRX</div>PRX</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred mid">58%</div><div class="bm-score win">2</div></div></div>
                <div class="bm-team"><div class="bm-left"><div class="bm-icon" style="background:#22c55e;">LEV</div>LEV</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred mid">42%</div><div class="bm-score lose">0</div></div></div>
            </div>
        </div>
        <div class="bracket-round">
            <div class="round-label">Grand Final</div>
            <div class="bracket-match">
                <div class="bm-team"><div class="bm-left"><div class="bm-icon" style="background:#00e5cc;">S</div>SEN</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred high">64%</div><div class="bm-score win">--</div></div></div>
                <div class="bm-team"><div class="bm-left"><div class="bm-icon" style="background:#ef4444;">PRX</div>PRX</div><div style="display:flex;gap:4px;align-items:center;"><div class="bm-pred low">36%</div><div class="bm-score lose">--</div></div></div>
            </div>
        </div>
    </div>

    <div class="stats-panel">
        <div class="sp-title">Head-to-Head Stats</div>
        <div class="sp-row"><span class="sp-label">Total Matches</span><span class="sp-val">12</span></div>
        <div class="sp-row"><span class="sp-label">SEN Wins</span><span class="sp-val green">8</span></div>
        <div class="sp-row"><span class="sp-label">PRX Wins</span><span class="sp-val red">4</span></div>
        <div class="sp-divider"></div>
        <div class="sp-title">Key Metrics</div>
        <div class="sp-row"><span class="sp-label">SEN Avg ACS</span><span class="sp-val green">248.3</span></div>
        <div class="sp-row"><span class="sp-label">PRX Avg ACS</span><span class="sp-val yellow">231.7</span></div>
        <div class="sp-row"><span class="sp-label">SEN First Blood %</span><span class="sp-val green">58%</span></div>
        <div class="sp-row"><span class="sp-label">PRX First Blood %</span><span class="sp-val red">42%</span></div>
        <div class="sp-row"><span class="sp-label">SEN Clutch WR</span><span class="sp-val green">34%</span></div>
        <div class="sp-row"><span class="sp-label">PRX Clutch WR</span><span class="sp-val yellow">28%</span></div>
        <div class="sp-divider"></div>
        <div class="sp-title">Map K/D by Player</div>
        <div class="kd-bars">
            <div class="kd-bar"><div class="kd-fill" style="height:85%;background:#00e5cc;"></div><div class="kd-label">TenZ</div></div>
            <div class="kd-bar"><div class="kd-fill" style="height:72%;background:#00e5cc;"></div><div class="kd-label">zekken</div></div>
            <div class="kd-bar"><div class="kd-fill" style="height:68%;background:#00e5cc;"></div><div class="kd-label">Sacy</div></div>
            <div class="kd-bar"><div class="kd-fill" style="height:78%;background:#ef4444;"></div><div class="kd-label">f0rsak</div></div>
            <div class="kd-bar"><div class="kd-fill" style="height:70%;background:#ef4444;"></div><div class="kd-label">Jinggg</div></div>
            <div class="kd-bar"><div class="kd-fill" style="height:62%;background:#ef4444;"></div><div class="kd-label">d4v41</div></div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# 7. TRADING-ENGINE — Quant trading dashboard (TradingView-style)
# ============================================================
def html_trading_engine():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK_MONO + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#131722;
    font-family:'Inter',system-ui,sans-serif;
    color:#d1d4dc; overflow:hidden;
    display:flex; flex-direction:column;
}

/* TOP BAR */
.topbar {
    display:flex; align-items:center; justify-content:space-between;
    padding:5px 12px;
    background:#1e222d;
    border-bottom:1px solid #2a2e39;
}
.topbar-left { display:flex; align-items:center; gap:12px; }
.logo { font-size:12px; font-weight:800; letter-spacing:-.3px; }
.logo .t { color:#26a69a; }
.logo .e { color:#ef5350; }
.ticker {
    display:flex; align-items:center; gap:4px;
    padding:3px 8px; background:#2a2e39; border-radius:4px;
}
.ticker .sym { font-size:10px; font-weight:700; color:#fff; }
.ticker .price { font-size:10px; font-weight:700; color:#26a69a; }
.ticker .change { font-size:8px; color:#26a69a; }
.intervals { display:flex; gap:3px; }
.interval {
    padding:2px 6px; font-size:7px; font-weight:600; border-radius:3px;
    color:rgba(209,212,220,.4);
}
.interval.active { background:rgba(38,166,154,.15); color:#26a69a; }
.indicator-tags { display:flex; gap:4px; }
.ind-tag { font-size:7px; padding:2px 5px; border-radius:3px; background:#2a2e39; color:rgba(209,212,220,.5); }

/* MAIN */
.main { display:flex; flex:1; overflow:hidden; }

/* CHART */
.chart-panel { flex:1; display:flex; flex-direction:column; position:relative; }
.chart-area {
    flex:1; position:relative; overflow:hidden;
    border-bottom:1px solid #2a2e39;
}
.y-axis {
    position:absolute; right:0; top:0; bottom:0; width:52px;
    background:#1e222d; border-left:1px solid #2a2e39;
    display:flex; flex-direction:column; justify-content:space-between;
    padding:8px 4px;
}
.y-label { font-size:7px; color:rgba(209,212,220,.3); text-align:right; font-family:'JetBrains Mono',monospace; }
.y-label.current { color:#26a69a; font-weight:700; background:rgba(38,166,154,.1); padding:1px 3px; border-radius:2px; }

/* Candlesticks */
.candles {
    position:absolute; left:8px; right:56px; top:12px; bottom:12px;
    display:flex; align-items:flex-end; gap:3px;
    padding-bottom:8px;
}
.candle {
    flex:1; display:flex; flex-direction:column; align-items:center;
    position:relative;
}
.candle-wick {
    width:1px; position:absolute;
}
.candle-body {
    width:70%; border-radius:1px; position:relative; z-index:1;
}
.candle.bull .candle-body { background:#26a69a; }
.candle.bull .candle-wick { background:#26a69a; }
.candle.bear .candle-body { background:#ef5350; }
.candle.bear .candle-wick { background:#ef5350; }

/* Volume bars below candles */
.volume-area {
    height:30px; position:relative;
    border-top:1px solid #2a2e39;
    display:flex; align-items:flex-end; gap:3px;
    padding:0 8px 0; margin-right:52px;
}
.vol-bar { flex:1; border-radius:1px 1px 0 0; opacity:.3; }

/* ORDER BOOK */
.orderbook {
    width:175px; background:#1e222d;
    border-left:1px solid #2a2e39;
    display:flex; flex-direction:column;
}
.ob-header {
    padding:4px 8px; border-bottom:1px solid #2a2e39;
    display:flex; justify-content:space-between;
}
.ob-title { font-size:8px; font-weight:700; color:rgba(209,212,220,.6); text-transform:uppercase; letter-spacing:.5px; }
.ob-spread { font-size:7px; color:rgba(209,212,220,.3); }
.ob-cols {
    display:flex; justify-content:space-between; padding:2px 8px;
    font-size:6px; color:rgba(209,212,220,.2); text-transform:uppercase;
    border-bottom:1px solid rgba(42,46,57,.5);
}
.ob-asks, .ob-bids { flex:1; }
.ob-row {
    display:flex; justify-content:space-between; padding:1px 8px;
    font-size:7px; font-family:'JetBrains Mono',monospace;
    position:relative;
}
.ob-row .bg { position:absolute; top:0; bottom:0; right:0; opacity:.08; }
.ob-row.ask .price { color:#ef5350; }
.ob-row.ask .bg { background:#ef5350; }
.ob-row.bid .price { color:#26a69a; }
.ob-row.bid .bg { background:#26a69a; }
.ob-row .size { color:rgba(209,212,220,.5); }
.ob-row .total { color:rgba(209,212,220,.3); }
.ob-mid {
    padding:3px 8px; text-align:center;
    background:rgba(38,166,154,.05); border-top:1px solid #2a2e39; border-bottom:1px solid #2a2e39;
    font-size:10px; font-weight:800; color:#26a69a;
    font-family:'JetBrains Mono',monospace;
}

/* BOTTOM: Strategy KPIs */
.bottom-panel {
    height:70px;
    background:#1e222d;
    border-top:1px solid #2a2e39;
    display:flex;
}
.strategy-info {
    flex:1; padding:6px 12px;
    display:flex; flex-direction:column; justify-content:center;
}
.si-header { display:flex; align-items:center; gap:8px; margin-bottom:4px; }
.si-name { font-size:9px; font-weight:700; }
.si-status { font-size:7px; padding:1px 5px; border-radius:3px; background:rgba(38,166,154,.15); color:#26a69a; font-weight:600; }
.kpi-grid { display:flex; gap:8px; }
.kpi {
    padding:4px 8px; background:#2a2e39; border-radius:4px;
    text-align:center;
}
.kpi-val { font-size:10px; font-weight:800; }
.kpi-val.green { color:#26a69a; }
.kpi-val.red { color:#ef5350; }
.kpi-label { font-size:6px; color:rgba(209,212,220,.3); text-transform:uppercase; margin-top:1px; }
.win-streak {
    display:flex; gap:2px; margin-top:4px;
}
.ws-dot {
    width:10px; height:10px; border-radius:2px;
    display:flex; align-items:center; justify-content:center;
    font-size:5px; font-weight:800;
}
.ws-dot.w { background:rgba(38,166,154,.2); color:#26a69a; }
.ws-dot.l { background:rgba(239,83,80,.2); color:#ef5350; }
</style></head><body>

<div class="topbar">
    <div class="topbar-left">
        <div class="logo"><span class="t">Trading</span><span class="e">Engine</span></div>
        <div class="ticker">
            <span class="sym">BTC/USDT</span>
            <span class="price">67,842.50</span>
            <span class="change">+2.34%</span>
        </div>
        <div class="intervals">
            <span class="interval">1m</span><span class="interval">5m</span><span class="interval active">15m</span><span class="interval">1H</span><span class="interval">4H</span><span class="interval">1D</span>
        </div>
    </div>
    <div class="indicator-tags">
        <span class="ind-tag">EMA 20</span>
        <span class="ind-tag">RSI 14</span>
        <span class="ind-tag">MACD</span>
        <span class="ind-tag">VOL</span>
    </div>
</div>

<div class="main">
    <div class="chart-panel">
        <div class="chart-area">
            <div class="y-axis">
                <div class="y-label">68,200</div>
                <div class="y-label">68,000</div>
                <div class="y-label current">67,842</div>
                <div class="y-label">67,600</div>
                <div class="y-label">67,400</div>
                <div class="y-label">67,200</div>
                <div class="y-label">67,000</div>
            </div>
            <div class="candles">
                <div class="candle bear"><div class="candle-wick" style="height:60%;bottom:15%;"></div><div class="candle-body" style="height:35%;margin-top:auto;margin-bottom:20%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:55%;bottom:20%;"></div><div class="candle-body" style="height:30%;margin-top:auto;margin-bottom:25%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:50%;bottom:25%;"></div><div class="candle-body" style="height:25%;margin-top:auto;margin-bottom:30%;"></div></div>
                <div class="candle bear"><div class="candle-wick" style="height:65%;bottom:10%;"></div><div class="candle-body" style="height:40%;margin-top:auto;margin-bottom:15%;"></div></div>
                <div class="candle bear"><div class="candle-wick" style="height:45%;bottom:8%;"></div><div class="candle-body" style="height:30%;margin-top:auto;margin-bottom:10%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:55%;bottom:10%;"></div><div class="candle-body" style="height:35%;margin-top:auto;margin-bottom:12%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:60%;bottom:15%;"></div><div class="candle-body" style="height:30%;margin-top:auto;margin-bottom:22%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:70%;bottom:12%;"></div><div class="candle-body" style="height:40%;margin-top:auto;margin-bottom:20%;"></div></div>
                <div class="candle bear"><div class="candle-wick" style="height:50%;bottom:25%;"></div><div class="candle-body" style="height:25%;margin-top:auto;margin-bottom:30%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:65%;bottom:18%;"></div><div class="candle-body" style="height:35%;margin-top:auto;margin-bottom:22%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:75%;bottom:12%;"></div><div class="candle-body" style="height:45%;margin-top:auto;margin-bottom:18%;"></div></div>
                <div class="candle bear"><div class="candle-wick" style="height:55%;bottom:22%;"></div><div class="candle-body" style="height:28%;margin-top:auto;margin-bottom:28%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:60%;bottom:20%;"></div><div class="candle-body" style="height:30%;margin-top:auto;margin-bottom:25%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:70%;bottom:15%;"></div><div class="candle-body" style="height:40%;margin-top:auto;margin-bottom:20%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:80%;bottom:10%;"></div><div class="candle-body" style="height:45%;margin-top:auto;margin-bottom:25%;"></div></div>
                <div class="candle bear"><div class="candle-wick" style="height:50%;bottom:30%;"></div><div class="candle-body" style="height:20%;margin-top:auto;margin-bottom:35%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:65%;bottom:22%;"></div><div class="candle-body" style="height:35%;margin-top:auto;margin-bottom:25%;"></div></div>
                <div class="candle bull"><div class="candle-wick" style="height:75%;bottom:15%;"></div><div class="candle-body" style="height:42%;margin-top:auto;margin-bottom:22%;"></div></div>
            </div>
        </div>
        <div class="volume-area">
            <div class="vol-bar" style="height:40%;background:#ef5350;"></div>
            <div class="vol-bar" style="height:55%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:45%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:70%;background:#ef5350;"></div>
            <div class="vol-bar" style="height:35%;background:#ef5350;"></div>
            <div class="vol-bar" style="height:60%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:50%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:80%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:30%;background:#ef5350;"></div>
            <div class="vol-bar" style="height:65%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:90%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:45%;background:#ef5350;"></div>
            <div class="vol-bar" style="height:55%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:70%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:95%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:40%;background:#ef5350;"></div>
            <div class="vol-bar" style="height:60%;background:#26a69a;"></div>
            <div class="vol-bar" style="height:75%;background:#26a69a;"></div>
        </div>
    </div>

    <div class="orderbook">
        <div class="ob-header"><div class="ob-title">Order Book</div><div class="ob-spread">Spread: 0.02%</div></div>
        <div class="ob-cols"><span>Price</span><span>Size</span><span>Total</span></div>
        <div class="ob-asks">
            <div class="ob-row ask"><div class="bg" style="width:30%;"></div><span class="price">67,920.00</span><span class="size">2.450</span><span class="total">12.8</span></div>
            <div class="ob-row ask"><div class="bg" style="width:45%;"></div><span class="price">67,905.50</span><span class="size">3.120</span><span class="total">10.3</span></div>
            <div class="ob-row ask"><div class="bg" style="width:60%;"></div><span class="price">67,890.00</span><span class="size">5.800</span><span class="total">7.2</span></div>
            <div class="ob-row ask"><div class="bg" style="width:35%;"></div><span class="price">67,878.50</span><span class="size">1.920</span><span class="total">1.4</span></div>
            <div class="ob-row ask"><div class="bg" style="width:80%;"></div><span class="price">67,860.00</span><span class="size">8.400</span><span class="total">0.0</span></div>
        </div>
        <div class="ob-mid">67,842.50</div>
        <div class="ob-bids">
            <div class="ob-row bid"><div class="bg" style="width:75%;"></div><span class="price">67,840.00</span><span class="size">7.200</span><span class="total">0.0</span></div>
            <div class="ob-row bid"><div class="bg" style="width:50%;"></div><span class="price">67,825.50</span><span class="size">4.100</span><span class="total">7.2</span></div>
            <div class="ob-row bid"><div class="bg" style="width:40%;"></div><span class="price">67,810.00</span><span class="size">3.500</span><span class="total">11.3</span></div>
            <div class="ob-row bid"><div class="bg" style="width:65%;"></div><span class="price">67,795.00</span><span class="size">6.300</span><span class="total">14.8</span></div>
            <div class="ob-row bid"><div class="bg" style="width:25%;"></div><span class="price">67,780.00</span><span class="size">1.800</span><span class="total">21.1</span></div>
        </div>
    </div>
</div>

<div class="bottom-panel">
    <div class="strategy-info">
        <div class="si-header">
            <div class="si-name">Momentum Alpha v3.2</div>
            <div class="si-status">RUNNING</div>
        </div>
        <div class="kpi-grid">
            <div class="kpi"><div class="kpi-val green">+18.4%</div><div class="kpi-label">Total PnL</div></div>
            <div class="kpi"><div class="kpi-val green">78%</div><div class="kpi-label">Win Rate</div></div>
            <div class="kpi"><div class="kpi-val green">2.4</div><div class="kpi-label">Sharpe</div></div>
            <div class="kpi"><div class="kpi-val red">-3.2%</div><div class="kpi-label">Max DD</div></div>
            <div class="kpi"><div class="kpi-val green">1.85</div><div class="kpi-label">Profit Factor</div></div>
            <div class="kpi"><div class="kpi-val">142</div><div class="kpi-label">Trades</div></div>
        </div>
        <div class="win-streak">
            <div class="ws-dot w">W</div><div class="ws-dot w">W</div><div class="ws-dot w">W</div><div class="ws-dot l">L</div><div class="ws-dot w">W</div><div class="ws-dot w">W</div><div class="ws-dot w">W</div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# 8. SOLANA-BOT — Telegram bot control panel
# ============================================================
def html_solana_bot():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK_MONO + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#0f0b1e;
    font-family:'Inter',system-ui,sans-serif;
    color:#e0dfe8; overflow:hidden;
    display:flex;
}

/* LEFT: Wallet Panel */
.wallet-panel {
    width:210px; background:#0a0816;
    border-right:1px solid rgba(153,69,255,.1);
    display:flex; flex-direction:column;
}
.wp-header {
    padding:10px 14px;
    border-bottom:1px solid rgba(153,69,255,.1);
}
.wp-logo { font-size:14px; font-weight:800; }
.wp-logo .sol { color:#9945FF; }
.wp-logo .bot { color:#14F195; }
.wp-subtitle { font-size:8px; color:rgba(255,255,255,.3); margin-top:2px; }
.wallet-card {
    margin:10px 12px; padding:10px;
    background:linear-gradient(135deg,rgba(153,69,255,.12),rgba(20,241,149,.06));
    border:1px solid rgba(153,69,255,.2);
    border-radius:10px;
}
.wc-label { font-size:7px; text-transform:uppercase; letter-spacing:.5px; color:rgba(255,255,255,.3); margin-bottom:4px; }
.wc-balance { font-size:20px; font-weight:800; }
.wc-balance .sol-unit { color:#14F195; font-size:12px; }
.wc-usd { font-size:9px; color:rgba(255,255,255,.35); margin-top:2px; }
.wc-addr {
    margin-top:6px; padding:3px 6px;
    background:rgba(0,0,0,.3); border-radius:4px;
    font-size:7px; font-family:'JetBrains Mono',monospace;
    color:rgba(153,69,255,.7); overflow:hidden; text-overflow:ellipsis;
}
.wp-tokens { padding:8px 12px; flex:1; overflow:hidden; }
.token-title { font-size:8px; font-weight:700; color:rgba(255,255,255,.4); text-transform:uppercase; letter-spacing:.5px; margin-bottom:6px; }
.token-item {
    display:flex; justify-content:space-between; align-items:center;
    padding:5px 0;
    border-bottom:1px solid rgba(255,255,255,.03);
}
.ti-left { display:flex; align-items:center; gap:6px; }
.ti-icon {
    width:20px; height:20px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:7px; font-weight:800;
}
.ti-name { font-size:8px; font-weight:600; }
.ti-amount { font-size:8px; color:rgba(255,255,255,.4); }
.ti-right { text-align:right; }
.ti-val { font-size:8px; font-weight:700; }
.ti-change { font-size:7px; }
.ti-change.up { color:#14F195; }
.ti-change.down { color:#ef4444; }

/* CHAT AREA */
.chat-area {
    flex:1; display:flex; flex-direction:column;
    background:#100d20;
}
.chat-header {
    padding:8px 16px;
    background:rgba(153,69,255,.06);
    border-bottom:1px solid rgba(153,69,255,.1);
    display:flex; align-items:center; justify-content:space-between;
}
.ch-left { display:flex; align-items:center; gap:8px; }
.ch-avatar {
    width:28px; height:28px; border-radius:50%;
    background:linear-gradient(135deg,#9945FF,#14F195);
    display:flex; align-items:center; justify-content:center;
    font-size:9px; font-weight:800;
}
.ch-name { font-size:11px; font-weight:700; }
.ch-status { font-size:7px; color:#14F195; }
.ch-right { display:flex; gap:6px; }
.ch-btn {
    padding:3px 8px; border-radius:5px; font-size:7px; font-weight:600;
    background:rgba(153,69,255,.15); border:1px solid rgba(153,69,255,.2);
    color:#c4a0ff;
}

.messages { flex:1; padding:10px 16px; overflow:hidden; display:flex; flex-direction:column; gap:5px; }
.msg {
    padding:7px 10px; border-radius:10px; font-size:9px; line-height:1.5;
    max-width:80%;
}
.msg-user {
    align-self:flex-end;
    background:rgba(153,69,255,.2);
    border:1px solid rgba(153,69,255,.2);
    border-bottom-right-radius:4px;
    font-family:'JetBrains Mono',monospace;
    font-size:9px; color:#c4a0ff;
}
.msg-bot {
    align-self:flex-start;
    background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.06);
    border-bottom-left-radius:4px;
}
.msg-bot .label { font-size:7px; font-weight:700; color:#9945FF; margin-bottom:2px; }
.tx-hash {
    font-family:'JetBrains Mono',monospace; font-size:7px;
    color:rgba(153,69,255,.6);
    background:rgba(0,0,0,.3); padding:2px 5px; border-radius:3px;
    display:inline-block; margin-top:3px;
}
.msg-success { border-left:2px solid #14F195; }
.msg-pending { border-left:2px solid #f59e0b; }
.sol-amount { color:#14F195; font-weight:700; }
.usd-amount { color:rgba(255,255,255,.35); }

.input-bar {
    padding:8px 16px;
    background:rgba(153,69,255,.04);
    border-top:1px solid rgba(153,69,255,.1);
    display:flex; gap:6px;
}
.cmd-btn {
    padding:4px 8px; border-radius:6px; font-size:7px; font-weight:700;
    font-family:'JetBrains Mono',monospace;
    background:rgba(153,69,255,.1); border:1px solid rgba(153,69,255,.15);
    color:#c4a0ff;
}
.cmd-btn.buy { background:rgba(20,241,149,.1); border-color:rgba(20,241,149,.2); color:#14F195; }
.cmd-btn.sell { background:rgba(239,68,68,.1); border-color:rgba(239,68,68,.2); color:#ef4444; }
.input-field {
    flex:1; padding:6px 10px;
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.06);
    border-radius:8px; font-size:9px; color:rgba(255,255,255,.3);
    font-family:'JetBrains Mono',monospace;
}

/* RIGHT: Trade History */
.history-panel {
    width:195px; background:#0a0816;
    border-left:1px solid rgba(153,69,255,.1);
    display:flex; flex-direction:column;
}
.hp-header {
    padding:8px 10px;
    border-bottom:1px solid rgba(153,69,255,.1);
    font-size:9px; font-weight:700; color:rgba(255,255,255,.5);
    text-transform:uppercase; letter-spacing:.5px;
}
.hp-trades { flex:1; padding:6px 10px; overflow:hidden; }
.trade-item {
    padding:5px 0;
    border-bottom:1px solid rgba(255,255,255,.03);
}
.trade-top { display:flex; justify-content:space-between; align-items:center; }
.trade-type { font-size:7px; font-weight:700; padding:1px 4px; border-radius:3px; }
.trade-type.buy { background:rgba(20,241,149,.15); color:#14F195; }
.trade-type.sell { background:rgba(239,68,68,.15); color:#ef4444; }
.trade-pair { font-size:8px; font-weight:600; }
.trade-bottom { display:flex; justify-content:space-between; margin-top:2px; }
.trade-amount { font-size:7px; color:rgba(255,255,255,.3); }
.trade-pnl { font-size:7px; font-weight:700; }
.trade-pnl.profit { color:#14F195; }
.trade-pnl.loss { color:#ef4444; }
</style></head><body>

<div class="wallet-panel">
    <div class="wp-header">
        <div class="wp-logo"><span class="sol">Solana</span><span class="bot">Bot</span></div>
        <div class="wp-subtitle">Automated DeFi Trading</div>
    </div>
    <div class="wallet-card">
        <div class="wc-label">Wallet Balance</div>
        <div class="wc-balance">24.87 <span class="sol-unit">SOL</span></div>
        <div class="wc-usd">~$4,215.90 USD</div>
        <div class="wc-addr">7xKX...3mFz</div>
    </div>
    <div class="wp-tokens">
        <div class="token-title">Holdings</div>
        <div class="token-item">
            <div class="ti-left"><div class="ti-icon" style="background:linear-gradient(135deg,#9945FF,#7b2ff2);">R</div><div><div class="ti-name">RAY</div><div class="ti-amount">1,245.00</div></div></div>
            <div class="ti-right"><div class="ti-val">$3,240</div><div class="ti-change up">+12.4%</div></div>
        </div>
        <div class="token-item">
            <div class="ti-left"><div class="ti-icon" style="background:linear-gradient(135deg,#2775ca,#1a5fa0);">U</div><div><div class="ti-name">USDC</div><div class="ti-amount">5,000.00</div></div></div>
            <div class="ti-right"><div class="ti-val">$5,000</div><div class="ti-change up">+0.0%</div></div>
        </div>
        <div class="token-item">
            <div class="ti-left"><div class="ti-icon" style="background:linear-gradient(135deg,#e84142,#c23132);">B</div><div><div class="ti-name">BONK</div><div class="ti-amount">8.4M</div></div></div>
            <div class="ti-right"><div class="ti-val">$420</div><div class="ti-change down">-5.2%</div></div>
        </div>
        <div class="token-item">
            <div class="ti-left"><div class="ti-icon" style="background:linear-gradient(135deg,#14F195,#0bc080);">J</div><div><div class="ti-name">JTO</div><div class="ti-amount">320.00</div></div></div>
            <div class="ti-right"><div class="ti-val">$896</div><div class="ti-change up">+8.7%</div></div>
        </div>
    </div>
</div>

<div class="chat-area">
    <div class="chat-header">
        <div class="ch-left">
            <div class="ch-avatar">SB</div>
            <div><div class="ch-name">SolanaBot Console</div><div class="ch-status">Connected to Mainnet</div></div>
        </div>
        <div class="ch-right">
            <div class="ch-btn">Settings</div>
            <div class="ch-btn">Logs</div>
        </div>
    </div>
    <div class="messages">
        <div class="msg msg-user">/buy RAY 100 --slippage 1%</div>
        <div class="msg msg-bot msg-success">
            <div class="label">Trade Executed</div>
            Bought <span class="sol-amount">100 RAY</span> at $2.604 <span class="usd-amount">($260.40)</span><br>
            Paid <span class="sol-amount">1.54 SOL</span> | Slippage: 0.3%
            <div class="tx-hash">TX: 4rVk...8mPx</div>
        </div>
        <div class="msg msg-user">/balance</div>
        <div class="msg msg-bot">
            <div class="label">Wallet Summary</div>
            SOL: <span class="sol-amount">24.87</span> (~$4,215.90)<br>
            RAY: <span class="sol-amount">1,245.00</span> (~$3,240.00)<br>
            USDC: <span class="sol-amount">5,000.00</span><br>
            Total: <span class="sol-amount">$12,875.90</span>
        </div>
        <div class="msg msg-user">/sell BONK 2000000 --limit 0.000055</div>
        <div class="msg msg-bot msg-pending">
            <div class="label">Limit Order Placed</div>
            Sell <span class="sol-amount">2,000,000 BONK</span> at $0.000055<br>
            Status: Pending | Expires in 24h
            <div class="tx-hash">Order: Lm9Q...7kXn</div>
        </div>
        <div class="msg msg-user">/snipe --token NEW_MINT --amount 2 --auto</div>
    </div>
    <div class="input-bar">
        <div class="cmd-btn buy">/buy</div>
        <div class="cmd-btn sell">/sell</div>
        <div class="cmd-btn">/snipe</div>
        <div class="cmd-btn">/dca</div>
        <div class="input-field">Enter command...</div>
    </div>
</div>

<div class="history-panel">
    <div class="hp-header">Recent Trades</div>
    <div class="hp-trades">
        <div class="trade-item">
            <div class="trade-top"><div class="trade-type buy">BUY</div><div class="trade-pair">RAY/SOL</div></div>
            <div class="trade-bottom"><div class="trade-amount">100 RAY @ $2.604</div><div class="trade-pnl profit">+$31.20</div></div>
        </div>
        <div class="trade-item">
            <div class="trade-top"><div class="trade-type sell">SELL</div><div class="trade-pair">JTO/SOL</div></div>
            <div class="trade-bottom"><div class="trade-amount">50 JTO @ $2.80</div><div class="trade-pnl profit">+$18.50</div></div>
        </div>
        <div class="trade-item">
            <div class="trade-top"><div class="trade-type buy">BUY</div><div class="trade-pair">BONK/SOL</div></div>
            <div class="trade-bottom"><div class="trade-amount">5M BONK @ $0.00005</div><div class="trade-pnl loss">-$12.00</div></div>
        </div>
        <div class="trade-item">
            <div class="trade-top"><div class="trade-type sell">SELL</div><div class="trade-pair">WIF/SOL</div></div>
            <div class="trade-bottom"><div class="trade-amount">200 WIF @ $1.82</div><div class="trade-pnl profit">+$64.00</div></div>
        </div>
        <div class="trade-item">
            <div class="trade-top"><div class="trade-type buy">BUY</div><div class="trade-pair">ORCA/SOL</div></div>
            <div class="trade-bottom"><div class="trade-amount">80 ORCA @ $4.10</div><div class="trade-pnl profit">+$22.40</div></div>
        </div>
        <div class="trade-item">
            <div class="trade-top"><div class="trade-type sell">SELL</div><div class="trade-pair">MNGO/SOL</div></div>
            <div class="trade-bottom"><div class="trade-amount">500 MNGO @ $0.058</div><div class="trade-pnl loss">-$4.50</div></div>
        </div>
        <div class="trade-item">
            <div class="trade-top"><div class="trade-type buy">BUY</div><div class="trade-pair">PYTH/SOL</div></div>
            <div class="trade-bottom"><div class="trade-amount">300 PYTH @ $0.42</div><div class="trade-pnl profit">+$9.60</div></div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# 9. GUIDEDGROWTH — Meeting intelligence dashboard (light theme)
# ============================================================
def html_guidedgrowth():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#f8faf9;
    font-family:'Inter',system-ui,sans-serif;
    color:#1a2e1a; overflow:hidden;
    display:flex; flex-direction:column;
}

/* NAV */
.nav {
    display:flex; align-items:center; justify-content:space-between;
    padding:8px 20px;
    background:#fff;
    border-bottom:1px solid #e5ebe5;
    box-shadow:0 1px 3px rgba(0,0,0,.03);
}
.logo { font-size:14px; font-weight:800; letter-spacing:-.3px; }
.logo .g { color:#22c55e; }
.nav-links { display:flex; gap:16px; }
.nav-links a { font-size:9px; color:#6b8f6b; text-decoration:none; font-weight:500; }
.nav-links a.active { color:#16a34a; font-weight:600; }
.nav-right { display:flex; gap:8px; align-items:center; }
.nav-avatar {
    width:26px; height:26px; border-radius:50%;
    background:linear-gradient(135deg,#22c55e,#16a34a);
}

/* MAIN */
.main { display:flex; flex:1; padding:12px 20px; gap:14px; overflow:hidden; }

/* LEFT: Recording */
.recording-panel {
    width:300px; display:flex; flex-direction:column; gap:10px;
}
.rec-card {
    background:#fff; border:1px solid #e5ebe5; border-radius:10px;
    padding:12px; box-shadow:0 1px 4px rgba(0,0,0,.04);
}
.rec-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; }
.rec-title { font-size:11px; font-weight:700; }
.rec-badge {
    padding:2px 8px; border-radius:4px; font-size:7px; font-weight:600;
    background:rgba(34,197,94,.1); color:#16a34a;
}
.rec-meeting-name { font-size:13px; font-weight:700; margin-bottom:4px; }
.rec-meta { font-size:8px; color:#6b8f6b; margin-bottom:8px; }
.waveform {
    display:flex; align-items:center; gap:1px; height:32px;
    margin-bottom:8px;
}
.wave-bar {
    flex:1; border-radius:2px;
    background:linear-gradient(180deg,#22c55e,#16a34a);
    opacity:.6;
}
.rec-controls {
    display:flex; align-items:center; gap:8px;
}
.play-btn {
    width:28px; height:28px; border-radius:50%;
    background:#22c55e; display:flex; align-items:center; justify-content:center;
    box-shadow:0 2px 6px rgba(34,197,94,.3);
}
.play-btn::after {
    content:''; width:0; height:0;
    border-left:10px solid #fff;
    border-top:6px solid transparent;
    border-bottom:6px solid transparent;
    margin-left:2px;
}
.rec-time { font-size:9px; color:#6b8f6b; font-weight:500; }
.rec-progress {
    flex:1; height:3px; background:#e5ebe5; border-radius:2px; position:relative;
}
.rec-progress .fill { position:absolute; left:0; top:0; height:100%; width:65%; background:#22c55e; border-radius:2px; }

/* Transcript */
.transcript-card {
    background:#fff; border:1px solid #e5ebe5; border-radius:10px;
    padding:12px; flex:1; overflow:hidden;
    box-shadow:0 1px 4px rgba(0,0,0,.04);
}
.transcript-title { font-size:10px; font-weight:700; margin-bottom:8px; }
.transcript-line {
    display:flex; gap:6px; margin-bottom:6px;
}
.tl-time { font-size:7px; color:#9cb89c; width:30px; flex-shrink:0; margin-top:1px; }
.tl-speaker { font-size:8px; font-weight:700; width:50px; flex-shrink:0; }
.tl-text { font-size:8px; color:#4a6b4a; line-height:1.4; }
.tl-highlight { background:rgba(34,197,94,.1); padding:0 2px; border-radius:2px; }

/* RIGHT: Actions & Insights */
.right-panel {
    flex:1; display:flex; flex-direction:column; gap:10px;
}

/* Action Items */
.actions-card {
    background:#fff; border:1px solid #e5ebe5; border-radius:10px;
    padding:12px; box-shadow:0 1px 4px rgba(0,0,0,.04);
}
.ac-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; }
.ac-title { font-size:10px; font-weight:700; }
.ac-count { font-size:8px; color:#16a34a; font-weight:600; }
.action-item {
    display:flex; align-items:flex-start; gap:6px;
    padding:5px 0; border-bottom:1px solid #f0f5f0;
}
.ai-checkbox {
    width:14px; height:14px; border-radius:4px;
    border:1.5px solid #c5d8c5; flex-shrink:0; margin-top:1px;
}
.ai-checkbox.done { background:#22c55e; border-color:#22c55e; }
.ai-content { flex:1; }
.ai-text { font-size:9px; font-weight:500; color:#1a2e1a; }
.ai-text.done { text-decoration:line-through; color:#9cb89c; }
.ai-meta { display:flex; gap:6px; margin-top:2px; }
.ai-assignee {
    font-size:7px; font-weight:600; padding:1px 5px; border-radius:3px;
    background:rgba(34,197,94,.1); color:#16a34a;
}
.ai-due { font-size:7px; color:#9cb89c; }
.ai-priority {
    font-size:6px; font-weight:700; padding:1px 4px; border-radius:2px;
}
.priority-high { background:rgba(239,68,68,.1); color:#ef4444; }
.priority-med { background:rgba(245,158,11,.1); color:#f59e0b; }

/* Insights */
.insights {
    display:grid; grid-template-columns:repeat(2,1fr); gap:8px; flex:1;
}
.insight-card {
    background:#fff; border:1px solid #e5ebe5; border-radius:10px;
    padding:10px; box-shadow:0 1px 4px rgba(0,0,0,.04);
}
.ic-label { font-size:7px; text-transform:uppercase; letter-spacing:.5px; color:#9cb89c; font-weight:600; margin-bottom:4px; }
.ic-val { font-size:16px; font-weight:800; color:#1a2e1a; }
.ic-val .accent { color:#22c55e; }
.ic-desc { font-size:7px; color:#6b8f6b; margin-top:2px; }
.ic-bar { height:4px; background:#e5ebe5; border-radius:2px; margin-top:4px; overflow:hidden; }
.ic-bar .fill { height:100%; background:linear-gradient(90deg,#22c55e,#16a34a); border-radius:2px; }

/* Sentiment dots */
.sentiment-row { display:flex; gap:2px; margin-top:4px; }
.sent-dot { width:8px; height:8px; border-radius:50%; }
</style></head><body>

<div class="nav">
    <div class="logo"><span class="g">Guided</span>Growth</div>
    <div class="nav-links">
        <a class="active">Meetings</a><a>Dashboard</a><a>Team</a><a>Reports</a>
    </div>
    <div class="nav-right"><div class="nav-avatar"></div></div>
</div>

<div class="main">
    <div class="recording-panel">
        <div class="rec-card">
            <div class="rec-header">
                <div class="rec-title">Recording</div>
                <div class="rec-badge">AI Processing</div>
            </div>
            <div class="rec-meeting-name">Q1 Sprint Review</div>
            <div class="rec-meta">Mar 18, 2026 -- 10:00 AM -- 4 participants</div>
            <div class="waveform">
                <div class="wave-bar" style="height:30%;"></div><div class="wave-bar" style="height:60%;"></div><div class="wave-bar" style="height:45%;"></div><div class="wave-bar" style="height:80%;"></div><div class="wave-bar" style="height:35%;"></div><div class="wave-bar" style="height:90%;"></div><div class="wave-bar" style="height:50%;"></div><div class="wave-bar" style="height:70%;"></div><div class="wave-bar" style="height:25%;"></div><div class="wave-bar" style="height:85%;"></div><div class="wave-bar" style="height:55%;"></div><div class="wave-bar" style="height:40%;"></div><div class="wave-bar" style="height:75%;"></div><div class="wave-bar" style="height:65%;"></div><div class="wave-bar" style="height:30%;"></div><div class="wave-bar" style="height:95%;"></div><div class="wave-bar" style="height:50%;"></div><div class="wave-bar" style="height:60%;"></div><div class="wave-bar" style="height:35%;"></div><div class="wave-bar" style="height:70%;"></div><div class="wave-bar" style="height:45%;"></div><div class="wave-bar" style="height:80%;"></div><div class="wave-bar" style="height:55%;"></div><div class="wave-bar" style="height:40%;"></div><div class="wave-bar" style="height:65%;"></div>
            </div>
            <div class="rec-controls">
                <div class="play-btn"></div>
                <div class="rec-time">32:15 / 49:30</div>
                <div class="rec-progress"><div class="fill"></div></div>
            </div>
        </div>
        <div class="transcript-card">
            <div class="transcript-title">Live Transcript</div>
            <div class="transcript-line"><div class="tl-time">32:10</div><div class="tl-speaker" style="color:#3b82f6;">Sarah</div><div class="tl-text">The <span class="tl-highlight">API migration</span> is 80% complete. We need two more days for testing.</div></div>
            <div class="transcript-line"><div class="tl-time">32:18</div><div class="tl-speaker" style="color:#22c55e;">Mike</div><div class="tl-text">I can help with the <span class="tl-highlight">integration tests</span> tomorrow morning.</div></div>
            <div class="transcript-line"><div class="tl-time">32:25</div><div class="tl-speaker" style="color:#f59e0b;">Lisa</div><div class="tl-text">We should also update the <span class="tl-highlight">documentation</span> before the release.</div></div>
            <div class="transcript-line"><div class="tl-time">32:32</div><div class="tl-speaker" style="color:#ef4444;">James</div><div class="tl-text">Agreed. I will <span class="tl-highlight">create the deployment checklist</span> by end of day.</div></div>
        </div>
    </div>

    <div class="right-panel">
        <div class="actions-card">
            <div class="ac-header"><div class="ac-title">AI-Extracted Action Items</div><div class="ac-count">6 items</div></div>
            <div class="action-item">
                <div class="ai-checkbox done"></div>
                <div class="ai-content"><div class="ai-text done">Set up staging environment</div><div class="ai-meta"><div class="ai-assignee">Sarah</div><div class="ai-due">Completed</div></div></div>
            </div>
            <div class="action-item">
                <div class="ai-checkbox"></div>
                <div class="ai-content"><div class="ai-text">Complete API migration testing</div><div class="ai-meta"><div class="ai-assignee">Sarah</div><div class="ai-due">Due: Mar 20</div><div class="ai-priority priority-high">HIGH</div></div></div>
            </div>
            <div class="action-item">
                <div class="ai-checkbox"></div>
                <div class="ai-content"><div class="ai-text">Write integration test suite</div><div class="ai-meta"><div class="ai-assignee">Mike</div><div class="ai-due">Due: Mar 19</div><div class="ai-priority priority-high">HIGH</div></div></div>
            </div>
            <div class="action-item">
                <div class="ai-checkbox"></div>
                <div class="ai-content"><div class="ai-text">Update API documentation</div><div class="ai-meta"><div class="ai-assignee">Lisa</div><div class="ai-due">Due: Mar 21</div><div class="ai-priority priority-med">MED</div></div></div>
            </div>
            <div class="action-item">
                <div class="ai-checkbox"></div>
                <div class="ai-content"><div class="ai-text">Create deployment checklist</div><div class="ai-meta"><div class="ai-assignee">James</div><div class="ai-due">Due: Mar 18</div><div class="ai-priority priority-high">HIGH</div></div></div>
            </div>
        </div>
        <div class="insights">
            <div class="insight-card">
                <div class="ic-label">Meeting Duration</div>
                <div class="ic-val">49<span class="accent">min</span></div>
                <div class="ic-desc">12% shorter than average</div>
                <div class="ic-bar"><div class="fill" style="width:72%;"></div></div>
            </div>
            <div class="insight-card">
                <div class="ic-label">Talk Ratio</div>
                <div class="ic-val">Well <span class="accent">Balanced</span></div>
                <div class="ic-desc">No single speaker above 35%</div>
                <div class="sentiment-row">
                    <div class="sent-dot" style="background:#3b82f6; width:28%;height:6px;border-radius:3px;"></div>
                    <div class="sent-dot" style="background:#22c55e; width:26%;height:6px;border-radius:3px;"></div>
                    <div class="sent-dot" style="background:#f59e0b; width:24%;height:6px;border-radius:3px;"></div>
                    <div class="sent-dot" style="background:#ef4444; width:22%;height:6px;border-radius:3px;"></div>
                </div>
            </div>
            <div class="insight-card">
                <div class="ic-label">Engagement Score</div>
                <div class="ic-val">92<span class="accent">%</span></div>
                <div class="ic-desc">Top 10% across all meetings</div>
                <div class="ic-bar"><div class="fill" style="width:92%;"></div></div>
            </div>
            <div class="insight-card">
                <div class="ic-label">Topics Covered</div>
                <div class="ic-val">8 <span class="accent">topics</span></div>
                <div class="ic-desc">API, Testing, Docs, Deploy...</div>
                <div class="ic-bar"><div class="fill" style="width:80%;"></div></div>
            </div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# 10. CF-BYPASS — Hacker terminal aesthetic
# ============================================================
def html_cf_bypass():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK_MONO + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#000;
    font-family:'JetBrains Mono',monospace;
    color:#00ff41; overflow:hidden;
    position:relative;
}
body::before {
    content:''; position:absolute; inset:0;
    background:
        repeating-linear-gradient(
            0deg,
            rgba(0,255,65,.03) 0px,
            rgba(0,255,65,.03) 1px,
            transparent 1px,
            transparent 3px
        );
    pointer-events:none; z-index:10;
}
body::after {
    content:''; position:absolute; inset:0;
    background:radial-gradient(ellipse at 50% 50%, transparent 60%, rgba(0,0,0,.4) 100%);
    pointer-events:none; z-index:11;
}

.layout {
    display:grid;
    grid-template-columns:1fr 1fr;
    grid-template-rows:auto 1fr 1fr;
    gap:4px;
    padding:4px;
    height:100%;
    position:relative; z-index:2;
}

/* STATUS BAR */
.status-bar {
    grid-column:1/3;
    display:flex; justify-content:space-between; align-items:center;
    padding:4px 10px;
    background:rgba(0,255,65,.06);
    border:1px solid rgba(0,255,65,.15);
}
.sb-left { display:flex; gap:12px; font-size:8px; }
.sb-label { color:rgba(0,255,65,.4); }
.sb-val { color:#00ff41; font-weight:700; }
.sb-right { display:flex; gap:10px; font-size:8px; }
.status-dot { display:inline-block; width:6px; height:6px; border-radius:50%; margin-right:3px; }
.dot-green { background:#00ff41; box-shadow:0 0 6px #00ff41; }
.dot-yellow { background:#ffff00; box-shadow:0 0 6px #ffff00; }

/* TERMINAL WINDOW */
.terminal {
    background:rgba(0,10,2,.8);
    border:1px solid rgba(0,255,65,.15);
    border-radius:3px;
    display:flex; flex-direction:column;
    overflow:hidden;
}
.term-header {
    padding:3px 8px;
    background:rgba(0,255,65,.08);
    border-bottom:1px solid rgba(0,255,65,.1);
    display:flex; justify-content:space-between; align-items:center;
}
.term-title { font-size:8px; color:rgba(0,255,65,.6); font-weight:700; }
.term-dots { display:flex; gap:4px; }
.term-dot { width:7px; height:7px; border-radius:50%; }
.term-body {
    padding:6px 8px; flex:1; overflow:hidden;
    font-size:7px; line-height:1.6;
}

/* Colors */
.green { color:#00ff41; }
.dim { color:rgba(0,255,65,.35); }
.bright { color:#00ff41; font-weight:700; text-shadow:0 0 4px rgba(0,255,65,.3); }
.red { color:#ff3333; }
.yellow { color:#ffff00; }
.cyan { color:#00ffff; }
.white { color:#ccc; }
.orange { color:#ff8800; }
.purple { color:#cc44ff; }
.prompt { color:#00ff41; }
.comment { color:rgba(0,255,65,.25); }

.line { white-space:nowrap; }
.indent { padding-left:16px; }

/* HTTP Log specific */
.method { color:#00ffff; font-weight:700; }
.url { color:rgba(0,255,65,.6); }
.status-200 { color:#00ff41; font-weight:700; }
.status-403 { color:#ff3333; font-weight:700; }
.status-301 { color:#ffff00; }
.header-key { color:#cc44ff; }
.header-val { color:rgba(0,255,65,.5); }
</style></head><body>

<div class="layout">
    <div class="status-bar">
        <div class="sb-left">
            <span><span class="sb-label">TARGET:</span> <span class="sb-val">cloudflare-protected.com</span></span>
            <span><span class="sb-label">MODE:</span> <span class="sb-val">STEALTH</span></span>
            <span><span class="sb-label">PROXY:</span> <span class="sb-val">ROTATING (847)</span></span>
        </div>
        <div class="sb-right">
            <span><span class="status-dot dot-green"></span>Engine Active</span>
            <span><span class="status-dot dot-yellow"></span>Rate: 12 req/s</span>
        </div>
    </div>

    <!-- Terminal 1: HTTP Request Log -->
    <div class="terminal">
        <div class="term-header">
            <div class="term-title">HTTP REQUEST LOG</div>
            <div class="term-dots"><div class="term-dot" style="background:#ff3333;"></div><div class="term-dot" style="background:#ffff00;"></div><div class="term-dot" style="background:#00ff41;"></div></div>
        </div>
        <div class="term-body">
            <div class="line"><span class="dim">[14:32:01]</span> <span class="method">GET</span> <span class="url">/api/data</span> <span class="status-403">403</span> <span class="dim">Blocked</span></div>
            <div class="line"><span class="dim">[14:32:02]</span> <span class="yellow">Rotating fingerprint...</span></div>
            <div class="line"><span class="dim">[14:32:03]</span> <span class="method">GET</span> <span class="url">/api/data</span> <span class="status-403">403</span> <span class="dim">Challenge</span></div>
            <div class="line"><span class="dim">[14:32:04]</span> <span class="cyan">Solving JS challenge...</span></div>
            <div class="line"><span class="dim">[14:32:05]</span> <span class="bright">Challenge solved (1247ms)</span></div>
            <div class="line"><span class="dim">[14:32:06]</span> <span class="method">GET</span> <span class="url">/api/data</span> <span class="status-200">200</span> <span class="bright">OK (847b)</span></div>
            <div class="line"><span class="dim">[14:32:07]</span> <span class="method">GET</span> <span class="url">/api/users</span> <span class="status-200">200</span> <span class="bright">OK (2.1kb)</span></div>
            <div class="line"><span class="dim">[14:32:08]</span> <span class="method">POST</span> <span class="url">/api/auth</span> <span class="status-200">200</span> <span class="bright">OK (412b)</span></div>
            <div class="line"><span class="dim">[14:32:09]</span> <span class="method">GET</span> <span class="url">/api/products</span> <span class="status-403">403</span> <span class="dim">Rate limit</span></div>
            <div class="line"><span class="dim">[14:32:10]</span> <span class="yellow">Switching proxy: 185.x.x.42</span></div>
            <div class="line"><span class="dim">[14:32:11]</span> <span class="method">GET</span> <span class="url">/api/products</span> <span class="status-200">200</span> <span class="bright">OK (5.4kb)</span></div>
            <div class="line"><span class="prompt">$</span> <span class="bright" style="animation:none;">_</span></div>
        </div>
    </div>

    <!-- Terminal 2: Response Headers -->
    <div class="terminal">
        <div class="term-header">
            <div class="term-title">RESPONSE HEADERS</div>
            <div class="term-dots"><div class="term-dot" style="background:#ff3333;"></div><div class="term-dot" style="background:#ffff00;"></div><div class="term-dot" style="background:#00ff41;"></div></div>
        </div>
        <div class="term-body">
            <div class="line"><span class="bright">HTTP/1.1 200 OK</span></div>
            <div class="line"><span class="header-key">server:</span> <span class="header-val">cloudflare</span></div>
            <div class="line"><span class="header-key">cf-ray:</span> <span class="header-val">8a2f3b4c5d6e7f-LAX</span></div>
            <div class="line"><span class="header-key">cf-cache-status:</span> <span class="header-val">DYNAMIC</span></div>
            <div class="line"><span class="header-key">content-type:</span> <span class="header-val">application/json</span></div>
            <div class="line"><span class="header-key">x-request-id:</span> <span class="header-val">a7b3c9d2-e4f5-6789</span></div>
            <div class="line"><span class="header-key">cf-mitigated:</span> <span class="red">challenge</span></div>
            <div class="line"><span class="header-key">set-cookie:</span> <span class="header-val">cf_clearance=eyJ...;path=/</span></div>
            <div class="line"><span class="header-key">alt-svc:</span> <span class="header-val">h3=":443"; ma=86400</span></div>
            <div class="line dim">---</div>
            <div class="line"><span class="cyan">Clearance cookie extracted</span></div>
            <div class="line"><span class="bright">Session valid for 1800s</span></div>
        </div>
    </div>

    <!-- Terminal 3: Browser Fingerprint -->
    <div class="terminal">
        <div class="term-header">
            <div class="term-title">BROWSER FINGERPRINT</div>
            <div class="term-dots"><div class="term-dot" style="background:#ff3333;"></div><div class="term-dot" style="background:#ffff00;"></div><div class="term-dot" style="background:#00ff41;"></div></div>
        </div>
        <div class="term-body">
            <div class="line"><span class="comment"># Active fingerprint config</span></div>
            <div class="line"><span class="purple">user_agent:</span> <span class="dim">Chrome/122.0.6261.94</span></div>
            <div class="line"><span class="purple">platform:</span> <span class="dim">Win32</span></div>
            <div class="line"><span class="purple">screen:</span> <span class="dim">1920x1080 @24bit</span></div>
            <div class="line"><span class="purple">webgl_vendor:</span> <span class="dim">Google Inc. (NVIDIA)</span></div>
            <div class="line"><span class="purple">canvas_hash:</span> <span class="dim">a7f3b2c8d9e4</span></div>
            <div class="line"><span class="purple">timezone:</span> <span class="dim">America/Los_Angeles</span></div>
            <div class="line"><span class="purple">languages:</span> <span class="dim">en-US,en</span></div>
            <div class="line"><span class="purple">plugins:</span> <span class="dim">[PDF,Chrome PDF]</span></div>
            <div class="line"><span class="purple">webrtc:</span> <span class="red">DISABLED</span></div>
            <div class="line"><span class="purple">tls_ja3:</span> <span class="dim">771,4865-4866-4867...</span></div>
            <div class="line"><span class="bright">Entropy score: 0.94 (human-like)</span></div>
        </div>
    </div>

    <!-- Terminal 4: Stats -->
    <div class="terminal">
        <div class="term-header">
            <div class="term-title">SESSION STATISTICS</div>
            <div class="term-dots"><div class="term-dot" style="background:#ff3333;"></div><div class="term-dot" style="background:#ffff00;"></div><div class="term-dot" style="background:#00ff41;"></div></div>
        </div>
        <div class="term-body">
            <div class="line"><span class="comment"># Session: 2026-03-18T14:30:00Z</span></div>
            <div class="line"><span class="dim">Total Requests:</span>  <span class="bright">2,847</span></div>
            <div class="line"><span class="dim">Successful:</span>     <span class="bright">2,691</span> <span class="green">(94.5%)</span></div>
            <div class="line"><span class="dim">Blocked:</span>        <span class="red">156</span> <span class="red">(5.5%)</span></div>
            <div class="line"><span class="dim">Challenges:</span>     <span class="yellow">89 solved</span></div>
            <div class="line"><span class="dim">Avg Latency:</span>    <span class="cyan">247ms</span></div>
            <div class="line"><span class="dim">Proxies Used:</span>   <span class="bright">42</span></div>
            <div class="line"><span class="dim">Data Scraped:</span>   <span class="bright">18.4 MB</span></div>
            <div class="line dim">---</div>
            <div class="line"><span class="dim">Bypass Rate:</span>    <span class="bright">94.5%</span> <span class="green">EXCELLENT</span></div>
            <div class="line"><span class="dim">Uptime:</span>         <span class="bright">4h 02m 18s</span></div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# 11. SHOPIFYCLONE — E-commerce storefront (light theme)
# ============================================================
def html_shopifyclone():
    return '''<!DOCTYPE html>
<html><head>
''' + FONT_LINK + '''
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    width:800px; height:450px;
    background:#fafaf9;
    font-family:'Inter',system-ui,sans-serif;
    color:#292524; overflow:hidden;
    display:flex; flex-direction:column;
}

/* NAV */
.nav {
    display:flex; align-items:center; justify-content:space-between;
    padding:8px 24px;
    background:#fff;
    border-bottom:1px solid #e7e5e4;
    box-shadow:0 1px 3px rgba(0,0,0,.04);
}
.logo { font-size:16px; font-weight:800; letter-spacing:-.5px; }
.logo .sh { color:#ea580c; }
.nav-center { display:flex; gap:18px; }
.nav-center a { font-size:10px; color:#78716c; text-decoration:none; font-weight:500; }
.nav-center a.active { color:#ea580c; font-weight:600; }
.nav-right { display:flex; gap:10px; align-items:center; }
.search-box {
    padding:5px 12px; background:#f5f5f4;
    border:1px solid #e7e5e4; border-radius:8px;
    font-size:9px; color:#a8a29e; width:140px;
}
.cart-btn {
    position:relative; padding:5px 10px;
    background:rgba(234,88,12,.08); border:1px solid rgba(234,88,12,.15);
    border-radius:8px; font-size:9px; font-weight:600; color:#ea580c;
}
.cart-badge {
    position:absolute; top:-4px; right:-4px;
    width:14px; height:14px; border-radius:50%;
    background:#ea580c; color:#fff; font-size:7px; font-weight:700;
    display:flex; align-items:center; justify-content:center;
}

/* HERO BANNER */
.hero {
    padding:18px 24px;
    background:linear-gradient(135deg,#ea580c 0%,#f97316 40%,#fb923c 70%,#fdba74 100%);
    position:relative; overflow:hidden;
}
.hero::before {
    content:''; position:absolute; top:-20px; right:40px;
    width:200px; height:200px;
    background:radial-gradient(circle,rgba(255,255,255,.15) 0%,transparent 70%);
    border-radius:50%;
}
.hero::after {
    content:''; position:absolute; bottom:-30px; left:200px;
    width:150px; height:150px;
    background:radial-gradient(circle,rgba(255,255,255,.1) 0%,transparent 70%);
    border-radius:50%;
}
.hero-content { position:relative; z-index:1; display:flex; justify-content:space-between; align-items:center; }
.hero-text h1 {
    font-size:22px; font-weight:800; color:#fff; line-height:1.2;
    letter-spacing:-.5px;
}
.hero-text p { font-size:10px; color:rgba(255,255,255,.8); margin-top:4px; }
.hero-cta {
    display:inline-block; margin-top:8px; padding:6px 18px;
    background:#fff; color:#ea580c; font-size:10px; font-weight:700;
    border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,.15);
}
.hero-stats { display:flex; gap:16px; }
.hero-stat { text-align:center; }
.hero-stat .hs-val { font-size:18px; font-weight:800; color:#fff; }
.hero-stat .hs-label { font-size:8px; color:rgba(255,255,255,.7); }

/* CATEGORIES */
.categories {
    display:flex; gap:6px; padding:10px 24px;
    border-bottom:1px solid #f0eeec;
}
.cat-pill {
    padding:4px 12px; border-radius:20px;
    font-size:8px; font-weight:600;
    background:#f5f5f4; color:#78716c;
    border:1px solid #e7e5e4;
}
.cat-pill.active { background:#ea580c; color:#fff; border-color:#ea580c; }

/* PRODUCTS */
.products-section { padding:10px 24px; flex:1; }
.section-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; }
.section-title { font-size:12px; font-weight:700; }
.view-all { font-size:9px; color:#ea580c; font-weight:600; }
.products-grid {
    display:grid; grid-template-columns:repeat(4,1fr); gap:12px;
}
.product-card {
    background:#fff; border:1px solid #e7e5e4;
    border-radius:12px; overflow:hidden;
    box-shadow:0 1px 4px rgba(0,0,0,.04);
    position:relative;
}
.product-image {
    height:100px; position:relative;
    display:flex; align-items:center; justify-content:center;
    overflow:hidden;
}
.product-image::after {
    content:''; position:absolute; inset:0;
    background:linear-gradient(180deg,transparent 60%,rgba(0,0,0,.05) 100%);
}
.product-badge {
    position:absolute; top:6px; left:6px; z-index:2;
    padding:2px 6px; border-radius:4px;
    font-size:7px; font-weight:700; color:#fff;
}
.badge-sale { background:#ea580c; }
.badge-new { background:#16a34a; }
.badge-trending { background:#8b5cf6; }
.product-body { padding:8px 10px; }
.product-name { font-size:10px; font-weight:600; color:#292524; margin-bottom:2px; }
.product-desc { font-size:7px; color:#a8a29e; margin-bottom:4px; }
.product-footer { display:flex; justify-content:space-between; align-items:center; }
.product-price { font-size:12px; font-weight:800; color:#ea580c; }
.product-price .old { font-size:8px; color:#a8a29e; text-decoration:line-through; margin-left:4px; font-weight:400; }
.add-btn {
    padding:4px 10px; border-radius:6px;
    background:#ea580c; color:#fff;
    font-size:8px; font-weight:700;
    box-shadow:0 2px 4px rgba(234,88,12,.2);
}
.stars { display:flex; gap:1px; margin-bottom:3px; }
.star { width:8px; height:8px; clip-path:polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); }
.star.filled { background:#f59e0b; }
.star.empty { background:#e7e5e4; }
</style></head><body>

<div class="nav">
    <div class="logo"><span class="sh">Shopify</span>Clone</div>
    <div class="nav-center">
        <a class="active">Shop</a><a>Collections</a><a>New Arrivals</a><a>Sale</a><a>About</a>
    </div>
    <div class="nav-right">
        <div class="search-box">Search products...</div>
        <div class="cart-btn">Cart<div class="cart-badge">3</div></div>
    </div>
</div>

<div class="hero">
    <div class="hero-content">
        <div class="hero-text">
            <h1>Summer Sale<br>Up to 50% Off</h1>
            <p>Limited time offer on our best-selling collections</p>
            <div class="hero-cta">Shop Now</div>
        </div>
        <div class="hero-stats">
            <div class="hero-stat"><div class="hs-val">2.4K</div><div class="hs-label">Products</div></div>
            <div class="hero-stat"><div class="hs-val">150+</div><div class="hs-label">Brands</div></div>
            <div class="hero-stat"><div class="hs-val">Free</div><div class="hs-label">Shipping</div></div>
        </div>
    </div>
</div>

<div class="categories">
    <div class="cat-pill active">All</div>
    <div class="cat-pill">Electronics</div>
    <div class="cat-pill">Clothing</div>
    <div class="cat-pill">Home</div>
    <div class="cat-pill">Sports</div>
    <div class="cat-pill">Books</div>
    <div class="cat-pill">Beauty</div>
</div>

<div class="products-section">
    <div class="section-header">
        <div class="section-title">Trending Now</div>
        <div class="view-all">View all</div>
    </div>
    <div class="products-grid">
        <div class="product-card">
            <div class="product-image" style="background:linear-gradient(135deg,#fecdd3,#fda4af,#fb7185);">
                <div class="product-badge badge-sale">-30%</div>
            </div>
            <div class="product-body">
                <div class="stars"><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div></div>
                <div class="product-name">Wireless Headphones</div>
                <div class="product-desc">Premium noise cancelling</div>
                <div class="product-footer">
                    <div class="product-price">$69<span class="old">$99</span></div>
                    <div class="add-btn">Add</div>
                </div>
            </div>
        </div>
        <div class="product-card">
            <div class="product-image" style="background:linear-gradient(135deg,#bfdbfe,#93c5fd,#60a5fa);">
                <div class="product-badge badge-new">NEW</div>
            </div>
            <div class="product-body">
                <div class="stars"><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div><div class="star empty"></div></div>
                <div class="product-name">Smart Watch Pro</div>
                <div class="product-desc">Health tracking & GPS</div>
                <div class="product-footer">
                    <div class="product-price">$249</div>
                    <div class="add-btn">Add</div>
                </div>
            </div>
        </div>
        <div class="product-card">
            <div class="product-image" style="background:linear-gradient(135deg,#d9f99d,#a3e635,#84cc16);">
                <div class="product-badge badge-trending">TRENDING</div>
            </div>
            <div class="product-body">
                <div class="stars"><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div></div>
                <div class="product-name">Eco Water Bottle</div>
                <div class="product-desc">Sustainable bamboo cap</div>
                <div class="product-footer">
                    <div class="product-price">$34</div>
                    <div class="add-btn">Add</div>
                </div>
            </div>
        </div>
        <div class="product-card">
            <div class="product-image" style="background:linear-gradient(135deg,#e9d5ff,#c084fc,#a855f7);">
                <div class="product-badge badge-sale">-20%</div>
            </div>
            <div class="product-body">
                <div class="stars"><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div><div class="star filled"></div><div class="star empty"></div></div>
                <div class="product-name">LED Desk Lamp</div>
                <div class="product-desc">Touch dimming, USB-C</div>
                <div class="product-footer">
                    <div class="product-price">$42<span class="old">$52</span></div>
                    <div class="add-btn">Add</div>
                </div>
            </div>
        </div>
    </div>
</div>

</body></html>'''


# ============================================================
# REGISTRY: all thumbnails
# ============================================================
THUMBNAILS = [
    ("topupcuk", html_topupcuk),
    ("epic-rpg", html_epic_rpg),
    ("promovideohub", html_promovideohub),
    ("openclaw", html_openclaw),
    ("jobboard", html_jobboard),
    ("event-platform", html_event_platform),
    ("cheatmc", html_cheatmc),
    ("trading-engine", html_trading_engine),
    ("solana-bot", html_solana_bot),
    ("guidedgrowth", html_guidedgrowth),
    ("cf-bypass", html_cf_bypass),
    ("shopifyclone", html_shopifyclone),
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 800, "height": 450})

        for slug, html_fn in THUMBNAILS:
            html = html_fn()
            page.set_content(html, wait_until="networkidle")
            page.wait_for_timeout(1500)  # wait for Google Fonts

            out_path = OUT / (slug + ".png")
            page.screenshot(path=str(out_path), type="png")
            print("Generated: " + str(out_path))

        browser.close()
        print("\nAll " + str(len(THUMBNAILS)) + " thumbnails generated successfully.")


if __name__ == "__main__":
    main()
