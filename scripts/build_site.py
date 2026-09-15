from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"

MENU_URL = "https://bit.ly/4bmp3aV"
EMAIL = "starshavenchildcare@gmail.com"
PHONE_DISPLAY = "437-990-1634"
PHONE_LINK = "+14379901634"

NAV = [
    ("home", "Home", ""),
    ("about", "About", "about/"),
    ("programs", "Our program", "programs/"),
    ("enrolment", "Enrolment", "enrolment-waitlist/"),
    ("licensed", "Licensed care", "licensing-journey/"),
    ("contact", "Contact", "contact/"),
]

STAR = """<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="m24 3 6.1 13.2L45 18l-10.9 10 3 14.8L24 35.4l-13.1 7.4 3-14.8L3 18l14.9-1.8Z" fill="currentColor"/></svg>"""


def button(label: str, href: str, secondary: bool = False, external: bool = False) -> str:
    extra = ' target="_blank" rel="noopener"' if external else ""
    kind = " button-secondary" if secondary else ""
    icon = "↗" if external else "→"
    return f'<a class="button{kind}" href="{href}"{extra}>{label}<span aria-hidden="true">{icon}</span></a>'


def brand(prefix: str) -> str:
    return f"""<a class="brand" href="{prefix}" aria-label="Stars Haven Childcare home"><span class="brand-mark">{STAR}</span><span>Stars Haven<small>CHILDCARE</small></span></a>"""


def header(active: str, prefix: str) -> str:
    links = "".join(
        f'<a href="{prefix}{path}"' + (' aria-current="page"' if active == key else "") + f'>{label}</a>'
        for key, label, path in NAV
    )
    return f"""
<a class="skip-link" href="#main">Skip to main content</a>
<div class="topline">YMCA Licensed Home Childcare <span aria-hidden="true">·</span> Port of Newcastle, Ontario</div>
<header class="site-header">
  <div class="header-inner wrap">
    {brand(prefix)}
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" hidden>Menu <span aria-hidden="true">☰</span></button>
    <nav id="site-nav" class="site-nav" aria-label="Main navigation">{links}</nav>
  </div>
</header>"""


def footer(prefix: str) -> str:
    return f"""
<footer class="site-footer">
  <div class="footer-grid wrap">
    <div>{brand(prefix)}<p>Little moments. Meaningful connections.<br>A place for your child to shine.</p></div>
    <div><h2>Come say hello</h2><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a><p>Port of Newcastle, Ontario</p></div>
    <div><h2>Stay connected</h2><a href="https://www.facebook.com/profile.php?id=61578596607470" target="_blank" rel="noopener">Facebook</a><a href="{prefix}contact/">Contact Mary</a><a href="{prefix}privacy/">Website privacy</a></div>
  </div>
  <div class="footer-bottom wrap"><span>© 2026 Stars Haven Childcare</span><span>YMCA Licensed Home Childcare</span></div>
</footer>"""


def intro(eyebrow: str, title: str, lead: str) -> str:
    return f"""<section class="page-intro wrap"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="lead">{lead}</p></section>"""


def cta(prefix: str) -> str:
    return f"""<section class="cta wrap" aria-labelledby="cta-title"><div><p class="eyebrow">Let’s get to know your family</p><h2 id="cta-title">Your next little chapter<br>starts with a conversation.</h2><p>Tell us about your child, the care you need and your preferred start date.</p></div>{button('Enquire about care', prefix + 'enrolment-waitlist/')}</section>"""


def render(
    active: str,
    title: str,
    description: str,
    body: str,
    directory: str = "",
    robots: str = "index, follow",
    canonical_path: str | None = None,
) -> str:
    prefix = "../" if directory else "./"
    canonical_path = canonical_path if canonical_path is not None else (f"{directory}/" if directory else "")
    canonical_url = f"https://starshavenchildcare.ca/{canonical_path}"
    return f"""<!doctype html>
<html lang="en-CA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="{description}">
  <meta name="robots" content="{robots}">
  <meta name="theme-color" content="#263e36">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_CA">
  <meta property="og:site_name" content="Stars Haven Childcare">
  <meta property="og:title" content="{title} | Stars Haven Childcare">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical_url}">
  <meta name="twitter:card" content="summary">
  <title>{title} | Stars Haven Childcare</title>
  <link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg">
  <link rel="stylesheet" href="{prefix}assets/style.css">
  <script src="{prefix}assets/site.js" defer></script>
</head>
<body>
{header(active, prefix)}
<main id="main" tabindex="-1">{body}</main>
{footer(prefix)}
</body>
</html>
"""


