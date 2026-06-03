"""
3D wireframe of the concrete loft + pinhole camera -> perspective line-drawings
from any position. Renders the four corner views + CAM B.

Room axes (meters):  x: 0=WEST(arch/duct) .. 10=EAST(art wall)
                      y: 0=SOUTH(office+door) .. 12=NORTH(windows)
                      z: 0=floor .. 4.2=ceiling
Render:  .venv/bin/python room_3d.py  ->  room_3d.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

RX, RY, RZ = 10.0, 12.0, 4.2
S = []  # segments: (P0, P1, color, lw)

FACES = []  # translucent volume faces: (list of 3D corner pts, color)

def seg(p0, p1, c="0.6", lw=1.0):
    S.append((np.array(p0, float), np.array(p1, float), c, lw))

def face(pts, c):
    FACES.append(([np.array(p, float) for p in pts], c))

def box(x0, x1, y0, y1, z0, z1, c="0.45", lw=1.0, fill=True):
    pts = [(x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0),
           (x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)]
    e = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
    for a,b in e: seg(pts[a], pts[b], c, lw)
    if fill:
        for q in [(0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(1,2,6,5),(0,3,7,4)]:
            face([pts[i] for i in q], c)

def rect_x(x, y0, y1, z0, z1, c, lw=1.4):   # rectangle on a constant-x (E/W) wall
    p=[(x,y0,z0),(x,y1,z0),(x,y1,z1),(x,y0,z1)]
    for i in range(4): seg(p[i], p[(i+1)%4], c, lw)
    face(p, c)

def rect_y(y, x0, x1, z0, z1, c, lw=1.4):   # rectangle on a constant-y (N/S) wall
    p=[(x0,y,z0),(x1,y,z0),(x1,y,z1),(x0,y,z1)]
    for i in range(4): seg(p[i], p[(i+1)%4], c, lw)
    face(p, c)

# ---------- ROOM SHELL ----------
box(0, RX, 0, RY, 0, RZ, c="0.78", lw=1.0, fill=False)   # shell: edges only, no fill

# ---------- NORTH WINDOW WALL (y=RY): mullion grid ----------
for x in np.arange(0, RX+0.01, 1.0):
    seg((x, RY, 0), (x, RY, RZ), "#2f7fbf", 1.0)
for z in np.arange(0, RZ+0.01, 0.7):
    seg((0, RY, z), (RX, RY, z), "#2f7fbf", 1.0)

# ---------- WEST ARCH/DUCT WALL (x=0) ----------
# arch (semicircle in the y-z plane), centered y=6.6, base z=2.4, radius 1.5
yc, zb, r = 6.6, 2.4, 1.5
th = np.linspace(0, np.pi, 28)
ay, az = yc + r*np.cos(th), zb + r*np.sin(th)
for i in range(len(th)-1):
    seg((0, ay[i], az[i]), (0, ay[i+1], az[i+1]), "0.4", 1.4)
seg((0, yc-r, 0), (0, yc-r, zb), "0.4", 1.4)
seg((0, yc+r, 0), (0, yc+r, zb), "0.4", 1.4)
rect_x(0.02, 6.0, 7.2, 1.1, 2.3, "#c0392b", 1.6)            # woman painting
box(0, 0.45, 4.2, 5.5, 0, 2.0, c="#9b7b53", lw=1.0)         # bookshelf
box(0, 0.45, 8.0, 9.4, 0, 2.0, c="#9b7b53", lw=1.0)         # bookshelf
# DUCT: big insulated pipe — ceiling run near west wall + curved drop to a
# round vent near the arch (jutting into the room, south of the arch).
dx0, dx1 = 0.45, 1.3
box(dx0, dx1, 4.6, 11.4, 3.4, 4.05, c="#9aa0a4", lw=1.2)    # horizontal ceiling run
box(dx0, dx1, 3.9, 4.8, 2.2, 3.7,  c="#9aa0a4", lw=1.2)     # vertical drop
# round vent face (octagon) on the front/south of the drop, pointing into room
cy_, cz_, rr = 4.35, 2.45, 0.45
ov = [(dx1, cy_+rr*np.cos(a), cz_+rr*np.sin(a)) for a in np.linspace(0, 2*np.pi, 9)]
for i in range(8): seg(ov[i], ov[i+1], "#9aa0a4", 1.2)

# ---------- EAST ART WALL (x=RX) ----------
rect_x(RX-0.02, 4.6, 6.5, 1.0, 2.4, "0.2", 1.6)             # framed nude photo
# credenza / sideboard along east wall with anglepoise lamp + plants
box(9.2, RX, 3.6, 7.0, 0, 0.85, c="#6b4f33", lw=1.0)        # credenza
# anglepoise lamp (base -> upright -> arm)
seg((9.5, 6.4, 0.85), (9.5, 6.4, 1.7), "#222", 1.4)
seg((9.5, 6.4, 1.7), (9.2, 6.0, 1.55), "#222", 1.4)
seg((9.2, 6.0, 1.55), (9.05, 5.8, 1.25), "#222", 1.4)
for py in (4.1, 4.7, 5.3):                                  # potted plants on credenza
    box(9.45, 9.8, py, py+0.35, 0.85, 1.25, c="#3f7d3f", lw=0.9)

# ---------- SOUTH OFFICE WALL (y=0): door ----------
rect_y(0.02, 4.0, 5.8, 0.0, 2.1, "#8a5a2b", 1.6)

# ---------- FURNITURE ----------
# desk island + monitors + chairs (sitting space in front toward south)
box(3.4, 7.8, 2.6, 3.7, 0, 0.75, c="#333", lw=1.0)               # desk top at z=0.75
for mx in (3.9, 5.1, 6.3):
    box(mx, mx+0.55, 2.82, 3.12, 0.70, 1.24, c="#cfd3d6", lw=1.0) # monitors ON desk (base embedded into top), screens face S
for cx in (4.2, 5.5, 6.8):
    box(cx-0.25, cx+0.25, 1.5, 2.05, 0, 1.05, c="#222", lw=0.9)   # chairs south of desk (people face N)
# sofas + coffee table (against west arch wall)
box(0.2, 1.5, 3.6, 7.1, 0, 0.7, c="#cfc6b4", lw=1.0)
box(1.5, 4.3, 6.1, 7.1, 0, 0.7, c="#cfc6b4", lw=1.0)
box(2.0, 2.9, 3.9, 5.5, 0, 0.4, c="#6b4f33", lw=1.0)   # long axis along Y -> perpendicular to desk (long X)
# dining table + chairs (along north windows)
box(3.0, 7.0, 9.4, 11.2, 0, 0.75, c="#4a3526", lw=1.0)
for cx in (3.4, 4.8, 6.2):
    box(cx-0.22, cx+0.22, 8.9, 9.34, 0, 0.95, c="#b89b6e", lw=0.8)
    box(cx-0.22, cx+0.22, 11.26, 11.7, 0, 0.95, c="#b89b6e", lw=0.8)
# credenza
box(7.6, 9.5, 10.9, 11.6, 0, 0.9, c="#6b4f33", lw=1.0)

# ====================== OBJECT LABELS (3D anchors) ======================
# label anchors sit ON each object (mid-height), not floating above it
LABELS = [
    ((0.15, 6.6, 1.7),  "arch + painting"),   # painting z1.1-2.3
    ((0.45, 4.8, 1.0),  "bookshelf"),         # shelf z0-2.0
    ((0.45, 8.7, 1.0),  "bookshelf"),
    ((1.0, 4.35, 2.5),  "duct + vent"),       # vent ~z2.45
    ((0.9, 5.6, 0.4),   "sofas"),             # sofa z0-0.7
    ((2.45, 4.7, 0.25), "coffee table"),      # table z0-0.4 (long axis Y)
    ((5.6, 2.97, 0.82), "desk + monitors"),   # on the desktop/monitor base
    ((5.5, 1.78, 0.55), "office chairs"),     # chair z0-1.05
    ((4.9, 0.06, 1.0),  "DOOR"),              # door z0-2.1
    ((5.0, 11.95, 2.4), "factory windows + city"),
    ((5.0, 10.3, 0.45), "dining table"),      # dining z0-0.75
    ((8.55, 11.2, 0.55),"plants"),            # credenza z0-0.9
    ((9.98, 5.55, 1.7), "nude photo (art wall)"),  # photo z1.0-2.4
    ((9.6, 5.3, 0.5),   "credenza + lamp"),   # credenza z0-0.85
]

# ====================== PINHOLE CAMERA ======================
def render(ax, eye, target, focal_mm=28, title="", near=0.12):
    # focal_mm = full-frame-equivalent focal length (36mm sensor width)
    hfov_deg = np.degrees(2*np.arctan(36.0/(2*focal_mm)))
    eye = np.array(eye, float); target = np.array(target, float)
    f = target - eye; f = f/np.linalg.norm(f)
    up = np.array([0,0,1.0])
    rgt = np.cross(f, up); rgt = rgt/np.linalg.norm(rgt)
    u = np.cross(rgt, f)
    focal = 1.0/np.tan(np.radians(hfov_deg)/2)
    def cam(P): v = P-eye; return np.array([v@rgt, v@u, v@f])
    def proj(c): return np.array([c[0]/c[2]*focal, c[1]/c[2]*focal])
    # translucent volume faces first (painter's algo: far -> near), behind the edges
    fpolys = []
    for pts, col in FACES:
        cps = [cam(p) for p in pts]
        if any(cp[2] <= near for cp in cps): continue
        fpolys.append((float(np.mean([cp[2] for cp in cps])), [proj(cp) for cp in cps], col))
    for depth, pp, col in sorted(fpolys, key=lambda t: -t[0]):
        ax.add_patch(plt.Polygon(pp, closed=True, facecolor=col, edgecolor="none", alpha=0.10, zorder=1))
    for P0, P1, c, lw in S:
        c0, c1 = cam(P0), cam(P1)
        if c0[2] <= near and c1[2] <= near: continue
        if c0[2] <= near:
            t = (near-c0[2])/(c1[2]-c0[2]); c0 = c0 + t*(c1-c0)
        elif c1[2] <= near:
            t = (near-c1[2])/(c0[2]-c1[2]); c1 = c1 + t*(c0-c1)
        a, b = proj(c0), proj(c1)
        dmean = (c0[2]+c1[2])/2.0
        lw_eff = float(np.clip(lw*(4.5/dmean), 0.3, 3.2))   # nearer = thicker, farther = thinner
        ax.plot([a[0], b[0]], [a[1], b[1]], color=c, lw=lw_eff, solid_capstyle="round")
    # object labels: dot on object + text pushed apart vertically + leader line
    labs = []
    for P, txt in LABELS:
        cc = cam(np.array(P, float))
        if cc[2] <= near: continue
        p = proj(cc)
        if abs(p[0]) > 1.05 or abs(p[1]) > 0.68: continue
        fs = float(np.clip(8.0*(4.5/cc[2]), 5.5, 12.0))
        labs.append({"x":float(p[0]),"y":float(p[1]),"ax":float(p[0]),"ay":float(p[1]),"t":txt,"fs":fs})
    GAP = 0.075
    for _ in range(80):                       # force-based vertical separation
        moved = False
        for i in range(len(labs)):
            for j in range(i+1, len(labs)):
                if abs(labs[i]["x"]-labs[j]["x"]) < 0.30 and abs(labs[i]["y"]-labs[j]["y"]) < GAP:
                    s = (GAP-abs(labs[i]["y"]-labs[j]["y"]))/2 + 0.002
                    hi, lo = (i, j) if labs[i]["y"] >= labs[j]["y"] else (j, i)
                    labs[hi]["y"] += s; labs[lo]["y"] -= s; moved = True
        if not moved: break
    for L in labs:
        L["y"] = min(max(L["y"], -0.66), 0.66)
        if abs(L["y"]-L["ay"]) > 0.02:
            ax.plot([L["ax"], L["x"]], [L["ay"], L["y"]], color="#b00020", lw=0.4, alpha=0.5, zorder=9)
        ax.plot(L["ax"], L["ay"], 'o', color="#b00020", ms=2.5, zorder=11)
        ax.text(L["x"], L["y"], L["t"], fontsize=L["fs"], color="#b00020", ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="#b00020", lw=0.5, alpha=0.9), zorder=10)
    # frame matches the lens: horizontal hfov edge = +/-1, 3:2 aspect
    ax.set_xlim(-1, 1); ax.set_ylim(-2/3, 2/3)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(f"{title}  [{focal_mm}mm]", fontsize=9, fontweight="bold")

EH = 1.55  # eye height
# (name, eye, target, focal_mm, title)
views = [
    ("v1_NW_to_SE", (0.7,11.3,EH), (8.0,2.5,1.0), 24, "NW corner -> SE"),
    ("v2_NE_to_SW", (9.3,11.3,EH), (2.0,2.5,1.0), 24, "NE corner -> SW"),
    ("v3_SE_to_NW", (9.3,0.7,EH),  (2.5,11.0,1.2),24, "SE corner -> NW (orig photo)"),
    ("v4_SW_to_NE", (0.7,0.7,EH),  (8.0,11.0,1.2),24, "SW corner -> NE"),
    ("v5_CAMB",     (0.35,6.6,EH), (5.0,1.5,1.0), 28, "CAM B: painting -> monitors"),
    ("v6_face_WEST",(7.6,6.4,EH),  (0.0,6.4,1.4), 28, "face WEST: arch+painting+sofas+duct"),
    ("v7_face_NORTH",(5.0,3.3,EH), (5.4,12.0,1.6),28, "face NORTH: windows+dining+plants"),
    ("v8_face_EAST",(3.0,5.1,EH),  (10.0,5.2,1.4),28, "face EAST: art wall+credenza+lamp"),
    ("v9_face_SOUTH",(4.6,9.2,EH), (5.3,0.0,1.2), 28, "face SOUTH: office+desks+door"),
]

# ---- contact sheet (3x3) ----
fig, axes = plt.subplots(3, 3, figsize=(19, 13))
axes = axes.ravel()
for ax, (nm, eye, tgt, fmm, ttl) in zip(axes, views):
    render(ax, eye, tgt, focal_mm=fmm, title=ttl)
fig.suptitle("Concrete Loft — 3D wireframe coverage set (4 corners + CAM B + 4 wall-facing)",
             fontsize=14, fontweight="bold")
plt.tight_layout(rect=[0,0,1,0.97])
plt.savefig("/Users/bash/Desktop/viraladsgen-service/video-gen/room_3d.png", dpi=110, bbox_inches="tight")
print("saved room_3d.png")

# ---- individual full-size exports ----
for nm, eye, tgt, fmm, ttl in views:
    f, a = plt.subplots(figsize=(12, 8))
    render(a, eye, tgt, focal_mm=fmm, title=ttl)
    f.savefig(f"/Users/bash/Desktop/viraladsgen-service/video-gen/wireframe_{nm}.png",
              dpi=150, bbox_inches="tight")
    plt.close(f)
    print(f"saved wireframe_{nm}.png")

# ---- TOP-DOWN COVERAGE MAP ----
fig2, axc = plt.subplots(figsize=(9, 10))
axc.add_patch(plt.Rectangle((0,0), RX, RY, fill=False, ec="0.5", lw=1.2))
axc.plot([0,RX],[RY,RY], color="#2f7fbf", lw=4)
axc.text(RX/2, RY+0.3, "NORTH: windows", ha="center", color="#2f7fbf", fontsize=8)
axc.text(-0.3, RY/2, "WEST: arch/duct", rotation=90, va="center", ha="right", fontsize=8, color="0.4")
axc.text(RX/2, -0.5, "SOUTH: office+door", ha="center", fontsize=8, color="0.4")
axc.text(RX+0.3, RY/2, "EAST: art wall+credenza", rotation=90, va="center", ha="left", fontsize=8, color="0.4")
cols = plt.cm.tab10(np.linspace(0,1,len(views)))
for (nm, eye, tgt, fmm, ttl), col in zip(views, cols):
    ex,ey = eye[0],eye[1]; tx,ty = tgt[0],tgt[1]
    ang = np.arctan2(ty-ey, tx-ex)
    hf = np.radians(np.degrees(2*np.arctan(36.0/(2*fmm)))/2)
    L = 13
    axc.add_patch(plt.Polygon([(ex,ey),(ex+L*np.cos(ang-hf),ey+L*np.sin(ang-hf)),
                               (ex+L*np.cos(ang+hf),ey+L*np.sin(ang+hf))], closed=True,
                              facecolor=col, alpha=0.08, ec=col, lw=0.6))
    axc.plot(ex,ey,'o',color=col,ms=9)
    axc.text(ex,ey, nm.split("_")[0][1:], ha="center", va="center", fontsize=6.5, color="w", fontweight="bold")
axc.set_xlim(-2,RX+4); axc.set_ylim(-2,RY+2); axc.set_aspect("equal"); axc.axis("off")
axc.legend([plt.Line2D([0],[0],marker='o',color='w',markerfacecolor=c,ms=8) for c in cols],
           [f"{i+1}. {v[4]}" for i,v in enumerate(views)], loc="upper center",
           bbox_to_anchor=(0.5,-0.02), fontsize=7, ncol=2, frameon=False)
axc.set_title("Camera coverage map (positions + FOV cones)", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.savefig("/Users/bash/Desktop/viraladsgen-service/video-gen/coverage_map.png", dpi=130, bbox_inches="tight")
print("saved coverage_map.png")
