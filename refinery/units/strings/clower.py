#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from refinery.units import Unit


class clower(Unit):
    """
    Transforms the input data to lowercase.
    """
    def process(self, data):
        return data.lower()
