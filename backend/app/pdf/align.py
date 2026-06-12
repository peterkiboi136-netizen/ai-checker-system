def convert_bbox(bbox, render_scale):
    x0, y0, x1, y1 = bbox

    return {
        "x": x0 * render_scale,
        "y": y0 * render_scale,
        "width": (x1 - x0) * render_scale,
        "height": (y1 - y0) * render_scale,
    }