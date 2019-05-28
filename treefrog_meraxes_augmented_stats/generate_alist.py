#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Generate a forest info file for Meraxes.
# Copyright © 2019 Simon Mutch
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import h5py as h5
import numpy as np
import click

def generate_alist(fname):
    """Generate the a_lists.txt file required for Meraxes.

    Parameters
    ----------
    fname : str
        The VELOCIraptor unified tree file with forest IDs.

    Notes
    -----
    This function is provided through a Click CLI interface.
    """

    with h5.File(fname, 'r') as fd:
        n_snaps = fd['Header'].attrs['NSnaps']

        alist = np.zeros(n_snaps)
        for snap in range(n_snaps):
            alist[snap] = fd[f'Snap_{snap:03d}'].attrs['scalefactor']

    with open("a_list.txt", "w") as fd:
        for v in alist:
            print(v, file=fd)

@click.command()
@click.argument("fname_in", type=click.Path(exists=True))
def cli(fname_in):
    generate_alist(fname_in)