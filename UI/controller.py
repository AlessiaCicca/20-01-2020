import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        grafo = self._model.creaGrafo(self._view.ddruolo.value)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))

        self._view.update_page()
    def handle_connessi(self, e):
        grafo = self._model.creaGrafo(self._view.ddruolo.value)
        for arco in grafo.edges:
            self._view.txt_result.controls.append(ft.Text(f"({arco[0].artist_id},{arco[1].artist_id}): {grafo[arco[0]][arco[1]]["weight"]}"))
        self._view.update_page()
    def handle_percorso(self, e):
        soluzione,peso=self._model.bestPath(int(self._view.txt_artisti.value))
        self._view.txt_result.controls.append(
            ft.Text(f"PERCORSO PIU' LUNGO:{peso}"))
        for nodi in soluzione:
            self._view.txt_result.controls.append(ft.Text(f"{nodi.artist_id}"))
        self._view.update_page()
    def fillDD(self):
        ruoli = self._model.ruoli
        for ruolo in ruoli:
            self._view.ddruolo.options.append(ft.dropdown.Option(
                text=ruolo))
