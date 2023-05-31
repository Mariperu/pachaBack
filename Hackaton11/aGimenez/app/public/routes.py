import logging
from flask import abort, render_template, current_app, redirect, url_for, request
from werkzeug.exceptions import NotFound
from flask_login import login_required, current_user
from app.models import Product
from . import public_bp

logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info('Mostrando los productos del minimarket')
    page = int(request.args.get('page', 1))
    per_page = current_app.config['ITEMS_PER_PAGE']
    product_pagination = Product.all_paginated(page, per_page)
    return render_template("public/index.html", product_pagination=product_pagination)


@public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
def show_product(slug):
    logger.info('Mostrando un producto')
    logger.debug(f'Slug: {slug}')
    product = Product.get_by_slug(slug)
    if not product:
        logger.info(f'El producto {slug} no existe')
        abort(404)

        return redirect(url_for('public.show_product', slug=product.nombne))
    return render_template("public/product_view.html", product=product)


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    products = Product.get_all()
    return render_template("public/index.html", products=products)
