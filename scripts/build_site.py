from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"

ACADEMY_EMAIL = "starshavenacademy@gmail.com"
WEBSITE_URL = "https://starshavenchildcare.ca"
FACEBOOK_URL = "https://www.facebook.com/profile.php?id=61578596607470"
INSTAGRAM_URL = "https://www.instagram.com/starshavenacademy/"
MENU_URL = "https://bit.ly/4bmp3aV"

NAV = [
    ("home", "Home", ""),
    ("about", "About", "about/"),
    ("services", "Services", "services/"),
    ("families", "For families", "families/"),
    ("professionals", "For professionals", "professionals/"),
    ("childcare", "Childcare", "childcare/"),
    ("book", "Book", "book/"),
]

STAR = """<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="m24 3 6.1 13.2L45 18l-10.9 10 3 14.8L24 35.4l-13.1 7.4 3-14.8L3 18l14.9-1.8Z" fill="currentColor"/></svg>"""


def button(label: str, href: str, secondary: bool = False, external: bool = False) -> str:
    extra = ' target="_blank" rel="noopener"' if external else ""
    kind = " button-secondary" if secondary else ""
    icon = "↗" if external else "→"
    return f'<a class="button{kind}" href="{href}"{extra}>{label}<span aria-hidden="true">{icon}</span></a>'


def brand(prefix: str) -> str:
    return f"""<a class="brand" href="{prefix}" aria-label="Stars Haven Academy home"><span class="brand-mark">{STAR}</span><span>Stars Haven<small>ACADEMY</small></span></a>"""


def header(active: str, prefix: str) -> str:
    links = "".join(
        f'<a href="{prefix}{path}"' + (' aria-current="page"' if active == key else "") + f'>{label}</a>'
        for key, label, path in NAV
    )
    return f"""
<a class="skip-link" href="#main">Skip to main content</a>
<div class="topline">Family &amp; Early Years Support <span aria-hidden="true">·</span> Education, consultation and coaching</div>
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
    <div>{brand(prefix)}<p>Practical support for the adults who help children grow.</p></div>
    <div><h2>Connect</h2><a href="mailto:{ACADEMY_EMAIL}">{ACADEMY_EMAIL}</a><a href="{WEBSITE_URL}">starshavenchildcare.ca</a><p>Ontario, Canada</p></div>
    <div><h2>Follow</h2><a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">Instagram</a><a href="{FACEBOOK_URL}" target="_blank" rel="noopener">Facebook</a><a href="{prefix}book/">Book a consultation</a><a href="{prefix}privacy/">Privacy</a></div>
  </div>
  <div class="footer-bottom wrap"><span>© 2026 Stars Haven Academy</span><span>Family &amp; Early Years Partner</span></div>
</footer>"""


def intro(eyebrow: str, title: str, lead: str) -> str:
    return f"""<section class="page-intro wrap"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="lead">{lead}</p></section>"""


def cta(prefix: str, title: str = "Start with a conversation.") -> str:
    return f"""<section class="cta wrap" aria-labelledby="cta-title"><div><p class="eyebrow">Book a consultation</p><h2 id="cta-title">{title}</h2><p>Share what you are navigating and request a time to speak with Mary.</p></div>{button('Request a time', prefix + 'book/')}</section>"""


