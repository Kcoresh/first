# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: HabitCompass
def print_table(data, headers):
    if not data: return
    col_widths = [max(len(str(h)), max((len(str(row[i])) for row in data), default=0)) + 2 
                   for i, h in enumerate(headers)]
    sep = '+' + '+'.join('-' * w for w in col_widths) + '+'
    header_line = '|' + '|'.join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)) + '|'
    rows = [header_line]
    for row in data:
        rows.append('|' + '|'.join(str(row.get(i, '') or '').ljust(col_widths[i]) 
                                   for i in range(len(headers))) + '|')
    footer = '+' + '+'.join('-' * w for w in col_widths) + '+'
    print(sep)
    print(header_line)
    for r in rows[1:]: print(r)
    print(footer)

print_table([{'name': 'Привычка', 'count': 5, 'streak': 3}, {'name': 'Спорт', 'count': 8, 'streak': 7}], 
            ['name', 'count', 'streak'])
