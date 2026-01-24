import os
from pathlib import Path
from typing import Any
from grid_universe.renderer.image import ImageMap, ImageRenderer as BaseImageRenderer


# Default asset root directory.
DEFAULT_ASSET_ROOT = os.path.join(Path(__file__).parent.resolve(), "assets")

# Mapping from (appearance name, properties) to image file/directory names.
IMAGE_MAP: ImageMap = ImageMap(
    {
        ("human", tuple([])): "human",
        ("human", tuple(["dead"])): "sleeping",
        ("coin", tuple([])): "coin",
        ("gem", tuple(["requirable"])): "gem",
        ("box", tuple(["pushable"])): "box",
        ("key", tuple([])): "key",
        ("door", tuple(["locked"])): "locked",
        ("door", tuple([])): "opened",
        ("shield", tuple(["immunity"])): "shield",
        ("ghost", tuple(["phasing"])): "ghost",
        ("boots", tuple(["speed"])): "boots",
        ("lava", tuple([])): "lava",
        ("exit", tuple([])): "exit",
        ("wall", tuple([])): "wall",
        ("floor", tuple([])): "floor",
    }
)


class ImageRenderer(BaseImageRenderer):
    """Image renderer for the Grid Adventure environment."""

    def __init__(
        self,
        asset_root: str = DEFAULT_ASSET_ROOT,
        image_map: ImageMap = IMAGE_MAP,
        **kwargs: Any,
    ):
        super().__init__(asset_root=asset_root, image_map=image_map, **kwargs)
