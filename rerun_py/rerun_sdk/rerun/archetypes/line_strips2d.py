# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/re_types/definitions/rerun/archetypes/line_strips2d.fbs".

# You can extend this class by creating a "LineStrips2DExt" class in "line_strips2d_ext.py".

from __future__ import annotations

from typing import Any

from attrs import define, field

from .. import components, datatypes
from .._baseclasses import Archetype
from ..error_utils import catch_and_log_exceptions

__all__ = ["LineStrips2D"]


@define(str=False, repr=False, init=False)
class LineStrips2D(Archetype):
    """
    **Archetype**: 2D line strips with positions and optional colors, radii, labels, etc.

    Example
    -------
    ### `line_strip2d_batch`:
    ```python
    import rerun as rr
    import rerun.blueprint as rrb

    rr.init("rerun_example_line_strip2d_batch", spawn=True)

    rr.log(
        "strips",
        rr.LineStrips2D(
            [
                [[0, 0], [2, 1], [4, -1], [6, 0]],
                [[0, 3], [1, 4], [2, 2], [3, 4], [4, 2], [5, 4], [6, 3]],
            ],
            colors=[[255, 0, 0], [0, 255, 0]],
            radii=[0.025, 0.005],
            labels=["one strip here", "and one strip there"],
        ),
    )

    # Set view bounds:
    rr.send_blueprint(rrb.Spatial2DView(visual_bounds=rrb.VisualBounds(min=[-1, -3], max=[7, 6])))
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/line_strip2d_batch/d8aae7ca3d6c3b0e3b636de60b8067fa2f0b6db9/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/line_strip2d_batch/d8aae7ca3d6c3b0e3b636de60b8067fa2f0b6db9/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/line_strip2d_batch/d8aae7ca3d6c3b0e3b636de60b8067fa2f0b6db9/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/line_strip2d_batch/d8aae7ca3d6c3b0e3b636de60b8067fa2f0b6db9/1200w.png">
      <img src="https://static.rerun.io/line_strip2d_batch/d8aae7ca3d6c3b0e3b636de60b8067fa2f0b6db9/full.png" width="640">
    </picture>
    </center>

    """

    def __init__(
        self: Any,
        strips: components.LineStrip2DArrayLike,
        *,
        radii: components.RadiusArrayLike | None = None,
        colors: datatypes.Rgba32ArrayLike | None = None,
        labels: datatypes.Utf8ArrayLike | None = None,
        draw_order: components.DrawOrderLike | None = None,
        class_ids: datatypes.ClassIdArrayLike | None = None,
    ):
        """
        Create a new instance of the LineStrips2D archetype.

        Parameters
        ----------
        strips:
            All the actual 2D line strips that make up the batch.
        radii:
            Optional radii for the line strips.
        colors:
            Optional colors for the line strips.
        labels:
            Optional text labels for the line strips.
        draw_order:
            An optional floating point value that specifies the 2D drawing order of each line strip.

            Objects with higher values are drawn on top of those with lower values.
        class_ids:
            Optional `ClassId`s for the lines.

            The class ID provides colors and labels if not specified explicitly.

        """

        # You can define your own __init__ function as a member of LineStrips2DExt in line_strips2d_ext.py
        with catch_and_log_exceptions(context=self.__class__.__name__):
            self.__attrs_init__(
                strips=strips, radii=radii, colors=colors, labels=labels, draw_order=draw_order, class_ids=class_ids
            )
            return
        self.__attrs_clear__()

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            strips=None,  # type: ignore[arg-type]
            radii=None,  # type: ignore[arg-type]
            colors=None,  # type: ignore[arg-type]
            labels=None,  # type: ignore[arg-type]
            draw_order=None,  # type: ignore[arg-type]
            class_ids=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> LineStrips2D:
        """Produce an empty LineStrips2D, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    strips: components.LineStrip2DBatch = field(
        metadata={"component": "required"},
        converter=components.LineStrip2DBatch._required,  # type: ignore[misc]
    )
    # All the actual 2D line strips that make up the batch.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    radii: components.RadiusBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.RadiusBatch._optional,  # type: ignore[misc]
    )
    # Optional radii for the line strips.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    colors: components.ColorBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ColorBatch._optional,  # type: ignore[misc]
    )
    # Optional colors for the line strips.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    labels: components.TextBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.TextBatch._optional,  # type: ignore[misc]
    )
    # Optional text labels for the line strips.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    draw_order: components.DrawOrderBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.DrawOrderBatch._optional,  # type: ignore[misc]
    )
    # An optional floating point value that specifies the 2D drawing order of each line strip.
    #
    # Objects with higher values are drawn on top of those with lower values.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    class_ids: components.ClassIdBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ClassIdBatch._optional,  # type: ignore[misc]
    )
    # Optional `ClassId`s for the lines.
    #
    # The class ID provides colors and labels if not specified explicitly.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
