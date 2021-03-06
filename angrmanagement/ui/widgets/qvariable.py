
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt

from .qgraph_object import QGraphObject


class QVariable(QGraphObject):

    IDENT_LEFT_PADDING = 5
    OFFSET_LEFT_PADDING = 12

    def __init__(self, workspace, disasm_view, variable, config):
        super(QVariable, self).__init__()

        # initialization
        self.workspace = workspace
        self.disasm_view = disasm_view
        self.variable = variable
        self._config = config

        self._variable_name = None
        self._variable_name_width = None
        self._variable_ident = None
        self._variable_ident_width = None
        self._variable_offset = None
        self._variable_offset_width = None

        self._init_widgets()

    #
    # Public methods
    #

    def paint(self, painter):

        x = self.x

        # variable name
        painter.setPen(Qt.darkGreen)
        painter.drawText(x, self.y + self._config.disasm_font_ascent, self._variable_name)
        x += self._variable_name_width
        x += self.IDENT_LEFT_PADDING


        # variable ident
        if self.disasm_view.show_variable_identifier:
            painter.setPen(Qt.blue)
            painter.drawText(x, self.y + self._config.disasm_font_ascent, self._variable_ident)
            x += self._variable_ident_width
            x += self.OFFSET_LEFT_PADDING

        # variable offset
        painter.setPen(Qt.darkYellow)
        painter.drawText(x, self.y + self._config.disasm_font_ascent, self._variable_offset)
        x += self._variable_offset_width

    def refresh(self):
        super(QVariable, self).refresh()

        self._update_size()

    #
    # Private methods
    #

    def _init_widgets(self):

        # variable name
        self._variable_name = "" if not self.variable.name else self.variable.name
        # variable ident
        self._variable_ident = "<%s>" % ("" if not self.variable.ident else self.variable.ident)
        # variable offset
        self._variable_offset = "%#x" % self.variable.offset

        self._update_size()

    def _update_size(self):

        self._variable_name_width = len(self._variable_name) * self._config.disasm_font_width
        self._variable_ident_width = len(self._variable_ident) * self._config.disasm_font_width
        self._variable_offset_width = len(self._variable_offset) * self._config.disasm_font_width

        self._width = self._variable_name_width + \
                      self.OFFSET_LEFT_PADDING + self._variable_offset_width
        if self.disasm_view.show_variable_identifier:
            self._width += self.IDENT_LEFT_PADDING + self._variable_ident_width

        self._height = self._config.disasm_font_height
