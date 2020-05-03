#!/usr/bin/env python

import argparse
from json import JSONDecoder

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.python import PythonLexer

from jenkins_flaky.serialization import from_json


def get_formatter():
    return HtmlFormatter()


def get_css():
    return get_formatter().get_style_defs()


def prettify_traceback(traceback):
    lexer = PythonLexer()
    formatter = get_formatter()
    return highlight(traceback, lexer, formatter)


def build_report(styles, tracebacks):
    report: str = f"""
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
       "http://www.w3.org/TR/html4/strict.dtd">
    <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
      <style type="text/css">
      {styles}
      </style>
    </head>
    <body>
    <div class="container">
    {tracebacks}
    </div>
    </body>
    </html>
    """
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Diff two files with flaky tests to get the new ones')
    parser.add_argument('db_file', type=argparse.FileType('r'))
    args = parser.parse_args()

    tracebacks: str = ''
    flaky_tests = JSONDecoder(object_hook=from_json).decode(args.db_file.read())
    for flaky_test in flaky_tests:
        for execution in flaky_test.executions:
            tracebacks += f'<code>{prettify_traceback(execution.traceback)}</code><hr/>\n'

    print(build_report(get_css(), tracebacks))