HOME_BODY = f"""
<section class="hero wrap">
  <div class="hero-copy">
    <p class="eyebrow"><span class="tiny-star" aria-hidden="true">✦</span> Home childcare in Port of Newcastle</p>
    <h1>A place to <em>belong.</em><br>A world to discover.</h1>
    <p class="lead">Nurturing, play-based care where little ones grow in confidence, build friendships and find joy in everyday discoveries.</p>
    <div class="actions">{button('Enquire about care', './enrolment-waitlist/')}{button('Explore our program', './programs/', True)}</div>
    <p class="hero-note">Led by Mary Aliu, RECE <span aria-hidden="true">·</span> YMCA Licensed Home Childcare</p>
  </div>
  <div class="play-scene" aria-hidden="true"><span class="scene-small-star">✧</span><div class="scene-circle"></div><div class="scene-arch"></div><div class="scene-card"><span class="eyebrow">EVERY LITTLE ONE</span><span class="scene-words">Loved.<br>Seen.<br>Known.</span><span class="scene-spark">✦</span></div><div class="scene-block block-one">a</div><div class="scene-block block-two">b</div><div class="scene-block block-three">c</div><span class="scene-caption">room to play. space to grow.</span></div>
</section>
<section class="facts wrap" aria-label="Our childcare at a glance"><div><span class="fact-label">Our community</span><strong>Port of Newcastle</strong></div><div><span class="fact-label">Our age focus</span><strong>18 months–4 years</strong></div><div><span class="fact-label">Our setting</span><strong>Small group, home care</strong></div><div><span class="fact-label">Typical hours</span><strong>8:00 a.m.–4:00 p.m.</strong></div></section>
<section class="availability wrap" aria-label="Fees and availability"><div><span class="availability-dot" aria-hidden="true"></span><strong>Currently accepting childcare enquiries</strong></div><p>Stars Haven participates in CWELCC, with fees currently approximately $22 per day. Availability depends on your child’s age, schedule and preferred start date.</p></section>
<section class="section wrap">
  <div class="section-heading"><div><p class="eyebrow">Big care for little people</p><h2>Growing through play.<br>Grounded in love.</h2></div><p>Our mission is to nurture joyful, confident and kind-hearted children through rich play experiences, meaningful relationships and Christian values.</p></div>
  <div class="cards three"><article class="card card-cream"><span class="card-symbol" aria-hidden="true">✦</span><h3>A sense of belonging</h3><p>A welcoming small group where children are seen, supported and encouraged at their own pace.</p></article><article class="card card-sage"><span class="card-symbol" aria-hidden="true">○</span><h3>Joy in discovery</h3><p>Stories, building, sensory exploration, art and music make room for curiosity throughout the day.</p></article><article class="card card-peach"><span class="card-symbol" aria-hidden="true">⌁</span><h3>Everyday connection</h3><p>Gentle routines and communication with families help home and childcare feel connected.</p></article></div>
</section>
<section class="educator section wrap"><div class="educator-name"><p class="eyebrow">Meet your educator</p><h2>Hello, I’m Mary.</h2><span class="pill">Registered Early Childhood Educator</span></div><div><p class="lead">I lead Stars Haven Childcare, a YMCA Licensed Home Childcare program in the Port of Newcastle.</p><p>Our days bring together play, outdoor time, meals, rest and the small moments that help children feel comfortable and connected.</p><a class="text-link" href="./about/">Get to know Stars Haven <span aria-hidden="true">→</span></a></div></section>
{cta('./')}
"""

VALUES = [
    ("Love first", "Every child is loved, seen and known."),
    ("Belonging", "Children and families feel welcome and connected."),
    ("Joy in play", "Learning through laughter, curiosity and discovery."),
    ("Thoughtful care", "Careful attention to the environment, routines and relationships."),
    ("Faith and purpose", "Our approach is grounded in Christian values."),
    ("Growth", "Supporting confidence, independence and each child’s development."),
]

