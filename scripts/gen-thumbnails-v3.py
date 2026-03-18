"""
Thumbnail Generator v3 — Each project gets UNIQUE custom HTML.
No templates, no copy-paste. Every thumbnail looks like a real website screenshot.
Uses real images where available.
"""
import base64, os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path("c:/BACKTOCAMPUS/portfolio-web")
IMG_DIR = ROOT / "public" / "img"
OUT_DIR = ROOT / "public" / "thumbnails"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def img_to_b64(path):
    if not path.exists():
        return ""
    with open(path, "rb") as f:
        return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode()}"

# Preload game images
ff_b64 = img_to_b64(IMG_DIR / "ff-icon.jpg")
genshin_b64 = img_to_b64(IMG_DIR / "genshin-icon.jpg")
ml_b64 = img_to_b64(IMG_DIR / "ml-icon.jpg")
valo_b64 = img_to_b64(IMG_DIR / "valo-icon.jpg")
pubg_b64 = img_to_b64(IMG_DIR / "pubg-icon.jpg")
rpg_b64 = img_to_b64(IMG_DIR / "rpg-bg.jpg")
castle_b64 = img_to_b64(IMG_DIR / "castle-bg.jpg")


def topupcuk_html():
    """E-commerce game top-up store — dark gaming theme with CSS game icons"""
    return '''<!DOCTYPE html>
<html><head><style>
* { margin:0; padding:0; box-sizing:border-box; }
body { width:800px; height:450px; background:#0f0f1a; font-family:'Segoe UI',sans-serif; color:#fff; overflow:hidden; }
.nav { display:flex; justify-content:space-between; align-items:center; padding:12px 24px; background:linear-gradient(90deg,#1a1a2e,#16213e); border-bottom:1px solid #2a2a4a; }
.logo { font-size:20px; font-weight:800; background:linear-gradient(135deg,#00d4ff,#7b2ff7); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.nav-links { display:flex; gap:20px; font-size:12px; color:#8888aa; }
.hero { padding:20px 24px 16px; background:linear-gradient(135deg,#1a1a2e 0%,#0d1b2a 50%,#1a0a2e 100%); }
.hero h2 { font-size:16px; color:#8888aa; margin-bottom:4px; }
.hero h1 { font-size:22px; font-weight:700; margin-bottom:12px; }
.hero h1 span { color:#00d4ff; }
.games { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; padding:16px 24px; }
.game-card { background:#1a1a2e; border-radius:12px; padding:12px; text-align:center; border:1px solid #2a2a4a; position:relative; overflow:hidden; }
.game-card::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg,#00d4ff,#7b2ff7); }
.gi { width:56px; height:56px; border-radius:10px; margin:0 auto 6px; display:flex; align-items:center; justify-content:center; font-weight:800; color:#fff; }
.game-card .name { font-size:11px; font-weight:600; color:#fff; }
.game-card .price { font-size:10px; color:#00d4ff; margin-top:2px; }
.game-card .badge { position:absolute; top:8px; right:8px; background:#ff4757; color:#fff; font-size:8px; padding:2px 6px; border-radius:4px; font-weight:700; }
.section-title { padding:0 24px; font-size:13px; color:#8888aa; margin-top:8px; }
.promos { display:flex; gap:12px; padding:12px 24px; }
.promo { flex:1; background:linear-gradient(135deg,#7b2ff7,#00d4ff); border-radius:10px; padding:12px; }
.promo .label { font-size:10px; opacity:.8; }
.promo .val { font-size:14px; font-weight:700; }
</style></head><body>
<div class="nav">
    <div class="logo">TopupCuk</div>
    <div class="nav-links"><span>Games</span><span>Pulsa</span><span>E-Wallet</span><span>Voucher</span><span>Login</span></div>
</div>
<div class="hero">
    <h2>Instant Digital Top-Up</h2>
    <h1>Top up game favoritmu <span>dalam hitungan detik</span></h1>
</div>
<div class="section-title">Popular Games</div>
<div class="games">
    <div class="game-card"><div class="badge">HOT</div><div class="gi" style="background:linear-gradient(135deg,#1a47b8,#0d2a7a);font-size:15px;">MLBB</div><div class="name">Mobile Legends</div><div class="price">From Rp5.000</div></div>
    <div class="game-card"><div class="gi" style="background:linear-gradient(135deg,#ff6b00,#ff3d00);font-size:18px;">FF</div><div class="name">Free Fire</div><div class="price">From Rp3.000</div></div>
    <div class="game-card"><div class="badge">NEW</div><div class="gi" style="background:linear-gradient(135deg,#00bcd4,#006978);font-size:14px;">GI</div><div class="name">Genshin Impact</div><div class="price">From Rp16.000</div></div>
    <div class="game-card"><div class="gi" style="background:linear-gradient(135deg,#fd4556,#bd3944);font-size:13px;">VAL</div><div class="name">Valorant</div><div class="price">From Rp12.000</div></div>
    <div class="game-card"><div class="gi" style="background:linear-gradient(135deg,#f2a900,#e8940a);font-size:12px;">PUBG</div><div class="name">PUBG Mobile</div><div class="price">From Rp8.000</div></div>
    <div class="game-card"><div class="gi" style="background:linear-gradient(135deg,#4fc3f7,#0288d1);font-size:20px;">XL</div><div class="name">XL Axiata</div><div class="price">From Rp5.000</div></div>
    <div class="game-card"><div class="gi" style="background:linear-gradient(135deg,#e53935,#b71c1c);font-size:18px;">T</div><div class="name">Telkomsel</div><div class="price">From Rp5.000</div></div>
    <div class="game-card"><div class="gi" style="background:linear-gradient(135deg,#1a237e,#283593);font-size:14px;">STEAM</div><div class="name">Steam Wallet</div><div class="price">From Rp12.000</div></div>
</div>
<div class="promos">
    <div class="promo"><div class="label">Weekend Special</div><div class="val">10% OFF All Games</div></div>
    <div class="promo" style="background:linear-gradient(135deg,#ff4757,#ff6b81);"><div class="label">Flash Sale</div><div class="val">ML Diamonds 50% OFF</div></div>
</div>
</body></html>'''


