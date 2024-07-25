import click

from blog.posts import(
    get_all_posts,
    get_post_by_slug,
    update_post_by_slug,
    new_post,
)

@click.group()
def post():
    """Manage blog posts."""

@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Add new post to database
    usage: flask post new --title "teste cli" --content "teste cli"
    """
    new = new_post(title, content)
    click.echo(f"New post created {new}")

@post.command("list")
def _list():
    """List all posts
    usage: flask post list
    """
    for post in get_all_posts():
        click.echo(post)
        click.echo("-" * 30) #lib rich


@post.command()
@click.argument("slug")
def get(slug):
    """Get post by slug
    usage: flask post get ***slug***
    """
    post = get_post_by_slug(slug)
    click.echo(post or "post_not_found")


@post.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, content, published):
    """Update post by slug
    usage: flask post update teste-cli  --content "teste cli update"
    """
    data = {}
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published.lower() == "true"
    update_post_by_slug(slug, data)
    click.echo("Post updated")

#TODO: Criar comando para despublicar
    
def configure(app):
    app.cli.add_command(post)