ABOUT_BODY = intro("A little more about us", "Care begins with connection.", "At Stars Haven, we nurture joyful, confident and kind-hearted children through rich play, meaningful relationships and Christian values.") + f"""
<section class="section wrap two-column"><div><p class="eyebrow">Your educator</p><h2>Mary Aliu, RECE</h2><p class="lead">Registered Early Childhood Educator and Stars Haven home childcare provider.</p></div><div><p>Stars Haven is a YMCA Licensed Home Childcare program in the Port of Newcastle. Our small group setting offers space for relationships, gentle transitions and learning through everyday play.</p><p>We value working with families. Sharing your child’s interests, routines and needs helps us get to know them and plan for their time in care.</p></div></section>
<section class="section wrap"><p class="eyebrow">What matters to us</p><h2>Our values, in everyday moments.</h2><div class="cards three">{''.join(f'<article class="card"><span class="value-number">0{i}</span><h3>{heading}</h3><p>{copy}</p></article>' for i, (heading, copy) in enumerate(VALUES, 1))}</div></section>
<section class="quote-band"><div class="wrap"><p class="eyebrow">Our vision</p><p class="vision">A beacon of faith-filled early learning where every child shines with purpose and belonging.</p></div></section>
{cta('../')}
"""

RHYTHM = [
    ("Arrival", "A gentle beginning", "Time to settle in, reconnect and choose something to explore."),
    ("Morning", "Play and discovery", "Stories, building, sensory play, movement and outdoor exploration."),
    ("Midday", "Nourishment and rest", "Lunch, quiet routines and rest time to recharge."),
    ("Afternoon", "More little adventures", "Snack, play, outdoor time and a warm goodbye."),
]

PROGRAM_BODY = intro("Room for curiosity", "Small moments.<br>Big discoveries.", "A play-based program with indoor and outdoor exploration, meals and snacks, rest, and time to connect.") + f"""
<section class="section wrap two-column"><div><p class="eyebrow">Our group</p><h2>Care for growing little ones.</h2></div><div><p>Our current age focus is 18 months to 4 years. Activities and routines are adapted to the children in care, with opportunities for sensory discovery, early language, creativity, movement and independence.</p><p>Availability depends on your child’s age, start date and care needs. Please get in touch to discuss a possible place.</p></div></section>
<section class="section wrap"><div class="section-heading"><div><p class="eyebrow">A familiar rhythm</p><h2>A day at Stars Haven.</h2></div><p>Our routine provides a familiar flow while allowing room for children’s interests, needs and the weather.</p></div><ol class="rhythm">{''.join(f'<li><span class="rhythm-time">{time}</span><div><h3>{heading}</h3><p>{copy}</p></div></li>' for time, heading, copy in RHYTHM)}</ol></section>
<section class="section wrap"><p class="eyebrow">Something to look forward to</p><h2>Our weekly play invitations.</h2><div class="week-grid">{''.join(f'<div><span>{day}</span><h3>{theme}</h3></div>' for day, theme in [('Monday','Blocks & books'),('Tuesday','Sensory play'),('Wednesday','Movement & dance'),('Thursday','Arts & crafts'),('Friday','Music & singing')])}</div></section>
<section class="meal-panel section wrap"><div><p class="eyebrow">Around the table</p><h2>Meals, snacks and time together.</h2><p>Meals and snacks are included in the program. Please discuss allergies and dietary needs with Mary before enrolment.</p></div>{button('View our two-week menu', MENU_URL, True, True)}</section>
{cta('../')}
"""

FAQ = [
    ("How do I enquire about a place?", "Complete the pre-enrolment form with your child’s age, preferred start date and care needs. Mary will follow up to discuss availability and next steps."),
    ("Does completing the form reserve a space?", "No. The form is an enquiry or waitlist request. A childcare place and start date need to be confirmed through the enrolment process."),
    ("What are the program hours?", "Typical program hours are 8:00 a.m. to 4:00 p.m., Monday to Friday, with occasional flexibility. Please discuss the drop-off and pick-up times you need with Mary before enrolment."),
    ("How are fees handled?", "All childcare fees are managed through YMCA Home Childcare. Stars Haven participates in CWELCC, with fees currently approximately $22 per day. Confirm the applicable fee during registration."),
    ("How will I hear about my child’s day?", "Brightwheel is used to share updates and communicate with enrolled families. Families will be informed if the communication arrangements change."),
    ("What should my child bring?", "Label belongings and prepare diapers or toileting supplies, changes of clothing, suitable outdoor clothing, and any agreed rest-time items. Your welcome information will include the full list for your child."),
    ("Can we arrange a meet and greet?", "Yes. Get in touch or complete the pre-enrolment form so we can discuss your needs and arrange a suitable time."),
]

