from flask import Flask, render_template
from jinja2 import DictLoader

app = Flask(__name__)

BUSINESS = {
    "name": "Super Vastuu",
    "tagline": "Vastu guidance for factory, home, office, plot and shop",
    "email": "svk.nitin@gmail.com",
}

PARTNERS = [
    {"name": "Nitin Mehra", "role": "Founder and Vastu Consultant",
     "bio": "Guides families and business owners towards balance and prosperity through Vastu.",
     "phone": "+91 94652 36435", "tel": "+919465236435", "whatsapp": "919465236435"},
    {"name": "Amit Sharma", "role": "Co-founder and Vastu Expert",
     "bio": "Helps homes, offices and shops get the right layout and energy flow.",
     "phone": "+91 97810 34333", "tel": "+919781034333", "whatsapp": "919781034333"},
]

SERVICES = [
    {"icon": "🏭", "title": "Factory Vastu", "desc": "Layout, machinery, storage and entrance planning for smooth production and growth."},
    {"icon": "🏠", "title": "Home Vastu", "desc": "Room placement, kitchen, bedroom and pooja direction for a peaceful, healthy home."},
    {"icon": "🏢", "title": "Office Vastu", "desc": "Cabin, seating and entrance guidance for focus, teamwork and success."},
    {"icon": "📐", "title": "Plot Vastu", "desc": "Plot shape, direction and slope checked before you buy or start building."},
    {"icon": "🏪", "title": "Shop Vastu", "desc": "Counter, stock and entrance placement to attract more customers."},
    {"icon": "✨", "title": "Other Vastu services", "desc": "Flats, farmhouses, hotels and custom consultations on request."},
]

