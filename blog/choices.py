from model_utils import Choices

# -*- coding: utf-8 -*-
POST_STATUS_ENUM = Choices(
    ('draft', u'Draft'),
    ('published', u'Published'),
    ('archived', u'Archived'),
)