ENROLMENT_BODY = intro("A thoughtful start", "Let’s find the right fit.", "Tell us a little about your child and the childcare you’re looking for. We’ll take the next steps together.") + f"""
<section class="enrol-panel wrap"><div><h2>Start with an enquiry.</h2><p>Complete the form below to enquire about care or ask to join the waitlist.</p><p class="small">Submitting an enquiry does not guarantee or reserve a childcare space.</p></div><a class="button button-secondary" href="#pre-enrolment-form">Go to the form<span aria-hidden="true">↓</span></a></section>
<section class="section wrap form-section" aria-labelledby="form-title"><div class="form-heading"><p class="eyebrow">Pre-enrolment form</p><h2 id="form-title">Tell us about your childcare needs.</h2><p>Fields marked with an asterisk are required. Mary will review your enquiry and contact you about availability and next steps.</p></div>
<form id="pre-enrolment-form" class="native-form" name="pre-enrolment" method="POST" action="/thank-you" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="pre-enrolment">
  <input type="hidden" name="subject" value="New Stars Haven pre-enrolment enquiry">
  <p class="bot-field"><label>Leave this field empty: <input name="bot-field" autocomplete="off"></label></p>
  <div class="form-grid">
    <label><span>Parent/guardian full name <b aria-hidden="true">*</b></span><input type="text" name="parent-name" autocomplete="name" required></label>
    <label><span>Email address <b aria-hidden="true">*</b></span><input type="email" name="email" autocomplete="email" required></label>
    <label><span>Phone number <b aria-hidden="true">*</b></span><input type="tel" name="phone" autocomplete="tel" required></label>
    <label><span>Child’s full name <b aria-hidden="true">*</b></span><input type="text" name="child-name" required></label>
    <label><span>Child’s date of birth <b aria-hidden="true">*</b></span><input type="date" name="child-date-of-birth" required></label>
    <label><span>Preferred start date <b aria-hidden="true">*</b></span><input type="date" name="preferred-start-date" required></label>
    <label><span>Preferred drop-off time <b aria-hidden="true">*</b></span><input type="time" name="preferred-drop-off-time" required></label>
    <label><span>Preferred pickup time <b aria-hidden="true">*</b></span><input type="time" name="preferred-pickup-time" required></label>
    <fieldset><legend>Care needed <b aria-hidden="true">*</b></legend><div class="choice-row"><label><input type="radio" name="care-needs" value="Full-time" required> Full-time</label><label><input type="radio" name="care-needs" value="Part-time"> Part-time</label></div></fieldset>
    <fieldset><legend>Current location <b aria-hidden="true">*</b></legend><select name="current-location" required><option value="">Select your area</option><option>Newcastle</option><option>Bowmanville</option><option>Courtice</option><option>Other</option></select></fieldset>
    <fieldset class="full"><legend>Preferred days <b aria-hidden="true">*</b></legend><div class="choice-grid"><label><input type="checkbox" name="preferred-days" value="Monday"> Monday</label><label><input type="checkbox" name="preferred-days" value="Tuesday"> Tuesday</label><label><input type="checkbox" name="preferred-days" value="Wednesday"> Wednesday</label><label><input type="checkbox" name="preferred-days" value="Thursday"> Thursday</label><label><input type="checkbox" name="preferred-days" value="Friday"> Friday</label></div><p class="field-note">Select all days that apply.</p></fieldset>
    <label class="full"><span>Allergies, special needs or medical considerations</span><textarea name="allergies-and-considerations" rows="4" placeholder="Write None if there are no considerations to share."></textarea></label>
    <label><span>How did you hear about Stars Haven? <b aria-hidden="true">*</b></span><select name="referral-source" required><option value="">Choose one</option><option>Friend or family</option><option>Facebook</option><option>Instagram</option><option>Local parent group</option><option>Flyer or community centre</option><option>Other</option></select></label>
    <fieldset><legend>Join the waitlist if no space is available? <b aria-hidden="true">*</b></legend><div class="choice-row"><label><input type="radio" name="join-waitlist" value="Yes" required> Yes</label><label><input type="radio" name="join-waitlist" value="No"> No</label></div></fieldset>
    <label class="full"><span>Additional comments or questions</span><textarea name="comments" rows="5"></textarea></label>
  </div>
  <p class="form-privacy">Your information will be used only to respond to your childcare enquiry. See our <a href="../privacy/">website privacy information</a>.</p>
  <button class="button submit-button" type="submit">Send enquiry <span aria-hidden="true">→</span></button>
</form></section>
<section class="section wrap"><p class="eyebrow">What happens next</p><h2>Three steps to get acquainted.</h2><ol class="cards three steps"><li class="card"><span class="value-number">01</span><h3>Share your needs</h3><p>Tell us your child’s age, preferred start date and the days and hours you need.</p></li><li class="card"><span class="value-number">02</span><h3>Connect with Mary</h3><p>Discuss availability, ask questions and arrange a meet and greet when appropriate.</p></li><li class="card"><span class="value-number">03</span><h3>Plan the next steps</h3><p>If a place is agreed, complete the YMCA registration process and discuss your child’s transition.</p></li></ol></section>
<section class="section wrap faq-section"><div><p class="eyebrow">Questions are welcome</p><h2>A few things families ask.</h2></div><div class="faq-list">{''.join(f'<details><summary>{question}</summary><p>{answer}</p></details>' for question, answer in FAQ)}</div></section>
"""