def epic_rpg_html():
    """Dark fantasy RPG game interface — looks like an actual game screenshot"""
    return '''<!DOCTYPE html>
<html><head><style>
* { margin:0; padding:0; box-sizing:border-box; }
body { width:800px; height:450px; background:#0a0a12; font-family:'Segoe UI',sans-serif; color:#fff; overflow:hidden; position:relative; }
.bg { position:absolute; inset:0; background:linear-gradient(180deg,#0f0520 0%,#1a0a2e 30%,#0d1520 60%,#050510 100%); }
.bg::before { content:''; position:absolute; inset:0; background:radial-gradient(ellipse at 50% 20%,rgba(100,40,180,.15) 0%,transparent 60%),radial-gradient(ellipse at 30% 80%,rgba(20,80,120,.1) 0%,transparent 40%),radial-gradient(ellipse at 70% 60%,rgba(80,20,100,.08) 0%,transparent 50%); }
.bg::after { content:''; position:absolute; bottom:0; left:0; right:0; height:120px; background:linear-gradient(180deg,transparent,rgba(5,5,10,.9)); }
.overlay { position:absolute; inset:0; }
.ui { position:relative; z-index:1; height:100%; display:flex; flex-direction:column; }
.top-bar { display:flex; justify-content:space-between; padding:12px 20px; }
.hp-bar { width:180px; }
.hp-label { font-size:9px; color:#aaa; display:flex; justify-content:space-between; }
.hp-track { width:100%; height:14px; background:#1a1a2e; border-radius:7px; overflow:hidden; border:1px solid #333; }
.hp-fill { width:72%; height:100%; background:linear-gradient(90deg,#22c55e,#16a34a); border-radius:7px; }
.mp-fill { width:58%; height:100%; background:linear-gradient(90deg,#3b82f6,#2563eb); border-radius:7px; }
.xp-fill { width:45%; height:100%; background:linear-gradient(90deg,#a855f7,#7c3aed); border-radius:7px; }
.player-info { text-align:right; }
.player-info .name { font-size:13px; font-weight:700; color:#fbbf24; }
.player-info .level { font-size:10px; color:#aaa; }
.player-info .gold { font-size:11px; color:#fbbf24; margin-top:2px; }
.game-area { flex:1; display:flex; align-items:center; justify-content:center; position:relative; }
.monster { text-align:center; }
.monster-sprite { width:120px; height:120px; background:radial-gradient(ellipse,#4a1a6b,#2a0a3b); border-radius:50% 50% 40% 40%; position:relative; box-shadow:0 0 40px rgba(138,43,226,.4); display:flex; align-items:center; justify-content:center; }
.monster-sprite::before { content:''; position:absolute; top:25px; left:30px; width:15px; height:15px; background:#ff0040; border-radius:50%; box-shadow:0 0 10px #ff0040, 45px 0 0 #ff0040, 45px 0 10px #ff0040; }
.monster-sprite::after { content:''; position:absolute; bottom:30px; left:35px; width:50px; height:8px; background:#ff0040; border-radius:0 0 20px 20px; }
.monster .name { font-size:12px; color:#c084fc; margin-top:8px; }
.monster .hp-m { width:100px; height:6px; background:#333; border-radius:3px; margin:4px auto 0; }
.monster .hp-m-fill { width:65%; height:100%; background:linear-gradient(90deg,#ef4444,#dc2626); border-radius:3px; }
.dmg-popup { position:absolute; top:80px; right:200px; font-size:28px; font-weight:900; color:#ef4444; text-shadow:0 0 10px rgba(239,68,68,.5); transform:rotate(-12deg); }
.combat-log { position:absolute; bottom:80px; left:20px; width:200px; }
.log-line { font-size:9px; padding:2px 0; opacity:.7; }
.log-line.dmg { color:#ef4444; }
.log-line.heal { color:#22c55e; }
.log-line.info { color:#60a5fa; }
.bottom-bar { display:flex; gap:8px; padding:12px 20px; background:rgba(10,10,18,.9); border-top:1px solid #222; }
.action-btn { flex:1; padding:10px; text-align:center; border-radius:8px; font-size:11px; font-weight:700; cursor:pointer; border:1px solid; }
.btn-attack { background:linear-gradient(135deg,#991b1b,#7f1d1d); border-color:#ef4444; color:#fca5a5; }
.btn-skill { background:linear-gradient(135deg,#1e3a5f,#1e3a8a); border-color:#3b82f6; color:#93c5fd; }
.btn-item { background:linear-gradient(135deg,#365314,#3f6212); border-color:#22c55e; color:#86efac; }
.btn-run { background:linear-gradient(135deg,#44403c,#57534e); border-color:#a8a29e; color:#d6d3d1; }
.inventory { position:absolute; top:60px; right:16px; display:grid; grid-template-columns:repeat(2,1fr); gap:4px; }
.inv-slot { width:36px; height:36px; background:rgba(26,26,46,.8); border:1px solid #333; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:16px; }
.inv-slot.rare { border-color:#a855f7; box-shadow:0 0 6px rgba(168,85,247,.3); }
.inv-slot.epic { border-color:#f59e0b; box-shadow:0 0 6px rgba(245,158,11,.3); }
.minimap { position:absolute; bottom:80px; right:16px; width:80px; height:80px; background:rgba(10,10,18,.8); border:1px solid #333; border-radius:8px; overflow:hidden; }
.minimap-dot { width:6px; height:6px; background:#22c55e; border-radius:50%; position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); box-shadow:0 0 8px #22c55e; }
.minimap-enemy { width:4px; height:4px; background:#ef4444; border-radius:50%; position:absolute; box-shadow:0 0 4px #ef4444; }
.dungeon-label { position:absolute; top:12px; left:50%; transform:translateX(-50%); font-size:10px; color:#c084fc; background:rgba(10,10,18,.7); padding:4px 12px; border-radius:12px; border:1px solid #7c3aed33; }
</style></head><body>
<div class="bg"></div>
<div class="overlay"></div>
<div class="ui">
    <div class="dungeon-label">Dungeon Floor 4 — Shadow Citadel</div>
    <div class="top-bar">
        <div class="hp-bar">
            <div class="hp-label"><span>HP</span><span>1,847 / 2,560</span></div>
            <div class="hp-track"><div class="hp-fill"></div></div>
            <div style="height:4px;"></div>
            <div class="hp-label"><span>MP</span><span>340 / 580</span></div>
            <div class="hp-track"><div class="mp-fill"></div></div>
            <div style="height:4px;"></div>
            <div class="hp-label"><span>XP</span><span>12,450 / 28,000</span></div>
            <div class="hp-track"><div class="xp-fill"></div></div>
        </div>
        <div class="player-info">
            <div class="name">ShadowKnight</div>
            <div class="level">Level 47 Warrior</div>
            <div class="gold">24,580 Gold</div>
        </div>
    </div>
    <div class="game-area">
        <div class="monster">
            <div class="monster-sprite"></div>
            <div class="name">Void Warden (Boss)</div>
            <div class="hp-m"><div class="hp-m-fill"></div></div>
        </div>
        <div class="dmg-popup">-2,847</div>
        <div class="combat-log">
            <div class="log-line dmg">You hit Void Warden for 2,847 damage!</div>
            <div class="log-line heal">Regeneration heals you for 180 HP</div>
            <div class="log-line dmg">Void Warden casts Shadow Bolt — 1,203 damage!</div>
            <div class="log-line info">Your shield absorbs 400 damage</div>
            <div class="log-line dmg">Critical hit! 4,128 damage!</div>
        </div>
        <div class="inventory">
            <div class="inv-slot rare" style="color:#a855f7;font-size:14px;font-weight:800;">S</div>
            <div class="inv-slot epic" style="color:#f59e0b;font-size:14px;font-weight:800;">A</div>
            <div class="inv-slot" style="color:#22c55e;font-size:14px;">P</div>
            <div class="inv-slot" style="color:#ef4444;font-size:14px;">R</div>
        </div>
        <div class="minimap">
            <div class="minimap-dot"></div>
            <div class="minimap-enemy" style="top:20%;left:70%;"></div>
            <div class="minimap-enemy" style="top:60%;left:30%;"></div>
            <div class="minimap-enemy" style="top:35%;left:45%;"></div>
        </div>
    </div>
    <div class="bottom-bar">
        <div class="action-btn btn-attack">ATTACK</div>
        <div class="action-btn btn-skill">SKILLS</div>
        <div class="action-btn btn-item">ITEMS</div>
        <div class="action-btn btn-run">FLEE</div>
    </div>
</div>
</body></html>'''


