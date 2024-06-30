import click
import logging
from .generator import ContentGenerator
from .config import load_config

@click.group()
@click.option('--debug/--no-debug', default=False, help="Enable debug logging")
@click.pass_context
def cli(ctx, debug):
    """Content Generator CLI"""
    ctx.ensure_object(dict)
    config = load_config()
    ctx.obj['config'] = config
    
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@cli.command()
@click.argument('topic')
@click.option('--output', '-o', type=click.File('w'), default='-', help="Output file (default: stdout)")
@click.pass_context
def generate(ctx, topic, output):
    """Generate content on a given topic"""
    config = ctx.obj['config']
    generator = ContentGenerator(config)
    content = generator.generate(topic)
    click.echo(content, file=output)

@cli.command()
@click.pass_context
def analyze_style(ctx):
    """Analyze and display the current writing style"""
    config = ctx.obj['config']
    generator = ContentGenerator(config)
    style_guide = generator.style_analyzer.get_style_guide()
    click.echo("Current Style Guide:")
    click.echo(style_guide)

if __name__ == '__main__':
    cli(obj={})