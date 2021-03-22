#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

## Overview

This module regroups utility functions used in thehive4py.

"""

def flatten_dict(dictionary, sep='.'):
    """
    Flattens a dictionary. Example:
    {"customFields": {"field1": {"string": "value1"}}} becomes {"customFields.field1.string": "value1"}
    
    Arguments:
        dictionary (dict): Dictionary to flatten
        sep (str): The separator we want to use between fields. Default is "."

    Returns:
        dict: Flattened dictionary
    """
    out = {}
    for key, val in dictionary.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten_dict(subdict, sep).items()
                out.update({key + sep + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out