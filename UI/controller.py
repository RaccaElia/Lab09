import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        distanza = self._view._txtIn.value
        self._model.buildGraph(distanza)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"numero nodi: {self._model.getNumNodes()}"))
        self._view._txt_result.controls.append(ft.Text(f"numero archi: {self._model.getNumEdges()}"))
        for arco in self._model.getArchi():
            self._view._txt_result.controls.append(ft.Text(f"from {arco[0]} to {arco[1]}: {self._model._grafo[arco[0]][arco[1]]['distanza']} miles"))
        self._view.update_page()