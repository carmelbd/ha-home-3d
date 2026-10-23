# Changelog

## 1.7.0 (2026-10-23): Wall display

- **⛶ Wall** button: the house fills the whole screen for a tablet on the wall, covering Home Assistant's sidebar and top bar. Tap three times to show the buttons (2D / 3D, Whole house, Night, All lights, Reset view, Wall settings, Exit).
- **Clock:** digital, analog or small, in any of 6 positions and 4 sizes, 24 or 12 hour, with seconds and date if you like, in any color, on a frosted-glass card or as plain text. Or no clock.
- **Weather:** current conditions, humidity and wind, plus the next 5 days (it falls back to twice-daily or hourly forecasts when that's all the integration has).
- **Scene buttons** for scenes, scripts, buttons and automations, with your own labels and emoji. One click adds all your scenes and scripts.
- **Camera pictures** that refresh every 2–30 seconds, in 4 sizes. Tap one to see it big. One click adds all your cameras.
- **Info:** any sensor values and a lights-on counter.
- **🧹 House only** hides the clock, weather, info, scenes and cameras at once. Each one can also be hidden on its own.
- **Screensaver** (black with a moving clock, or a dimmed house), **automatic night look** after sunset, **slow auto-rotate**, and it asks the browser to keep the screen on.
- **Card option `wall: true`** opens the card straight into the wall display.
- The wall settings are saved with your design in Home Assistant.

## 1.6.1 (2026-10-23): Walls around outdoor areas

- Outdoor rooms (Garden / lawn, Outdoor paving, Gravel yard, Parking) get a **Walls around this area** option: None (open, the default), Walls (full height), Low wall (1.2 m) or Railing. The Top / Right / Bottom / Left ticks still remove single sides, for example where two yards meet.

## 1.6.0 (2026-10-23): Pool, pergola & yard

- **New catalog group "Pool, pergola & yard":** louvered pergola, outdoor kitchen (gas or charcoal grill, sink, mini fridge), outdoor LED screen, garden / boundary wall with lights, outdoor steps, car, and a corner L-shaped sofa (in Living & media).
- **Outdoor room types:** Garden / lawn, Outdoor paving, Gravel yard and Parking. They have no walls and don't count toward the house area. New floor: outdoor grey porcelain 80 cm.
- **Pool:** water color, steps at either end, and a stone edge in any color, together with the electric cover / shade screen and underwater lights. A new pool has no cover until you choose one.
- **Gate:** the sliding track is only as long as needed.
- Designs made with other copies of the designer that use these items now open with the same look.

## 1.5.1 (2026-10-23): Any entity works with any button

- **Fix:** a button only worked when its entity matched the button type, so a **Light** linked to a Sonoff `switch.…`, or a **TV** linked to a `remote.…`, said "link it to a Home Assistant entity first". Now any entity works with any button.
- If the entity doesn't exist in Home Assistant, the panel now says so, so typos are easy to spot. Entity IDs are made lowercase automatically.

## 1.5.0 (2026-10-23): View mode

- **View mode for everyday use.** In Home Assistant, Home 3D now opens as just your house in 3D, with no editor panels. Drag to rotate, scroll or pinch to zoom, and tap a light to switch it. Other devices open Home Assistant's control window. Switch floors with the tabs at the top, and use Whole house, Night and All lights at the bottom.
- **✏️ Edit** (top right) brings back the designer, and **✓ Done** returns to view mode. Each device remembers your choice. Opening the page with `#edit` at the end of the address starts in edit mode.
- Leaving Preview or the catalog no longer resets the live on/off states in Home Assistant.

## 1.4.0 (2026-10-23): Pool with electric cover, and alarm

- **Swimming pool** (Balcony & outdoor) with an **electric slatted cover** on the water or an **electric shade screen** above it, underwater lights in any color, and a choice of tiles, edge stone and cover color.
- **Pool cover / screen** button (Doors, blinds & locks): link it to the cover entity and the 3D cover or screen opens and closes live with the real one, including half open.
- **Alarm** button (Sensors & cameras) for `alarm_control_panel` entities. It lights up when the alarm is armed or triggered. Tapping it opens Home Assistant's alarm keypad.

## 1.3.0 (2026-10-23): Electric gate

- **Electric gate** (Balcony & outdoor): sliding gate (with track and motor), swing gate with 2 leaves or 1 leaf, or roll-up garage door. Choose the style (horizontal slats, vertical bars or solid), color and height (1.2–2.4 m), plus an amber warning light that glows while it's open.
- **Opens live from Home Assistant.** Add the new **Electric gate** device (Doors, blinds & locks) next to it and link it to your gate's `cover.` entity. The 3D gate opens and closes with the real one, including half-open positions. Tapping the device opens Home Assistant's control window (no accidental opening). You can also set the position by hand: closed, half open or open.

## 1.2.1 (2026-10-23): Faster 3D

- **Smoother rotating and zooming.** Each piece of furniture, the walls and the soft floor shadows are drawn in far fewer pieces (about 40% fewer draw calls). The sun shadows are only redrawn when the house changes, not on every camera move. On high-resolution screens the 3D view renders at 1.5× instead of 2×.
- **Lamps cost nothing while they're off.** Only lights that are on add a lamp (in groups of 4, so switching stays instant).

## 1.2.0 (2026-10-23): Kitchen and glass closet

- **Kitchen chair** with 4 legs: table, counter or bar height, with backrest, low back or no back, and any seat and legs color.
- **Kitchen counter and island options:** cabinet color, countertop (dark stone, white marble, white quartz, black, wood), handles, and doors/drawers. The counter can get wall cabinets above it. The island can get a seating overhang, waterfall sides, and a sink or cooktop.
- **Tall kitchen cabinets** (built-in): pantry doors, built-in oven + microwave, or built-in fridge, at 2.0 / 2.2 / 2.4 m.
- **Handles** for all kitchen cabinets: steel bar, black bar, **big gold ring**, gold knob, or handleless (integrated groove).
- **Glass closet with LEDs:** glass doors, 1–6 glass shelves, LEDs under each shelf and/or side strips in any color, any frame color, filled with bags, shoes or folded clothes. It glows at night.
- **Clear shoe boxes** can have LEDs inside.

## 1.1.1 (2026-10-23): Instant light switching

- Turning a light (or any device) on or off in 3D is instant again. Only the changed light updates; the house isn't rebuilt and the realistic materials aren't recompiled. Live changes from Home Assistant update the same fast way.

## 1.1.0 (2026-10-23): Realistic 3D

- **Real photo textures.** Wood planks, herringbone parquet, concrete, decking, stone pavers, pebbles and grass use real CC0 textures from [Poly Haven](https://polyhaven.com), with depth and shine. Tiles, marble, terrazzo and carpet keep their exact sizes and colours and get real relief on grout lines and surfaces.
- **Wood grain and fabric** on furniture: tables, chairs, cabinets and stairs show wood grain, and sofas, armchairs and beds show a fabric weave in any colour. Walls have a subtle plaster surface.
- **Realistic light.** Filmic colours, a lower warm sun with sharper wall shadows, light and reflections from a real sky, and soft contact shadows where walls meet the floor and under furniture. Furniture edges are softly rounded. Metal, mirrors and glass reflect.
- **Nicer night mode.** Lamp light falls off more naturally and is less blown out.
- Textures download the first time they're used (about 2 MB each). Offline, the previous drawn textures are used.

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
