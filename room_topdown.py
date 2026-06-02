"""
Concrete loft — Top-Down v5 (CORNER UNIT, arch on LEFT) + WALL ELEVATIONS.

Plan (N up):
  N (top)   = WINDOW wall (glass + city + sun); dining table + plants + credenza along it
  W (left)  = ARCH/DUCT wall: arched alcove + woman painting, duct drop near NW, bookshelves, sofas
  S (bottom)= DESK/OFFICE wall (opposite windows) + DOOR; desks are an ISLAND with sitting space
  E (right) = plain concrete wall (leaning art)
  windows N and arch W are ADJACENT, meeting at the NW corner.

Around the plan, four ELEVATION strips show what is mounted on each wall.
Render:  .venv/bin/python room_topdown.py  ->  room_topdown.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, Polygon, Circle, Wedge
import numpy as np

W, H = 10.0, 12.0
fig, ax = plt.subplots(figsize=(13, 13.5))
ax.set_xlim(-6.2, 16.5)
ax.set_ylim(-6.0, 17.2)
ax.set_aspect("equal")
ax.axis("off")

def box(x, y, w, h, color, label=None, alpha=0.85, fs=8, ec="0.25", lw=1.0, rot=0, tc="0.1"):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor=ec, lw=lw, alpha=alpha, zorder=3))
    if label:
        ax.text(x+w/2, y+h/2, label, ha="center", va="center", fontsize=fs, zorder=5, rotation=rot, color=tc)

# ===== PLAN GRID =====
for gx in range(0, 11):
    ax.plot([gx, gx], [0, H], color="0.93", lw=0.6, zorder=0)
for gy in range(0, 13):
    ax.plot([0, W], [gy, gy], color="0.93", lw=0.6, zorder=0)

# ===== WALLS =====
ax.plot([0, W], [H, H], color="#2f7fbf", lw=7, solid_capstyle="butt", zorder=2)  # N windows
for gx in np.arange(0.4, W, 0.85):
    ax.plot([gx, gx+0.28], [H, H+0.32], color="#2f7fbf", lw=1, zorder=2)
ax.plot([0, 0], [0, H], color="0.45", lw=9, solid_capstyle="butt", zorder=2)     # W arch/duct
ax.plot([0, W], [0, 0], color="0.45", lw=9, solid_capstyle="butt", zorder=2)     # S desk wall
ax.plot([W, W], [0, H], color="0.6", lw=7, solid_capstyle="butt", zorder=2)      # E plain
ax.text(0.2, H-0.2, "window+arch CORNER", ha="left", va="top", fontsize=7.5, color="#7a5", fontweight="bold")

# door in south wall
ax.plot([3.8, 5.6], [0, 0], color="#8a5a2b", lw=9, solid_capstyle="butt", zorder=3)

# ===== ARCH/DUCT WALL items (plan) =====
ax.add_patch(Arc((0, 6.6), 2.4, 1.5, angle=0, theta1=-90, theta2=90, color="0.3", lw=2, zorder=3))
ax.text(0.9, 6.6, "arch+\npainting", ha="left", va="center", fontsize=6.5, color="#c0392b", fontweight="bold")
box(0.05, 4.2, 0.5, 1.3, "#9b7b53", "shelf", fs=5)
box(0.05, 8.0, 0.5, 1.5, "#9b7b53", "shelf", fs=5)
ax.add_patch(Circle((0.85, 10.6), 0.4, facecolor="#cfd3d6", edgecolor="0.4", lw=1, zorder=3))
ax.text(0.85, 10.6, "duct", ha="center", va="center", fontsize=5, color="0.2")

# ===== OFFICE / DESKS (island with sitting space) =====
box(3.4, 2.6, 4.4, 1.1, "#3a3a3a", "DESK (island)", fs=8, tc="w")     # desk top
for mx in (3.9, 5.1, 6.3):                                            # monitors on SOUTH edge, screens face S
    box(mx, 2.45, 0.6, 0.25, "#f2f2f2", None, ec="0.3")
ax.annotate("", xy=(5.2, 1.95), xytext=(5.2, 2.55), arrowprops=dict(arrowstyle="-|>", color="#c0392b", lw=2), zorder=6)
for cx in (4.2, 5.5, 6.8):                                            # chairs SOUTH of desk (people sit here)
    ax.add_patch(Circle((cx, 1.5), 0.34, facecolor="#222", edgecolor="0.3", zorder=4))
ax.text(8.0, 2.0, "monitors face S\n(away from windows);\nchairs + sitting space\nhere; DOOR behind", ha="left", va="center", fontsize=6.3, color="#c0392b")
ax.annotate("", xy=(5.2, 0.15), xytext=(5.2, 1.1), arrowprops=dict(arrowstyle="-", color="0.6", lw=0.8, ls=":"), zorder=2)

# ===== SOFAS + coffee table + rug (against arch / West) =====
box(0.0, 3.4, 4.4, 3.9, "#e7e1d4", None, alpha=0.5, ec="none")
box(0.2, 3.6, 1.3, 3.5, "#d9d2c2", "sofa", fs=6, rot=90)
box(1.5, 6.1, 2.8, 1.0, "#d9d2c2", "sofa", fs=6)
box(1.7, 4.4, 1.5, 0.9, "#6b4f33", "coffee\ntable", fs=5.5, tc="w")

# ===== DINING + plants + credenza (along North windows) =====
box(3.0, 9.4, 4.0, 1.8, "#4a3526", "DINING TABLE", fs=8, tc="w")
for cx in (3.4, 4.8, 6.2):
    box(cx, 8.95, 0.42, 0.42, "#b89b6e", None, ec="0.3")
    box(cx, 11.25, 0.42, 0.42, "#b89b6e", None, ec="0.3")
box(7.6, 10.9, 1.9, 0.7, "#6b4f33", None)
ax.text(8.55, 11.25, "credenza", ha="center", va="center", fontsize=5.5, color="w")
for px in (0.8, 1.5, 2.2):
    ax.add_patch(Circle((px, 11.0), 0.28, facecolor="#3f7d3f", edgecolor="0.3", zorder=3))
ax.text(1.5, 11.7, "plants", ha="center", fontsize=5.5, color="#225522")
box(W-0.42, 4.6, 0.32, 1.9, "#2b2b2b", "nude\nphoto", fs=4.5, tc="w", rot=90)   # framed photo on east ART wall

# ===== CAM B =====
def camera(x, y, ang, fov, length, label, color, lx, ly):
    a=np.radians(ang); half=np.radians(fov/2)
    p1=(x+length*np.cos(a-half), y+length*np.sin(a-half)); p2=(x+length*np.cos(a+half), y+length*np.sin(a+half))
    ax.add_patch(Polygon([(x,y),p1,p2], closed=True, facecolor=color, alpha=0.15, edgecolor=color, lw=1.1, zorder=4))
    ax.add_patch(Circle((x,y),0.24, facecolor=color, edgecolor="k", lw=1, zorder=7))
    ax.text(lx, ly, label, ha="center", va="center", fontsize=7.5, fontweight="bold", color=color, zorder=8)
camera(0.5, 6.6, np.degrees(np.arctan2(1.5-6.6, 5.2-0.5)), 48, 8.5, "CAM B\n(painting->monitors)", "#c0392b", 2.6, 8.6)

# N arrow + sun
ax.annotate("", xy=(15.5,12.4), xytext=(15.5,10.9), arrowprops=dict(arrowstyle="-|>", color="k", lw=2))
ax.text(15.5,12.8,"N",ha="center",fontsize=11,fontweight="bold")
ax.annotate("", xy=(14.4,10.4), xytext=(15.8,11.8), arrowprops=dict(arrowstyle="-|>", color="#e8a300", lw=2.4))
ax.text(15.9,12.1,"sun",color="#e8a300",fontsize=9,fontweight="bold")

# ============================================================
#  WALL ELEVATIONS (what is mounted on each wall — vertical info)
# ============================================================
def elev_frame(x, y, w, h, title):
    ax.add_patch(Rectangle((x,y), w, h, facecolor="#f4f2ee", edgecolor="0.5", lw=1.2, zorder=1))
    ax.text(x+w/2, y+h+0.25, title, ha="center", va="bottom", fontsize=8, fontweight="bold", color="0.25")

# ---- WEST (arch/duct) elevation — left of plan ----
ex, ey, ew, eh = -5.6, 2.0, 4.2, 8.0
elev_frame(ex, ey, ew, eh, "WEST WALL (arch / duct)")
ax.add_patch(Wedge((ex+ew*0.55, ey+eh*0.42), 1.5, 0, 180, facecolor="#dcd7cd", edgecolor="0.45", lw=1.3, zorder=2))  # arch
box(ex+ew*0.40, ey+eh*0.30, 0.85, 1.15, "#2b2b2b", None, ec="0.3")   # portrait inside arch
box(ex+ew*0.60, ey+eh*0.30, 0.55, 1.15, "#2b2b2b", None, ec="0.3")
ax.text(ex+ew*0.55, ey+eh*0.22, "woman painting", ha="center", fontsize=5.5, color="#c0392b")
box(ex+0.25, ey+eh*0.18, 0.7, 2.6, "#9b7b53", "books", fs=5, rot=90)  # bookshelf
box(ex+ew-1.0, ey+eh*0.18, 0.7, 2.6, "#9b7b53", "books", fs=5, rot=90)
ax.add_patch(Rectangle((ex+ew*0.70, ey+eh*0.72), 0.55, eh*0.26, facecolor="#cfd3d6", edgecolor="0.4", zorder=2))  # duct drop
ax.text(ex+ew*0.78, ey+eh*0.85, "duct", rotation=90, fontsize=5, color="0.3", va="center")

# ---- NORTH (windows) elevation — above plan ----
nx, ny, nw, nh = 0.0, 13.6, W, 2.8
elev_frame(nx, ny, nw, nh, "NORTH WALL (factory windows + city)")
for i in range(11):
    ax.plot([nx+i*nw/10, nx+i*nw/10],[ny+0.2, ny+nh-0.2], color="#2f7fbf", lw=0.8, zorder=2)
for j in range(1,4):
    ax.plot([nx+0.2, nx+nw-0.2],[ny+j*nh/4, ny+j*nh/4], color="#2f7fbf", lw=0.8, zorder=2)
ax.plot([nx+0.4, nx+nw-0.4],[ny+0.7, ny+0.7], color="0.55", lw=2, zorder=2)  # skyline
ax.text(nx+nw*0.5, ny+0.4, "city skyline", ha="center", fontsize=5.5, color="0.4")
ax.add_patch(Circle((nx+nw*0.8, ny+nh*0.72), 0.3, facecolor="#ffe9a8", edgecolor="#e8a300", zorder=3))
ax.text(nx+nw*0.8, ny+nh*0.72, "sun", ha="center", va="center", fontsize=4.5, color="#a06b00")

# ---- SOUTH (desk wall) elevation — below plan ----
sx, sy, sw, sh = 0.0, -5.0, W, 2.6
elev_frame(sx, sy, sw, sh, "SOUTH WALL (office wall + DOOR, behind the desks)")
box(sx+sw*0.36, sy+0.25, 1.7, sh-0.5, "#8a5a2b", "DOOR", fs=7, tc="w")
box(sx+sw*0.12, sy+sh*0.45, 0.9, 1.0, "#2b2b2b", "frame", fs=4.5, tc="w")
box(sx+sw*0.72, sy+sh*0.45, 0.9, 1.0, "#2b2b2b", "frame", fs=4.5, tc="w")

# ---- EAST (solid ART wall) elevation — right of plan ----
qx, qy, qw, qh = 11.6, 2.0, 4.2, 8.0
elev_frame(qx, qy, qw, qh, "EAST WALL (solid concrete ART wall)")
box(qx+qw*0.34, qy+qh*0.42, 1.4, 1.9, "#2b2b2b", "framed\nnude\nphoto", fs=5.5, tc="w")
# window-grid light cast onto this wall
for i in range(4):
    ax.plot([qx+0.4+i*0.5, qx+0.4+i*0.5],[qy+qh*0.62, qy+qh*0.95], color="#e8d9a8", lw=2, alpha=0.7, zorder=1)
for j in range(3):
    ax.plot([qx+0.4, qx+2.2],[qy+qh*0.66+j*0.4, qy+qh*0.66+j*0.4], color="#e8d9a8", lw=2, alpha=0.7, zorder=1)
ax.text(qx+qw*0.62, qy+qh*0.20, "window-grid\nlight cast here", ha="center", fontsize=5.5, color="#a08000")

ax.text(W+1.5, H/2, "EAST = solid ART wall", rotation=90, ha="center", va="center", color="0.45", fontsize=8)
ax.set_title("Concrete Loft — Top-Down v6  +  WALL ELEVATIONS\nW=arch/duct, N=windows (only glass), S=plain+door+desks, E=solid art wall (nude photo)",
             fontsize=10.5, fontweight="bold")
plt.tight_layout()
plt.savefig("/Users/bash/Desktop/viraladsgen-service/video-gen/room_topdown.png", dpi=125, bbox_inches="tight")
print("saved room_topdown.png")
