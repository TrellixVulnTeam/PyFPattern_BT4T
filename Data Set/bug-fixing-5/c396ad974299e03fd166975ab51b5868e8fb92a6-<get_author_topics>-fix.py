def get_author_topics(self, author_name, minimum_probability=None):
    'Get topic distribution the given author.\n\n        Parameters\n        ----------\n        author_name : str\n            Name of the author for which the topic distribution needs to be estimated.\n        minimum_probability : float, optional\n            Sets the minimum probability value for showing the topics of a given author, topics with probability <\n            `minimum_probability` will be ignored.\n\n        Returns\n        -------\n        list of (int, float)\n            Topic distribution of an author.\n\n        Example\n        -------\n        >>> from gensim.models import AuthorTopicModel\n        >>> from gensim.corpora import mmcorpus\n        >>> from gensim.test.utils import common_dictionary, datapath, temporary_file\n\n        >>> author2doc = {\n        ...     \'john\': [0, 1, 2, 3, 4, 5, 6],\n        ...     \'jane\': [2, 3, 4, 5, 6, 7, 8],\n        ...     \'jack\': [0, 2, 4, 6, 8]\n        ... }\n        >>>\n        >>> corpus = mmcorpus.MmCorpus(datapath(\'testcorpus.mm\'))\n        >>>\n        >>> with temporary_file("serialized") as s_path:\n        ...     model = AuthorTopicModel(\n        ...          corpus, author2doc=author2doc, id2word=common_dictionary, num_topics=4,\n        ...          serialized=True, serialization_path=s_path\n        ...     )\n        ...\n        ...     model.update(corpus, author2doc)  # update the author-topic model with additional documents\n        >>>\n        >>> # construct vectors for authors\n        >>> author_vecs = [model.get_author_topics(author) for author in model.id2author.values()]\n\n        '
    author_id = self.author2id[author_name]
    if (minimum_probability is None):
        minimum_probability = self.minimum_probability
    minimum_probability = max(minimum_probability, 1e-08)
    topic_dist = (self.state.gamma[author_id, :] / sum(self.state.gamma[author_id, :]))
    author_topics = [(topicid, topicvalue) for (topicid, topicvalue) in enumerate(topic_dist) if (topicvalue >= minimum_probability)]
    return author_topics