def promovideohub_html():
    """Video editing dashboard — timeline, preview, clips panel"""
    return '''<!DOCTYPE html>
<html><head><style>
* { margin:0; padding:0; box-sizing:border-box; }
body { width:800px; height:450px; background:#111118; font-family:'Segoe UI',sans-serif; color:#fff; overflow:hidden; display:flex; flex-direction:column; }
.toolbar { display:flex; align-items:center; justify-content:space-between; padding:8px 16px; background:#1a1a24; border-bottom:1px solid #2a2a3a; }
.toolbar .logo { font-size:14px; font-weight:700; }
.toolbar .logo span { color:#e040fb; }
.toolbar .actions { display:flex; gap:8px; }
.toolbar .btn { padding:4px 12px; font-size:10px; border-radius:4px; border:none; cursor:pointer; }
.btn-export { background:#e040fb; color:#fff; }
.btn-save { background:#2a2a3a; color:#aaa; border:1px solid #3a3a4a; }
.main { display:flex; flex:1; overflow:hidden; }
.sidebar { width:180px; background:#16161e; border-right:1px solid #2a2a3a; padding:8px; overflow:hidden; }
.sidebar h3 { font-size:10px; color:#888; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px; }
.clip { display:flex; gap:6px; align-items:center; padding:6px; border-radius:6px; margin-bottom:4px; cursor:pointer; }
.clip:hover { background:#222; }
.clip.active { background:#2a1a3a; border:1px solid #e040fb33; }
.clip-thumb { width:48px; height:28px; border-radius:4px; flex-shrink:0; }
.clip-info { font-size:9px; }
.clip-info .name { color:#ddd; font-weight:600; }
.clip-info .dur { color:#666; }
.preview-area { flex:1; display:flex; flex-direction:column; }
.preview { flex:1; background:#0a0a10; display:flex; align-items:center; justify-content:center; position:relative; }
.preview-screen { width:85%; height:85%; border-radius:4px; position:relative; overflow:hidden; }
.preview-screen .bg-grad { width:100%; height:100%; background:linear-gradient(135deg,#1a0a2e,#0d1b2a,#1a2a1a); }}
.play-btn { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:40px; height:40px; background:rgba(224,64,251,.9); border-radius:50%; display:flex; align-items:center; justify-content:center; }
.play-btn::after { content:''; width:0; height:0; border-style:solid; border-width:8px 0 8px 14px; border-color:transparent transparent transparent #fff; margin-left:3px; }
.timecode { position:absolute; bottom:8px; right:12px; font-size:10px; color:#888; font-family:monospace; }
.controls { padding:6px 12px; display:flex; align-items:center; gap:8px; background:#16161e; border-top:1px solid #2a2a3a; }
.ctrl-btn { width:24px; height:24px; background:#2a2a3a; border-radius:4px; display:flex; align-items:center; justify-content:center; font-size:10px; color:#aaa; }
.progress { flex:1; height:3px; background:#2a2a3a; border-radius:2px; position:relative; }
.progress-fill { width:35%; height:100%; background:#e040fb; border-radius:2px; }
.progress-dot { width:8px; height:8px; background:#fff; border-radius:50%; position:absolute; top:-2.5px; left:35%; }
.timeline { height:100px; background:#0d0d14; border-top:1px solid #2a2a3a; padding:8px 12px; overflow:hidden; }
.timeline-header { display:flex; justify-content:space-between; margin-bottom:6px; }
.timeline-header span { font-size:9px; color:#666; }
.tracks { display:flex; flex-direction:column; gap:4px; }
.track { display:flex; align-items:center; height:20px; }
.track-label { width:50px; font-size:8px; color:#666; flex-shrink:0; }
.track-clips { flex:1; display:flex; gap:2px; height:100%; position:relative; }
.t-clip { height:100%; border-radius:3px; position:relative; overflow:hidden; }
.t-clip::after { content:''; position:absolute; inset:0; background:repeating-linear-gradient(90deg,transparent,transparent 8px,rgba(0,0,0,.15) 8px,rgba(0,0,0,.15) 9px); }
.playhead { position:absolute; top:0; left:35%; width:1px; height:100%; background:#e040fb; z-index:5; }
.playhead::before { content:''; position:absolute; top:-4px; left:-4px; width:9px; height:4px; background:#e040fb; border-radius:2px 2px 0 0; }
.right-panel { width:160px; background:#16161e; border-left:1px solid #2a2a3a; padding:8px; }
.right-panel h3 { font-size:10px; color:#888; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px; }
.effect { padding:6px 8px; background:#1e1e28; border-radius:6px; margin-bottom:4px; font-size:9px; }
.effect .label { color:#aaa; }
.effect .val { color:#e040fb; float:right; }
.slider { width:100%; height:3px; background:#2a2a3a; border-radius:2px; margin-top:4px; }
.slider-fill { height:100%; border-radius:2px; }
</style></head><body>
<div class="toolbar">
    <div class="logo">Promo<span>Video</span>Hub</div>
    <div class="actions">
        <div class="btn btn-save">Save Draft</div>
        <div class="btn btn-export">Export 1080p</div>
    </div>
</div>
<div class="main">
    <div class="sidebar">
        <h3>Media Library</h3>
        <div class="clip active">
            <div class="clip-thumb" style="background:linear-gradient(135deg,#e040fb,#7c3aed);"></div>
            <div class="clip-info"><div class="name">intro_scene.mp4</div><div class="dur">0:12</div></div>
        </div>
        <div class="clip">
            <div class="clip-thumb" style="background:linear-gradient(135deg,#3b82f6,#06b6d4);"></div>
            <div class="clip-info"><div class="name">product_hero.mp4</div><div class="dur">0:08</div></div>
        </div>
        <div class="clip">
            <div class="clip-thumb" style="background:linear-gradient(135deg,#22c55e,#14b8a6);"></div>
            <div class="clip-info"><div class="name">features_demo.mp4</div><div class="dur">0:15</div></div>
        </div>
        <div class="clip">
            <div class="clip-thumb" style="background:linear-gradient(135deg,#f59e0b,#ef4444);"></div>
            <div class="clip-info"><div class="name">testimonials.mp4</div><div class="dur">0:20</div></div>
        </div>
        <div class="clip">
            <div class="clip-thumb" style="background:linear-gradient(135deg,#8b5cf6,#ec4899);"></div>
            <div class="clip-info"><div class="name">cta_outro.mp4</div><div class="dur">0:06</div></div>
        </div>
        <div class="clip">
            <div class="clip-thumb" style="background:linear-gradient(135deg,#64748b,#475569);"></div>
            <div class="clip-info"><div class="name">bg_music.mp3</div><div class="dur">1:02</div></div>
        </div>
    </div>
    <div class="preview-area">
        <div class="preview">
            <div class="preview-screen">
                <div class="bg-grad" style="width:100%;height:100%;background:linear-gradient(135deg,#1a0a2e,#0d1b2a,#1a2a1a);display:flex;align-items:center;justify-content:center;flex-direction:column;">
                    <div style="font-size:28px;font-weight:800;background:linear-gradient(135deg,#e040fb,#00d4ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">YOUR PRODUCT</div>
                    <div style="font-size:12px;color:#888;margin-top:4px;">The Future Starts Here</div>
                </div>
            </div>
            <div class="play-btn"></div>
            <div class="timecode">00:12:04 / 01:01:23</div>
        </div>
        <div class="controls">
            <div class="ctrl-btn">|&lt;</div>
            <div class="ctrl-btn" style="background:#e040fb;color:#fff;font-size:12px;">||</div>
            <div class="ctrl-btn">&gt;|</div>
            <div class="progress"><div class="progress-fill"></div><div class="progress-dot"></div></div>
            <span style="font-size:9px;color:#888;">1x</span>
        </div>
    </div>
    <div class="right-panel">
        <h3>Effects</h3>
        <div class="effect"><div class="label">Transition</div><div class="val">Fade</div>
            <div class="slider"><div class="slider-fill" style="width:60%;background:#e040fb;"></div></div>
        </div>
        <div class="effect"><div class="label">Brightness</div><div class="val">+12</div>
            <div class="slider"><div class="slider-fill" style="width:55%;background:#f59e0b;"></div></div>
        </div>
        <div class="effect"><div class="label">Contrast</div><div class="val">+8</div>
            <div class="slider"><div class="slider-fill" style="width:48%;background:#3b82f6;"></div></div>
        </div>
        <div class="effect"><div class="label">Saturation</div><div class="val">+15</div>
            <div class="slider"><div class="slider-fill" style="width:65%;background:#22c55e;"></div></div>
        </div>
        <h3 style="margin-top:12px;">Text Overlay</h3>
        <div class="effect"><div class="label">Font</div><div class="val">Montserrat</div></div>
        <div class="effect"><div class="label">Size</div><div class="val">48px</div></div>
        <div class="effect"><div class="label">Color</div><div style="float:right;width:12px;height:12px;background:#e040fb;border-radius:2px;"></div></div>
    </div>
</div>
<div class="timeline">
    <div class="timeline-header">
        <span>Timeline</span>
        <span>0:00 &nbsp;&nbsp; 0:10 &nbsp;&nbsp; 0:20 &nbsp;&nbsp; 0:30 &nbsp;&nbsp; 0:40 &nbsp;&nbsp; 0:50 &nbsp;&nbsp; 1:00</span>
    </div>
    <div class="tracks" style="position:relative;">
        <div class="playhead"></div>
        <div class="track">
            <div class="track-label">Video 1</div>
            <div class="track-clips">
                <div class="t-clip" style="width:18%;background:linear-gradient(90deg,#e040fb,#7c3aed);"></div>
                <div class="t-clip" style="width:12%;background:linear-gradient(90deg,#3b82f6,#06b6d4);"></div>
                <div class="t-clip" style="width:22%;background:linear-gradient(90deg,#22c55e,#14b8a6);"></div>
                <div class="t-clip" style="width:30%;background:linear-gradient(90deg,#f59e0b,#ef4444);"></div>
                <div class="t-clip" style="width:10%;background:linear-gradient(90deg,#8b5cf6,#ec4899);"></div>
            </div>
        </div>
        <div class="track">
            <div class="track-label">Text</div>
            <div class="track-clips">
                <div class="t-clip" style="width:15%;margin-left:2%;background:rgba(224,64,251,.3);border:1px solid #e040fb55;"></div>
                <div class="t-clip" style="width:20%;margin-left:15%;background:rgba(224,64,251,.3);border:1px solid #e040fb55;"></div>
                <div class="t-clip" style="width:8%;margin-left:5%;background:rgba(224,64,251,.3);border:1px solid #e040fb55;"></div>
            </div>
        </div>
        <div class="track">
            <div class="track-label">Audio</div>
            <div class="track-clips">
                <div class="t-clip" style="width:95%;background:linear-gradient(90deg,#64748b,#475569);"></div>
            </div>
        </div>
    </div>
</div>
</body></html>'''