LICENSED_BODY = intro("YMCA Licensed Home Childcare", "A home setting.<br>A licensed program.", "Stars Haven operates as YMCA Licensed Home Childcare in the Port of Newcastle.") + f"""
<section class="section wrap two-column"><div><p class="eyebrow">Our program today</p><h2>Care led by Mary Aliu, RECE.</h2></div><div><p>Stars Haven provides small group home childcare with a Registered Early Childhood Educator. Our program brings together play, everyday routines and communication with families.</p><p>Childcare registration and fees are managed through YMCA Home Childcare. Mary can guide you through the next steps when a suitable place is available.</p></div></section>
<section class="section wrap cards two"><article class="card card-sage"><p class="eyebrow">Enrolment</p><h2>Get to know the program.</h2><p>Ask about the setting, routines, your child’s needs and the registration process.</p><a class="text-link" href="../enrolment-waitlist/">Enrolment information <span aria-hidden="true">→</span></a></article><article class="card card-cream"><p class="eyebrow">Fees</p><h2>CWELCC participation.</h2><p>Childcare fees are currently approximately $22 per day through CWELCC. The applicable fee is confirmed through YMCA registration.</p><p class="small">Please ask about your family’s circumstances and any applicable subsidy arrangements.</p></article></section>
{cta('../')}
"""

CONTACT_BODY = intro("We’d love to hear from you", "Hello, neighbour.", "Whether you’re exploring your options or ready to enquire, let’s talk about what your family needs.") + f"""
<section class="section wrap contact-grid"><div class="contact-card"><p class="eyebrow">Get in touch</p><h2>Speak with Mary.</h2><dl><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>Phone</dt><dd><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></dd></div><div><dt>Location</dt><dd>Port of Newcastle, Ontario</dd></div><div><dt>Typical hours</dt><dd>Monday–Friday, 8:00 a.m.–4:00 p.m.<br><span class="small">Occasional flexibility may be discussed with Mary.</span></dd></div></dl></div><div class="contact-aside"><span class="card-symbol" aria-hidden="true">✦</span><h2>Looking for childcare?</h2><p>Our pre-enrolment form is a helpful place to tell us about your child and your preferred schedule.</p>{button('Enquire about care', '../enrolment-waitlist/')}<p class="small">We can also discuss a meet and greet at a suitable time.</p></div></section>
"""

