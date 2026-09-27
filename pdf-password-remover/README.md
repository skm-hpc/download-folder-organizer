# PrimeRonin PDF Unlocker

A privacy-first, browser-based PDF password removal utility with two processing paths: direct PDF decryption and a Deep Recovery mode that reconstructs a readable PDF from rendered pages.

> **Author:** PrimeRonin  
> **License:** MIT  
> **Runtime:** Modern web browser  
> **Processing model:** Client-side / browser-only

## Overview

PrimeRonin PDF Unlocker is a standalone HTML application. It does not require a backend, database, build system, or server-side API. PDF files and passwords are processed locally by JavaScript running in the user's browser.

The application first attempts to unlock the PDF directly with `pdf-lib`. If the PDF uses encryption that cannot be directly rewritten, the application falls back to a Deep Recovery pipeline using PDF.js and jsPDF.

## Features

- Unlock password-protected PDFs in the browser.
- Standard PDF decryption using `pdf-lib`.
- Deep Recovery fallback using `pdf.js` + `jsPDF`.
- Drag-and-drop PDF selection.
- PDF validation before processing.
- Password visibility toggle.
- File size and page-count information.
- Configurable recovery/rendering quality.
- Configurable JPEG quality for Deep Recovery.
- Automatic portrait/landscape page handling.
- Live processing progress.
- Cancel processing support.
- Clear/reset workflow.
- Automatic output filename generation.
- Dark/light theme support.
- Responsive desktop and mobile interface.
- Keyboard shortcuts for faster operation.
- No application backend required.

## Important: How Deep Recovery Works

The normal path attempts to load and save the decrypted PDF without changing its page content.

When direct decryption cannot produce a downloadable PDF, Deep Recovery:

1. Opens the password-protected PDF through PDF.js.
2. Decrypts and renders each page in the browser.
3. Converts the rendered page into a JPEG image.
4. Places the rendered image on a new PDF page using jsPDF.
5. Produces a new PDF without the original encryption layer.

### Deep Recovery limitation

Because Deep Recovery rebuilds pages from rendered images, the resulting PDF may not preserve the original text layer, hyperlinks, annotations, form fields, bookmarks, vector objects, or accessibility metadata. Use the standard path whenever possible when preservation of the original PDF structure matters.

## Privacy & Security

The application is designed for local processing. Files and passwords are passed to JavaScript libraries running in the browser and are not intentionally uploaded to an application server.

However, the application loads third-party JavaScript libraries from public CDNs. Users who require a fully offline or controlled environment should self-host the dependencies rather than relying on external CDN resources.

Do not use the tool to bypass access controls on documents you do not own or have permission to process. The included legal notice is informational and does not replace professional legal advice.

## Project Structure

```text
.
├── index.html
├── README.md
└── LICENSE
```

The supplied application can be renamed to `index.html` for GitHub Pages deployment.

## Technologies

| Technology | Purpose |
|---|---|
| HTML5 | Application structure |
| CSS3 | Responsive UI, themes and animations |
| JavaScript | Application logic and state management |
| PDF-LIB | Direct PDF loading, decryption and saving |
| PDF.js | Password-protected PDF parsing and page rendering |
| jsPDF | Deep Recovery PDF reconstruction |

## CDN Dependencies

The application currently loads:

- PDF-LIB from `unpkg.com`
- PDF.js from `cdnjs.cloudflare.com`
- PDF.js worker from `cdnjs.cloudflare.com`
- jsPDF from `cdnjs.cloudflare.com`

For production environments where dependency integrity and availability are critical, consider pinning exact library versions and self-hosting the assets.

## Running Locally

No build step is required.

### Option 1 — Open directly

Rename the application to `index.html` and open it in a modern browser.

### Option 2 — Local HTTP server

Using Python:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

A local HTTP server is recommended for consistent browser behavior and easier testing.

## GitHub Upload

### 1. Create the repository

Create a new GitHub repository, for example:

