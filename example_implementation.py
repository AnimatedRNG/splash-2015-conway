#!/bin/env python3

from life_renderer import LifeWindow

living_cells = set()
ROWS, COLS = 100, 100

def setup(life_window):
	global living_cells
	living_cells = set([(55, 55), (54, 55), (55, 54), \
		 (56, 55), (56, 56)])
	for cell in living_cells:
		life_window.create_cell(row = cell[0], col = cell[1])


def loop(life_window):
	life_window.clear_grid()
	check_cells = set(living_cells)
	for cell in set(living_cells):
		check_cells = check_cells.union(check_cells, set(__get_neighbors__(cell, living_cells, False)))
	temp_living_cells = set(living_cells)	
	for cell in check_cells:
		neighbor_count = len(__get_neighbors__(cell, temp_living_cells))
		if neighbor_count < 2 or neighbor_count > 3:
			living_cells.discard(cell)
		elif neighbor_count == 3:
			living_cells.add(cell)

	for cell in living_cells:
		life_window.create_cell(row = cell[0], col = cell[1])


def __get_neighbors__(pos, cells, live_only = True, torus_used = True):
	positions = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), \
		(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1] + 1), \
		(pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1] + 1)]

	torus = []
	for pos in positions:
		if torus_used:
			if pos[0] < 0:
				pos = (ROWS + pos[0], pos[1])
			elif pos[0] > ROWS:
				pos = (pos[0] - ROWS, pos[1])
			if pos[1] < 0:
				pos = (pos[0], COLS + pos[1])
			elif pos[1] > ROWS:
				pos = (pos[0], pos[1] - COLS)
		torus.append(pos)

	if not live_only:
		return torus

	neighbors = []
	for p in torus:
		if p in cells:
			neighbors.append(p)
	return neighbors


life_window = LifeWindow(ROWS, COLS, setup, loop)