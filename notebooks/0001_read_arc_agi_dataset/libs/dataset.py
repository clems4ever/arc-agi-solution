import yaml
import os

def grid_size(g):
    return [len(g[0]), len(g)]

class Dataset:
    def __init__(self, dir):
        self._dir = dir
        self._files = os.listdir(dir)

    def __len__(self):
        return len(self._files)

    def get(self, i):
        file = self._files[i]
        path = f"{self._dir}/{file}" 
        with open(path, "r") as f:
            return Data(yaml.safe_load(f), path)
        
class Data:
    def __init__(self, data, path):
        self._data = data
        self._path = path
    
    @property
    def path(self):
        return self._path

    def train(self, i):
        grids = self._data['train'][i]
        return { 
            'input': Grid(grids['input']),
            'output': Grid(grids['output']),
        }

    def test(self, i):
        grids = self._data['test'][0]
        return {
            'input': Grid(grids['input']),
            'output': Grid(grids['output']),
        }

class Grid:
    def __init__(self, grid):
        self._grid = grid

    def size(self):
        return [len(self._grid), len(self._grid[0])]