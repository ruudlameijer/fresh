# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Generate some data
clowns = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4','Mercedes S500'],
        'Price': [22000,25000,27000,35000,79000]
        }

# Convert to dataframe
clown_data_df = pd.DataFrame(clowns, columns = ['Brand', 'Price'])

# Change that is not part of REL 1

# Write recipe outputs
clown_data = dataiku.Dataset("clown_data")
clown_data.write_with_schema(clown_data_df)
