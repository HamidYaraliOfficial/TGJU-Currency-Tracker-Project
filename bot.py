import requests
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
import pyfiglet
import base64

console = Console()

class TGJUCurrencyTracker:
    def __init__(self):
        self.url = "https://www.tgju.org/"
        self.previous_prices = {}
        self.currency_names = {
            'price_dollar_rl': {'fa': 'دلار آمریکا', 'en': 'US Dollar', 'zh': '美元', 'ru': 'Доллар США'},
            'price_eur': {'fa': 'یورو', 'en': 'Euro', 'zh': '欧元', 'ru': 'Евро'},
            'price_gbp': {'fa': 'پوند انگلیس', 'en': 'British Pound', 'zh': '英镑', 'ru': 'Британский фунт'},
            'price_aed': {'fa': 'درهم امارات', 'en': 'UAE Dirham', 'zh': '阿联酋迪拉姆', 'ru': 'Дирхам ОАЭ'},
            'price_try': {'fa': 'لیر ترکیه', 'en': 'Turkish Lira', 'zh': '土耳其里拉', 'ru': 'Турецкая лира'},
            'price_cny': {'fa': 'یوان چین', 'en': 'Chinese Yuan', 'zh': '人民币', 'ru': 'Китайский юань'},
            'price_rub': {'fa': 'روبل روسیه', 'en': 'Russian Rubles', 'zh': '俄罗斯卢布', 'ru': 'Российский рубль'},
            'price_kwd': {'fa': 'دینار کویت', 'en': 'Kuwaiti Dinar', 'zh': '科威特第纳尔', 'ru': 'Кувейтский динар'},
            'price_cad': {'fa': 'دلار کانادا', 'en': 'Canadian Dollar', 'zh': '加拿大元', 'ru': 'Канадский доллар'},
            'price_usdt': {'fa': 'تتر', 'en': 'Tether', 'zh': '泰达币', 'ru': 'Тетер'},
            'price_sekeb': {'fa': 'سکه بهار آزادی', 'en': 'Bahare Azadi Coin', 'zh': '巴哈雷自由币', 'ru': 'Монета Бахар Азади'},
            'price_nim': {'fa': 'نیم سکه', 'en': 'Half Coin', 'zh': '半枚硬币', 'ru': 'Половина монеты'},
            'price_rob': {'fa': 'ربع سکه', 'en': 'Quarter Coin', 'zh': '四分之一硬币', 'ru': 'Четверть монеты'},
            'price_geram18': {'fa': 'طلای 18 عیار', 'en': '18K Gold', 'zh': '18K金', 'ru': 'Золото 18 карат'},
            'price_geram24': {'fa': 'طلای 24 عیار (مثقال)', 'en': '24K Gold (Mesghal)', 'zh': '24K金（每盎司）', 'ru': 'Золото 24 карата (Мескаль)'},
            'price_ounce': {'fa': 'انس طلا', 'en': 'Gold Ounce', 'zh': '金盎司', 'ru': 'Унция золота'},
            'price_mesghal': {'fa': 'مثقال طلا', 'en': 'Mesghal Gold', 'zh': '金盎司（伊朗计量）', 'ru': 'Мескаль золота'}
        }
        self.load_previous_prices()

    def load_previous_prices(self):
        try:
            with open('tgju_prices.json', 'r', encoding='utf-8') as f:
                self.previous_prices = json.load(f)
        except FileNotFoundError:
            self.previous_prices = {}

    def save_current_prices(self, prices):
        with open('tgju_prices.json', 'w', encoding='utf-8') as f:
            json.dump(prices, f, ensure_ascii=False, indent=4)

    def get_currency_prices(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(self.url, headers=headers, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            prices = {}

            script_tags = soup.find_all('script')
            for script in script_tags:
                if script.string and 'window.__INITIAL_STATE__' in script.string:
                    data_str = script.string.split('window.__INITIAL_STATE__ = ')[1].split(';')[0]
                    data = json.loads(data_str)

                    if 'market' in data and 'main' in data['market']:
                        for key, value in data['market']['main'].items():
                            if key in self.currency_names:
                                price = value.get('p', 0)
                                if price:
                                    prices[key] = {
                                        'fa': {'name': self.currency_names[key]['fa'], 'price': float(price)},
                                        'en': {'name': self.currency_names[key]['en'], 'price': float(price)},
                                        'zh': {'name': self.currency_names[key]['zh'], 'price': float(price)},
                                        'ru': {'name': self.currency_names[key]['ru'], 'price': float(price)}
                                    }

            prices['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return prices

        except Exception as e:
            console.print(f"[red]❌ خطا در دریافت داده ها: {e}[/red]")
            console.print(f"[red]❌ Error retrieving data: {e}[/red]")
            console.print(f"[red]❌ 获取数据时出错: {e}[/red]")
            console.print(f"[red]❌ Ошибка при получении данных: {e}[/red]")
            return {}

    def check_changes(self, current_prices):
        changes = []
        for key, lang_data in current_prices.items():
            if key == 'last_update':
                continue
            for lang in ['fa', 'en', 'zh', 'ru']:
                name = lang_data[lang]['name']
                current_price = lang_data[lang]['price']
                prev_key = f"{key}_{lang}"
                if prev_key in self.previous_prices:
                    previous_price = self.previous_prices[prev_key]['price']
                    if current_price != previous_price:
                        if current_price > previous_price:
                            change_type = {
                                'fa': "📈 افزایش",
                                'en': "📈 Increase",
                                'zh': "📈 增加",
                                'ru': "📈 Увеличение"
                            }[lang]
                            emoji = "🟢"
                        else:
                            change_type = {
                                'fa': "📉 کاهش",
                                'en': "📉 Decrease",
                                'zh': "📉 减少",
                                'ru': "📉 Уменьшение"
                            }[lang]
                            emoji = "🔴"
                        change_percent = ((current_price - previous_price) / previous_price) * 100
                        changes.append({
                            'lang': lang,
                            'name': name,
                            'current': current_price,
                            'previous': previous_price,
                            'type': change_type,
                            'percent': round(change_percent, 2),
                            'emoji': emoji
                        })
                else:
                    changes.append({
                        'lang': lang,
                        'name': name,
                        'current': current_price,
                        'previous': 0,
                        'type': {
                            'fa': "🆕 اولین ثبت",
                            'en': "🆕 First Record",
                            'zh': "🆕 首次记录",
                            'ru': "🆕 Первая запись"
                        }[lang],
                        'percent': 0,
                        'emoji': "🔵"
                    })
        return changes

    def format_price(self, price):
        return f"{price:,.0f}".replace(',', ',')

    def display_banner(self):
        ascii_banner = pyfiglet.figlet_format("TGJU Tracker", font="slant")
        console.print(ascii_banner, style="bold cyan")

        dev_info = "@Hamid_Yarali"
        developed_by = "Hamid Yarali"
        github = "https://github.com/HamidYaraliOfficial"
        instagram = "https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ=="
        channel_info = "CodeClubiR"

        console.print(Panel.fit(
            f"""[bold yellow]توسعه‌دهنده: {dev_info}
توسعه‌یافته توسط: {developed_by}
گیت‌هاب: {github}
اینستاگرام: {instagram}
کانال: {channel_info}
Developer: {dev_info}
Developed by: {developed_by}
GitHub: {github}
Instagram: {instagram}
开发者: {dev_info}
由开发: {developed_by}
GitHub: {github}
Instagram: {instagram}
Разработчик: {dev_info}
Разработано: {developed_by}
GitHub: {github}
Instagram: {instagram}""",
            title="🔥 اطلاعات ربات / Bot Info / 机器人信息 / Информация о боте 🔥",
            border_style="bright_magenta",
            padding=(1, 4)
        ))

    def run(self, check_interval=10):
        self.display_banner()
        console.print("[green]✅ ربات ردیابی قیمت ارزها و طلا شروع به کار کرد...[/green]")
        console.print("[green]✅ Currency and Gold Price Tracker Bot Started...[/green]")
        console.print("[green]✅ 货币和黄金价格追踪机器人已启动...[/green]")
        console.print("[green]✅ Бот для отслеживания цен на валюту и золото запущен...[/green]")
        console.print("[cyan]در حال رصد تغییرات قیمت...[/cyan]")
        console.print("[cyan]Monitoring price changes...[/cyan]")
        console.print("[cyan]监控价格变化...[/cyan]")
        console.print("[cyan]Отслеживание изменений цен...[/cyan]\n")

        current_prices = self.get_currency_prices()
        if current_prices:
            console.print("[bold]📊 قیمت‌های اولیه / Initial Prices / 初始价格 / Начальные цены:[/bold]")
            for key, lang_data in current_prices.items():
                if key != 'last_update':
                    console.print(f"   {lang_data['fa']['name']}: {self.format_price(lang_data['fa']['price'])} تومان")
                    console.print(f"   {lang_data['en']['name']}: {self.format_price(lang_data['en']['price'])} IRR")
                    console.print(f"   {lang_data['zh']['name']}: {self.format_price(lang_data['zh']['price'])} 伊朗里亚尔")
                    console.print(f"   {lang_data['ru']['name']}: {self.format_price(lang_data['ru']['price'])} Иранский риал")

            self.previous_prices = {f"{key}_{lang}": lang_data[lang] for key, lang_data in current_prices.items() if key != 'last_update' for lang in ['fa', 'en', 'zh', 'ru']}
            self.save_current_prices(self.previous_prices)
            console.print("\n💾 قیمت‌ها ذخیره شدند. منتظر تغییرات باشید...\n")
            console.print("\n💾 Prices saved. Waiting for changes...\n")
            console.print("\n💾 价格已保存。等待变化...\n")
            console.print("\n💾 Цены сохранены. Ожидание изменений...\n")
        else:
            console.print("[red]❌ خطا در دریافت قیمت‌ها. لطفا اتصال اینترنت را بررسی کنید.[/red]")
            console.print("[red]❌ Error retrieving prices. Please check your internet connection.[/red]")
            console.print("[red]❌ 获取价格时出错。请检查您的网络连接。[/red]")
            console.print("[red]❌ Ошибка при получении цен. Проверьте подключение к интернету.[/red]")
            return

        while True:
            current_prices = self.get_currency_prices()
            if current_prices:
                changes = self.check_changes(current_prices)
                if changes:
                    console.rule(f"[bold red]📌 تغییرات شناسایی شده در {current_prices['last_update']} / Changes Detected at {current_prices['last_update']} / 在 {current_prices['last_update']} 检测到变化 / Изменения обнаружены в {current_prices['last_update']}[/bold red]")
                    for change in changes:
                        console.print(f"{change['emoji']} [bold]{change['name']}[/bold]")
                        console.print(f"   {change['type']}")
                        if change['previous'] > 0:
                            console.print(f"   درصد تغییر / Change Percent / 变化百分比 / Процент изменения: {change['percent']}%")
                            console.print(f"   قیمت قبلی / Previous Price / 前一个价格 / Предыдущая цена: {self.format_price(change['previous'])} {'تومان' if change['lang'] == 'fa' else 'IRR' if change['lang'] == 'en' else '伊朗里亚尔' if change['lang'] == 'zh' else 'Иранский риал'}")
                            console.print(f"   قیمت فعلی / Current Price / 当前价格 / Текущая цена: {self.format_price(change['current'])} {'تومان' if change['lang'] == 'fa' else 'IRR' if change['lang'] == 'en' else '伊朗里亚尔' if change['lang'] == 'zh' else 'Иранский риал'}")
                            console.print(f"   تفاوت / Difference / 差额 / Разница: {self.format_price(abs(change['current'] - change['previous']))} {'تومان' if change['lang'] == 'fa' else 'IRR' if change['lang'] == 'en' else '伊朗里亚尔' if change['lang'] == 'zh' else 'Иранский риал'}")
                        else:
                            console.print(f"   قیمت فعلی / Current Price / 当前价格 / Текущая цена: {self.format_price(change['current'])} {'تومان' if change['lang'] == 'fa' else 'IRR' if change['lang'] == 'en' else '伊朗里亚尔' if change['lang'] == 'zh' else 'Иранский риал'}")
                        console.print("-" * 40)
                    console.print("\n")
                else:
                    console.print(f"[blue]ℹ️ هیچ تغییری در قیمت‌ها شناسایی نشد ({current_prices['last_update']})[/blue]")
                    console.print(f"[blue]ℹ️ No changes detected in prices ({current_prices['last_update']})[/blue]")
                    console.print(f"[blue]ℹ️ 未检测到价格变化 ({current_prices['last_update']})[/blue]")
                    console.print(f"[blue]ℹ️ Изменения цен не обнаружены ({current_prices['last_update']})[/blue]")

                self.previous_prices = {f"{key}_{lang}": lang_data[lang] for key, lang_data in current_prices.items() if key != 'last_update' for lang in ['fa', 'en', 'zh', 'ru']}
                self.save_current_prices(self.previous_prices)
            else:
                console.print("[red]❌ خطا در دریافت قیمت‌ها. تلاش مجدد در 30 ثانیه...[/red]")
                console.print("[red]❌ Error retrieving prices. Retrying in 30 seconds...[/red]")
                console.print("[red]❌ 获取价格时出错。30秒后重试...[/red]")
                console.print("[red]❌ Ошибка при получении цен. Повторная попытка через 30 секунд...[/red]")
                time.sleep(30)
                continue

            for i in range(check_interval, 0, -1):
                print(f"\r⏳ بررسی بعدی در {i} ثانیه... / Next check in {i} seconds... / 下次检查在{i}秒后... / Следующая проверка через {i} секунд...", end="")
                time.sleep(1)
            print("\n")


if __name__ == "__main__":
    tracker = TGJUCurrencyTracker()
    CHECK_INTERVAL = 300
    try:
        tracker.run(CHECK_INTERVAL)
    except KeyboardInterrupt:
        console.print("\n[red]⛔ ربات متوقف شد[/red]")
        console.print("\n[red]⛔ Bot stopped[/red]")
        console.print("\n[red]⛔ 机器人已停止[/red]")
        console.print("\n[red]⛔ Бот остановлен[/red]")