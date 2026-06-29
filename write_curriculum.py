import toml


def write_cv(data):
    return fr'''\documentclass[a4paper]{{article}}

\usepackage{{curriculum}}
\usepackage{{multicol}}
{write_header(data['header'])}

\begin{{document}}
{indent(write_content(data))}
\end{{document}}'''


def write_header(content):
    return ''.join([
        (f'\n\\{command}{{{content[field]}}}' if field in content else '')
        for command, field in [
            ('name', 'name'),
            ('email', 'email'),
            ('phonenumber', 'phonenumber'),
            ('address', 'address'),
            ('nationality', 'nationality'),
            ('worktitle', 'worktitle'),
            ('website', 'website'),
        ]
    ])


def write_content(data):
    return f'\\maketitle\n{write_sections(data['sections'])}'


def write_sections(content):
    return '\n'.join(
        write_section(title, section)
        for title, section in content.items()
    )


def write_section(title, content):
    column_count = max(
        (
            item['column']
            for item in content
            if 'column' in item
        ),
        default=0
    ) + 1

    if column_count == 1:
        section_content = '\n'.join(map(write_item, content))
    else:
        columns_content = '\n\n\\columnbreak\n'.join(
            '\n'.join(
                write_item(item)
                for item in content
                if item.get('column', 0) == column_idx
            )
            for column_idx in range(column_count)
        )
        section_content = fr'''
\vspace{{-1em}}
\begin{{multicols}}{{2}}{indent(columns_content)}
\end{{multicols}}'''

    return f'\n\\section{{{title}}}' + indent(section_content)


def write_item(content):
    if 'raw' in content:
        return f'\n{content['raw']}'

    return fr'''
\begin{{resumeitem}}
{indent(write_item_inner(content))}
\end{{resumeitem}}'''


def write_item_inner(content):
    return f'{{{content['title']}}}{{{content['time-frame']}}}\n{content['description']}'


def indent(text):
    return '\n'.join(f'  {line}' if line else line for line in text.split('\n'))


def main():
    with open('data.toml', 'r') as file:
        data = toml.load(file)

    print(write_cv(data))


if __name__ == '__main__':
    main()
