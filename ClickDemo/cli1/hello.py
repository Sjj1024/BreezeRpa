import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
  """Simple program that greets NAME for a total of COUNT times."""
  for x in range(count):
    click.echo('Hello %s!' % name)


@click.command()
@click.option('--home', prompt='home type', help='The person to greet')
def gethome(home):
  click.echo(f'获取回家的路,可以获取到很多个哦:{home}')


if __name__ == '__main__':
  hello()
