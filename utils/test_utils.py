import os
import shutil
import glob
from utils.constants import REPORTS_DIR, SCREENSHOTS_DIR, ALLURE_RESULTS_DIR

def cleanup_old_reports():
    """Clean up old test reports and screenshots before running new tests."""
    
    # Clean up XML test reports
    xml_files = glob.glob(os.path.join(REPORTS_DIR, "*.xml"))
    for xml_file in xml_files:
        try:
            os.remove(xml_file)
            print(f"Removed old report: {xml_file}")
        except OSError as e:
            print(f"Warning: Could not remove {xml_file}: {e}")
    
    # Clean up allure results
    if os.path.exists(ALLURE_RESULTS_DIR):
        try:
            shutil.rmtree(ALLURE_RESULTS_DIR)
            print(f"Removed old allure results: {ALLURE_RESULTS_DIR}")
        except OSError as e:
            print(f"Warning: Could not remove {ALLURE_RESULTS_DIR}: {e}")
    
    # Clean up screenshots
    if os.path.exists(SCREENSHOTS_DIR):
        try:
            shutil.rmtree(SCREENSHOTS_DIR)
            print(f"Removed old screenshots: {SCREENSHOTS_DIR}")
        except OSError as e:
            print(f"Warning: Could not remove {SCREENSHOTS_DIR}: {e}")
    
    # Recreate directories
    _create_directories()

def _create_directories():
    """Create necessary directories for reports and screenshots."""
    directories = [ALLURE_RESULTS_DIR, SCREENSHOTS_DIR]
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError as e:
            print(f"Warning: Could not create directory {directory}: {e}")