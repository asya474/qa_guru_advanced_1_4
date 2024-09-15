import os
import shutil
import pytest
@pytest.fixture(scope='session', autouse=True)
def clean_allure_results():
    allure_dir = 'allure-results'
    if os.path.exists(allure_dir):
        shutil.rmtree(allure_dir)
        print(f"Директория '{allure_dir}' очищена.")
    os.makedirs(allure_dir, exist_ok=True)