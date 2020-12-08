
import ta_microsoft_o365_email_add_on_for_splunk_declare

from splunktaucclib.rest_handler.endpoint import (
    field,
    validator,
    RestModel,
    DataInputModel,
)
from splunktaucclib.rest_handler import admin_external, util
from splunk_aoblib.rest_migration import ConfigMigrationHandler

util.remove_http_proxy_env_vars()


fields = [
    field.RestField(
        'interval',
        required=True,
        encrypted=False,
        default=None,
        validator=validator.Pattern(
            regex=r"""^\-[1-9]\d*$|^\d*$""", 
        )
    ), 
    field.RestField(
        'index',
        required=True,
        encrypted=False,
        default='default',
        validator=validator.String(
            min_len=1, 
            max_len=80, 
        )
    ), 
    field.RestField(
        'audit_email_account',
        required=True,
        encrypted=False,
        default=None,
        validator=validator.String(
            min_len=0, 
            max_len=8192, 
        )
    ), 
    field.RestField(
        'tenant',
        required=True,
        encrypted=False,
        default=None,
        validator=validator.String(
            min_len=0, 
            max_len=8192, 
        )
    ), 
    field.RestField(
        'get_attachment_info',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'file_hash_algorithm',
        required=False,
        encrypted=False,
        default='md5',
        validator=None
    ), 
    field.RestField(
        'attachment_analysis',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'get_body',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'get_body_preview',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'show_relays',
        required=False,
        encrypted=False,
        default=None,
        validator=None
    ), 
    field.RestField(
        'global_account',
        required=True,
        encrypted=False,
        default=None,
        validator=None
    ), 

    field.RestField(
        'disabled',
        required=False,
        validator=None
    )

]
model = RestModel(fields, name=None)



endpoint = DataInputModel(
    'o365_email',
    model,
)


if __name__ == '__main__':
    admin_external.handle(
        endpoint,
        handler=ConfigMigrationHandler,
    )
