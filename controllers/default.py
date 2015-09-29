# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

## CREATE

@auth.requires_membership('funcionario')
def novo_filme():
    form = SQLFORM(Filmes)
    if form.process().accepted:
        session.flash = 'Novo vídeo cadastrado: %s' % form.vars.titulo
        redirect(URL('novo_filme'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

@auth.requires_membership('funcionario')
def estocar():
    form = SQLFORM(ItemsEstoque)
    if form.process().accepted:
        session.flash = 'Filme adicionado ao estoque!'
        redirect(URL('estocar'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

@auth.requires_membership('funcionario')
def locar():
    form = SQLFORM(Locacao)
    if form.process().accepted:
        session.flash = 'Locação realizada!'
        redirect(URL('locar'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

## READ

def ver_filmes():
    grid = SQLFORM.grid(Filmes)
    return dict(grid=grid)

@auth.requires_membership('funcionario')
def ver_estoque():
    estoque = db(ItemsEstoque).select()
    return dict(estoque=estoque)

@auth.requires_membership('funcionario')
def ver_locacoes():
    locacoes = db(Locacao).select()
    return dict(locacoes=locacoes)

## UPDATE

@auth.requires_membership('funcionario')
def editar_filme():
    form = SQLFORM(Filmes, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Filme atualizado: %s' % form.vars.titulo
        redirect(URL('ver_filmes'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

@auth.requires_membership('funcionario')
def alterar_estoque():
    form = SQLFORM(ItemsEstoque, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Estoque atualizado!'
        redirect(URL('ver_estoque'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

@auth.requires_membership('funcionario')
def editar_locacao():
    form = SQLFORM(Locacao, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Locação atualizada!'
        redirect(URL('ver_locacoes'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

## DELETE

@auth.requires_membership('funcionario')
def apagar_filme():
    db(Filmes.id==request.args(0, cast=int)).delete()
    session.flash = 'Filme apagado!'
    redirect(URL('ver_filmes'))

@auth.requires_membership('funcionario')
def apagar_estoque():
    db(ItemsEstoque.id==request.args(0, cast=int)).delete()
    session.flash = 'Item apagado!'
    redirect(URL('ver_estoque'))

@auth.requires_membership('funcionario')
def apagar_locacao():
    db(Locacao.id==request.args(0, cast=int)).delete()
    session.flash = 'Locação apagada!'
    redirect(URL('ver_locacoes'))
