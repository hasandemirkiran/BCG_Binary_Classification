"""Modules to setup all data sources.

The ``DataSet`` class collects different data sources from the abstracted
``datasource``.

The idea is to have a common handling of the datasources
independent on where the data comes from (file, rds,...). The specific data
load is configured in ``datasource_*``.

Currently a
``datasource_file`` with the option to load csv files is implemented."""

from source.datasource.datasource import DataSource
from source.datasource.datasource_file import FileDataSource

__all__ = [
    "DataSource",
    "FileDataSource",
]
