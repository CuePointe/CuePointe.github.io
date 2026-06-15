# CuePointe Action Pool 🎱
**Uganda's #1 Youth Cue-Sports Platform**

> Structured leagues. Digital rankings. Real pathways for talent — from Kabalagala to the world.

🌐 **Live Site:** [cuepointe.github.io](https://cuepointe.github.io)
📍 **Base:** Kabalagala, Kampala, Uganda
📧 **Email:** cuepointe@gmail.com
📱 **WhatsApp:** +256 743 482 588

---

## What is CuePointe?

CuePointe Action Pool is Uganda's first integrated youth cue-sports platform. Founded in the vibrant urban hubs of Kabalagala and Kansanga, we have transformed a traditional neighbourhood pastime into a structured, data-driven career path for emerging talent.

We run weekly knockouts, seasonal leagues, and community tournaments across Kampala — with digital player rankings, talent tracking, and transparent prize pools.

---

## Site Structure

```
cuepointe.github.io/
│
├── index.html              # Homepage — hero slideshow, schedule, rankings, registration
├── about.html              # Our story, team, partners & sponsors
├── rankings.html           # Live player rankings with photo slideshows
├── register.html           # Player registration form
├── news.html               # News & updates
├── venues.html             # Venue listings & host application
├── contact.html            # Contact form & info
├── talent-fund.html        # Talent fund transparency dashboard
├── view-schedule.html      # Tournament schedule feed
│
├── players.json            # Player data — rankings source of truth
├── update_rankings.py      # CLI tool to add/update player entries
├── add_player.py           # CLI tool to add a new player
├── record_match.py         # CLI tool to record match results
│
├── CuePointe_Logo.jpg      # Brand logo
├── favicon.ico             # Favicon
├── robots.txt              # SEO crawler rules
├── sitemaps.xml            # XML sitemap
├── site.webmanifest        # PWA manifest
│
└── images/                 # All media assets
    ├── hero-1.jpg          # Homepage hero slideshow (hero-1 to hero-5)
    ├── hero-2.jpg
    ├── hero-3.jpg
    ├── hero-4.jpg
    ├── hero-5.jpg
    ├── about/              # About page story images & videos
    ├── team/               # Staff & team member photos
    ├── partners/           # Partner & sponsor logos
    ├── players/            # Player profile photos
    └── videos/             # Short video clips (MP4)
```

---

## How to Update Content

### Add or Update a Player

Open `players.json` and add or edit a player object:

```json
{
  "id": "0001",
  "name": "Player Name",
  "area": "Kabalagala",
  "events": "10",
  "wins": "7",
  "score": "45.2",
  "traits": "Strong Breaker",
  "photo": "images/players/0001.jpg"
}
```

For multiple profile photos (slideshow):

```json
"photos": ["images/players/0001a.jpg", "images/players/0001b.jpg"]
```

Or use the CLI tool:

```bash
python3 update_rankings.py
```

---

### Add Story Images / Videos (About Page)

Upload files to `images/about/` with these names:

| File | Purpose |
|------|---------|
| `story-1.jpg` or `story-1.mp4` | Story slideshow slide 1 |
| `story-2.jpg` or `story-2.mp4` | Story slideshow slide 2 |
| `story-3.jpg` or `story-3.mp4` | Story slideshow slide 3 |

Then in `about.html`, replace the placeholder `<div>` inside each slide with:

```html
<!-- For a photo -->
<img src="images/about/story-1.jpg" alt="CuePointe Story">

<!-- For a video -->
<video autoplay muted loop playsinline>
  <source src="images/about/story-1.mp4" type="video/mp4">
</video>
```

---

### Add Team Members (About Page)

Upload photo to `images/team/member-1.jpg` then in `about.html` update the relevant team card:

```html
<div class="team-name">Thomas Otieno</div>
<div class="team-role">Founder & Director</div>
<div class="team-bio">Your bio text here.</div>
```

Duplicate a full `team-card` block to add more members.

---

### Add Partners & Sponsors (About Page)

Upload logo to `images/partners/partner-1.png` then in `about.html` update:

```html
<div class="partner-name">Company Name</div>
<div class="partner-type">Gold Sponsor</div>
<div class="partner-desc">Description of the partnership.</div>
```

Tier options: `Gold Sponsor` · `Silver Sponsor` · `Bronze Sponsor` · `Community Partner`

---

### Add Videos (Homepage)

Upload MP4 clips to `images/videos/` or use YouTube embed codes.

In `index.html`, find the video slot divs and replace the placeholder with:

```html
<!-- MP4 option -->
<video autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover">
  <source src="images/videos/highlight-1.mp4" type="video/mp4">
</video>

<!-- YouTube option -->
<iframe style="width:100%;height:100%;border:none"
  src="https://www.youtube.com/embed/YOUR_VIDEO_ID?rel=0"
  allowfullscreen>
</iframe>
```

---

### Update Hero Slideshow (Homepage)

Replace `images/hero-1.jpg` through `images/hero-5.jpg` with new images. Recommended size: **1920×1080px**, JPEG at 80% quality.

---

## Player Data Fields (`players.json`)

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique CP-ID e.g. `"0001"` |
| `name` | string | Full player name |
| `area` | string | Neighbourhood / area |
| `events` | string | Total events played |
| `wins` | string | Total wins |
| `score` | string | Talent score / rating |
| `traits` | string | Badge e.g. `"Strong Breaker"` |
| `photo` | string | Path to single photo |
| `photos` | array | Paths to multiple photos (slideshow) |

---

## Social & Contact

| Platform | Link |
|----------|------|
| 🌐 Website | [cuepointe.github.io](https://cuepointe.github.io) |
| 📘 Facebook | [facebook.com/CuePointe](https://www.facebook.com/CuePointe) |
| 📸 Instagram | [instagram.com/cuepointe](https://www.instagram.com/cuepointe) |
| 🎵 TikTok | [tiktok.com/@cuepointe](https://www.tiktok.com/@cuepointe) |
| ▶ YouTube | [CuePointe Channel](https://www.youtube.com/channel/UCJs5yTrm9EU0CBG6YOfU3Cw) |
| 📝 Blog | [cuepointe.blogspot.com](https://cuepointe.blogspot.com) |

---

## Tech Stack

- Pure **HTML5 / CSS3 / Vanilla JavaScript** — no frameworks, no build tools
- Hosted on **GitHub Pages** — free, fast, zero server cost
- Player data driven by **`players.json`** — update once, reflects everywhere
- Google Analytics via **GA4** (`G-221BNVJR22`)
- Form submissions via **Formspree**

---

## License

© 2026 CuePointe Action Pool · Kampala, Uganda · All Rights Reserved.

This repository contains the official CuePointe website. Content, branding, and media are proprietary and may not be reproduced without permission.
