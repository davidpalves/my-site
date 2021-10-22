# -*- coding: utf-8 -*-
class PostStatusEnum(object):

    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'


POST_STATUS_ENUM = (
    (PostStatusEnum.DRAFT, u'Draft'),
    (PostStatusEnum.PUBLISHED, u'Published'),
    (PostStatusEnum.ARCHIVED, u'Archived'),
)