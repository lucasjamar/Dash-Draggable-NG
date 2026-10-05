# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.types import NumberType  # noqa: F401
except ImportError:
    # Backwards compatibility for dash<=4.1.0
    if typing.TYPE_CHECKING:
        raise
    NumberType = typing.Union[  # noqa: F401
        typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
    ]

ComponentSingleType = typing.Union[str, int, float, Component, None]
ComponentType = typing.Union[
    ComponentSingleType,
    typing.Sequence[ComponentSingleType],
]


class DashboardItem(Component):
    """A DashboardItem component.
DashboardItem is a wrapper that is intended to be used with DraggableDashboard 
to specify the position and size of the wrapped components.

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional):
    The child or list of children wrapped by the component.

- h (number; default NROWS):
    The height on the of y axis (default is 4).

- i (string; optional):
    The ID used to identify this component in layout definition.

- isBounded (boolean; optional)

- isDraggable (boolean; optional):
    If False, will not be draggable. Overrides `static`.

- isResizable (boolean; optional):
    If False, will not be resizable. Overrides `static`.

- maxH (number; optional)

- maxW (number; optional)

- minH (number; optional)

- minW (number; optional)

- moved (boolean; optional)

- resizeHandles (string; optional)

- static (boolean; optional):
    If True, equal to `isDraggable: False, isResizable: False`.

- w (number; default NCOLS):
    The width of the x axis (default is 6).

- x (number; default 0):
    The position on the x axis in number of columns (by default, the
    max is 12).

- y (number; default 0):
    The position on the y axis (the unit is 30px, by default)."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'dash_draggable'
    _type = 'DashboardItem'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        i: typing.Optional[str] = None,
        x: typing.Optional[NumberType] = None,
        y: typing.Optional[NumberType] = None,
        w: typing.Optional[NumberType] = None,
        h: typing.Optional[NumberType] = None,
        static: typing.Optional[bool] = None,
        isDraggable: typing.Optional[bool] = None,
        isResizable: typing.Optional[bool] = None,
        isBounded: typing.Optional[bool] = None,
        maxH: typing.Optional[NumberType] = None,
        maxW: typing.Optional[NumberType] = None,
        minH: typing.Optional[NumberType] = None,
        minW: typing.Optional[NumberType] = None,
        moved: typing.Optional[bool] = None,
        resizeHandles: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'h', 'i', 'isBounded', 'isDraggable', 'isResizable', 'maxH', 'maxW', 'minH', 'minW', 'moved', 'resizeHandles', 'static', 'w', 'x', 'y']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'h', 'i', 'isBounded', 'isDraggable', 'isResizable', 'maxH', 'maxW', 'minH', 'minW', 'moved', 'resizeHandles', 'static', 'w', 'x', 'y']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DashboardItem, self).__init__(children=children, **args)

setattr(DashboardItem, "__init__", _explicitize_args(DashboardItem.__init__))
