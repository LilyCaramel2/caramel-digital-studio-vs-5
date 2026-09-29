# Caramel Digital Studio

The static website for Caramel Digital Studio.

## Pages

- `index.html` — Home
- `capabilities.html` — Capabilities and AI tiers
- `work.html` — Selected client work and interface demonstrations
- `pricing.html` — Packages, maintenance, content and add-ons
- `start.html` — Project enquiry and contact details

## Preview

Open `index.html` in a browser, or run a local static server from this folder:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Connect the enquiry form

The project form uses Web3Forms to deliver enquiries to the inbox registered with its access key. Before the form can send:

1. Create an access key at [web3forms.com](https://web3forms.com/) using `lily@carameldigitalstudio.com`.
2. In `start.html`, replace `YOUR_WEB3FORMS_ACCESS_KEY` in the hidden `access_key` field with that key.
3. Commit the change to GitHub. Vercel will redeploy the site.

The key is intended to be embedded in a static client-side form. Until it is added, the form explains that it is not connected and provides the direct email address as an alternative.

## GitHub Pages

To publish through GitHub Pages, open the repository's **Settings → Pages**, select **Deploy from a branch**, choose `main` and `/(root)`, then save. The site will be available at the GitHub Pages URL shown there.# caramel-digital-studio-vs-5
Caramel Digital Studio website
