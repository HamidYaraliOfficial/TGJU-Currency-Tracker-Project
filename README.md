# پروژه ردیاب قیمت ارز و طلا (TGJU Currency Tracker)

## توضیحات پروژه (فارسی)
این پروژه یک اسکریپت پایتون است که برای ردیابی قیمت ارزها و طلا از وب‌سایت `tgju.org` طراحی شده است. این اسکریپت با استفاده از کتابخانه‌های `requests` و `BeautifulSoup` داده‌های قیمت را استخراج کرده و تغییرات قیمت را در مقایسه با داده‌های قبلی نمایش می‌دهد. خروجی‌ها با استفاده از کتابخانه `rich` به‌صورت زیبا و خوانا ارائه می‌شوند و از زبان‌های فارسی، انگلیسی، چینی و روسی پشتیبانی می‌کند. این پروژه توسط حمید یارعلی توسعه یافته است.

### ویژگی‌ها
- استخراج داده‌های قیمت ارز و طلا از وب‌سایت `tgju.org`
- نمایش تغییرات قیمت با درصد و تفاوت قیمت
- پشتیبانی از خروجی چندزبانه (فارسی، انگلیسی، چینی، روسی)
- ذخیره‌سازی قیمت‌ها در فایل JSON برای مقایسه‌های بعدی
- رابط کاربری زیبا با استفاده از کتابخانه `rich` و `pyfiglet`
- بررسی دوره‌ای قیمت‌ها با فواصل زمانی قابل تنظیم

### پیش‌نیازها
- پایتون نسخه 3.8 یا بالاتر
- کتابخانه‌های مورد نیاز:
  - `requests`
  - `beautifulsoup4`
  - `rich`
  - `pyfiglet`
- دسترسی به اینترنت برای اتصال به وب‌سایت `tgju.org`

### نصب
1. مخزن پروژه را دانلود کنید.
2. کتابخانه‌های مورد نیاز را با استفاده از دستور زیر نصب کنید:
   ```
   pip install requests beautifulsoup4 rich pyfiglet
   ```
3. فایل `tgju_tracker.py` را اجرا کنید:
   ```
   python tgju_tracker.py
   ```

### نحوه استفاده
1. اسکریپت را اجرا کنید تا ردیابی قیمت‌ها آغاز شود.
2. قیمت‌های اولیه نمایش داده می‌شوند و سپس اسکریپت به‌صورت دوره‌ای (هر 300 ثانیه به‌صورت پیش‌فرض) تغییرات قیمت را بررسی می‌کند.
3. تغییرات قیمت با جزئیات (درصد تغییر، قیمت قبلی و فعلی) به‌صورت چندزبانه نمایش داده می‌شود.
4. برای توقف اسکریپت، از `Ctrl+C` استفاده کنید.

### توسعه‌دهنده
- توسعه‌یافته توسط: حمید یارعلی
- گیت‌هاب: [https://github.com/HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)
- اینستاگرام: [https://www.instagram.com/hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)

---

# TGJU Currency Tracker Project

## Project Description (English)
This project is a Python script designed to track currency and gold prices from the `tgju.org` website. It uses the `requests` and `BeautifulSoup` libraries to scrape price data and displays price changes compared to previous data. The output is presented in a visually appealing format using the `rich` library and supports Persian, English, Chinese, and Russian languages. This project was developed by Hamid Yarali.

### Features
- Scrapes currency and gold price data from `tgju.org`
- Displays price changes with percentage and difference
- Supports multilingual output (Persian, English, Chinese, Russian)
- Saves prices to a JSON file for future comparisons
- Beautiful user interface using `rich` and `pyfiglet` libraries
- Periodic price checks with configurable intervals

### Requirements
- Python version 3.8 or higher
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `rich`
  - `pyfiglet`
- Internet access to connect to `tgju.org`

### Installation
1. Download the project repository.
2. Install the required libraries using the following command:
   ```
   pip install requests beautifulsoup4 rich pyfiglet
   ```
3. Run the `tgju_tracker.py` file:
   ```
   python tgju_tracker.py
   ```

### Usage
1. Run the script to start tracking prices.
2. Initial prices are displayed, and the script periodically checks for price changes (every 300 seconds by default).
3. Price changes are displayed with details (percentage change, previous and current prices) in multiple languages.
4. Stop the script using `Ctrl+C`.

### Developer
- Developed by: Hamid Yarali
- GitHub: [https://github.com/HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)
- Instagram: [https://www.instagram.com/hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)

---

# 货币和黄金价格追踪项目

## 项目描述 (中文)
该项目是一个Python脚本，旨在从`tgju.org`网站跟踪货币和黄金价格。它使用`requests`和`BeautifulSoup`库提取价格数据，并与之前的数据比较以显示价格变化。输出通过`rich`库以美观的方式呈现，支持波斯语、英语、中文和俄语。该项目由Hamid Yarali开发。

### 功能
- 从`tgju.org`提取货币和黄金价格数据
- 显示价格变化，包括百分比和差额
- 支持多语言输出（波斯语、英语、中文、俄语）
- 将价格保存到JSON文件以便于后续比较
- 使用`rich`和`pyfiglet`库提供美观的界面
- 可配置间隔的定期价格检查

### 要求
- Python版本3.8或更高
- 所需库：
  - `requests`
  - `beautifulsoup4`
  - `rich`
  - `pyfiglet`
- 连接到`tgju.org`的互联网访问权限

### 安装
1. 下载项目仓库。
2. 使用以下命令安装所需库：
   ```
   pip install requests beautifulsoup4 rich pyfiglet
   ```
3. 运行`tgju_tracker.py`文件：
   ```
   python tgju_tracker.py
   ```

### 使用方法
1. 运行脚本以开始跟踪价格。
2. 显示初始价格，脚本将定期检查价格变化（默认每300秒）。
3. 价格变化将显示详细信息（变化百分比、之前和当前价格），支持多语言。
4. 使用`Ctrl+C`停止脚本。

### 开发者
- 开发人员：Hamid Yarali
- GitHub: [https://github.com/HamidYaraliOfficial](https://github.com/HamidYaraliOfficial)
- Instagram: [https://www.instagram.com/hamidyaraliofficial](https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==)