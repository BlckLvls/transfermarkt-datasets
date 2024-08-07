import os
import yaml

def create_directories():
    # Читаємо конфігурацію dbt
    with open('dbt_project.yml', 'r') as f:
        config = yaml.safe_load(f)

    # Отримуємо шлях для Parquet файлів
    parquet_path = config['vars']['parquet_output_path']

    # Створюємо директорії для dev і prod
    for env in ['dev', 'prod']:
        full_path = os.path.join(parquet_path, env)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created directory: {full_path}")

if __name__ == "__main__":
    create_directories()