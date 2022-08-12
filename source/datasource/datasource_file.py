import pandas as pd
from pathlib import Path
import source
from source.datasource import DataSource



class FileDataSource(DataSource):
    """
    FileDataSource is a data source loading local CSV files
    """

    def __init__(self, source_conf, **_):
        super().__init__(source_conf)
        # Set project root directory (OS-independent using pathlib)
        project_root = Path(source.__file__).parents[1]
        self._location = Path(project_root, source_conf.file.location)

        self._sheet = source_conf.file.sheet

    def load_csv(self) -> pd.DataFrame:
        """
        Loads the excel file according to the provided configuration

        :return: Dataframe from csv as configured in data source config
        :rtype: pd.DataFrame
        """
        # df_impact = pd.read_csv(f'../../data/{customer}/impact_values_pl.csv', sep=';')
        # df_features = pd.read_csv(f'../../data/{customer}/input.csv', sep=';')

        df = pd.read_excel(
            self._location,
            sheet_name=self._sheet,
        )

        return self._transform(df)