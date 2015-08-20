# -*- coding: utf-8 -*-

## Validadores de Filmes
Filmes.titulo.requires = [IS_NOT_EMPTY(),
                          IS_NOT_IN_DB(db, 'filmes.titulo')]
Filmes.generos.requires = IS_NOT_EMPTY()
Filmes.diretor.requires = IS_NOT_EMPTY()
Filmes.capa.requires = IS_EMPTY_OR(IS_IMAGE())

## Validadores de Estoque
ItemsEstoque.filme.requires = IS_IN_DB(db, 'filmes.id', '%(titulo)s', _and=IS_NOT_IN_DB(db, 'items_estoque.filme'))

## Validadores de Locação
Locacao.filmes.requires = IS_IN_DB(db, 'filmes.id', '%(titulo)s')
Locacao.cliente.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s')
Locacao.data_locacao.requires = IS_DATETIME(format='%d/%m/%Y')
Locacao.data_devolucao.requires = IS_DATETIME(format='%d/%m/%Y')
