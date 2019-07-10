# -*- coding: utf-8 -*-
class PostStatusEnum(object):

    DRAFT = 0
    PUBLISHED = 1
    ARCHIVED = 2


POST_STATUS_ENUM = (
    (PostStatusEnum.DRAFT, u'Draft'),
    (PostStatusEnum.PUBLISHED, u'Published'),
    (PostStatusEnum.ARCHIVED, u'Archived'),
)