def render(active: str, title: str, description: str, body: str, directory: str = "", robots: str = "index, follow", canonical_path: str | None = None) -> str:
    prefix = "../" if directory else "./"
    canonical_path = canonical_path if canonical_path is not None else (f"{directory}/" if directory else "")
    canonical_url = f"{WEBSITE_URL}/{canonical_path}"
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
  <meta property="og:site_name" content="Stars Haven Academy">
  <meta property="og:title" content="{title} | Stars Haven Academy">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical_url}">
  <meta name="twitter:card" content="summary">
  <title>{title} | Stars Haven Academy</title>
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
    <p class="eyebrow"><span class="tiny-star" aria-hidden="true">✦</span> Family &amp; Early Years Partner</p>
    <h1>Practical support.<br><em>Stronger connections.</em></h1>
    <p class="lead">Stars Haven Academy provides practical, evidence-informed support to parents and early-learning professionals in children’s emotional development, routines, behaviour, communication, play and inclusion.</p>
    <div class="actions">{button('Book a consultation', './book/')}{button('Explore services', './services/', True)}</div>
    <p class="hero-note">Led by Mary Aliu, RECE <span aria-hidden="true">·</span> Education, consultation, observation, coaching and referral support</p>
  </div>
  <div class="play-scene" aria-hidden="true"><span class="scene-small-star">✧</span><div class="scene-circle"></div><div class="scene-arch"></div><div class="scene-card"><span class="eyebrow">SUPPORT THAT IS</span><span class="scene-words">Practical.<br>Thoughtful.<br>Connected.</span><span class="scene-spark">✦</span></div><div class="scene-block block-one">a</div><div class="scene-block block-two">b</div><div class="scene-block block-three">c</div><span class="scene-caption">understand. respond. grow.</span></div>
</section>
<section class="facts wrap" aria-label="Stars Haven Academy at a glance"><div><span class="fact-label">For families</span><strong>Clear, practical guidance</strong></div><div><span class="fact-label">For professionals</span><strong>Reflective consultation</strong></div><div><span class="fact-label">Our approach</span><strong>Evidence-informed</strong></div><div><span class="fact-label">Our scope</span><strong>Educational, not clinical</strong></div></section>
<section class="section wrap">
  <div class="section-heading"><div><p class="eyebrow">Support for everyday challenges</p><h2>Understand what is happening.<br>Plan what to try next.</h2></div><p>We turn early-years knowledge into realistic strategies that fit the child, the adults supporting them and the setting around them.</p></div>
  <div class="cards three"><article class="card card-cream"><span class="card-symbol" aria-hidden="true">✦</span><h3>For parents and caregivers</h3><p>Consultation and coaching around routines, behaviour, emotions, communication, play and inclusion.</p><a class="text-link" href="./families/">Support for families <span aria-hidden="true">→</span></a></article><article class="card card-sage"><span class="card-symbol" aria-hidden="true">○</span><h3>For early-learning professionals</h3><p>Observation, reflective consultation and practical planning for responsive, inclusive practice.</p><a class="text-link" href="./professionals/">Professional support <span aria-hidden="true">→</span></a></article><article class="card card-peach"><span class="card-symbol" aria-hidden="true">⌁</span><h3>Workshops and resources</h3><p>Clear learning sessions and tools for families, teams and community organizations.</p><a class="text-link" href="./services/">View all services <span aria-hidden="true">→</span></a></article></div>
