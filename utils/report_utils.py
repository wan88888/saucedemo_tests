import os
import shutil

def cleanup_old_reports():
    """清理旧的测试报告和截图文件"""
    cleanup_dirs = [
        'reports/allure-results',
        'reports/screenshots', 
        'test-results',
        'playwright-report'
    ]
    
    for dir_path in cleanup_dirs:
        if os.path.exists(dir_path):
            try:
                shutil.rmtree(dir_path)
                print(f"已清理旧报告目录: {dir_path}")
            except Exception as e:
                print(f"清理目录 {dir_path} 时出错: {e}")
    
    # 重新创建必要的目录
    os.makedirs('reports/allure-results', exist_ok=True)
    os.makedirs('reports/screenshots', exist_ok=True)

def save_failure_screenshot(page, scenario_name):
    """保存失败测试的截图"""
    import time
    timestamp = str(int(time.time()))
    screenshot_path = f"reports/screenshots/failed_{scenario_name}_{timestamp}.png"
    try:
        page.screenshot(path=screenshot_path)
        print(f"已保存失败截图: {screenshot_path}")
    except Exception as e:
        print(f"保存截图失败: {e}")