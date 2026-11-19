# Echocardiography Report (ECHO TRANS)

Live site: https://echo-trans007.netlify.app  (Netlify deploys automatically from this repository)

- `index.html` — the app (built from `source/`)
- `config.js` — Firebase settings for project `echo-trans-007`
- `firestore.rules` — database security rules (paste into Firebase console → Firestore → Rules)
- `source/echo-report.html` — master copy of the app (same as the Claude artifact); `python3 source/mkweb.py` rebuilds `index.html` from it
- `source/echo.js`, `base.css`, `echo_extra.css`, `build.py` — older split source (kept for reference)

Reports live in Firebase (Firestore), not in this repository — updating the app never touches them.

## Licence

© 2026 Dr. Md. Shayeekh Mahbub Setu. All rights reserved. Not open source — see `LICENSE`. Copying or reuse without written permission is not allowed.
