# Rail Park — Compass Sign

A single-file, iOS-ready web app that recreates the Rail Park welcome sign. The
big white arrow uses your phone's **compass to stay pointed at true north** as
you turn — hold the phone flat and rotate; the arrow counter-rotates to keep
aiming north.

## Files
- `index.html` — the whole app (no build step, no dependencies).
- `serve.py` — an HTTPS server so the compass works on your iPhone.

## Run it on your iPhone (recommended)

The iOS compass API **only works over HTTPS**, so use the included server:

```bash
cd rail-park-compass
python3 serve.py
```

Then on your iPhone (connected to the **same Wi-Fi**):

1. Open Safari → `https://<your-mac-ip>:8443`
   (find the IP with `ipconfig getifaddr en0`, or read it from the script output).
2. You'll see a certificate warning — that's expected for a self-signed cert.
   Tap **Show Details → visit this website → Visit Website**.
3. Tap **Enable Compass** and allow "Motion & Orientation Access".
4. Hold the phone flat. The arrow now points north.

### Make it feel like an app
In Safari tap the **Share** button → **Add to Home Screen**. It launches
full-screen with no browser chrome.

> Tip: if the compass seems off, calibrate it by moving your phone in a
> figure-8 motion a few times (this recalibrates the iOS magnetometer).

## Quick desktop preview (no compass)

```bash
cd rail-park-compass
python3 -m http.server 5173
# open http://localhost:5173
```

## How the compass logic works
iOS provides `event.webkitCompassHeading` — the direction the **top of the
phone** points, in degrees clockwise from north. To keep the arrow visually
aimed at north, the app rotates the arrow by `-heading`. Readings are smoothed
each animation frame and take the shortest rotational path to avoid jitter and
the 359°→0° spin. On Android/standard browsers it falls back to the absolute
`deviceorientation` event (`heading = 360 − alpha`).
