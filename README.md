# ND2 viewer – flat-field corrected

Browser-based viewer for Nikon `.nd2` fluorescence stacks (flat-field correction, per-channel LUTs,
Z browsing, object detection by bright body / dark edge, workflow figure, PNG export).
Everything runs in the browser; files are never uploaded.

## Option 1 – GitHub Pages (recommended)
1. Push this folder to a GitHub repository (branch `main`).
2. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. The included workflow publishes `index.html`; the link is `https://<user>.github.io/<repo>/`.

## Option 2 – Streamlit Community Cloud
1. Push this folder to GitHub.
2. On share.streamlit.io choose the repo, branch `main`, main file `streamlit_app.py`.
3. `streamlit_app.py` simply embeds `index.html`.

## Run locally
Open `index.html` in Chrome, or `pip install -r requirements.txt && streamlit run streamlit_app.py`.

Supports ND2 version 3 files (uncompressed or lossless). Needs a current Chrome/Edge.
