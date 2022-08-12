"""
Defines abstraction for different datasources (e.g.: files, RDS,...). Currently
csv files are implemented.
"""

from abc import ABCMeta, abstractmethod
import pandas as pd


class DataSource(metaclass=ABCMeta):
    """
    DataSource is the abstract class every data source should implement
    """

    def __init__(self, source_config):
        self.source_config = source_config

    @abstractmethod
    def load(self) -> pd.DataFrame:
        """
        This common method is be overridden by the final implementation
        classes.

        load() can then mean from csv, rds, xlsx,...
        """
        pass

    def _convert_time_cols(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        This method converts timezones depending on the source configuration

        :param df: Dataframe to convert. Specify columns in data source
                   configuration
        :type df: pd.DataFrame
        :return: Dataframe with converted columns
        :rtype: pd.DataFrame
        """

        config = self.source_config
        for col in config.date_cols:
            if "read_timezone" in vars(config):
                if "datetime_format" in vars(config):
                    df.loc[:, col] = pd.to_datetime(
                        df[col], format=config.datetime_format
                    )
                df.loc[:, col] = df[col].dt.tz_localize(
                    config.read_timezone, ambiguous=True
                )
                if "target_timezone" in vars(config):
                    df.loc[:, col] = df[col].dt.tz_convert(
                        config.target_timezone
                    )
            else:
                df.loc[:, col] = pd.to_datetime(
                    df[col], format=config.datetime_format
                )

        return df

    def _convert_dtypes(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        This method converts data types depending on the source configuration

        :param df: Dataframe to convert. Specify columns in data source
                   configuration
        :type df: pd.DataFrame
        :return: Dataframe with converted data types
        :rtype: pd.DataFrame
        """

        config = self.source_config
        for col in config.dtypes.__dict__:
            df.loc[:, col] = df[col].astype(config.dtypes.__dict__[col])

        return df

    def _transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        This method does general transformations based on the source
        configuration

        use_cols: use only specific columns
        drop_nans: drop nan values
        dtypes: fix data types
        date_cols: convert date/time columns
        drop_cols: drop columns entirely

        :param df: Dataframe to tranform
        :type df: pd.DataFrame
        :return: transformed dataframe
        :rtype: pd.DataFrame
        """

        # we lower every column header
        df.columns = map(str.lower, df.columns)

        source_config = self.source_config

        if "use_cols" in vars(source_config):
            df = df.loc[:, source_config.use_cols]

        if hasattr(source_config, "index_col"):
            df.set_index(source_config.index_col, inplace=True)

        if "drop_nans" in vars(source_config):
            for col in source_config.drop_nans:
                df = df[~df[col].isna()]

        if "dtypes" in vars(source_config):
            df = self._convert_dtypes(df)

        if "date_cols" in vars(source_config):
            df = self._convert_time_cols(df)

        if "drop_cols" in vars(source_config):
            try:
                df = df.drop(columns=source_config.drop_cols)
            except KeyError as e:
                print(
                    "WARN Non-existent columns "
                    "specified to be dropped: {}".format(e)
                )

        return df


class DummyDataSource(DataSource):
    """
    DummyDataSource is a test datasource that returns static results
    """

    def load(self) -> pd.DataFrame:
        return pd.DataFrame()