def openclaw_html():
    """AI Chatbot — Telegram-style dark chat interface"""
    return '''<!DOCTYPE html>
<html><head><style>
* { margin:0; padding:0; box-sizing:border-box; }
body { width:800px; height:450px; background:#0e1621; font-family:'Segoe UI',sans-serif; color:#fff; overflow:hidden; display:flex; }
.sidebar { width:220px; background:#17212b; border-right:1px solid #1e2c3a; }
.sidebar-header { padding:12px; display:flex; align-items:center; gap:8px; border-bottom:1px solid #1e2c3a; }
.sidebar-header .hamburger { color:#8a9bae; font-size:16px; }
.search { margin:8px; padding:8px 12px; background:#242f3d; border-radius:20px; font-size:10px; color:#8a9bae; }
.chat-item { display:flex; gap:10px; padding:10px 12px; cursor:pointer; }
.chat-item:hover { background:#202b36; }
.chat-item.active { background:#2b5278; }
.chat-avatar { width:36px; height:36px; border-radius:50%; flex-shrink:0; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:700; }
.chat-meta { flex:1; overflow:hidden; }
.chat-meta .name { font-size:12px; font-weight:600; color:#fff; }
.chat-meta .last-msg { font-size:10px; color:#8a9bae; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; margin-top:2px; }
.chat-meta .time { font-size:9px; color:#8a9bae; float:right; }
.chat-area { flex:1; display:flex; flex-direction:column; background:#0e1621; }
.chat-header { padding:10px 16px; display:flex; align-items:center; gap:10px; background:#17212b; border-bottom:1px solid #1e2c3a; }
.chat-header-avatar { width:32px; height:32px; border-radius:50%; background:linear-gradient(135deg,#7c3aed,#3b82f6); display:flex; align-items:center; justify-content:center; font-size:14px; }
.chat-header-info .name { font-size:13px; font-weight:600; }
.chat-header-info .status { font-size:10px; color:#4fc3f7; }
.messages { flex:1; padding:12px 16px; display:flex; flex-direction:column; gap:8px; overflow:hidden; }
.msg { max-width:65%; padding:8px 12px; border-radius:12px; font-size:11px; line-height:1.5; }
.msg.bot { background:#182533; align-self:flex-start; border-bottom-left-radius:4px; }
.msg.user { background:#2b5278; align-self:flex-end; border-bottom-right-radius:4px; }
.msg .time { font-size:8px; color:#8a9bae; text-align:right; margin-top:4px; }
.msg code { background:#0d1117; padding:2px 4px; border-radius:3px; font-size:10px; color:#7ee787; }
.msg pre { background:#0d1117; padding:8px; border-radius:6px; font-size:9px; color:#c9d1d9; margin-top:6px; overflow:hidden; font-family:monospace; }
.typing { align-self:flex-start; padding:8px 14px; background:#182533; border-radius:12px; display:flex; gap:4px; }
.typing span { width:6px; height:6px; background:#8a9bae; border-radius:50%; animation:blink 1.4s infinite; }
.typing span:nth-child(2) { animation-delay:.2s; }
.typing span:nth-child(3) { animation-delay:.4s; }
@keyframes blink { 0%,60%,100% { opacity:.3; } 30% { opacity:1; } }
.input-area { padding:8px 16px; background:#17212b; border-top:1px solid #1e2c3a; display:flex; gap:8px; align-items:center; }
.input-box { flex:1; padding:8px 14px; background:#242f3d; border-radius:20px; font-size:11px; color:#fff; border:none; }
.send-btn { width:32px; height:32px; background:#2b5278; border-radius:50%; display:flex; align-items:center; justify-content:center; }
.send-btn::after { content:''; width:0; height:0; border-style:solid; border-width:5px 0 5px 9px; border-color:transparent transparent transparent #fff; margin-left:2px; }
</style></head><body>
<div class="sidebar">
    <div class="sidebar-header"><span class="hamburger">=</span><span style="font-size:14px;font-weight:700;">OpenClaw</span></div>
    <div class="search">Search conversations...</div>
    <div class="chat-item active">
        <div class="chat-avatar" style="background:linear-gradient(135deg,#7c3aed,#3b82f6);">OC</div>
        <div class="chat-meta"><div class="time">now</div><div class="name">OpenClaw Assistant</div><div class="last-msg">Here's the analysis of your data...</div></div>
    </div>
    <div class="chat-item">
        <div class="chat-avatar" style="background:linear-gradient(135deg,#22c55e,#14b8a6);">D</div>
        <div class="chat-meta"><div class="time">2m</div><div class="name">Data Pipeline Bot</div><div class="last-msg">Pipeline completed: 2,847 rows</div></div>
    </div>
    <div class="chat-item">
        <div class="chat-avatar" style="background:linear-gradient(135deg,#f59e0b,#ef4444);">M</div>
        <div class="chat-meta"><div class="time">15m</div><div class="name">Meeting Summarizer</div><div class="last-msg">3 action items extracted</div></div>
    </div>
    <div class="chat-item">
        <div class="chat-avatar" style="background:linear-gradient(135deg,#ec4899,#8b5cf6);">C</div>
        <div class="chat-meta"><div class="time">1h</div><div class="name">Code Review Agent</div><div class="last-msg">Found 2 issues in auth.ts</div></div>
    </div>
</div>
<div class="chat-area">
    <div class="chat-header">
        <div class="chat-header-avatar">OC</div>
        <div class="chat-header-info">
            <div class="name">OpenClaw Assistant</div>
            <div class="status">online - Claude API</div>
        </div>
    </div>
    <div class="messages">
        <div class="msg bot">Hey! I'm OpenClaw, your self-hosted AI assistant. What can I help with today?<div class="time">10:24</div></div>
        <div class="msg user">Analyze the sales data from last week and give me a summary<div class="time">10:25</div></div>
        <div class="msg bot">
            Here's your weekly sales analysis:
            <pre>Total Revenue:  $24,580 (+12.3%)
Orders:         847 (+8.7%)
Avg Order:      $29.02 (+3.3%)
Top Product:    Premium Plan
Conversion:     4.2% (up from 3.8%)</pre>
            Key insights: Revenue up 12.3% WoW driven by Premium Plan upgrades. Conversion rate improved after the checkout redesign shipped Monday.
            <div class="time">10:25</div>
        </div>
        <div class="msg user">Great. Now draft a Slack update for the team<div class="time">10:26</div></div>
        <div class="msg bot">
            Here's a draft:
            <br><br>
            <strong>Weekly Sales Update</strong><br>
            Revenue hit <code>$24.6K</code> this week — up 12.3% from last week. 847 orders processed with a 4.2% conversion rate. The checkout redesign is showing results. Full dashboard link in thread.
            <div class="time">10:26</div>
        </div>
        <div class="typing"><span></span><span></span><span></span></div>
    </div>
    <div class="input-area">
        <div class="input-box">Type a message...</div>
        <div class="send-btn"></div>
    </div>
</div>
</body></html>'''


