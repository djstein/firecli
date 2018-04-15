import click


@click.group()
def cli():
    """firecli
    Set of command line tools for FIRE calculations.
    """
    # if sys.version_info[0] == 2:
    #     print("Current environment is Python 2.")
    #     print("Please use a Python 3.6 virtualenv.")
    #     raise SystemExit


@cli.command('configure')
def configure(user, cli):
    print('configuring')


def main():
    cli()


if __name__ == '__main__':
    main()
