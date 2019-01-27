from CTFd.models import ma, Notifications


class NotificationSchema(ma.ModelSchema):
    class Meta:
        model = Notifications
        include_fk = True
        dump_only = ('id', 'date')

    def __init__(self, view=None, *args, **kwargs):
        if view:
            if type(view) == str:
                kwargs['only'] = self.views[view]
            elif type(view) == list:
                kwargs['only'] = view

        super(NotificationSchema, self).__init__(*args, **kwargs)
