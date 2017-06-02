class QueryResponse:
    def __init__(self, json, answer, session):
        self.query = json['query']
        self.count = json['count']
        self.client_id = json['client_id']
        self.query_date = json['query_date']
        self.answer_time = json['answer_time']
        self.session = session
        self.answer = answer

    def __repr__(self):
        return 'QueryResponse (query = %s , count = %s, client_id = %s, ' \
               'query_date = %s, answer_time = %s, session = %s, answer = %s )' % \
               (self.query, self.count, self.client_id, self.query_date, self.answer_time, self.session, self.answer)


class LoginResponse:
    def __init__(self, json, session):
        self.message = json['message']
        self.session = session
        self.valid_seconds = json['valid_seconds']
        self.access_token = json['access_token']

    def __repr__(self):
        return 'LoginResponse: (message = %s, session = %s, valid_seconds = %s, access_token = %s )' % \
               (self.message, self.session, self.valid_seconds, self.access_token)


class SignUpResponse:
    def __init__(self, json, session):
        self.session = session
        self.message = json['message']

    def __repr__(self):
        return 'SignUpResponse: (message = %s, session = %s' % \
               (self.message, self.session)


class ForgotPasswordResponse:
    def __init__(self, json):
        self.message = json['message']

    def __repr__(self):
        return 'ForgotPasswordResponse: (message = %s)' % self.message


class Answer:
    def __init__(self, data, metadata, actions):
        self.data = data
        self.metadata = metadata
        self.actions = actions

    def __repr__(self):
        return 'Answer: (data = %s, metadata = %s, actions = %s)' % \
               (self.data, self.metadata, self.actions)


class Datum:
    def __init__(self, json):
        # all properties of Datum are exposed as a dictionary rather than by field names
        self.values = json

    def __repr__(self):
        return 'Datum: (values = %s)' % self.values


class Metadata:
    def __init__(self, json):
        self.count = json['count']

    def __repr__(self):
        return 'Metadata: (count = %s)' % self.count


class BaseAction:
    def __init__(self):
        pass

class UnknownAction(BaseAction):
    def __init__(self):
        super().__init__()


class AnswerAction(BaseAction):
    def __init__(self, expression):
        super().__init__()
        self.expression = expression


class TableAction(BaseAction):
    def __init__(self, columns):
        super().__init__()
        # columns is a dictionary containing list of names of column to be displayed on client.
        self.columns = columns


class Session:
    def __init__(self, identity):
        self.identity = identity

    def __repr__(self):
        return 'Session: (identity = %s)' % self.identity


class Identity:
    def __init__(self, json):
        self.name = json['name']
        self.type = json['type']
        self.anonymous = json['anonymous']

    def __repr__(self):
        return 'Identity: (name = %s, type = %s, anonymous = %s)' % \
               (self.name, self.type, self.anonymous)


class Table:
    def __init__(self, columns, data):
        self.head = list(columns.values())

        table_data = []
        for datum in data:
            table_datum = []
            for key in columns.keys():
                table_datum.append(datum.values[key])
            table_data.append(table_datum)

        self.data = table_data