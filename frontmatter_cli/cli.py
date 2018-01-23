# -*- coding: utf-8 -*-

import click
import frontmatter

from click_default_group import DefaultGroup

__author__ = 'Jeff Triplett'
__email__ = 'jeff.triplett@gmail.com'
__version__ = '0.1.0'


def validate_extra_context(ctx, param, value):
    """Validate extra context."""

    for key in value:
        if '=' not in key:
            raise click.BadParameter(
                'EXTRA_CONTEXT should contain items of the form key=value; '
                "'{}' doesn't match that form".format(key)
            )

    return dict(key.lstrip('-').split('=', 1) for key in value) or None


@click.group(cls=DefaultGroup, default='main', default_if_no_args=True)
@click.pass_context
def cli(context):
    pass


@cli.command(context_settings=dict(ignore_unknown_options=True,))
@click.version_option(prog_name='frontmatter-cli', version=__version__)
@click.argument('extra_context', nargs=-1, callback=validate_extra_context)
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def main(input, output, extra_context):
    chunk = input.read()
    post = frontmatter.loads(chunk)
    post.metadata.update(dict(extra_context))
    frontmatter.dump(post, output)


if __name__ == '__main__':
    cli()
