{% macro export_to_parquet(model) %}
  {% set schema = model.schema %}
  {% set identifier = model.identifier %}
  {% set output_path = var('parquet_output_path') ~ '/' ~ schema ~ '/' ~ identifier ~ '.parquet' %}

  {% set export_query %}
    COPY (SELECT * FROM {{ model }}) TO '{{ output_path }}' (FORMAT PARQUET, CODEC 'SNAPPY')
  {% endset %}

  {% do run_query(export_query) %}
  {{ log("Exported " ~ identifier ~ " to " ~ output_path, info=True) }}
{% endmacro %}