def jobboard_html():
    """Job board platform — clean white UI with job listings, filters, company logos"""
    return '''<!DOCTYPE html>
<html><head><style>
* { margin:0; padding:0; box-sizing:border-box; }
body { width:800px; height:450px; background:#f8fafc; font-family:'Segoe UI',sans-serif; color:#1e293b; overflow:hidden; }
.nav { display:flex; justify-content:space-between; align-items:center; padding:10px 24px; background:#fff; border-bottom:1px solid #e2e8f0; }
.nav .logo { font-size:18px; font-weight:800; color:#1e293b; }
.nav .logo span { color:#3b82f6; }
.nav-links { display:flex; gap:16px; font-size:11px; color:#64748b; align-items:center; }
.nav .post-btn { background:#3b82f6; color:#fff; padding:6px 14px; border-radius:6px; font-size:10px; font-weight:600; }
.hero { padding:16px 24px; background:linear-gradient(135deg,#1e3a5f,#3b82f6); color:#fff; }
.hero h1 { font-size:18px; margin-bottom:8px; }
.search-bar { display:flex; gap:8px; }
.search-bar input { flex:1; padding:8px 12px; border-radius:6px; border:none; font-size:11px; background:rgba(255,255,255,.95); color:#333; }
.search-bar .s-btn { padding:8px 16px; background:#f59e0b; color:#fff; border-radius:6px; font-size:11px; font-weight:600; border:none; }
.content { display:flex; padding:12px 24px; gap:16px; }
.filters { width:160px; flex-shrink:0; }
.filters h3 { font-size:11px; font-weight:700; color:#334155; margin-bottom:6px; }
.filter-group { margin-bottom:12px; }
.filter-item { display:flex; align-items:center; gap:6px; font-size:10px; color:#64748b; margin-bottom:4px; }
.filter-item .check { width:12px; height:12px; border:1.5px solid #cbd5e1; border-radius:3px; }
.filter-item .check.checked { background:#3b82f6; border-color:#3b82f6; }
.filter-item .count { color:#94a3b8; margin-left:auto; }
.jobs { flex:1; display:flex; flex-direction:column; gap:8px; }
.job { background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:12px 14px; display:flex; gap:12px; align-items:center; }
.job:hover { border-color:#3b82f6; box-shadow:0 2px 8px rgba(59,130,246,.1); }
.job-logo { width:40px; height:40px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:800; flex-shrink:0; }
.job-info { flex:1; }
.job-title { font-size:12px; font-weight:700; color:#1e293b; }
.job-company { font-size:10px; color:#64748b; margin-top:1px; }
.job-tags { display:flex; gap:4px; margin-top:4px; }
.tag { padding:2px 8px; border-radius:4px; font-size:8px; font-weight:600; }
.tag-ft { background:#dbeafe; color:#2563eb; }
.tag-remote { background:#dcfce7; color:#16a34a; }
.tag-onsite { background:#fef3c7; color:#d97706; }
.job-salary { text-align:right; flex-shrink:0; }
.job-salary .amount { font-size:12px; font-weight:700; color:#1e293b; }
.job-salary .period { font-size:9px; color:#94a3b8; }
.job-salary .posted { font-size:8px; color:#cbd5e1; margin-top:4px; }
</style></head><body>
<div class="nav">
    <div class="logo">Job<span>Board</span></div>
    <div class="nav-links"><span>Find Jobs</span><span>Companies</span><span>Salaries</span><span>Blog</span><div class="post-btn">Post a Job</div></div>
</div>
<div class="hero">
    <h1>Find your dream job today</h1>
    <div class="search-bar">
        <input placeholder="Job title, keywords, or company" />
        <input placeholder="Location or remote" style="max-width:160px;" />
        <div class="s-btn">Search</div>
    </div>
</div>
<div class="content">
    <div class="filters">
        <div class="filter-group">
            <h3>Job Type</h3>
            <div class="filter-item"><div class="check checked"></div>Full-time<span class="count">248</span></div>
            <div class="filter-item"><div class="check checked"></div>Remote<span class="count">187</span></div>
            <div class="filter-item"><div class="check"></div>Part-time<span class="count">42</span></div>
            <div class="filter-item"><div class="check"></div>Contract<span class="count">63</span></div>
        </div>
        <div class="filter-group">
            <h3>Salary Range</h3>
            <div class="filter-item"><div class="check"></div>$50k - $100k<span class="count">89</span></div>
            <div class="filter-item"><div class="check checked"></div>$100k - $150k<span class="count">134</span></div>
            <div class="filter-item"><div class="check"></div>$150k+<span class="count">67</span></div>
        </div>
        <div class="filter-group">
            <h3>Experience</h3>
            <div class="filter-item"><div class="check"></div>Entry Level<span class="count">56</span></div>
            <div class="filter-item"><div class="check checked"></div>Mid Level<span class="count">178</span></div>
            <div class="filter-item"><div class="check"></div>Senior<span class="count">112</span></div>
        </div>
    </div>
    <div class="jobs">
        <div class="job">
            <div class="job-logo" style="background:linear-gradient(135deg,#4285f4,#34a853);">G</div>
            <div class="job-info"><div class="job-title">Senior React Developer</div><div class="job-company">Google - Mountain View, CA</div><div class="job-tags"><span class="tag tag-ft">Full-time</span><span class="tag tag-remote">Remote OK</span></div></div>
            <div class="job-salary"><div class="amount">$140k-180k</div><div class="period">/year</div><div class="posted">2h ago</div></div>
        </div>
        <div class="job">
            <div class="job-logo" style="background:linear-gradient(135deg,#000,#333);">OA</div>
            <div class="job-info"><div class="job-title">AI/ML Research Engineer</div><div class="job-company">OpenAI - San Francisco, CA</div><div class="job-tags"><span class="tag tag-ft">Full-time</span><span class="tag tag-onsite">On-site</span></div></div>
            <div class="job-salary"><div class="amount">$200k+</div><div class="period">/year</div><div class="posted">4h ago</div></div>
        </div>
        <div class="job">
            <div class="job-logo" style="background:linear-gradient(135deg,#635bff,#8b5cf6);">S</div>
            <div class="job-info"><div class="job-title">Backend Engineer (Go)</div><div class="job-company">Stripe - Remote</div><div class="job-tags"><span class="tag tag-ft">Full-time</span><span class="tag tag-remote">Remote</span></div></div>
            <div class="job-salary"><div class="amount">$150k-190k</div><div class="period">/year</div><div class="posted">6h ago</div></div>
        </div>
        <div class="job">
            <div class="job-logo" style="background:linear-gradient(135deg,#ff4500,#ff6b35);">R</div>
            <div class="job-info"><div class="job-title">Full-Stack Developer</div><div class="job-company">Reddit - San Francisco, CA</div><div class="job-tags"><span class="tag tag-ft">Full-time</span><span class="tag tag-remote">Remote OK</span></div></div>
            <div class="job-salary"><div class="amount">$130k-160k</div><div class="period">/year</div><div class="posted">1d ago</div></div>
        </div>
    </div>
</div>
</body></html>'''


# Map project IDs to their HTML generators
PROJECTS = {
    "topupcuk": topupcuk_html,
    "epic-rpg": epic_rpg_html,
    "promovideohub": promovideohub_html,
    "openclaw": openclaw_html,
    "jobboard": jobboard_html,
}


def generate():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 800, "height": 450})

        for pid, html_fn in PROJECTS.items():
            print(f"Generating {pid}...")
            html = html_fn()
            page.set_content(html, wait_until="networkidle")
            page.wait_for_timeout(500)
            out = OUT_DIR / f"{pid}.png"
            page.screenshot(path=str(out), type="png")
            print(f"  -> {out}")

        browser.close()
    print("\nDone! Generated 5 thumbnails.")


if __name__ == "__main__":
    generate()
