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


class DashboardItemResponsive(Component):
    """A DashboardItemResponsive component.
DashboardItemResponsive is a wrapper that is intended to be used with DraggableDashboard.
DashboardItemResponsive specify the position and size of the item on the dashboard.

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional):
    The child or list of children wrapped by the component.

- id (string | dict; optional):
    The ID used to identify this component in Dash callbacks.

- __isDashboardItem (boolean; default True):
    This is an internal prop used to identify the component, this
    property default value is True.   Setting this value to False is
    equivalent to not using the DashboardItem wrapper.

- h (number | dict; default NROWS):
    The height on the of y axis (default is 4).

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

- w (number | dict; default NCOLS):
    The width of the x axis (default is 6).

- x (number | dict; default 0):
    The position on the x axis in number of columns (by default, the
    max is 12).

- y (number | dict; default 0):
    The position on the y axis (the unit is 30px, by default)."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'dash_draggable'
    _type = 'DashboardItemResponsive'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        x: typing.Optional[typing.Union[NumberType, dict]] = None,
        y: typing.Optional[typing.Union[NumberType, dict]] = None,
        w: typing.Optional[typing.Union[NumberType, dict]] = None,
        h: typing.Optional[typing.Union[NumberType, dict]] = None,
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
        __isDashboardItem: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', '__isDashboardItem', 'h', 'isBounded', 'isDraggable', 'isResizable', 'maxH', 'maxW', 'minH', 'minW', 'moved', 'resizeHandles', 'static', 'w', 'x', 'y']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', '__isDashboardItem', 'h', 'isBounded', 'isDraggable', 'isResizable', 'maxH', 'maxW', 'minH', 'minW', 'moved', 'resizeHandles', 'static', 'w', 'x', 'y']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DashboardItemResponsive, self).__init__(children=children, **args)

setattr(DashboardItemResponsive, "__init__", _explicitize_args(DashboardItemResponsive.__init__))
