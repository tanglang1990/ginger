class Redprint:

    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop("endpoint", f.__name__)
            self.mound.append((rule, endpoint, f, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        for rule, endpoint, f, options in self.mound:
            if url_prefix is None:
                url_prefix = '/' + self.name

            rule = url_prefix + rule
            bp.add_url_rule(rule, endpoint, f, **options)
