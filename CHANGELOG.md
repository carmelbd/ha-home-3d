# Changelog

## 1.0.0 (2026-10-22): Install with HACS

- **HACS support.** Add the repository to HACS as a **Dashboard** plugin, download it, and use the `custom:home-3d-card` card. There are no files to copy, and updates arrive through HACS.
- The card also appears in the **Add card** picker as **Home 3D**, with an optional `height` setting.
- It works on the default dashboard too, not only on dashboards with their own URL.

## 2026-10-22: Stairs that connect, and stair LEDs

- **Automatic opening in the floor above.** Straight and U-shaped stairs cut a matching hole in the floor above, with a glass railing on the open sides (the arrival side stays open). In 2D the upper floor shows it as "↓ stairs", and in 3D you can look down through it. Turn it off per stair with *Opening in the floor above → No*. Stairs that already sit inside an "Open to the floor below" stairwell don't get a second railing.
- **Stairs going down.** New *Direction* option on stairs: *Down to the floor below*. The stairs start on the current floor, cut an opening in it with a railing, and land exactly on the floor below. The lower floor shows them faded in 2D and fully in 3D.
- **Number of steps.** Stairs get a *Number of steps* option (*Auto* or 3–30). The panel shows the height of each step and warns when steps are too steep, too low, or too shallow to stand on.
- **Railing option.** Stairs get a *Railing* option: handrail + railing around the opening, only the handrail, only the opening railing, or none.
- **Stair LEDs.** *Under each step*, *Along the bottom* or *Both*, with a color picker. They glow and add a soft light, stronger in night mode.

## 2026-10-22: Search, zoom and new products

- **2D zoom and pan.** Mouse wheel or trackpad pinch zooms toward the cursor. Drag empty space (or right/middle-drag anywhere) to pan. Two-finger pinch works on touch screens. − / + / Fit buttons sit in the corner, and each floor keeps its own zoom.
- **Product search.** A search box above the catalog filters rooms, furniture and devices, and also matches related words (for example "garbage" finds the trash can). Enter adds the first result, Esc clears.
- **New: Makeup vanity.** Lit mirror (Hollywood bulbs, LED frame or none), optional stool and drawers, any color. The lights glow in night mode.
- **New: Sensor trash can.** Rectangular, round or double (recycling). 12 / 30 / 50 L. Steel, black or white. Glowing sensor light.
- **Fix:** the designer re-reads the dashboard before saving, so an edit made to the dashboard while Home 3D is open isn't overwritten.

## 2026-10-22: First release

- Floor designer running inside Home Assistant as a sidebar dashboard.
- 2D editor and 3D view (rotate, whole house, full-height walls, explode, night mode).
- Live device states, tap to toggle or open Home Assistant's control window, and the design saves into Home Assistant.
