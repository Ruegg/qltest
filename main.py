
class ApiParam():
    def __init__(self, name, required):
        self.name = name
        self.required = required

class StringParam(ApiParam):
    def __init__(self, name, required):
        super().__init__(name, required)

class api_method():
    def __init__(self, uri, methods, params):
        self.uri = uri
        self.methods= methods
        self.params = params
    
    def __call__(self, *argv):
        pass


@api_method(
    "/v3/something/test",
    methods=['PUT'],
    params=[
        StringParam("bucket", required=True)
    ]
)
def v3_something(ctx, bucket):
    test = 4
    print('something')
    print(bucket)
