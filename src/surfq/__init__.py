# SurfQ Copyright (C) 2025 João Ramos
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""A library for simulating the surface code.

This library provides a set of tools for simulating the behavior of the surface code.

It includes classes for representing the lattice, the qubits, and the
stabilizers, as well as functions for applying quantum gates and simulating
errors.

Typical usage example:

  >>> from surfq import Lattice
  >>>
  >>> lattice = Lattice(3)
  >>> lattice.qubits[0, 0].X()
  >>> lattice.qubits[0, 1].Z()
  >>> lattice.show()
"""

from .lattice import Lattice

__all__ = ["Lattice"]
