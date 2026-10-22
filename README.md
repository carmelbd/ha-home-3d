# Home 3D: floor designer for Home Assistant

Draw your home, walk around it in 3D, and control your real devices from the plan. Everything runs inside Home Assistant as a dashboard in the sidebar. There's no add-on, no HACS and no YAML to write.

![Whole house, exploded 3D view](screenshots/3d-explode.png)

## 🆕 What's new

**Already installed?** Jump to [Updating](#updating-to-a-new-version). It takes a minute and your design is kept.

- **🪜 Stairs that connect to the floor above.** Stairs now cut a matching opening in the floor above automatically, with a glass railing around it, so they go up *through* the floor and look right in 3D. On the upper floor's 2D plan the opening shows as "↓ stairs". Don't want it? Set **Opening in the floor above → No**.
- **⬇️ Stairs going down.** Set a stair's **Direction → Down to the floor below** and it starts on the floor you're on, sinks through it and lands on the floor below (great for a basement). The floor gets the opening and railing automatically, and the floor below shows where the stairs land. In "Whole house" 3D it's one continuous staircase.
- **💡 LED lights on stairs.** Choose **Under each step**, **Along the bottom** or **Both**, in any color. They glow, especially in 🌙 night mode.
- **Zoom in 2D.** Scroll or pinch on the plan to zoom in on a room, and drag empty space to move around. There are also **− / + / Fit** buttons in the corner. Phones and tablets support two-finger pinch. Each floor remembers its own zoom.
- **🔍 Search products.** A search box sits above the catalog. Type `light`, `sofa`, `trash`… and only the matches show. **Enter** adds the first one, **Esc** clears.
- **💄 Makeup vanity** (Bedroom, closet & office). It has a mirror with Hollywood bulbs or an LED frame that glow in night mode, plus optional stool and drawers, in any color.
- **🗑️ Sensor trash can** (Kitchen & bath). It comes rectangular, round or as a double recycling bin, in 12 / 30 / 50 L, in steel, black or white, with a glowing blue sensor light.
- **Safer saving.** If the dashboard is edited while Home 3D is open, saving no longer overwrites that edit.

| Stairs through the floor | Stairs going down | Stair LEDs at night |
|---|---|---|
| ![Stairs opening with railing](screenshots/stairs-opening.png) | ![Stairs going down to the basement](screenshots/stairs-down.png) | ![Stair LEDs glowing at night](screenshots/stairs-led-night.png) |

| Zoom + search | Vanity and trash can | …at night |
|---|---|---|
| ![Zoom and search](screenshots/2d-zoom-search.png) | ![Makeup vanity and sensor trash can](screenshots/3d-vanity-trash.png) | ![Vanity bulbs glowing at night](screenshots/3d-vanity-night.png) |

The full list of changes is in [CHANGELOG.md](CHANGELOG.md).

## What it does

- **Design your home.** Draw rooms, walls, doors, windows and stairs. Add any number of floors (and a basement), then furnish it from a catalog of sofas, beds, kitchens, plants, a makeup vanity, a sensor trash can and more. Use 🔍 search to find things fast.
- **Zoom in 2D.** Scroll or pinch to zoom, drag to move around, or use the − / + / Fit buttons.
- **Look around in 3D.** Drag to rotate, right-drag to pan and scroll to zoom. You can show one floor or the whole house, use full-height walls, or "explode" the floors apart.
- **Day or night.** 🌙 Night mode darkens the house so you can see which lights are on.
- **Control your devices.** Place lights, switches, ACs, shutters, TVs, sensors, cameras and more, and link each one to a Home Assistant entity.
  - Tap a light or switch to turn it on or off.
  - Tap anything else (AC, TV, shutter, sensor) to open Home Assistant's normal control window.
  - "All lights" switches every light on the floor at once.
- **Live.** Lights glow when they're really on, and the plan updates by itself when something changes in your home.
- **Saves to Home Assistant.** The design is stored in Home Assistant, so it's the same on your computer, phone and tablet.

| Night mode | 2D editor |
|---|---|
| ![Night mode](screenshots/3d-night.png) | ![2D editor](screenshots/2d-editor.png) |

## Install (about 5 minutes)

### 1. Copy the file into Home Assistant

Download [`floor-designer.html`](floor-designer.html) (click it, then the download button ⤓). Put it in the **`www`** folder inside your Home Assistant config folder (the folder that has `configuration.yaml`). If there is no `www` folder, create it and restart Home Assistant once.

Ways to get the file there:
- **Home Assistant OS:** the *File editor* or *Studio Code Server* add-on (upload into `/config/www`), or the *Samba share* add-on.
- **Docker / NAS:** Finder, Windows Explorer or Cyberduck (SFTP/SMB) into the folder you mapped as `/config`.

To check it worked, open `http://<your-ha-address>:8123/local/floor-designer.html` in a browser. You should see the designer.

### 2. Add the dashboard

1. In Home Assistant go to **Settings → Dashboards → + Add dashboard → New dashboard from scratch**. Name it **Home 3D** and pick an icon (`mdi:home-floor-3` looks nice).
2. Open the new dashboard, click ✏️ (top right) → ⋮ → **Raw configuration editor**, replace everything with this, and save:

```yaml
views:
  - title: Home 3D
    path: home
    type: panel
    cards:
      - type: iframe
        url: /local/floor-designer.html?v=1
```

3. Open **Home 3D** in the sidebar. That's it.

### 3. Design your home

- Start from the example house with ⋯ → **Load example home**, or begin empty with ⋯ → **Start from empty floors**.
- Pick a device and type its entity in **Entity ID**. Your entities show up as suggestions while you type.
- Use **2D** to edit precisely and **3D** to look around. In 2D, **▶ Preview** lets you tap devices without moving them.

## Good to know

- **Saving needs an admin user.** Changes are saved into the dashboard itself, and Home Assistant only lets admins change dashboards. Other users can still view and control.
- **Backup or share a design:** ⋯ → **Save design file** / **Open design file**.
- **It needs internet** the first time it loads, because the 3D engine (three.js) comes from a CDN.
- You can also open the file on its own, outside Home Assistant, to play with a design. Devices are then simulated and the design is saved in that browser only.

## Updating to a new version

Your design is stored in Home Assistant, not in the file, so updating never touches it.

1. Download the new [`floor-designer.html`](floor-designer.html) and replace the old one in your `www` folder.
2. In Home Assistant, open the **Home 3D** dashboard → ✏️ → ⋮ → **Raw configuration editor**. Raise the number at the end of the URL by one, for example `/local/floor-designer.html?v=1` → `?v=2`, then save. Leave everything else in that editor as it is. This makes browsers and the phone app load the new version instead of an old saved copy.
3. Reload the page. On a phone, close and reopen the Home Assistant app.

If something looks off after updating, clear the browser cache or bump the number once more.

## License

MIT. Use it, change it and share it.
