{{ config(
    materialized='incremental',
    unique_key='club_id',
    file_format='parquet',
    incremental_strategy='delete+insert'
) }}

select *

from {{ ref('base_clubs') }}