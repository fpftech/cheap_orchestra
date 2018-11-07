# -*- coding: utf-8 -*-

"""Console script for cheap_orchestra."""
from cheap_orchestra import Configuration
import click
import sys


@click.group()
def main():
    """
    Cheap Orchestra is a CLI that's meant to remotely deploy multiple versions
    of your docker-compose based app on a single host coordinating them to make
    sure they all play in harmony.

    Imagine you have to deploy multiple versions of your app for testing (this
    is just an example, it really could be anything else). Each version must
    work independently and must not get in the way of the others. Like an
    orchestra, all the versions have their own space and should work in a way
    that brings harmony for your objective.

    You are the Maestro for this Orchestra! Take a look at your tools:

    Setup: This command configures the connection information for your remote
    host so you can stay DRY about this info. You can also configure a Discord
    webhook to be notified about the deploys.

    Ingress: This command is all about setting up the ingress controller with a
    dead simple service discovery technique so it's a no-brainer for you to
    deploy multiple versions of your service.

    Service: This command is actually used to deploy multiple versions of your
    service.

    For specific information about each command:

    $ cheap_orchestra COMMAND --help
    """
    pass


@main.command()
@click.option('--remote_user', required=True, help="user that connect's to the remote machine")
@click.option('--remote_server', required=True, help="remote machine ip address")
@click.option('--private_key', required=True, help="private key for ssh connection")
@click.option('--webhook_name', help="bot name configured in discord for notification")
@click.option('--webhook_url', help="unique discord's url for notification")
def setup(remote_user, remote_server, private_key, webhook_name, webhook_url):
    """
    Setup the necessary connection information.

    The setup command will create a configuration file called .cheap_orchestra
    on the current folder. This file will be used by other commands to establish
    a remote connection to the host server and optionally to a Discord Webhook
    so your team is informed about what's going on.

    The remote connection will use the SSH protocol with private key validation.
    If you want other options for this connection, please get in touch.
    """
    click.echo('*--------cheap_orchestra--------*')
    click.echo('cheap_orchestra: Welcome to show time! '
               'Sit tight while the orchestra is tuning the instruments...')
    config = Configuration()
    config.persist_connection_setup(remote_user, remote_server, private_key)
    if all((webhook_name, webhook_url)):
        config.persist_webhook_setup(webhook_name, webhook_url)
    click.echo('cheap_orchestra: Configuration complete!')
    return 0


@main.command()
def ingress():
    """Configure the ingress controller."""
    click.echo('this command will setup the ingress service')
    return 0


@main.command()
def service():
    """Deploy your service"""
    click.echo('this command will setup the ingress service')
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
