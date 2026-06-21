import os
import time
from datetime import datetime
from PIL import ImageGrab


def start_screenshot_session(output_dir: str, interval_seconds: int, duration_minutes: int):
    # 确保目标文件夹存在
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n[配置] 截屏保存目录: {os.path.abspath(output_dir)}")
    print(f"[配置] 截屏时间间隔: {interval_seconds} 秒")
    print(f"[配置] 预设终止时间: {duration_minutes} 分钟")
    print("[提示] 程序运行中... 按 Ctrl+C 可提前安全终止。")

    counter = 1
    start_time = time.time()  # 记录启动绝对时间
    max_duration_seconds = duration_minutes * 60  # 转换为秒

    try:
        while True:
            # 检查是否达到了设定的终止时间
            elapsed_time = time.time() - start_time
            if elapsed_time >= max_duration_seconds:
                print(f"\n[结束] 已达到预设运行时间 ({duration_minutes} 分钟)，程序自动安全退出。")
                break

            # 1. 获取当前时间并格式化
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"{counter:03d}-{timestamp}.png"
            filepath = os.path.join(output_dir, filename)

            # 2. 捕获主屏幕并保存
            screenshot = ImageGrab.grab()
            screenshot.save(filepath)

            print(f"[已保存] {filename}")

            # 3. 状态步进
            counter += 1
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\n[结束] 收到手动终止信号，定时截屏已安全停止。")


if __name__ == "__main__":
    SAVE_FOLDER = "D:/Screenshots"  # 目标文件夹

    print("====================================")
    print("            定时截屏工具             ")
    print("====================================")

    # 动态获取用户输入，若直接回车则激活默认值
    try:
        input_interval = input("请输入截屏间隔 (秒) [直接回车默认为 300]: ").strip()
        interval = int(input_interval) if input_interval else 300

        input_duration = input("请输入多长时间后终止 (分钟) [直接回车默认为 60]: ").strip()
        duration = int(input_duration) if input_duration else 60
    except ValueError:
        print("\n[警告] 输入格式非整数数字，将自动启用安全默认值 (300秒/60分钟)")
        interval = 300
        duration = 60

    start_screenshot_session(SAVE_FOLDER, interval, duration)