```text
pdf-password-remover
```

### 2. Prepare the files

Rename:

```text
PrimeRonin_PDF_Unlocker.html
```

to:

```text
index.html
```

Then place these files in the repository:

```text
index.html
README.md
LICENSE
```

### 3. Initialize Git

```bash
git init
git add index.html README.md LICENSE
git commit -m "Initial PrimeRonin PDF Unlocker release"
```

### 4. Connect the GitHub repository

Replace the URL with your actual GitHub repository:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pdf-password-remover.git
git push -u origin main
```

### 5. Enable GitHub Pages

In GitHub:

```text
Repository
  → Settings
  → Pages
  → Build and deployment
  → Deploy from a branch
  → main / root
  → Save
```

GitHub will then publish `index.html` as the website entry point.

## Recommended Git Workflow

Before making changes:

```bash
git status
git pull --rebase origin main
```

After changes:

```bash
git add .
git commit -m "Improve PDF recovery workflow"
git push origin main
```

Useful history commands:

```bash
git log --oneline --decorate --graph --all
git diff
git status
```

## Code Organization

The single-page application is intentionally self-contained.

### HTML

Defines the upload interface, password controls, recovery options, progress display, dialogs, footer and legal notices.

### CSS

Contains the complete visual system, including:

- CSS custom properties
- Dark/light themes
- Responsive breakpoints
- Drag-and-drop states
- Buttons and controls
- Progress indicators
- Toast notifications
- Modal dialogs

### JavaScript

The main processing flow is organized around these responsibilities:

- `selectFile()` — validates and registers the selected PDF.
- `detectPageCount()` — obtains PDF metadata through PDF.js.
- `startProcess()` — coordinates the complete unlock workflow.
- `visualRecoveryUnlock()` — performs page-by-page reconstruction.
- `finishProcess()` — creates the downloadable PDF.
- `resetUI()` — resets transient state.
- `clearAll()` — clears the entire application form.
- `updateStatus()` — displays processing messages.
- `setLoading()` — controls processing state.
- `applyTheme()` — manages theme persistence.
- `openModal()` / `closeModal()` — manage informational dialogs.

## Troubleshooting

### "Incorrect password"

Verify that the password is exactly correct. PDF passwords are case-sensitive.

### PDF opens but Deep Recovery fails

Try a lower rendering scale or JPEG quality. Very large or highly complex PDFs can require substantial browser memory.

### Browser becomes slow

Deep Recovery renders every page into an image. Large PDFs, high rendering scales, and maximum JPEG quality increase memory and CPU usage.

### Output quality is lower than the original

Use the Standard Decryption path when available. Deep Recovery is a compatibility fallback and is inherently raster-based.

### GitHub Pages does not show the application

Confirm that the main application file is named exactly:

```text
index.html
```

Then verify that GitHub Pages is configured to publish the correct branch and root directory.

## Development Guidelines

When extending the application:

1. Preserve the existing standard decryption path.
2. Preserve Deep Recovery as a fallback rather than replacing it.
3. Keep processing client-side unless a backend is intentionally introduced.
4. Avoid storing PDF passwords in localStorage, cookies, URLs, or analytics systems.
5. Revoke generated Blob URLs when they are no longer needed.
6. Keep third-party dependencies version-pinned for reproducible deployments.
7. Document user-visible behavior changes in the README.
8. Test with both small and large PDFs before release.

## Suggested Commit Messages

```text
feat: add PDF recovery quality controls
fix: improve encrypted PDF handling
fix: release generated blob URLs
ui: improve mobile PDF upload layout
docs: update GitHub deployment guide
refactor: organize PDF processing helpers
```

## License

This project is intended to be released under the MIT License. See `LICENSE` for the complete license text.

## Disclaimer

This software is provided as-is without warranty. Users are responsible for ensuring that they have the legal right or explicit permission to remove protection from documents they process.

© 2026 PrimeRonin. All rights reserved where applicable.
