from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models.post import Post
from app.posts.forms import NewPostForm, UpdatePostForm

post = Blueprint('post', __name__)


@login_required
@post.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = NewPostForm()

    if form.validate_on_submit():
        Post(form, current_user, add_to_db=True)
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))

    return render_template('post_pages/new_post.html', title='New Post',
                           form=form)


@login_required
@post.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id: int):
    form = UpdatePostForm()
    post = Post.query.get_or_404(post_id)

    if request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    if form.validate_on_submit():
        post.update(form)
        flash('Your post has benn updated!')
        return redirect(url_for('main.index'))

    return render_template('post_pages/update_post.html', title='Update Post',
                           form=form)


@login_required
@post.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.index'))
