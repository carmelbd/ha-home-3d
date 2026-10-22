# Home 3D: floor designer for Home Assistant

Draw your home, walk around it in 3D, and control your real devices from the plan. Everything runs inside Home Assistant as a dashboard in the sidebar. There's no add-on, no HACS and no YAML to write.

![Whole house, exploded 3D view](screenshots/3d-explode.png)

## What it does

- **Design your home.** Draw rooms, walls, doors, windows and stairs. Add any number of floors (and a basement), then furnish it from a catalog of sofas, beds, kitchens, plants and more.
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
- **Updating to a new version:** replace `floor-designer.html` in `www`. Then change `?v=1` to `?v=2` in the dashboard so phones don't keep the old copy. Your design isn't touched.
- **Backup or share a design:** ⋯ → **Save design file** / **Open design file**.
- **It needs internet** the first time it loads, because the 3D engine (three.js) comes from a CDN.
- You can also open the file on its own, outside Home Assistant, to play with a design. Devices are then simulated and the design is saved in that browser only.

## License

MIT. Use it, change it and share it.
