from matplotlib.patches import Rectangle
width = detections[k].right()-detections[k].left()
height = detections[k].top()-detections[k].bottom()

rect = Rectangle((detections[k].left(),detections[k].bottom()),width,height,linewidth=1,edgecolor='g', facecolor="None")
ax.add_patch(rect)