</section>
<section class="scope-note wrap"><div><p class="eyebrow">Clear professional scope</p><h2>Educational support with responsible referrals.</h2></div><p>Mary Aliu, RECE, offers education, consultation, observation, coaching and referral support. Stars Haven Academy does not diagnose, provide psychotherapy or advertise treatment for mental illness. When clinical support is required, we recommend connecting with an appropriately regulated professional.</p></section>
<section class="educator section wrap"><div class="educator-name"><p class="eyebrow">Meet your partner</p><h2>Hello, I’m Mary.</h2><span class="pill">Registered Early Childhood Educator</span></div><div><p class="lead">I help adults understand children’s development and turn concerns into thoughtful, manageable next steps.</p><p>My approach combines early-years knowledge, observation, collaboration and respect for each family or learning setting.</p><a class="text-link" href="./about/">Learn more about Mary <span aria-hidden="true">→</span></a></div></section>
{cta('./')}
"""


ABOUT_BODY = intro("About Mary", "Early-years knowledge.<br>Practical partnership.", "Mary Aliu is a Registered Early Childhood Educator and the founder of Stars Haven Academy.") + f"""
<section class="section wrap two-column"><div><p class="eyebrow">Mary Aliu, RECE</p><h2>Helping adults support children with clarity and confidence.</h2></div><div><p>Mary’s work is grounded in child development, responsive relationships, play-based learning, observation and collaboration with families and professionals.</p><p>Her experience includes licensed home childcare, early-learning programs, family communication, program planning and inclusive early-years practice.</p><p>Stars Haven Academy makes that knowledge accessible through education, consultation, observation, coaching, workshops and referral support.</p></div></section>
<section class="section wrap"><p class="eyebrow">How we work</p><h2>Thoughtful support, clearly defined.</h2><div class="cards three"><article class="card"><span class="value-number">01</span><h3>Listen first</h3><p>Begin with the child, the concern, the setting and what has already been tried.</p></article><article class="card"><span class="value-number">02</span><h3>Make it practical</h3><p>Translate early-years knowledge into realistic strategies and manageable next steps.</p></article><article class="card"><span class="value-number">03</span><h3>Stay within scope</h3><p>Provide education and coaching, with referral to regulated clinical professionals when needed.</p></article></div></section>
{cta('../')}
"""


SERVICES_BODY = intro("Services", "Support designed around real early-years questions.", "Choose a focused consultation, observation and planning support, or learning for a wider team or community.") + f"""
<section class="section wrap"><div class="cards two"><article class="card card-cream"><p class="eyebrow">One-to-one</p><h2>Family consultation</h2><p>Practical education and coaching for parents and caregivers navigating routines, behaviour, emotional development, communication, play or inclusion.</p></article><article class="card card-sage"><p class="eyebrow">Reflective practice</p><h2>Professional consultation</h2><p>Collaborative support for educators and early-learning professionals considering responsive strategies, environments, family communication and inclusion.</p></article><article class="card card-peach"><p class="eyebrow">Look, understand, plan</p><h2>Observation and action planning</h2><p>Non-diagnostic observation of a child or early-learning setting, followed by practical reflections, priorities and suggested next steps.</p></article><article class="card"><p class="eyebrow">Shared learning</p><h2>Workshops and resources</h2><p>Learning sessions and practical tools for parent groups, early-learning teams and community organizations. Topics can be adapted to the audience.</p></article></div></section>
<section class="scope-note wrap"><div><p class="eyebrow">Important</p><h2>This is not clinical care.</h2></div><p>Services are educational and consultative. Stars Haven Academy does not diagnose conditions, conduct clinical assessments, provide psychotherapy or treat mental illness. Urgent, diagnostic or clinical concerns should be directed to an appropriate regulated professional or emergency service.</p></section>
{cta('../', 'Choose a helpful next step.')}
"""


FAMILIES_BODY = intro("For parents and caregivers", "Support for the moments that feel hard to untangle.", "Talk through what you are noticing, understand the developmental context and leave with practical ideas to try.") + f"""
<section class="section wrap two-column"><div><p class="eyebrow">What we can explore</p><h2>Everyday questions about development and family life.</h2></div><div><ul class="service-list"><li>Emotional development and co-regulation</li><li>Daily routines, transitions and sleep-related routines</li><li>Age-appropriate behaviour guidance</li><li>Communication, interaction and play</li><li>Preparing for childcare or school transitions</li><li>Participation, belonging and inclusion</li></ul></div></section>
<section class="section wrap"><p class="eyebrow">What to expect</p><h2>A collaborative, practical process.</h2><ol class="cards three steps"><li class="card"><span class="value-number">01</span><h3>Share the concern</h3><p>Describe what you are seeing, what matters most and what you have already tried.</p></li><li class="card"><span class="value-number">02</span><h3>Build understanding</h3><p>Consider development, relationships, routines, communication and the surrounding environment.</p></li><li class="card"><span class="value-number">03</span><h3>Plan next steps</h3><p>Leave with realistic strategies, useful resources and referral guidance when needed.</p></li></ol></section>
{cta('../', 'You do not have to figure it out alone.')}
"""


PROFESSIONALS_BODY = intro("For early-learning professionals", "A reflective partner for thoughtful practice.", "Step back from a concern, examine the context and develop practical strategies that support children, families and educators.") + f"""
<section class="section wrap two-column"><div><p class="eyebrow">Consultation and learning</p><h2>Support for individual educators, teams and organizations.</h2></div><div><ul class="service-list"><li>Responsive relationships and behaviour guidance</li><li>Observation and non-diagnostic reflection</li><li>Inclusive environments and participation</li><li>Routines, transitions and play-based learning</li><li>Family communication and partnership</li><li>Workshops, resource development and team learning</li></ul></div></section>
<section class="quote-band"><div class="wrap"><p class="eyebrow">Our approach</p><p class="vision">Reflective, evidence-informed and focused on strategies that can work in real early-learning settings.</p></div></section>
{cta('../', 'Bring a question, concern or learning goal.')}
"""


BOOK_BODY = intro("Book a consultation", "Request a time to talk.", "Tell us what kind of support you are looking for and suggest a convenient date and time. Mary will confirm availability by email.") + f"""
<section class="enrol-panel wrap"><div><h2>Before you submit</h2><p>Submitting this form requests an appointment; it does not confirm one. Stars Haven Academy provides educational and consultative support rather than diagnosis, psychotherapy or emergency services.</p></div><a class="button button-secondary" href="#consultation-form">Go to the form<span aria-hidden="true">↓</span></a></section>
<section class="section wrap form-section" aria-labelledby="form-title"><div class="form-heading"><p class="eyebrow">Consultation request</p><h2 id="form-title">What would you like support with?</h2><p>Fields marked with an asterisk are required. No phone number is requested.</p></div>
<form id="consultation-form" class="native-form" name="consultation-request" method="POST" action="/booking-thank-you" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="consultation-request"><input type="hidden" name="subject" value="New Stars Haven Academy consultation request">
  <p class="bot-field"><label>Leave this field empty: <input name="bot-field" autocomplete="off"></label></p>
  <div class="form-grid">
    <label><span>Full name <b aria-hidden="true">*</b></span><input type="text" name="name" autocomplete="name" required></label><label><span>Email address <b aria-hidden="true">*</b></span><input type="email" name="email" autocomplete="email" required></label>
    <label><span>I am a… <b aria-hidden="true">*</b></span><select name="client-type" required><option value="">Choose one</option><option>Parent or caregiver</option><option>Early-learning professional</option><option>Organization or community group</option><option>Other</option></select></label><label><span>Support requested <b aria-hidden="true">*</b></span><select name="service" required><option value="">Choose one</option><option>Family consultation</option><option>Professional consultation</option><option>Observation and action planning</option><option>Workshop or team learning</option><option>Not sure yet</option></select></label>
    <label><span>Preferred date <b aria-hidden="true">*</b></span><input type="date" name="preferred-date" required></label><label><span>Preferred time <b aria-hidden="true">*</b></span><input type="time" name="preferred-time" required></label>
    <label><span>Meeting format <b aria-hidden="true">*</b></span><select name="meeting-format" required><option value="">Choose one</option><option>Virtual</option><option>In person, if available</option><option>Either</option></select></label><label><span>Main area of support <b aria-hidden="true">*</b></span><select name="support-area" required><option value="">Choose one</option><option>Emotional development</option><option>Routines or transitions</option><option>Behaviour guidance</option><option>Communication</option><option>Play</option><option>Inclusion</option><option>Professional practice</option><option>Other</option></select></label>
    <label class="full"><span>Briefly describe what you would like to discuss <b aria-hidden="true">*</b></span><textarea name="message" rows="6" required></textarea></label>
    <label class="full consent"><input type="checkbox" name="scope-acknowledgement" value="Agreed" required> <span>I understand that Stars Haven Academy provides educational and consultative support, not diagnosis, psychotherapy, treatment or emergency services. <b aria-hidden="true">*</b></span></label>
  </div>
  <p class="form-privacy">Your information will be used to respond to this request and arrange the consultation. See our <a href="../privacy/">privacy information</a>.</p><button class="button submit-button" type="submit">Request a time <span aria-hidden="true">→</span></button>
