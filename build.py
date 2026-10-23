"""Build dist/ha-home-3d.js (the HACS card) from floor-designer.html.

Run after every change to floor-designer.html:  python3 build.py
"""
import json, pathlib, re

root = pathlib.Path(__file__).parent
html = (root / "floor-designer.html").read_text()
version = (root / "VERSION").read_text().strip()

js = f"""/* Home 3D card for Home Assistant, v{version}. Built from floor-designer.html by build.py. Do not edit by hand. */
(() => {{
const VERSION = {json.dumps(version)};
const HTML = {json.dumps(html)};

class Home3DCard extends HTMLElement {{
  setConfig(config) {{ this._config = config || {{}}; if (this._frame) this._size(); }}
  set hass(hass) {{ this._hass = hass; }}
  connectedCallback() {{
    if (this._frame) return;
    const root = this.shadowRoot || this.attachShadow({{ mode: "open" }});
    root.innerHTML = `<style>
      :host {{ display: block; }}
      ha-card {{ overflow: hidden; }}
      iframe {{ display: block; width: 100%; border: 0; }}
    </style><ha-card><iframe title="Home 3D" allow="fullscreen"></iframe></ha-card>`;
    this._frame = root.querySelector("iframe");
    this._size();
    // srcdoc keeps the page on Home Assistant's origin, so it can use the live connection.
    // Card options (for example `wall: true`) are handed to the page before it starts.
    const cfg = JSON.stringify(this._config || {{}}).replace(/</g, "\\\\u003c");
    this._frame.srcdoc = HTML.replace("<head>", `<head><script>window.HOME3D_CONFIG=${{cfg}};</script>`);
  }}
  _size() {{
    const h = (this._config && this._config.height) || "calc(100vh - var(--header-height, 56px))";
    this._frame.style.height = h;
  }}
  getCardSize() {{ return 12; }}
  static getStubConfig() {{ return {{}}; }}
}}

if (!customElements.get("home-3d-card")) customElements.define("home-3d-card", Home3DCard);
window.customCards = window.customCards || [];
if (!window.customCards.some(c => c.type === "home-3d-card"))
  window.customCards.push({{
    type: "home-3d-card",
    name: "Home 3D",
    description: "Design your home in 3D and control your devices from the plan.",
    preview: false,
    documentationURL: "https://github.com/carmelbd/ha-home-3d",
  }});
console.info(`%c HOME 3D %c ${{VERSION}} `, "background:#2f6fed;color:#fff;border-radius:3px 0 0 3px", "background:#eef2f7;color:#2f6fed;border-radius:0 3px 3px 0");
}})();
"""
(root / "dist" / "ha-home-3d.js").write_text(js)
print(f"dist/ha-home-3d.js built (v{version}, {len(js)//1024} KB)")
