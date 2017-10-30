# Instagram

## Requirements

- Python 3.6.2

## Secret config JSON files

.config_secret/settings_common.json

```json
{
  "django": {
    "secret_key": "<Django secret key value>",
    "databases": "RDS-psql"
  },
  "facebook": {
    "app_id": "",
    "secret_code": ""
  },
  "aws": {
    "AWS_ACCESS_KEY_ID": "",
    "AWS_SECRET_ACCESS_KEY": "",
    "AWS_STORAGE_BUCKET_NAME":""
  }
}
```