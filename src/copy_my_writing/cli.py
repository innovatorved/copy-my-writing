import click
from .generator import ContentGenerator
from .config import load_config, load_logger

logger = load_logger()


@click.group()
@click.option("--debug/--no-debug", default=False, help="Enable debug logging")
@click.pass_context
def cli(ctx, debug):
    """Content Generator CLI"""
    ctx.ensure_object(dict)
    config = load_config()
    ctx.obj["config"] = config

    logger.debug(debug) if debug else logger.info("Debug logging is disabled")


@cli.command()
@click.argument("topic")
@click.option(
    "--output",
    "-o",
    type=click.File("w"),
    default="-",
    help="Output file (default: stdout)",
)
@click.pass_context
def generate(ctx, topic, output):
    """Generate content on a given topic"""
    config = ctx.obj["config"]
    generator = ContentGenerator(config)
    full_content = ""
    content = generator.generate(topic)
    for message in content:
        full_content += message
        click.echo(message, file=output, nl=False)
    logger.debug(f"Generated content: {full_content}")
    click.echo(file=output)


@cli.command()
@click.pass_context
def analyze_style(ctx):
    """Analyze and display the current writing style"""
    config = ctx.obj["config"]
    generator = ContentGenerator(config)
    style_guide = generator.style_analyzer.get_style_guide()
    click.echo("Current Style Guide:")
    click.echo(style_guide)


if __name__ == "__main__":
    cli(obj={})