</form></section>
"""


CHILDCARE_BODY = intro("Stars Haven Childcare", "Licensed home childcare, now in one simple place.", "Stars Haven Childcare is a YMCA Licensed Home Childcare program in the Port of Newcastle and a secondary service of Stars Haven Academy.") + f"""
<section class="facts wrap" aria-label="Childcare at a glance"><div><span class="fact-label">Age focus</span><strong>18 months–4 years</strong></div><div><span class="fact-label">Typical hours</span><strong>8:00 a.m.–4:00 p.m.</strong></div><div><span class="fact-label">Setting</span><strong>Small group, home care</strong></div><div><span class="fact-label">Fees</span><strong>Approximately $22/day</strong></div></section>
<section class="section wrap two-column"><div><p class="eyebrow">YMCA licensed care</p><h2>Play-based care in the Port of Newcastle.</h2></div><div><p>Led by Mary Aliu, RECE, the program includes play, outdoor time, meals and snacks, rest, and communication with families.</p><p>Childcare registration and fees are managed through YMCA Home Childcare. Stars Haven participates in CWELCC; the applicable fee is confirmed through YMCA registration.</p><div class="actions">{button('View the two-week menu', MENU_URL, True, True)}<a class="text-link" href="#pre-enrolment-form">Go to the childcare form <span aria-hidden="true">↓</span></a></div></div></section>
<section class="section wrap form-section" aria-labelledby="childcare-form-title"><div class="form-heading"><p class="eyebrow">Childcare pre-enrolment</p><h2 id="childcare-form-title">Tell us about your childcare needs.</h2><p>Submitting an enquiry does not guarantee or reserve a childcare space.</p></div>
<form id="pre-enrolment-form" class="native-form" name="pre-enrolment" method="POST" action="/childcare-thank-you" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="pre-enrolment"><input type="hidden" name="subject" value="New Stars Haven childcare enquiry"><p class="bot-field"><label>Leave this field empty: <input name="bot-field" autocomplete="off"></label></p>
  <div class="form-grid">
    <label><span>Parent/guardian full name <b aria-hidden="true">*</b></span><input type="text" name="parent-name" autocomplete="name" required></label><label><span>Email address <b aria-hidden="true">*</b></span><input type="email" name="email" autocomplete="email" required></label>
    <label><span>Parent/guardian phone number <b aria-hidden="true">*</b></span><input type="tel" name="phone" autocomplete="tel" required></label><label><span>Child’s full name <b aria-hidden="true">*</b></span><input type="text" name="child-name" required></label>
    <label><span>Child’s date of birth <b aria-hidden="true">*</b></span><input type="date" name="child-date-of-birth" required></label><label><span>Preferred start date <b aria-hidden="true">*</b></span><input type="date" name="preferred-start-date" required></label>
    <label><span>Preferred drop-off time <b aria-hidden="true">*</b></span><input type="time" name="preferred-drop-off-time" required></label><label><span>Preferred pickup time <b aria-hidden="true">*</b></span><input type="time" name="preferred-pickup-time" required></label>
    <fieldset><legend>Care needed <b aria-hidden="true">*</b></legend><div class="choice-row"><label><input type="radio" name="care-needs" value="Full-time" required> Full-time</label><label><input type="radio" name="care-needs" value="Part-time"> Part-time</label></div></fieldset><fieldset><legend>Current location <b aria-hidden="true">*</b></legend><select name="current-location" required><option value="">Select your area</option><option>Newcastle</option><option>Bowmanville</option><option>Courtice</option><option>Other</option></select></fieldset>
    <fieldset class="full"><legend>Preferred days <b aria-hidden="true">*</b></legend><div class="choice-grid"><label><input type="checkbox" name="preferred-days" value="Monday"> Monday</label><label><input type="checkbox" name="preferred-days" value="Tuesday"> Tuesday</label><label><input type="checkbox" name="preferred-days" value="Wednesday"> Wednesday</label><label><input type="checkbox" name="preferred-days" value="Thursday"> Thursday</label><label><input type="checkbox" name="preferred-days" value="Friday"> Friday</label></div><p class="field-note">Select all days that apply.</p></fieldset>
    <label class="full"><span>Allergies, special needs or medical considerations</span><textarea name="allergies-and-considerations" rows="4" placeholder="Write None if there are no considerations to share."></textarea></label>
    <label><span>How did you hear about Stars Haven? <b aria-hidden="true">*</b></span><select name="referral-source" required><option value="">Choose one</option><option>Friend or family</option><option>Facebook</option><option>Instagram</option><option>Local parent group</option><option>Flyer or community centre</option><option>Other</option></select></label><fieldset><legend>Join the waitlist if no space is available? <b aria-hidden="true">*</b></legend><div class="choice-row"><label><input type="radio" name="join-waitlist" value="Yes" required> Yes</label><label><input type="radio" name="join-waitlist" value="No"> No</label></div></fieldset>
    <label class="full"><span>Additional comments or questions</span><textarea name="comments" rows="5"></textarea></label>
  </div>
  <p class="form-privacy">Your information will be used only to respond to your childcare enquiry. See our <a href="../privacy/">privacy information</a>.</p><button class="button submit-button" type="submit">Send childcare enquiry <span aria-hidden="true">→</span></button>
