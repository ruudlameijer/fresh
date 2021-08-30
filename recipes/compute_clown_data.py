# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu



# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

clown_data_df = ... # Compute a Pandas dataframe to write into clown_data


# Write recipe outputs
clown_data = dataiku.Dataset("clown_data")
clown_data.write_with_schema(clown_data_df)
