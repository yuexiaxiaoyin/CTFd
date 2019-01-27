from CTFd.models import ma, Tags


class TagSchema(ma.ModelSchema):
    class Meta:
        model = Tags
        include_fk = True
        dump_only = ('id',)

    views = {
        'admin': [
            'id',
            'challenge',
            'value'
        ],
        'user': [
            'value'
        ]
    }

    def __init__(self, view=None, *args, **kwargs):
        if view:
            if type(view) == str:
                kwargs['only'] = self.views[view]
            elif type(view) == list:
                kwargs['only'] = view

        super(TagSchema, self).__init__(*args, **kwargs)
