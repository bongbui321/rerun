# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/re_types/definitions/rerun/archetypes/boxes2d.fbs".

# You can extend this class by creating a "Boxes2DExt" class in "boxes2d_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components
from .._baseclasses import Archetype
from .boxes2d_ext import Boxes2DExt

__all__ = ["Boxes2D"]


@define(str=False, repr=False, init=False)
class Boxes2D(Boxes2DExt, Archetype):
    """
    **Archetype**: 2D boxes with half-extents and optional center, rotations, rotations, colors etc.

    Example
    -------
    ### Simple 2D boxes:
    ```python
    import rerun as rr

    rr.init("rerun_example_box2d", spawn=True)

    rr.log("simple", rr.Boxes2D(mins=[-1, -1], sizes=[2, 2]))
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/box2d_simple/ac4424f3cf747382867649610cbd749c45b2020b/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/box2d_simple/ac4424f3cf747382867649610cbd749c45b2020b/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/box2d_simple/ac4424f3cf747382867649610cbd749c45b2020b/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/box2d_simple/ac4424f3cf747382867649610cbd749c45b2020b/1200w.png">
      <img src="https://static.rerun.io/box2d_simple/ac4424f3cf747382867649610cbd749c45b2020b/full.png" width="640">
    </picture>
    </center>

    """

    # __init__ can be found in boxes2d_ext.py

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            half_sizes=None,  # type: ignore[arg-type]
            centers=None,  # type: ignore[arg-type]
            colors=None,  # type: ignore[arg-type]
            radii=None,  # type: ignore[arg-type]
            labels=None,  # type: ignore[arg-type]
            draw_order=None,  # type: ignore[arg-type]
            class_ids=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> Boxes2D:
        """Produce an empty Boxes2D, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    half_sizes: components.HalfSizes2DBatch = field(
        metadata={"component": "required"},
        converter=components.HalfSizes2DBatch._required,  # type: ignore[misc]
    )
    # All half-extents that make up the batch of boxes.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    centers: components.Position2DBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.Position2DBatch._optional,  # type: ignore[misc]
    )
    # Optional center positions of the boxes.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    colors: components.ColorBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ColorBatch._optional,  # type: ignore[misc]
    )
    # Optional colors for the boxes.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    radii: components.RadiusBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.RadiusBatch._optional,  # type: ignore[misc]
    )
    # Optional radii for the lines that make up the boxes.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    labels: components.TextBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.TextBatch._optional,  # type: ignore[misc]
    )
    # Optional text labels for the boxes.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    draw_order: components.DrawOrderBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.DrawOrderBatch._optional,  # type: ignore[misc]
    )
    # An optional floating point value that specifies the 2D drawing order.
    #
    # Objects with higher values are drawn on top of those with lower values.
    #
    # The default for 2D boxes is 10.0.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    class_ids: components.ClassIdBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ClassIdBatch._optional,  # type: ignore[misc]
    )
    # Optional `ClassId`s for the boxes.
    #
    # The class ID provides colors and labels if not specified explicitly.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
