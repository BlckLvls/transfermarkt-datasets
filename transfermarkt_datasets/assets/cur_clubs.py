from frictionless.field import Field
from frictionless.schema import Schema
from frictionless import checks

from datetime import datetime

import pandas as pd

from transfermarkt_datasets.core.asset import Asset
from transfermarkt_datasets.assets.base_games import BaseGamesAsset
from transfermarkt_datasets.assets.base_clubs import BaseClubsAsset

class CurClubsAsset(Asset):

  name = "cur_clubs"
  description = """
  The `clubs` asset contains one row per club in the dataset.
  All clubs are tied to one particular `competition`.
  """
  file_name = "clubs.csv"

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

    self.schema = Schema()

    self.schema.add_field(Field(name='club_id', type='integer'))
    self.schema.add_field(Field(name='name', type='string'))
    self.schema.add_field(Field(name='pretty_name', type='string'))
    self.schema.add_field(Field(name='domestic_competition_id', type='string'))
    self.schema.add_field(Field(
        name='total_market_value',
        type='number',
        description="Aggregated players' Transfermarkt market value in millions of pounds"
      )
    )
    self.schema.add_field(Field(name='squad_size', type='integer'))
    self.schema.add_field(Field(name='average_age', type='number'))
    self.schema.add_field(Field(name='foreigners_number', type='integer'))
    self.schema.add_field(Field(name='foreigners_percentage', type='number'))
    self.schema.add_field(Field(name='national_team_players', type='integer'))
    self.schema.add_field(Field(name='stadium_name', type='string'))
    self.schema.add_field(Field(name='stadium_seats', type='integer'))
    self.schema.add_field(Field(name='net_transfer_record', type='string'))
    self.schema.add_field(Field(name='coach_name', type='string'))
    self.schema.add_field(Field(
      name='url',
      type='string',
      format='uri'
      )
    )

    self.schema.primary_key = ['club_id']
    self.schema.foreign_keys = [
      {"fields": "domestic_competition_id", "reference": {"resource": "competitions", "fields": "competition_id"}}
    ]

    self.checks = [
      checks.table_dimensions(min_rows=400)
    ]

  def build(self, base_clubs: BaseClubsAsset):

    clubs = base_clubs.prep_df
    self.prep_df = clubs
