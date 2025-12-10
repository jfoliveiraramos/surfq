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
"""Test Pauli Frame."""

from surfq.pauli import Pauli


def test_single_pauli_operations():
    """Test Single-Qubit Pauli operations."""
    assert Pauli.I * Pauli.I == Pauli.I
    assert Pauli.X * Pauli.I == Pauli.X
    assert Pauli.Z * Pauli.I == Pauli.Z
    assert Pauli.Y * Pauli.I == Pauli.Y
    assert Pauli.I * Pauli.X == Pauli.X
    assert Pauli.X * Pauli.X == Pauli.I
    assert Pauli.Z * Pauli.X == Pauli.Y
    assert Pauli.Y * Pauli.X == Pauli.Z
    assert Pauli.I * Pauli.Z == Pauli.Z
    assert Pauli.X * Pauli.Z == Pauli.Y
    assert Pauli.Z * Pauli.Z == Pauli.I
    assert Pauli.Y * Pauli.Z == Pauli.X
    assert Pauli.I * Pauli.Y == Pauli.Y
    assert Pauli.X * Pauli.Y == Pauli.Z
    assert Pauli.Z * Pauli.Y == Pauli.X
    assert Pauli.Y * Pauli.Y == Pauli.I
