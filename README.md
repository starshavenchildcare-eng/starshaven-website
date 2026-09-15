# Stars Haven Childcare website

Replacement for the existing Google Site at <https://www.starshavenchildcare.ca/>.

## Current state

The replacement is staged on `migration/google-sites`. It has not been connected to the live domain. The Google Site remains the current site. The public source repository is owned by `starshavenchildcare-eng`.

The existing routes are retained:

- `/` and `/home/`
- `/about/`
- `/programs/`
- `/enrolment-waitlist/`
- `/licensing-journey/`, now containing current licensed-home-childcare information
- `/contact/`

A website privacy page and a custom 404 page are included.

## Preview locally

The complete static website is in `site/`; no application build or production dependency is required.

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --directory site
```

Then visit <http://localhost:8000/>.

The verification workflow checks desktop and mobile browsers and creates a `website-review` artifact containing the site and screenshots.

## Content decisions

The existing public Google Site was retrieved on September 14, 2026. Its mission, Christian values, six-page navigation and published business telephone number were retained.

Current owner-provided information supersedes the old website’s September 2025 launch, unlicensed status, proposed centre-opening timeline and school-age offering. The replacement identifies the current YMCA Licensed Home Childcare program, Mary Aliu’s RECE designation, an age focus of 18 months to 4 years, typical hours of 8:00 a.m. to 4:00 p.m. with occasional flexibility, and approximate CWELCC fees of $22 per day with YMCA confirmation.

The current contact email is `starshavenchildcare@gmail.com`. No private family records, child photographs or enrolment responses are included. The original logo and images have not been copied. The draft uses HTML and CSS illustrations that do not represent photographs of the childcare environment.

The enrolment button uses the owner’s existing pre-enrolment link. Form submissions remain in the existing Google Form. The website itself has no form backend, analytics, advertising scripts or external font dependencies.

## Before domain cutover

1. Review the staged pages, business contact details, imagery and stated hours.
2. Resolve permission to copy the existing public website images into this public source repository, or provide approved replacements.
3. Connect a suitable host and deploy the contents of `site/` to a separate review URL.
4. Verify every route, the mobile menu and the external form without submitting a real enquiry.
5. Remove the draft `noindex, nofollow` tags and allow indexing only when the production version is ready.
6. Add final canonical URLs and a sitemap for the live domain.
7. Validate HTTPS and redirects, then change only the necessary website DNS records. Preserve email records.
8. Keep the Google Site available for rollback until the replacement is confirmed working.

GitHub stores the source. No GitHub Pages, Cloudflare or DNS configuration has been changed. GitHub Pages has restrictions on free hosting for online business and commercial transactions, so production hosting must be selected separately: <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits>.