</form></section>
"""


CONTACT_BODY = intro("Contact", "Choose the easiest way to connect.", "Request a consultation, send an email or follow Stars Haven Academy online.") + f"""
<section class="section wrap contact-grid"><div class="contact-card"><p class="eyebrow">Contact Stars Haven Academy</p><h2>Connect with Mary.</h2><dl><div><dt>Email</dt><dd><a href="mailto:{ACADEMY_EMAIL}">{ACADEMY_EMAIL}</a></dd></div><div><dt>Website</dt><dd><a href="{WEBSITE_URL}">starshavenchildcare.ca</a></dd></div><div><dt>Instagram</dt><dd><a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">@StarsHavenAcademy</a></dd></div><div><dt>Facebook</dt><dd><a href="{FACEBOOK_URL}" target="_blank" rel="noopener">Stars Haven on Facebook</a></dd></div></dl></div><div class="contact-aside"><span class="card-symbol" aria-hidden="true">✦</span><h2>Ready to talk?</h2><p>Use the consultation request form to share the support you are looking for and suggest a suitable time.</p>{button('Book a consultation', '../book/')}<p class="small">Mary will confirm availability by email.</p></div></section>
"""


PRIVACY_BODY = intro("Privacy", "Your information, your choice.", "You can browse this website without submitting personal information.") + f"""
<section class="section wrap prose"><h2>Browsing the website</h2><p>This website does not include analytics scripts or advertising trackers. The hosting provider may process technical information, such as IP addresses and request logs, to deliver and protect the site.</p><h2>Consultation requests</h2><p>The consultation form is processed and stored by Netlify on behalf of Stars Haven Academy. The information you provide is used to understand your request, contact you and arrange a consultation. Do not use the form for emergencies or include sensitive clinical information beyond what is reasonably needed for the initial request.</p><h2>Childcare enquiries</h2><p>The childcare form is used to assess childcare needs, contact families about availability and manage enquiries or waitlist requests.</p><h2>Access and retention</h2><p>Access is limited to Stars Haven and service providers needed to process your request. Information is kept only as long as reasonably needed for the enquiry, booking or waitlist process and applicable recordkeeping, then removed.</p><h2>Your choices</h2><p>You may request access to, correction of or deletion of information you submitted by emailing <a href="mailto:{ACADEMY_EMAIL}">{ACADEMY_EMAIL}</a>.</p><h2>Other services</h2><p>Social-media and email links open services with their own privacy practices.</p></section>
"""


BOOKING_THANK_YOU_BODY = intro("Request received", "Thank you for reaching out.", "Your consultation request has been submitted to Stars Haven Academy.") + f"""<section class="section wrap prose"><h2>What happens next?</h2><p>Mary will review your request and reply by email to confirm whether the proposed time is available or suggest another option.</p><div class="actions">{button('Return to the homepage', '../')}{button('View services', '../services/', True)}</div></section>"""
CHILDCARE_THANK_YOU_BODY = intro("Childcare enquiry received", "Thank you for getting in touch.", "Your childcare pre-enrolment enquiry has been submitted.") + f"""<section class="section wrap prose"><h2>What happens next?</h2><p>Mary will review the information and contact you about availability and next steps. Submitting an enquiry does not guarantee or reserve a childcare space.</p><div class="actions">{button('Return to the Academy', '../')}{button('Childcare information', '../childcare/', True)}</div></section>"""

PAGES = {
    "index.html": render("home", "Family and early years support", "Stars Haven Academy provides practical, evidence-informed support to parents and early-learning professionals.", HOME_BODY),
    "about/index.html": render("about", "About Mary Aliu, RECE", "Meet Mary Aliu, RECE, founder of Stars Haven Academy and Family & Early Years Partner.", ABOUT_BODY, "about"),
    "services/index.html": render("services", "Family and early years services", "Explore consultation, observation, coaching, workshops and referral support from Stars Haven Academy.", SERVICES_BODY, "services"),
    "families/index.html": render("families", "Support for families", "Practical early-years consultation and coaching for parents and caregivers.", FAMILIES_BODY, "families"),
    "professionals/index.html": render("professionals", "Support for early-learning professionals", "Reflective consultation, observation and learning for early-years professionals and teams.", PROFESSIONALS_BODY, "professionals"),
    "book/index.html": render("book", "Book a consultation", "Request a consultation with Mary Aliu, RECE, at Stars Haven Academy.", BOOK_BODY, "book"),
    "childcare/index.html": render("childcare", "YMCA licensed home childcare", "Stars Haven Childcare is a YMCA Licensed Home Childcare program in the Port of Newcastle.", CHILDCARE_BODY, "childcare"),
    "contact/index.html": render("", "Contact Stars Haven Academy", "Book a consultation or connect with Stars Haven Academy by email, Instagram or Facebook.", CONTACT_BODY, "contact"),
    "privacy/index.html": render("", "Privacy", "How Stars Haven Academy handles website, consultation and childcare enquiry information.", PRIVACY_BODY, "privacy"),
    "booking-thank-you/index.html": render("", "Consultation request received", "Confirmation that a Stars Haven Academy consultation request was submitted.", BOOKING_THANK_YOU_BODY, "booking-thank-you", robots="noindex, follow"),
    "childcare-thank-you/index.html": render("", "Childcare enquiry received", "Confirmation that a Stars Haven childcare enquiry was submitted.", CHILDCARE_THANK_YOU_BODY, "childcare-thank-you", robots="noindex, follow"),
}

PAGES["404.html"] = render("", "Page not found", "The requested Stars Haven Academy page could not be found.", intro("Page not found", "Let’s get you back home.", "This page may have moved. You can return to the homepage or contact Mary.") + f'<section class="wrap section">{button("Go to the homepage", "./")}</section>', robots="noindex, follow", canonical_path="404.html")


def write_pages() -> None:
    for old_page in SITE.rglob("*.html"):
        old_page.unlink()
    for relative_path, content in PAGES.items():
        destination = SITE / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
    (SITE / "_redirects").write_text("/home  /  301!\n/home/  /  301!\n/programs  /services/  301!\n/programs/  /services/  301!\n/enrolment-waitlist  /childcare/#pre-enrolment-form  301!\n/enrolment-waitlist/  /childcare/#pre-enrolment-form  301!\n/licensing-journey  /childcare/  301!\n/licensing-journey/  /childcare/  301!\n/thank-you  /childcare-thank-you/  301!\n/thank-you/  /childcare-thank-you/  301!\n", encoding="utf-8")
    public_paths = ["", "about/", "services/", "families/", "professionals/", "book/", "childcare/", "contact/", "privacy/"]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{WEBSITE_URL}/{path}</loc></url>\n" for path in public_paths)
    sitemap += "</urlset>\n"
    (SITE / "sitemap.xml").write_text(sitemap, encoding="utf-8")


if __name__ == "__main__":
    write_pages()
    print(f"Built {len(PAGES)} pages in {SITE}")
