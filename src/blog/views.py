from flask import Blueprint, render_template, redirect, request, url_for

from .models import Post
from ..data.db import db
from ..util import convert

blueprint = Blueprint('blog', __name__)

@blueprint.route('/', methods=['GET'])
def list():
    " Displays a list of published posts "
    posts = db.session.query(Post).filter(Post.published)\
        .order_by(Post.published_dt.desc())
    page = convert(request.args.get('page'), int, 1)
    paginated_posts = posts.paginate(page=page, per_page=8)

    return render_template('blog/list.tmpl', posts=paginated_posts)

@blueprint.route("/<string:slug>")
def show(slug):
    " Displays an individual post "
    post = db.session.query(Post).filter_by(slug=slug).first()
    if not post:
        return redirect(url_for('blog.list'))

    tags = ', '.join([t.name for t in post.tags])

    prev_post = db.session.query(Post).filter(Post.published)\
        .filter(Post.id < post.id)\
        .order_by(Post.id.desc()).first()

    next_post = db.session.query(Post).filter(Post.published)\
        .filter(Post.id > post.id)\
        .order_by(Post.id.asc()).first()

    return render_template('blog/show.tmpl', post=post, tags=tags,
                           prev_post=prev_post, next_post=next_post)
