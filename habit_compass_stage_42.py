# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: HabitCompass
import sys
from enum import Enum, auto


class Color(Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


class ColorfulPrinter:
    def __init__(self, enabled=True):
        self._enabled = enabled

    @property
    def enabled(self):
        return self._enabled

    def enable(self):
        if not sys.stdout.isatty():
            return
        self._enabled = True

    def disable(self):
        if not sys.stdout.isatty():
            return
        self._enabled = False

    @property
    def is_terminal(self):
        return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

    def _colorize(self, color: Color, text: str) -> str:
        if not self._enabled or not self.is_terminal:
            return text
        return f'{color.value}{text}{Color.RESET}'

    def red(self, text): return self._colorize(Color.RED, text)
    def green(self, text): return self._colorize(Color.GREEN, text)
    def yellow(self, text): return self._colorize(Color.YELLOW, text)
    def blue(self, text): return self._colorize(Color.BLUE, text)
    def magenta(self, text): return self._colorize(Color.MAGENTA, text)
    def cyan(self, text): return self._colorize(Color.CYAN, text)
    def bold(self, text): return self._colorize(Color.BOLD, text)

    def print_row(self, label: str, value: str = '', color: Color = None, sep=' | '):
        if not self._enabled or not self.is_terminal:
            print(f'{label} {sep}{value}' if value else label)
            return
        c = color.value if color and color != Color.RESET else ''
        print(f'{c}{label}{Color.RESET}{c}{value}{Color.RESET}')

    def print_header(self, title):
        print(self.bold(title))


# --- Пример использования в коде ---
def demo_printer():
    p = ColorfulPrinter()
    if not p.is_terminal:
        print("ANSI-вывод отключен (не терминал)")
        return

    p.print_header('HabitCompass — пример отчёта')
    p.green('  ✅ Серия за неделю: 5/7 дней')
    p.yellow('  ⚠️  Пропущено: Пн, Ср, Пт')
    p.red('  💀 Награда потеряна: -10 баллов')


if __name__ == '__main__':
    demo_printer()
