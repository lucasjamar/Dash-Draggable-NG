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


class DraggableDashboardResponsive(Component):
    """A DraggableDashboardResponsive component.
DraggableDashboard is a component for building
dashboards with draggable and resizable items.
It takes a list of children and display them in
div elements that can be moved around the page.
The initial size of each element can either be
defined with the layout argument or by wrapping
each element with the DashboardItem component.
By default, DraggableDashboard will saved the
position of the elements on client side, when
moved on the page. But you can also save it
on server side by defining a callback with :
`Input("<my-id>", "layout")`.

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional):
    Children is a list of the items (dash Components and/or
    DashboardItem) to diplay on the layout.  By default all the items
    can be dragged and resized.

- id (string; optional):
    (string) The ID used to identify this component in Dash callbacks.
    The id is also used to automatically save the layout on client
    side.

- breakpoints (dict; optional):
    ({breakpoint: number}) The breakpoints for the responsive layout.
    For each screen size (breakpoint) we can define a different
    layout.  (see also 'layouts' and 'gridCols' arguments)  Default
    value is {lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}.

- className (string; default ""):
    (string) class passed to the react-grid-layout component.

- clearSavedLayout (boolean; default False):
    (bool) If set to True, then the layout saved in the client browser
    will be cleared in the next page load.

- gridCols (dict; optional):
    ({breakpoint: number}) the number of columns in the grid layout.
    Default value is {lg: 12, md: 10, sm: 6, xs: 4, xxs: 2}.

- height (number; optional):
    (number) height of a row (in px).  Default value is 30.

- layouts (dict; optional):
    Layout is a list(python)/vector(R) of dictionnary(Python)/list(R)
    with the format:  {x: number, y: number, w: number, h: number}
    The index into the layout must match the id used on each item
    component with DashboardItem.  If you choose to use custom keys,
    you can specify that key in the layout  array objects like so:
    {i: string, x: number, y: number, w: number, h: number}  The ID
    used to identify this component in Dash callbacks.  The id is also
    used to automatically save the layout on client side.

- ncols (number; optional):
    ({breakpoint: number}) the default number of columns by item.
    Default value is {lg: 6, md: 5, sm: 3, xs: 4, xxs: 2}.

- nrows (number; optional):
    (number) the default number of row by item.  Default value is 8.

- save (boolean; default True):
    (bool) If True, then the layout is automatically saved on client
    browser.  Default value is True."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'dash_draggable'
    _type = 'DraggableDashboardResponsive'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        layouts: typing.Optional[dict] = None,
        breakpoints: typing.Optional[dict] = None,
        gridCols: typing.Optional[dict] = None,
        save: typing.Optional[bool] = None,
        clearSavedLayout: typing.Optional[bool] = None,
        ncols: typing.Optional[NumberType] = None,
        nrows: typing.Optional[NumberType] = None,
        height: typing.Optional[NumberType] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'breakpoints', 'className', 'clearSavedLayout', 'gridCols', 'height', 'layouts', 'ncols', 'nrows', 'save', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'breakpoints', 'className', 'clearSavedLayout', 'gridCols', 'height', 'layouts', 'ncols', 'nrows', 'save', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DraggableDashboardResponsive, self).__init__(children=children, **args)

setattr(DraggableDashboardResponsive, "__init__", _explicitize_args(DraggableDashboardResponsive.__init__))
