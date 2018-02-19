from typing import Optional

from PyQt5.Qt import QObject, pyqtSlot

from cura.Machines.ContainerNode import ContainerNode


class ContainerGroup(QObject):

    def __init__(self, name: str, parent = None):
        super().__init__(parent)
        self.name = name
        self.node_for_global = None  # type: Optional[ContainerNode]
        self.nodes_for_extruders = dict()

    @pyqtSlot(result = str)
    def getName(self) -> str:
        return self.name

    def getAllKeys(self) -> set:
        result = set()
        for node in [self.node_for_global] + list(self.nodes_for_extruders.values()):
            if node is None:
                continue
            for key in node.getContainer().getAllKeys():
                result.add(key)
        return result