BASE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{{ b.name }} - {{ b.tagline }}">
<title>{{ b.name }} | Vastu Consultants</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{--maroon:#5c1a0b;--maroon2:#7a2a14;--saffron:#e8871e;--gold:#f2c14e;--cream:#fff7e8;--sand:#f5e6c8;--ink:#2b1a10;--muted:#6f5a48}
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;font-family:'Poppins',sans-serif;background:var(--cream);color:var(--ink);line-height:1.65}
  h1,h2,h3{font-family:'Playfair Display',Georgia,serif;line-height:1.2;margin:0 0 12px}
  a{color:inherit}
  .wrap{max-width:1080px;margin:auto;padding:0 20px}

  header{background:var(--maroon);position:sticky;top:0;z-index:20;border-bottom:3px solid var(--gold)}
  .bar{display:flex;align-items:center;justify-content:space-between;padding:14px 0}
  .logo{font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:700;color:var(--gold);text-decoration:none}
  .logo small{display:block;font-family:'Poppins',sans-serif;font-size:.65rem;color:#f5d9a8;letter-spacing:.18em;text-transform:uppercase;font-weight:500}
  nav a{color:#fff;text-decoration:none;margin-left:22px;font-size:.95rem}
  nav a:hover{color:var(--gold)}
  #menu{display:none}
  .burger{display:none;color:#fff;font-size:1.7rem;cursor:pointer}

  .btn{display:inline-block;background:var(--saffron);color:#fff;padding:12px 26px;border-radius:50px;text-decoration:none;font-weight:600;border:0;cursor:pointer;font-size:1rem;font-family:inherit}
  .btn:hover{background:#cf7410}
  .btn.ghost{background:transparent;border:2px solid var(--gold);color:var(--gold)}
  .btn.ghost:hover{background:var(--gold);color:var(--maroon)}
  .btn.wa{background:#1fa855}

  .hero{background:var(--maroon);color:#fff;padding:70px 0;position:relative;overflow:hidden}
  .hero:before{content:'';position:absolute;right:-180px;top:-180px;width:560px;height:560px;border-radius:50%;
    background:repeating-conic-gradient(rgba(242,193,78,.10) 0 10deg,transparent 10deg 20deg)}
  .hero .wrap{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center;position:relative}
  .eyebrow{color:var(--gold);letter-spacing:.2em;text-transform:uppercase;font-size:.8rem;font-weight:600}
  .hero h1{font-size:3rem;margin:12px 0 16px}
  .hero h1 span{color:var(--gold)}
  .hero p{color:#f3dfc0;max-width:520px}
  .actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}

  .compass{background:rgba(255,255,255,.06);border:1px solid rgba(242,193,78,.4);border-radius:20px;padding:20px}
  .compass .cg{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
  .compass .cg div{background:rgba(255,255,255,.07);border-radius:12px;padding:16px 6px;text-align:center;font-weight:600;color:var(--gold)}
  .compass .cg div small{display:block;color:#f3dfc0;font-weight:400;font-size:.72rem}
  .compass .cg .mid{background:var(--gold);color:var(--maroon);font-family:'Playfair Display',serif}
  .compass .cg .mid small{color:var(--maroon2)}

  section{padding:64px 0}
  .head{text-align:center;max-width:640px;margin:0 auto 36px}
  .head h2{font-size:2.1rem;color:var(--maroon)}
  .head p{color:var(--muted);margin:0}
  .alt{background:var(--sand)}

  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:22px}
  .card{background:#fff;border:1px solid #ecd9b3;border-radius:16px;padding:26px}
  .card h3{font-size:1.25rem;color:var(--maroon)}
  .card p{margin:0 0 14px;color:var(--muted)}
  .ico{font-size:2rem;margin-bottom:8px}
  .card.lift{transition:.2s}
  .card.lift:hover{transform:translateY(-4px);box-shadow:0 12px 26px rgba(92,26,11,.12)}

  .step .n{width:42px;height:42px;border-radius:50%;background:var(--maroon);color:var(--gold);display:flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:12px}

  .cta{background:var(--maroon);color:#fff;text-align:center;padding:56px 20px}
  .cta h2{color:var(--gold);font-size:2rem}
  .cta p{color:#f3dfc0}

  .avatar{width:64px;height:64px;border-radius:50%;background:var(--maroon);color:var(--gold);font-family:'Playfair Display',serif;font-size:1.8rem;display:flex;align-items:center;justify-content:center;margin-bottom:12px}
  .role{color:var(--saffron);font-weight:600;margin:0 0 8px !important}
  .contact{display:grid;grid-template-columns:1fr 1fr;gap:26px}
  label{display:block;font-weight:500;margin:12px 0 4px}
  input,select,textarea{width:100%;padding:12px;border:1px solid #d9c196;border-radius:10px;font-family:inherit;font-size:1rem;background:#fffdf7}

  footer{background:#2b1208;color:#e9d3ad;padding:40px 0 20px}
  .fgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px}
  footer h4{color:var(--gold);margin:0 0 10px;font-family:'Playfair Display',serif;font-size:1.1rem}
  footer a{display:block;text-decoration:none;margin-bottom:6px}
  footer a:hover{color:var(--gold)}
  .copy{border-top:1px solid #4a2a18;margin-top:24px;padding-top:14px;text-align:center;font-size:.85rem}

  .float{position:fixed;right:18px;bottom:18px;background:#1fa855;color:#fff;padding:14px 20px;border-radius:50px;text-decoration:none;font-weight:600;box-shadow:0 6px 18px rgba(0,0,0,.25);z-index:30}

  @media(max-width:820px){
    .hero .wrap,.contact{grid-template-columns:1fr}
    .hero h1{font-size:2.3rem}
    .burger{display:block}
    nav{display:none;position:absolute;left:0;right:0;top:100%;background:var(--maroon2);padding:10px 20px 16px}
    nav a{display:block;margin:0;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.1)}
    #menu:checked ~ nav{display:block}
    header{position:relative}
  }
</style>
</head>
<body>
<header>
  <div class="wrap bar">
    <a class="logo" href="/">{{ b.name }}<small>Vastu Consultants</small></a>
    <input type="checkbox" id="menu">
    <label class="burger" for="menu">&#9776;</label>
    <nav>
      <a href="/">Home</a>
      <a href="/services">Services</a>
      <a href="/about">About us</a>
      <a href="/contact">Contact</a>
    </nav>
  </div>
</header>

{% block content %}{% endblock %}

<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <h4>{{ b.name }}</h4>
        <div>{{ b.tagline }}.</div>
      </div>
      <div>
        <h4>Pages</h4>
        <a href="/">Home</a><a href="/services">Services</a><a href="/about">About us</a><a href="/contact">Contact</a>
      </div>
      <div>
        <h4>Contact</h4>
        {% for p in partners %}<a href="tel:{{ p.tel }}">{{ p.name }}: {{ p.phone }}</a>{% endfor %}
        <a href="mailto:{{ b.email }}">{{ b.email }}</a>
      </div>
    </div>
    <div class="copy">&copy; {{ b.name }}. All rights reserved.</div>
  </div>
</footer>

<a class="float" target="_blank" href="https://wa.me/{{ partners[0].whatsapp }}?text={{ 'Namaste, I need Vastu guidance.'|urlencode }}">WhatsApp us</a>
</body>
</html>"""

HOME = """{% extends "base.html" %}
{% block content %}
<section class="hero">
  <div class="wrap">
    <div>
      <div class="eyebrow">Vastu Shastra Consultants</div>
      <h1>Bring balance and <span>prosperity</span> to your space</h1>
      <p>Welcome to {{ b.name }}. {{ partners[0].name }} and {{ partners[1].name }} guide you with practical Vastu advice for your factory, home, office, plot and shop.</p>
      <div class="actions">
        <a class="btn" href="/services">Our services</a>
        <a class="btn ghost" href="/contact">Talk to us</a>
      </div>
    </div>
    <div class="compass">
      <div class="cg">
        <div>NW<small>Vayu</small></div><div>N<small>Kubera</small></div><div>NE<small>Ishan</small></div>
        <div>W<small>Varuna</small></div><div class="mid">Vastu<small>Balance</small></div><div>E<small>Indra</small></div>
        <div>SW<small>Nairuti</small></div><div>S<small>Yama</small></div><div>SE<small>Agni</small></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <h2>What we do</h2>
      <p>Vastu guidance for every kind of space.</p>
    </div>
    <div class="grid">
      {% for s in services %}
      <div class="card lift">
        <div class="ico">{{ s.icon }}</div>
        <h3>{{ s.title }}</h3>
        <p>{{ s.desc }}</p>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="head">
      <h2>How it works</h2>
      <p>Simple and clear, from first message to final advice.</p>
    </div>
    <div class="grid">
      <div class="card step"><div class="n">1</div><h3>Contact us</h3><p>Call or message us on WhatsApp and tell us what kind of space it is.</p></div>
      <div class="card step"><div class="n">2</div><h3>Share your plan</h3><p>Send the map or layout, or arrange a visit, so we can study the directions.</p></div>
      <div class="card step"><div class="n">3</div><h3>Get guidance</h3><p>We explain what is right, what needs correction and the simple steps to follow.</p></div>
    </div>
  </div>
</section>

<section class="cta">
  <h2>Ready to improve your space?</h2>
  <p>Speak to {{ partners[0].name }} or {{ partners[1].name }} today.</p>
  <a class="btn" href="/contact">Contact us</a>
</section>
{% endblock %}"""

SERVICES_PAGE = """{% extends "base.html" %}
{% block content %}
<section>
  <div class="wrap">
    <div class="head">
      <h2>Our Vastu services</h2>
      <p>Choose your space and message us on WhatsApp to book.</p>
    </div>
    <div class="grid">
      {% for s in services %}
      <div class="card lift">
        <div class="ico">{{ s.icon }}</div>
        <h3>{{ s.title }}</h3>
        <p>{{ s.desc }}</p>
        <a class="btn wa" target="_blank"
           href="https://wa.me/{{ partners[0].whatsapp }}?text={{ ('Namaste, I need ' ~ s.title)|urlencode }}">Book on WhatsApp</a>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
{% endblock %}"""

ABOUT = """{% extends "base.html" %}
{% block content %}
<section>
  <div class="wrap">
    <div class="head">
      <h2>About {{ b.name }}</h2>
      <p>Two consultants, one aim: harmony between people and the spaces they live and work in.</p>
    </div>
    <div class="grid">
      {% for p in partners %}
      <div class="card">
        <div class="avatar">{{ p.name[0] }}</div>
        <h3>{{ p.name }}</h3>
        <p class="role">{{ p.role }}</p>
        <p>{{ p.bio }}</p>
        <a class="btn" href="tel:{{ p.tel }}">Call {{ p.name.split()[0] }}</a>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
{% endblock %}"""

CONTACT = """{% extends "base.html" %}
{% block content %}
<section>
  <div class="wrap">
    <div class="head">
      <h2>Contact us</h2>
      <p>Call, WhatsApp or send us your details below.</p>
    </div>
    <div class="contact">
      <div>
        {% for p in partners %}
        <div class="card" style="margin-bottom:20px">
          <h3>{{ p.name }}</h3>
          <p class="role">{{ p.role }}</p>
          <p>Phone: <a href="tel:{{ p.tel }}">{{ p.phone }}</a></p>
          <a class="btn wa" target="_blank" href="https://wa.me/{{ p.whatsapp }}">WhatsApp {{ p.name.split()[0] }}</a>
        </div>
        {% endfor %}
        <p>Email: <a href="mailto:{{ b.email }}">{{ b.email }}</a></p>
      </div>
      <div class="card">
        <h3>Send us a message</h3>
        <form onsubmit="sendWA(event)">
          <label for="n">Your name</label>
          <input id="n" required placeholder="Enter your name">
          <label for="s">Service needed</label>
          <select id="s">
            {% for s in services %}<option>{{ s.title }}</option>{% endfor %}
          </select>
          <label for="m">Message</label>
          <textarea id="m" rows="4" placeholder="Tell us about your space"></textarea>
          <p></p>
          <button class="btn wa" type="submit">Send on WhatsApp</button>
        </form>
      </div>
    </div>
  </div>
</section>
<script>
function sendWA(e){
  e.preventDefault();
  var t = 'Namaste, my name is ' + document.getElementById('n').value +
          '. I need ' + document.getElementById('s').value + '. ' +
          document.getElementById('m').value;
  window.open('https://wa.me/{{ partners[0].whatsapp }}?text=' + encodeURIComponent(t), '_blank');
}
</script>
{% endblock %}"""

app.jinja_loader = DictLoader({
    "base.html": BASE,
    "home.html": HOME,
    "services.html": SERVICES_PAGE,
    "about.html": ABOUT,
    "contact.html": CONTACT,
})


@app.context_processor
def inject_globals():
    return {"b": BUSINESS, "partners": PARTNERS, "services": SERVICES}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)