PRIVACY_BODY = intro("Website information", "Your enquiry, your choice.", "You can browse this website without submitting personal information.") + f"""
<section class="section wrap prose"><h2>Browsing the website</h2><p>This website does not include analytics scripts or advertising trackers. The hosting provider may process technical information, such as IP addresses and request logs, to deliver and protect the site.</p><h2>Enrolment enquiries</h2><p>The pre-enrolment form is processed and stored by Netlify on behalf of Stars Haven Childcare. The information you provide is used to assess your childcare needs, contact you about availability and manage your enquiry or waitlist request. Please provide only information that is relevant to your childcare enquiry.</p><h2>Access and retention</h2><p>Access is limited to Stars Haven and service providers needed to process your enquiry. Information is kept only as long as reasonably needed for the enquiry or waitlist process and any applicable recordkeeping, then removed.</p><h2>Your choices</h2><p>You may request access to, correction of or deletion of information you submitted by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p><h2>Other links</h2><p>Menu and social links open services with their own privacy practices. Contacting us by email or telephone uses your chosen email or telephone service.</p></section>
"""

THANK_YOU_BODY = intro("Enquiry received", "Thank you for getting in touch.", "Your pre-enrolment enquiry has been submitted to Stars Haven Childcare.") + f"""
<section class="section wrap prose"><h2>What happens next?</h2><p>Mary will review the information you provided and contact you about availability and next steps. Submitting an enquiry does not guarantee or reserve a childcare space.</p><div class="actions">{button('Return to the homepage', '../')}{button('Contact Mary', '../contact/', True)}</div></section>
"""


PAGES = {
    "index.html": render("home", "Home childcare in Port of Newcastle", "Stars Haven Childcare is a YMCA Licensed Home Childcare program in Port of Newcastle, led by Mary Aliu, RECE.", HOME_BODY),
    "home/index.html": render("home", "Home childcare in Port of Newcastle", "Nurturing, play-based home childcare in Port of Newcastle.", HOME_BODY.replace('href="./', 'href="../'), "home", robots="noindex, follow", canonical_path=""),
    "about/index.html": render("about", "About Mary and Stars Haven", "Meet Mary Aliu, RECE, and learn about the values behind Stars Haven Childcare in Port of Newcastle.", ABOUT_BODY, "about"),
    "programs/index.html": render("programs", "Our play-based program", "Explore the daily rhythm, weekly activities and meals at Stars Haven Childcare.", PROGRAM_BODY, "programs"),
    "enrolment-waitlist/index.html": render("enrolment", "Enrolment and waitlist", "Enquire about childcare or join the Stars Haven waitlist. Learn what happens next and find answers to common questions.", ENROLMENT_BODY, "enrolment-waitlist"),
    "licensing-journey/index.html": render("licensed", "YMCA licensed home childcare", "Information about Stars Haven’s current YMCA Licensed Home Childcare program and enrolment.", LICENSED_BODY, "licensing-journey"),
    "contact/index.html": render("contact", "Contact Stars Haven", "Contact Mary at Stars Haven Childcare in Port of Newcastle to discuss availability, care needs and a meet and greet.", CONTACT_BODY, "contact"),
    "privacy/index.html": render("", "Website privacy", "How Stars Haven Childcare handles website and pre-enrolment enquiry information.", PRIVACY_BODY, "privacy"),
    "thank-you/index.html": render("", "Thank you", "Confirmation that a Stars Haven Childcare pre-enrolment enquiry was submitted.", THANK_YOU_BODY, "thank-you", robots="noindex, follow"),
}

PAGES["404.html"] = render(
    "",
    "Page not found",
    "The requested Stars Haven Childcare page could not be found.",
    intro("Page not found", "Let’s get you back home.", "This page may have moved. You can return to the homepage or contact Mary.")
    + f'<section class="wrap section">{button("Go to the homepage", "./")}</section>',
    robots="noindex, follow",
    canonical_path="404.html",
)


def write_pages() -> None:
    for relative_path, content in PAGES.items():
        destination = SITE / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
    (SITE / "_redirects").write_text("/home  /  301!\n/home/  /  301!\n", encoding="utf-8")


if __name__ == "__main__":
    write_pages()
    print(f"Built {len(PAGES)} pages in {SITE}")
