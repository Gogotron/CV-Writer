import toml


def write_cv(data):
    return fr'''\documentclass[a4paper]{{article}}

\usepackage{{curriculum}}
{write_header(data['header'])}

\begin{{document}}
\maketitle
{write_sections(data['sections'])}

\end{{document}}'''


def write_header(content):
    return ''.join([
        (f'\n\\{command}{{{content[field]}}}' if field in content else '')
        for command, field in [
            ('name', 'name'),
            ('email', 'email'),
            ('phonenumber', 'phonenumber'),
            ('address', 'address'),
        ]
    ])


def write_sections(content):
    return '\n'.join(
        write_section(title, section)
        for title, section in content.items()
    )


def write_section(title, content):
    return f'\n\\section{{{title}}}'+''.join(map(write_item, content))


def write_item(content):
    return fr'''
\begin{{resumeitem}}
{{{content['title']}}}{{{content['time-frame']}}}
{content['description']}
\end{{resumeitem}}'''


def main():
    with open('data.toml', 'r') as file:
        data = toml.load(file)

    print(write_cv(data))


if __name__ == '__main__':
    main()
