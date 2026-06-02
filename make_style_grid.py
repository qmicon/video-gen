"""
Combine the four loft style photos into one 2x2 grid image.
Put the 4 photos in  video-gen/style/  (any names; sorted alphabetically),
then run:  .venv/bin/python make_style_grid.py  ->  style_grid.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob, os

folder = "/Users/bash/Desktop/viraladsgen-service/video-gen/style"
paths = sorted(glob.glob(os.path.join(folder, "*.png")) +
               glob.glob(os.path.join(folder, "*.jpg")) +
               glob.glob(os.path.join(folder, "*.jpeg")) +
               glob.glob(os.path.join(folder, "*.webp")))
assert len(paths) >= 4, f"need 4 images in {folder}, found {len(paths)}: {paths}"
paths = paths[:4]
print("using:", [os.path.basename(p) for p in paths])

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
for ax, p in zip(axes.ravel(), paths):
    ax.imshow(mpimg.imread(p))
    ax.axis("off")
plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0.01, hspace=0.01)
fig.savefig("/Users/bash/Desktop/viraladsgen-service/video-gen/style_grid.png",
            dpi=150, bbox_inches="tight", pad_inches=0)
print("saved style_grid.png")
