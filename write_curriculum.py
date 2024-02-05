import toml


def write_cv(data):
    return r'''\documentclass{article}

\usepackage{curriculum}

\begin{document}'''+write_header(data['header'])+r'''
\maketitle

'''+write_sections(data['sections'])+r'''
\end{document}'''


def write_header(content):
    return r'''
\name{'''+content['name']+r'''}
\email{'''+content['email']+r'''}
\phonenumber{'''+content['phone-number']+r'''}
\address{'''+content['address']+'}'


def write_sections(content):
    return '\n'.join(write_section(title, section) for title, section in content.items())


def write_section(title, content):
    return r'''
\section{'''+title+'}'+''.join(map(write_item, content))


def write_item(content):
    return r'''
\begin{resumeitem}
{'''+content['title']+r'}{'+content['time-frame']+r'''}
'''+content['description']+r'''
\end{resumeitem}'''


def main():
    with open('data.toml', 'r') as file:
        data = toml.load(file)

    print(write_cv(data))


if __name__ == '__main__':
    main()
