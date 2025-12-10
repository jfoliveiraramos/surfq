# SurfQ Copyright (C) 2025 João Ramos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
"""A module for representing Pauli operators.

This module provides a `Pauli` enum that represents the four Pauli operators:
I, X, Y, and Z. These operators are fundamental to quantum computing and are
used to describe the state of a qubit.

The `Pauli` enum provides a convenient way to work with Pauli operators in
Python. It includes methods for multiplication, string representation, and
color representation for plotting.

Typical usage example:

  >>> from surfq.pauli import Pauli
  >>>
  >>> p1 = Pauli.X
  >>> p2 = Pauli.Y
  >>> p3 = p1 * p2
  >>> print(p3)
  Z
"""

from enum import Enum
from functools import cached_property
from typing import override


class Pauli(Enum):
    """A class representing a single-qubit Pauli operator.

    This enum represents the four Pauli operators: I, X, Y, and Z. These
    operators are fundamental to quantum computing and are used to describe the
    state of a qubit.

    Attributes:
        I: The identity operator.
        X: The Pauli-X operator.
        Y: The Pauli-Y operator.
        Z: The Pauli-Z operator.
    """

    I = 0
    Z = 1
    X = 2
    Y = 3

    def __mul__(self, other: "Pauli") -> "Pauli":
        """Define Pauli Mulitplication."""
        return Pauli(self.value ^ other.value)

    @override
    def __repr__(self) -> str:
        match self:
            case Pauli.I:
                return "I"
            case Pauli.Z:
                return "Z"
            case Pauli.X:
                return "X"
            case Pauli.Y:
                return "Y"

    @override
    def __str__(self) -> str:
        match self:
            case Pauli.I:
                return "I"
            case Pauli.Z:
                return "Z"
            case Pauli.X:
                return "X"
            case Pauli.Y:
                return "Y"

    @cached_property
    def color(self) -> str:
        """Define color per Pauli operator for plotting."""
        match self:
            case Pauli.I:
                return "#FFFFFF"  # white for identity
            case Pauli.Z:
                return "#D15567"  # muted purple, complements red/pink
            case Pauli.X:
                return "#E17C88"  # muted red, in tone with syndrome reds
            case Pauli.Y:
                return "#F28EBF"  # softer pink, between X and Z
