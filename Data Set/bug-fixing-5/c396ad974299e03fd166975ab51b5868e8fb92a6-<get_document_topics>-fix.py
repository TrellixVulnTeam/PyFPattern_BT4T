def get_document_topics(self, word_id, minimum_probability=None):
    'Override :meth:`~gensim.models.ldamodel.LdaModel.get_document_topics` and simply raises an exception.\n\n        Warnings\n        --------\n        This method invalid for model, use :meth:`~gensim.models.atmodel.AuthorTopicModel.get_author_topics` or\n        :meth:`~gensim.models.atmodel.AuthorTopicModel.get_new_author_topics` instead.\n\n        Raises\n        ------\n        NotImplementedError\n            Always.\n\n        '
    raise NotImplementedError('Method "get_document_topics" is not valid for the author-topic model. Use the "get_author_topics" method.')